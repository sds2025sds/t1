import streamlit as st
import pandas as pd

# ---------------------
# Mot de passe d'accès
# ---------------------
password = st.text_input("Mot de passe :", type="password")
if password != "PAMPAM2025":  # interne uniquement
    st.warning("Mot de passe incorrect.")
    st.stop()

# ---------------------
# Données internes (10 fonds pour démo)
# ---------------------
fonds = [
    {
        "nom": "Carmignac Investissement",
        "logo": "🟢", "banniere": "🌍 Global Growth",
        "perf": 42, "vol": 12.3, "frais": 1.8, "theme": "Global", "usa": 40
    },
    {
        "nom": "Comgest Monde",
        "logo": "🔵", "banniere": "🌐 Qualité internationale",
        "perf": 47, "vol": 11.7, "frais": 1.7, "theme": "Qualité", "usa": 35
    },
    {
        "nom": "EdR Big Data",
        "logo": "🟣", "banniere": "💾 Thématique Tech",
        "perf": 55, "vol": 15.1, "frais": 2.0, "theme": "Technologie", "usa": 50
    },
    {
        "nom": "Sextant Grand Large",
        "logo": "🟠", "banniere": "⚖️ Flexible multi-zones",
        "perf": 38, "vol": 10.8, "frais": 1.5, "theme": "Diversifié", "usa": 20
    },
    {
        "nom": "BlackRock Global Fund",
        "logo": "⚫️", "banniere": "🏦 Best of World",
        "perf": 53, "vol": 13.8, "frais": 1.8, "theme": "Diversifié", "usa": 48
    },
    {
        "nom": "Amundi World Equity",
        "logo": "🔴", "banniere": "🌎 Actions monde",
        "perf": 46, "vol": 12.1, "frais": 1.7, "theme": "Global", "usa": 42
    },
    {
        "nom": "Pictet Global Megatrend",
        "logo": "🟡", "banniere": "💡 Megatrends",
        "perf": 50, "vol": 13.9, "frais": 2.1, "theme": "Thématique", "usa": 46
    },
    {
        "nom": "Invesco Global Equity",
        "logo": "🟤", "banniere": "🌍 Pure Equity",
        "perf": 47, "vol": 12.6, "frais": 1.6, "theme": "Croissance", "usa": 41
    },
    {
        "nom": "M&G Global Dividend",
        "logo": "⚪️", "banniere": "💰 Rendement stable",
        "perf": 39, "vol": 10.9, "frais": 1.4, "theme": "Dividende", "usa": 36
    },
    {
        "nom": "Fidelity World",
        "logo": "🔶", "banniere": "🌐 Stratégie mondiale",
        "perf": 61, "vol": 13.2, "frais": 1.9, "theme": "Global", "usa": 60
    }
]

# ---------------------
# Filtres utilisateurs
# ---------------------
st.title("🔍 Explorer des fonds internationaux")

perf_min = st.slider("📈 Performance 5 ans minimum (%)", 0, 100, 30)
frais_max = st.slider("💸 Frais courants maximum (%)", 0, 3, 2)
usa_min = st.slider("🇺🇸 Exposition minimale aux États-Unis (%)", 0, 100, 30)
themes = st.multiselect("🎯 Thématiques", list(set(f["theme"] for f in fonds)), default=list(set(f["theme"] for f in fonds)))

# ---------------------
# Filtrage logique
# ---------------------
filtered = [
    f for f in fonds
    if f["perf"] >= perf_min and f["frais"] <= frais_max and f["usa"] >= usa_min and f["theme"] in themes
]

st.markdown(f"### 📊 {len(filtered)} fonds correspondent à vos critères")

# ---------------------
# Affichage en blocs 3 par ligne
# ---------------------
for i in range(0, len(filtered), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(filtered):
            fond = filtered[i + j]
            with cols[j]:
                st.markdown("----")
                st.markdown(f"#### {fond['logo']} {fond['nom']}")
                st.markdown(f"**{fond['banniere']}**")
                st.metric("Performance 5 ans", f"{fond['perf']}%")
                st.metric("Volatilité", f"{fond['vol']}%")
                st.metric("Frais courants", f"{fond['frais']}%")
                st.progress(fond["usa"] / 100, text=f"🇺🇸 Exposition USA : {fond['usa']}%")
                st.markdown(f"📌 Thématique : *{fond['theme']}*")
                st.markdown("----")
