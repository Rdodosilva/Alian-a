import streamlit as st
import folium
from streamlit_folium import st_folium
from folium import plugins

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Aliança por Floripa - Praça Fernando Machado",
    page_icon="🌿",
    layout="wide"
)

# =========================
# ESTILO GLOBAL
# =========================
st.markdown("""
    <style>
    body {
        background-color: #0a0f1c;
        color: white;
    }
    .main {
        background-color: #0a0f1c;
        color: white;
    }
    .stApp {
        background-color: #0a0f1c;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .card {
        background: rgba(0, 255, 200, 0.1);
        border: 1px solid rgba(0, 255, 200, 0.3);
        border-radius: 15px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .metric {
        background: rgba(0, 100, 255, 0.15);
        border-radius: 10px;
        padding: 10px;
        text-align: center;
    }
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 200px;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# CABEÇALHO
# =========================
st.markdown("<h1 style='text-align: center; color: #00ffaa;'>🌿 Aliança por Floripa</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #66c2ff;'>Revitalização da Praça Fernando Machado</h3>", unsafe_allow_html=True)

# =========================
# LOGO (coloque o caminho certo da sua logo)
# =========================
st.image("alianca_logo.png", caption="Projeto Aliança por Floripa", use_column_width=True)

# =========================
# DESCRIÇÃO DO PROJETO
# =========================
with st.container():
    st.markdown("""
    ### 🧭 Sobre a ação
    Estivemos recentemente na Praça **Fernando Machado**, junto com o **Marquinho**, que demonstrou interesse imediato na **revitalização da área**.  
    O projeto **Aliança por Floripa** vai realizar:

    - 🧽 Lavação e esfregação do chão com **cloro**, com apoio do **Bida**  
    - 🎨 **Pintura dos pilares** e da base de apoio social  
    - 🚮 **Despichação e limpeza das lixeiras**  
    - 💡 Reorganização estética e ambiental da praça

    Tudo isso com o objetivo de transformar o espaço em um ambiente mais **agradável, limpo e acolhedor** para todos.
    """)

# =========================
# MAPA DE ATUAÇÃO
# =========================

# Coordenadas aproximadas da Praça Fernando Machado
coords_praca = [-27.59864, -48.55183]

# Cria o mapa base
m = folium.Map(location=coords_praca, zoom_start=18, tiles="CartoDB dark_matter")

# Adiciona marcador da praça
folium.Marker(
    coords_praca,
    popup="Praça Fernando Machado",
    tooltip="Praça Fernando Machado 🌿",
    icon=folium.Icon(color="green", icon="leaf")
).add_to(m)

# Delimitação simbólica da praça (retângulo verde-azulado)
folium.Rectangle(
    bounds=[[-27.59895, -48.55205], [-27.59840, -48.55155]],
    color="#00ffcc",
    fill=True,
    fill_opacity=0.2,
    popup="Área de revitalização - Aliança por Floripa"
).add_to(m)

# Camada de calor simbólica (representando concentração de trabalho)
heat_data = [
    [-27.59860, -48.55180],
    [-27.59863, -48.55190],
    [-27.59870, -48.55175],
]
plugins.HeatMap(heat_data, radius=20, blur=30, gradient={0.4: 'blue', 0.65: 'lime', 1: 'cyan'}).add_to(m)

# Exibe o mapa
st_folium(m, width=800, height=600)

# =========================
# EQUIPE ENVOLVIDA
# =========================
st.markdown("### 👥 Equipe Aliança por Floripa")

equipe = {
    "Coordenação Geral": ["Marquinho", "Rodrigo"],
    "Apoio Técnico": ["Bida", "Equipe de Pintura", "Equipe de Limpeza"],
    "Voluntários": ["Ana", "Lucas", "João", "Maria", "Tiago"]
}

for cargo, nomes in equipe.items():
    with st.container():
        st.markdown(f"#### {cargo}")
        st.markdown(f"**Participantes:** {', '.join(nomes)}")
        st.markdown("---")

# =========================
# RODAPÉ
# =========================
st.markdown("""
<hr>
<p style='text-align: center; color: #66c2ff;'>
Projeto <b>Aliança por Floripa</b> — Unidos pela revitalização dos espaços públicos 🌎<br>
Desenvolvido com ❤️ em Florianópolis
</p>
""", unsafe_allow_html=True)
