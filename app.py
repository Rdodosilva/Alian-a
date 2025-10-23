# app.py
import os
import io
from typing import Optional
import streamlit as st
from PIL import Image, UnidentifiedImageError
import folium
from folium import Marker, PolyLine, Polygon
from streamlit_folium import st_folium
import pandas as pd

# ---------------------------
# Configuração inicial
# ---------------------------
st.set_page_config(page_title="Aliança por Floripa", page_icon="🌿", layout="wide")

# ---------------------------
# Cores e estilo (identidade)
# ---------------------------
ACCENT_A = "#00b894"  # verde água (ajustável)
ACCENT_B = "#06aed5"  # azul (ajustável)
TEXT = "#0b2b2b"
MUTED = "#6c7a7a"

st.markdown(
    f"""
    <style>
    :root {{
        --acc-a: {ACCENT_A};
        --acc-b: {ACCENT_B};
    }}
    body, .stApp, .block-container {{
        background: #f6fbfb;
        color: {TEXT};
    }}
    .topbar {{
        background: linear-gradient(90deg,var(--acc-a), var(--acc-b));
        color: white;
        padding: 26px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 16px;
        box-shadow: 0 10px 30px rgba(6,174,213,0.12);
    }}
    .topbar h1 {{ margin:0; font-size:28px; font-weight:800; }}
    .topbar p {{ margin:6px 0 0; opacity:0.95; }}
    .card {{ background: white; border-radius:10px; padding:14px; box-shadow:0 6px 18px rgba(11,79,127,0.04); }}
    .map-container {{ border-radius:10px; overflow:hidden; border: 1px solid #e6f3f2; }}
    .small-muted {{ color: {MUTED}; font-size:13px; }}
    .team-card {{ border-radius:10px; padding:12px; background: linear-gradient(180deg,#ffffff,#f7fffd); box-shadow: 0 6px 18px rgba(11,79,127,0.03); }}
    table.dataframe td, table.dataframe th {{ padding: 6px 12px; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# Helpers de imagem
# ---------------------------
def load_logo_local(path="alianca_logo.png") -> Optional[Image.Image]:
    if os.path.exists(path):
        try:
            return Image.open(path)
        except Exception:
            return None
    return None

def load_uploaded_image(uploaded):
    if uploaded is None:
        return None
    try:
        image = Image.open(io.BytesIO(uploaded.read()))
        return image
    except UnidentifiedImageError:
        return None

# ---------------------------
# Sidebar (logo + navegação)
# ---------------------------
with st.sidebar:
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)

    uploaded_logo = st.file_uploader("📎 Carregar logo do projeto (opcional)", type=["png", "jpg", "jpeg", "svg"])
    logo = load_uploaded_image(uploaded_logo) or load_logo_local("alianca_logo.png")

    if logo:
        st.image(logo, width=170)
    else:
        st.markdown("<h3 style='color:var(--acc-a);'>Aliança por Floripa</h3>", unsafe_allow_html=True)
        st.markdown("<div class='small-muted'>Revitalização do Centro Histórico</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")

    page = st.radio("Navegação", ["Início", "Mapa Interativo", "Equipes", "Roteiro", "Recursos", "Sobre"])
    st.markdown("---")
    st.markdown("**Parceiros**")
    st.markdown("<div style='display:flex;gap:6px;flex-wrap:wrap'><span class='card' style='padding:6px 10px;border-radius:8px;'>ACIF</span><span class='card' style='padding:6px 10px;border-radius:8px;'>CDL</span><span class='card' style='padding:6px 10px;border-radius:8px;'>Conseg</span></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("🔗 [aliancaporfloripa.com.br](https://www.aliancaporfloripa.com.br)")

# ---------------------------
# Header
# ---------------------------
st.markdown("<div class='topbar'><h1>Aliança por Floripa</h1><p>Revitalização do Centro Histórico — foco: Praça Fernando Machado</p></div>", unsafe_allow_html=True)

# ---------------------------
# Conteúdo das páginas
# ---------------------------

# Central coords (Praça Fernando Machado area)
CENTER = [-27.59864, -48.55183]

# Note: below coordinates are approximate. If you have GeoJSON or precise coords, replace them.
# Polygons/lines created to visually match the areas you provided.

if page == "Início":
    c1, c2, c3 = st.columns([1,1,1])
    c1.metric("Áreas Prioritárias", "10")
    c2.metric("Vasos (Felipe Schmidt)", "69")
    c3.metric("Equipes", "2 (20 colaboradores)")
    st.markdown("<div class='card' style='margin-top:12px'><h2>Sobre o Projeto</h2><p class='small-muted'>A Aliança por Floripa mobiliza organizações e cidadãos para revitalizar espaços públicos do centro histórico de Florianópolis. A primeira fase foca em limpeza, replantio e manutenção de praças e ruas centrais.</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Destaques / Próximas ações")
    st.write("- Limpeza e revitalização do prédio dos Correios (Praça XV)")
    st.write("- Replantio dos 69 vasos na Rua Felipe Schmidt")
    st.write("- Lavação e pintura de pilares na Praça Fernando Machado (apoio Bida / Comcap)")
    st.markdown("---")

elif page == "Mapa Interativo":
    st.markdown("## 🗺️ Mapa Interativo — Centro de Florianópolis")
    st.markdown("Clique nos elementos do mapa para ver o nome do local. As áreas estão destacadas no estilo do projeto.")

    # Criar mapa Folium
    m = folium.Map(location=CENTER, zoom_start=16.7, tiles="CartoDB Positron")

    # ---------- MARCADORES IMPORTANTES ----------
    correios_coords = [-27.595215, -48.548846]  # Agência Central dos Correios (Praça XV) approx
    ticen_coords = [-27.59910, -48.55155]       # Antigo Terminal Cidade (approx)
    Marker(correios_coords,
           popup=folium.Popup("<b>Agência Central dos Correios</b><br>Praça XV - Limpeza e pintura", max_width=300),
           tooltip="Agência dos Correios",
           icon=folium.Icon(color="darkblue", icon="envelope", prefix="fa")).add_to(m)
    Marker(ticen_coords,
           popup=folium.Popup("<b>Antigo Terminal Cidade (TICEN)</b><br>Área de atenção", max_width=300),
           tooltip="TICEN (antigo)",
           icon=folium.Icon(color="darkgreen", icon="bus", prefix="fa")).add_to(m)

    # ---------- RUA: Felipe Schmidt (polyline) ----------
    felipe_coords = [
        [-27.59620, -48.54960],
        [-27.59600, -48.54995],
        [-27.59580, -48.55040],
    ]
    PolyLine(felipe_coords, color="#00b8d4", weight=8, opacity=0.7, tooltip="Rua Felipe Schmidt (69 vasos)").add_to(m)

    # ---------- RUA: Conselheiro Mafra ----------
    mafra_coords = [
        [-27.59640, -48.54920],
        [-27.59620, -48.54860],
    ]
    PolyLine(mafra_coords, color="#00b8d4", weight=6, opacity=0.7, tooltip="Rua Conselheiro Mafra").add_to(m)

    # ---------- RUA: Jerônimo Coelho ----------
    jeronimo_coords = [
        [-27.59670, -48.54880],
        [-27.59630, -48.54800],
    ]
    PolyLine(jeronimo_coords, color="#00b8d4", weight=6, opacity=0.7, tooltip="Rua Jerônimo Coelho").add_to(m)

    # ---------- RUA: Trajano ----------
    trajano_coords = [
        [-27.59690, -48.54990],
        [-27.59650, -48.54920],
    ]
    PolyLine(trajano_coords, color="#00b8d4", weight=6, opacity=0.7, tooltip="Rua Trajano").add_to(m)

    # ---------- RUA: Tiradentes ----------
    tiradentes_coords = [
        [-27.59490, -48.54830],
        [-27.59460, -48.54770],
    ]
    PolyLine(tiradentes_coords, color="#00b8d4", weight=6, opacity=0.7, tooltip="Rua Tiradentes").add_to(m)

    # ---------- Calçadão João Pinto ----------
    joaopinto_coords = [
        [-27.59780, -48.54880],
        [-27.59750, -48.54790],
    ]
    PolyLine(joaopinto_coords, color="#00b8d4", weight=6, opacity=0.7, tooltip="Calçadão João Pinto").add_to(m)

    # ---------- Saldanha / Nunes ----------
    saldanha_coords = [
        [-27.59720, -48.54980],
        [-27.59680, -48.55030],
    ]
    PolyLine(saldanha_coords, color="#00b8d4", weight=6, opacity=0.7, tooltip="Saldanha Marinho / Nunes Machado").add_to(m)

    # ---------- PRAÇAS: contornos ----------
    praca_xv = [
        [-27.59570, -48.54980],
        [-27.59570, -48.54860],
        [-27.59620, -48.54860],
        [-27.59620, -48.54980]
    ]
    Polygon(locations=praca_xv, color="#0b6b6a", weight=3, fill=True, fill_color="#0b6b6a", fill_opacity=0.12, tooltip="Praça XV de Novembro").add_to(m)

    praca_fernando = [
        [-27.59895, -48.55190],
        [-27.59895, -48.55090],
        [-27.59795, -48.55090],
        [-27.59795, -48.55190]
    ]
    Polygon(locations=praca_fernando, color="#0b6b6a", weight=3, fill=True, fill_color="#0b6b6a", fill_opacity=0.12, tooltip="Praça Fernando Machado").add_to(m)

    # ---------- Legenda ----------
    legend_html = f"""
     <div style='position: fixed; 
                 bottom: 50px; left: 20px; width: 240px; z-index:9999; font-size:14px;'>
       <div style='background: white; padding:10px; border-radius:8px; box-shadow:0 6px 18px rgba(0,0,0,0.12);'>
         <b>Legenda</b>
         <div style='margin-top:8px'><span style='display:inline-block;width:18px;height:10px;background:#00b8d4;margin-right:8px;'></span>Ruas / Ações (em destaque)</div>
         <div style='margin-top:6px'><span style='display:inline-block;width:18px;height:10px;background:#0b6b6a;margin-right:8px;'></span>Praças (contorno + preenchimento leve)</div>
         <div style='margin-top:6px'><span style='display:inline-block;width:18px;height:10px;background:#2f80ed;margin-right:8px;'></span>Marcadores</div>
       </div>
     </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))

    # Exibir mapa com folium
    st.markdown("<div class='map-container card'>", unsafe_allow_html=True)
    st_folium(m, width="100%", height=680)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("**Observação:** As coordenadas usadas são aproximadas; se você tiver GeoJSON ou o traçado exato exportado do Google MyMaps ou QGIS, posso importar direto para o mapa com precisão total (faça upload pelo sidebar).")

    # Upload de GeoJSON opcional
    geojson_file = st.file_uploader("📁 (opcional) Upload GeoJSON com traçados exatos das ruas/polígonos", type=["geojson", "json"])
    if geojson_file:
        try:
            import json
            gj = json.load(geojson_file)
            folium.GeoJson(gj, name="GeoJSON importado").add_to(m)
            st.success("GeoJSON carregado. Recarregue a página para visualização interativa atualizada.")
        except Exception as e:
            st.error("Erro ao carregar GeoJSON: " + str(e))

