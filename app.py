# app.py
import streamlit as st
import folium
from folium import PolyLine, Polygon, CircleMarker, Marker
from streamlit_folium import st_folium
from PIL import Image
import os

# ------------- Configuração da página -------------
st.set_page_config(
    page_title="Aliança por Floripa",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------- CSS e Estilo -------------
st.markdown("""
<style>
/* corpo */
body, .stApp, .block-container {
    background: #f6fbfb;
    color: #0b2b2b;
}

/* header */
.header {
    background: linear-gradient(90deg,#1abc9c 0%, #0b9dbf 100%);
    color: white;
    padding: 28px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 18px;
    box-shadow: 0 8px 30px rgba(11, 157, 191, 0.12);
}
.header h1 { margin: 0; font-size: 28px; font-weight:800; }
.header p { margin: 6px 0 0 0; opacity: 0.95; }

/* cards*/
.card {
    background: white;
    border-radius: 10px;
    padding: 16px;
    box-shadow: 0 6px 18px rgba(11,79,127,0.04);
}

/* sidebar improvements */
[data-testid="stSidebar"] { background: linear-gradient(180deg,#eafaf8,#ffffff); }
.stRadio > div { gap: 6px; }

/* map box */
.map-box { border-radius: 8px; overflow: hidden; border: 1px solid #e6f3f2; }

/* pequenos ajustes */
h2 { color: #0b6b6a; }
.small-muted { color: #6c7a7a; font-size:13px; }
.legend {
    background: white;
    padding:8px;
    border-radius:6px;
    box-shadow:0 4px 10px rgba(0,0,0,0.06);
}
</style>
""", unsafe_allow_html=True)

# ------------- Sidebar -------------
with st.sidebar:
    # logo (tenta carregar local, senão mostra texto)
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    logo_path = "alianca_logo.png"  # coloque aqui sua logo local
    if os.path.exists(logo_path):
        try:
            img = Image.open(logo_path)
            st.image(img, use_column_width=False, width=160)
        except Exception as e:
            st.markdown("<h3 style='color:#0b6b6a;'>Aliança por Floripa</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color:#0b6b6a;'>Aliança por Floripa</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Navegação")
    page = st.radio("", ["Início", "Mapa de Atuação", "Equipes", "Roteiro", "Recursos", "Sobre"], index=0)
    st.markdown("---")
    st.markdown("### Parceiros")
    st.markdown("<div style='display:flex;flex-wrap:wrap;gap:6px'><span style='background:#fff;padding:6px 10px;border-radius:12px;border:1px solid #cdebe8;color:#0b6b6a;'>ACIF</span><span style='background:#fff;padding:6px 10px;border-radius:12px;border:1px solid #cdebe8;color:#0b6b6a;'>CDL</span><span style='background:#fff;padding:6px 10px;border-radius:12px;border:1px solid #cdebe8;color:#0b6b6a;'>Conseg</span></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("Mais em: [aliancaporfloripa.com.br](https://www.aliancaporfloripa.com.br)")

# ------------- Header -------------
st.markdown("<div class='header'><h1>Aliança por Floripa</h1><p>Revitalização do Centro Histórico — foco: Praça Fernando Machado</p></div>", unsafe_allow_html=True)

# ------------- Páginas -------------
if page == "Início":
    col1, col2, col3 = st.columns(3)
    col1.metric("Áreas Prioritárias", "10", "")
    col2.metric("Vasos para Replantio", "69", "Rua Felipe Schmidt")
    col3.metric("Equipes", "10", "2 por equipe (20 pessoas)")
    st.markdown("<div class='card' style='margin-top:14px'><h2>Sobre o Projeto</h2><p class='small-muted'>A Aliança por Floripa mobiliza organizações e cidadãos para limpeza, replantio e manutenção do centro histórico. Esta ação busca gerar oportunidades e transformar espaços públicos.</p></div>", unsafe_allow_html=True)

elif page == "Mapa de Atuação":
    st.markdown("## Mapa de Atuação — Centro Histórico")
    st.markdown("<p class='small-muted'>Contornos das praças e traçado das ruas alvo (sem polígonos quadrados). Clique nos marcadores para detalhes.</p>", unsafe_allow_html=True)

    # coordenadas centrais (Praça Fernando Machado)
    center = [-27.59864, -48.55183]
    m = folium.Map(location=center, zoom_start=16.8, tiles="CartoDB Positron")

    # --- MARCADORES CORREIOS E TICEN ---
    # Correios (Agência Central) - Praça XV (approx)
    correios = [-27.595215, -48.548846]  # ajuste se tiver coordenadas melhores
    Marker(correios, popup="Agência Central dos Correios (Praça XV)", tooltip="Agência dos Correios", icon=folium.Icon(color="blue", icon="envelope")).add_to(m)

    # TICEN - antigo Terminal Cidade (ponto aproximado)
    ticen = [-27.59910, -48.55155]  # ajuste conforme necessário
    Marker(ticen, popup="Antigo Terminal Cidade (TICEN)", tooltip="TICEN (antigo terminal)", icon=folium.Icon(color="gray", icon="bus")).add_to(m)

    # --- RUA: Felipe Schmidt (polyline exemplo) ---
    felipe_coords = [
        [-27.59620, -48.54960],
        [-27.59600, -48.54995],
        [-27.59580, -48.55040],
    ]
    PolyLine(felipe_coords, color="#dc3545", weight=5, opacity=0.8, tooltip="Rua Felipe Schmidt (69 vasos)").add_to(m)

    # --- RUA: Conselheiro Mafra (exemplo) ---
    mafra_coords = [
        [-27.59640, -48.54920],
        [-27.59620, -48.54860],
    ]
    PolyLine(mafra_coords, color="#dc3545", weight=4, opacity=0.8, tooltip="Rua Conselheiro Mafra").add_to(m)

    # --- RUA: Tiradentes ---
    tiradentes = [
        [-27.59490, -48.54830],
        [-27.59460, -48.54770],
    ]
    PolyLine(tiradentes, color="#dc3545", weight=4, opacity=0.8, tooltip="Rua Tiradentes").add_to(m)

    # --- Calçadão João Pinto ---
    joaopinto = [
        [-27.59780, -48.54880],
        [-27.59750, -48.54790],
    ]
    PolyLine(joaopinto, color="#dc3545", weight=4, opacity=0.8, tooltip="Calçadão João Pinto").add_to(m)

    # --- Saldanha Marinho / Nunes Machado (exemplo) ---
    saldanha = [
        [-27.59720, -48.54980],
        [-27.59680, -48.55030],
    ]
    PolyLine(saldanha, color="#dc3545", weight=4, opacity=0.8, tooltip="Rua Saldanha Marinho / Nunes Machado").add_to(m)

    # --- PRAÇAS: desenhar contorno com Polygon (só contorno visual) ---
    # Praça XV (contorno aproximado)
    praca_xv = [
        [-27.59570, -48.54980],
        [-27.59570, -48.54860],
        [-27.59620, -48.54860],
        [-27.59620, -48.54980]
    ]
    Polygon(locations=praca_xv, color="#0b6b6a", weight=3, fill=False, tooltip="Praça XV de Novembro").add_to(m)

    # Praça Fernando Machado (contorno aproximado)
    praca_fernando = [
        [-27.59895, -48.55190],
        [-27.59895, -48.55090],
        [-27.59795, -48.55090],
        [-27.59795, -48.55190]
    ]
    Polygon(locations=praca_fernando, color="#0b6b6a", weight=3, fill=False, tooltip="Praça Fernando Machado").add_to(m)

    # --- Legenda simples (HTML inserido no canto) ---
    legend_html = """
     <div style='position: fixed; 
                 bottom: 50px; left: 30px; width: 200px; height: 110px; 
                 z-index:9999; font-size:14px;'>
       <div class='legend card'>
         <b>Legenda</b>
         <div style='margin-top:6px'><span style='display:inline-block;width:14px;height:8px;background:#dc3545;margin-right:6px;'></span> Planejada</div>
         <div style='margin-top:6px'><span style='display:inline-block;width:14px;height:8px;background:#0073e6;margin-right:6px;'></span> Em andamento</div>
         <div style='margin-top:6px'><span style='display:inline-block;width:14px;height:8px;background:#0b6b6a;margin-right:6px;'></span> Praças (contorno)</div>
       </div>
     </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))

    # Mostra o mapa com streamlit_folium
    st_folium(m, width=1000, height=650, returned_objects=[])

    st.markdown("**Observação:** as coordenadas acima são aproximadas. Se você tiver os traçados exatos (GeoJSON ou lista de coordenadas), posso importar diretamente para exatidão.")

elif page == "Equipes":
    st.markdown("## Distribuição das Equipes")
    st.markdown("10 equipes (2 pessoas cada) — exemplo de alocação:")
    st.table({
        "Equipe":[f"Equipe {i}" for i in range(1,11)],
        "Área":[
            "Correios",
            "Felipe Schmidt",
            "Conselheiro Mafra",
            "Jerônimo Coelho",
            "Trajano",
            "Praça XV",
            "Fernando Machado",
            "Tiradentes",
            "João Pinto",
            "Saldanha / Nunes"
        ]
    })

elif page == "Roteiro":
    st.markdown("## Roteiro Operacional (resumido)")
    st.write("""
    1. Reunião no ponto de apoio (Praça XV) — distribuição de EPIs e material.
    2. Limpeza do prédio dos Correios e entorno (Equipe 1).
    3. Replantio dos 69 vasos na Rua Felipe Schmidt (Equipe 2).
    4. Varrição e higienização nas ruas designadas (Equipes 3-5).
    5. Jardinagem e manutenção nas praças (Equipes 6-7).
    6. Revisão, registro fotográfico e relatório.
    """)

elif page == "Recursos":
    st.markdown("## Recursos e Materiais")
    st.write("- Vassouras, pás, carrinhos, sacos 100L\n- 69 mudas, substrato e adubo\n- EPIs: luvas, coletes, protetor solar\n- Mangueiras e lavadora de pressão (se possível)\n- Sinalização e cones de trânsito")

else:  # Sobre
    st.markdown("## Sobre o Projeto")
    st.write("Aliança por Floripa — iniciativa da sociedade civil com apoio da ACIF, CDL, Conseg Centro e Prefeitura.")

# ------------- rodapé -------------
st.markdown("---")
st.markdown("<div style='text-align:center;font-size:12px;color:#6c7a7a'>Aliança por Floripa • Projeto de revitalização do Centro Histórico • www.aliancaporfloripa.com.br</div>", unsafe_allow_html=True)
