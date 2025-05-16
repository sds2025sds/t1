import streamlit as st
import pandas as pd

# Mot de passe d’accès
password = st.text_input("Entrez le mot de passe pour accéder à l'application :", type="password")
if password != "pampam2025":
    st.warning("Mot de passe incorrect.")
    st.stop()

# Données de test
data = {
    "Nom du fonds": [
        "Carmignac Investissement", 
        "EdR Big Data", 
        "Sextant Grand Large", 
        "Comgest Monde", 
        "DNCA Global Leaders"
    ],
    "Performance 5 ans (%)": [42, 55, 38, 47, 51],
    "Volatilité (%)": [12.3, 15.1, 10.8, 11.7, 14.5],
    "Frais courants (%)": [1.8, 2.0, 1.5, 1.7, 2.2],
    "Thématique": ["Global", "Technologie", "Diversifié", "Qualité", "Croissance"]
}

df = pd.DataFrame(data)

# Interface utilisateur
st.title("🌍 Comparateur de fonds internationaux – Prototype ")

perf_min = st.slider("Performance minimum sur 5 ans (%)", 0, 100, 30)
vol_max = st.slider("Volatilité maximale (%)", 0, 30, 15)
frais_max = st.slider("Frais courants maximum (%)", 0.0, 3.0, 2.0)
thematique = st.multiselect(
    "Thématiques recherchées :", 
    options=df["Thématique"].unique(), 
    default=df["Thématique"].unique()
)

# Filtrage
filtered_df = df[
    (df["Performance 5 ans (%)"] >= perf_min) &
    (df["Volatilité (%)"] <= vol_max) &
    (df["Frais courants (%)"] <= frais_max) &
    (df["Thématique"].isin(thematique))
]

st.markdown(f"🔍 **{len(filtered_df)} fonds trouvés** selon vos critères :")

# Affichage des résultats
for i in range(0, len(filtered_df), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(filtered_df):
            fond = filtered_df.iloc[i + j]
            with cols[j]:
                st.subheader(fond["Nom du fonds"])
                st.metric("Perf. 5 ans", f'{fond["Performance 5 ans (%)"]}%')
                st.metric("Volatilité", f'{fond["Volatilité (%)"]}%')
                st.metric("Frais", f'{fond["Frais courants (%)"]}%')
                st.write(f"📌 Thématique : {fond['Thématique']}")