elif page == "Equipes":
    st.markdown("## 👥 Equipes (2 equipes — 10 pessoas cada)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='team-card'><h3>Equipe 1 — Zona Norte do Centro</h3><p><b>Membros:</b> 10</p><p><b>Responsabilidades:</b> Limpeza do prédio dos Correios, Vidal Ramos, Conselheiro Mafra, Tiradentes e adjacências.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='team-card'><h3>Equipe 2 — Zona Sul do Centro</h3><p><b>Membros:</b> 10</p><p><b>Responsabilidades:</b> Praça Fernando Machado, Calçadão João Pinto, Praça XV, Felipe Schmidt, Nunes Machado.</p></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Atividades principais (por equipe)")
    st.write("- Lavação e esfregação do piso com cloro (apoio Bida/Comcap)")
    st.write("- Pintura de pilares e bases de apoio social")
    st.write("- Replantio e manutenção dos 69 vasos")
    st.write("- Despichação e limpeza das lixeiras")

elif page == "Roteiro":
    st.markdown("## 📋 Roteiro Operacional (resumido)")
    df = pd.DataFrame([
        {"Etapa": "1", "Local": "Prédio dos Correios (Praça XV)", "Tarefa": "Limpeza, pintura e retirada de pichações", "Responsável": "Equipe 1", "Status": "Em andamento"},
        {"Etapa": "2", "Local": "Rua Felipe Schmidt", "Tarefa": "Replantio de 69 vasos e limpeza de piso", "Responsável": "Equipe 2", "Status": "A executar"},
        {"Etapa": "3", "Local": "Praça XV / Fernando Machado", "Tarefa": "Lavação com cloro e pintura dos apoios", "Responsável": "Ambas", "Status": "Planejado"},
    ])
    st.table(df)

elif page == "Recursos":
    st.markdown("## 🧰 Recursos e Materiais")
    st.markdown("- **Equipamentos de limpeza:** vassouras, pás, carrinhos, sacos 100L, lavadora de pressão (se disponível).")
    st.markdown("- **Jardinagem:** 69 mudas, substrato, adubo, regadores, ferramentas de poda.")
    st.markdown("- **EPIs:** luvas, coletes identificadores, bonés, protetor solar, kit primeiros socorros.")
    st.markdown("- **Logística:** veículos para transporte, cones, sinalização, rádio/celular para coordenação.")
    st.warning("Checklist: Uso obrigatório de EPIs, sinalização das áreas, hidratação e pausas regulares.")

else:  # Sobre
    st.markdown("## ℹ️ Sobre")
    st.markdown("A Aliança por Floripa é uma iniciativa da sociedade civil com apoio da ACIF, CDL, Conseg Centro e Prefeitura de Florianópolis.")
    st.markdown("Objetivo: revitalizar o centro histórico com ações de limpeza, replantio e geração de trabalho digno.")
    st.markdown("---")
    st.markdown("© Aliança por Floripa — www.aliancaporfloripa.com.br")

# ---------------------------
# Rodapé discreto
# ---------------------------
st.markdown("<div style='text-align:center; color:#6c7a7a; margin-top:18px;'>Aliança por Floripa • Projeto de revitalização do Centro Histórico</div>", unsafe_allow_html=True)
