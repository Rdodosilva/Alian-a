# app.py
import os
import io
import streamlit as st
from PIL import Image, UnidentifiedImageError
import folium
from folium import PolyLine, Polygon, Marker
from streamlit_folium import st_folium

# ---------------------------
# CONFIGURAÇÃO INICIAL
# ---------------------------
st.set_page_config(
    page_title="Aliança por Floripa",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------
# FUNÇÕES AUXILIARES
# ---------------------------
def try_load_local_logo(path: str):
    """Tenta abrir um arquivo de logo local e retornar PIL Image, ou None."""
    if path and os.path.exists(path):
        try:
            return Image.open(path)
        except Exception:
            return None
    return None

def load_image_from_bytes(uploaded_file):
    """Carrega PIL image a partir de UploadedFile (ou BytesIO)."""
    try:
        if uploaded_file is None:
            return None
        # streamlit uploaded file has .read method
        image = Image.open(io.BytesIO(uploaded_file.read()))
        return image
    except UnidentifiedImageError:
        return None
    except Exception:
        return None

def draw_legend(fmap):
    """Adiciona uma legenda HTML fixa no mapa (folium Element)."""
    legend_html = """
    <div style='position: fixed; 
                bottom: 60px; left: 20px; width: 210px; z-index:9999; font-size:14px;'>
      <div style='background: white; padding:10px; border-radius:8px; box-shadow:0 6px 18px rgba(0,0,0,0.12);'>
        <b>Legenda</b>
        <div style='margin-top:8px;'><span style='display:inline-block;width:16px;height:10px;background:#dc3545;margin-right:8px;'></span>Planejada</div>
        <div style='margin-top:6px;'><span style='display:inline-block;width:16px;height:10px;background:#0073e6;margin-right:8px;'></span>Em andamento</div>
        <div style='margin-top:6px;'><span style='display:inline-block;width:16px;height:10px;background:#0b6b6a;margin-right:8px;'></span>Praças (contorno)</div>
      </div>
    </div>
    """
    fmap.get_root().html.add_child(folium.Element(legend_html))

# ---------------------------
# ESTILO (CSS)
# ---------------------------
st.markdown(
    """
    <style>
    /* Paleta inspirada na identidade do projeto (verde/azul) - layout moderno */
    :root {
        --accent-1: #0b6b6a;
        --accent-2: #1abc9c;
        --accent-3: #0b9dbf;
        --muted: #526c6a;
    }
    body, .stApp, .block-container {
        background: #f6fbfb;
        color: #0b2b2b;
    }
    .header {
        background: linear-gradient(90deg,var(--accent-2), var(--accent-3));
        color: white;
        padding: 26px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 16px;
        box-shadow: 0 10px 30px rgba(11,157,191,0.12);
    }
    .header h1 {margin:0; font-size:28px; font-weight:800;}
    .header p {margin:6px 0 0; opacity:0.95;}
    .card {
        background: white; border-radius:10px; padding:14px; box-shadow:0 6px 18px rgba(11,79,127,0.04);
    }
    .map-container { border-radius:10px; overflow:hidden; border: 1px solid #e6f3f2; }
    .sidebar .block-container { background: linear-gradient(180deg,#eafcf9,#ffffff); }
    .small-muted { color: #6c7a7a; font-size:13px; }
    footer { text-align:center; color:#6c7a7a; margin-top:18px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------
# SIDEBAR
# ---------------------------
with st.sidebar:
    # Logo upload ou tentativa de carregar arquivo local
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.write("")  # espaço
    uploaded_logo = st.file_uploader("📎 Carregar logo do projeto (opcional)", type=["png", "jpg", "jpeg", "svg"])
    logo_image = None

    # tenta carregar logo local 'alianca_logo.png' automaticamente se existir
    if uploaded_logo is None:
        logo_image = try_load_local_logo("alianca_logo.png")
    else:
        logo_image = load_image_from_bytes(uploaded_logo)

    # mostra logo (se carregada), senão mostra nome estilizado
    if logo_image:
        st.image(logo_image, width=160)
    else:
        st.markdown("<h3 style='color:#0b6b6a;'>Aliança por Floripa</h3>", unsafe_allow_html=True)
        st.markdown("<div class='small-muted'>Revitalização do Centro Histórico</div>", unsafe_allow_html=True)
    st.markdown("---")

    # Navegação
    st.markdown("### Navegação")
    page = st.radio(
        "",
        ("Início", "Mapa de Atuação", "Equipes", "Roteiro", "Recursos", "Sobre"),
        index=0,
    )
    st.markdown("---")
    st.markdown("### Parceiros")
    st.markdown("<div style='display:flex;flex-wrap:wrap;gap:6px'><span style='background:#fff;padding:6px 10px;border-radius:12px;border:1px solid #cdebe8;color:#0b6b6a;'>ACIF</span><span style='background:#fff;padding:6px 10px;border-radius:12px;border:1px solid #cdebe8;color:#0b6b6a;'>CDL</span><span style='background:#fff;padding:6px 10px;border-radius:12px;border:1px solid #cdebe8;color:#0b6b6a;'>Conseg</span></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("🔗 Site: [aliancaporfloripa.com.br](https://www.aliancaporfloripa.com.br)")

# ---------------------------
# HEADER / TOP
# ---------------------------
st.markdown("<div class='header'><h1>Aliança por Floripa</h1><p>Revitalização do Centro Histórico — foco: Praça Fernando Machado</p></div>", unsafe_allow_html=True)

# ---------------------------
# PÁGINAS (conteúdo principal)
# ---------------------------
# central coordinates (Praça Fernando Machado area)
CENTER = [-27.59864, -48.55183]

if page == "Início":
    col1, col2, col3 = st.columns([1, 1, 1])
    col1.metric("Áreas Prioritárias", "10")
    col2.metric("Vasos (Felipe Schmidt)", "69")
    col3.metric("Equipes", "10 (20 colaboradores)")
    st.markdown("<div class='card' style='margin-top:12px'><h2>Sobre o Projeto</h2><p class='small-muted'>A Aliança por Floripa mobiliza organizações e cidadãos para revitalizar espaços públicos do centro histórico de Florianópolis. A primeira fase foca em limpeza, replantio e manutenção de praças e ruas centrais.</p></div>", unsafe_allow_html=True)

elif page == "Mapa de Atuação":
    st.markdown("## 🗺️ Mapa de Atuação — Centro Histórico")
    st.markdown("**Clique nos marcadores para abrir informações.**")
    # create folium map
    m = folium.Map(location=CENTER, zoom_start=16.7, tiles="CartoDB Positron")

    # --- MARCADORES IMPORTANTES (ajuste as coords se tiver as exatas) ---
    correios_coords = [-27.595215, -48.548846]  # Agência Central dos Correios / Praça XV (aprox)
    ticen_coords = [-27.59910, -48.55155]      # Antigo Terminal Cidade (aprox)

    Marker(location=correios_coords,
           popup="<b>Agência Central dos Correios</b><br>Praça XV",
           tooltip="Agência Central dos Correios",
           icon=folium.Icon(color="blue", icon="envelope", prefix="fa")).add_to(m)

    Marker(location=ticen_coords,
           popup="<b>Antigo Terminal Cidade (TICEN)</b>",
           tooltip="TICEN (antigo terminal)",
           icon=folium.Icon(color="darkgreen", icon="bus", prefix="fa")).add_to(m)

    # --- RUAS: desenhar PolyLine seguindo o traçado aproximado ---
    # Rua Felipe Schmidt (exemplo de traçado)
    felipe_coords = [
        [-27.59620, -48.54960],
        [-27.59600, -48.54995],
        [-27.59580, -48.55040],
    ]
    PolyLine(felipe_coords, color="#dc3545", weight=5, opacity=0.9, tooltip="Rua Felipe Schmidt (69 vasos)").add_to(m)

    # Rua Conselheiro Mafra
    mafra_coords = [
        [-27.59640, -48.54920],
        [-27.59620, -48.54860],
    ]
    PolyLine(mafra_coords, color="#dc3545", weight=4, opacity=0.9, tooltip="Rua Conselheiro Mafra").add_to(m)

    # Rua Jerônimo Coelho (linha exemplo)
    jeronimo_coords = [
        [-27.59670, -48.54880],
        [-27.59630, -48.54800],
    ]
    PolyLine(jeronimo_coords, color="#dc3545", weight=4, opacity=0.9, tooltip="Rua Jerônimo Coelho").add_to(m)

    # Rua Trajano (linha exemplo)
    trajano_coords = [
        [-27.59690, -48.54990],
        [-27.59650, -48.54920],
    ]
    PolyLine(trajano_coords, color="#dc3545", weight=4, opacity=0.9, tooltip="Rua Trajano").add_to(m)

    # Rua Tiradentes
    tiradentes_coords = [
        [-27.59490, -48.54830],
        [-27.59460, -48.54770],
    ]
    PolyLine(tiradentes_coords, color="#dc3545", weight=4, opacity=0.9, tooltip="Rua Tiradentes").add_to(m)

    # Calçadão João Pinto
    joaopinto_coords = [
        [-27.59780, -48.54880],
        [-27.59750, -48.54790],
    ]
    PolyLine(joaopinto_coords, color="#dc3545", weight=4, opacity=0.9, tooltip="Calçadão João Pinto").add_to(m)

    # Saldanha / Nunes (exemplo)
    saldanha_coords = [
        [-27.59720, -48.54980],
        [-27.59680, -48.55030],
    ]
    PolyLine(saldanha_coords, color="#dc3545", weight=4, opacity=0.9, tooltip="Ruas Saldanha Marinho / Nunes Machado").add_to(m)

    # --- PRAÇAS: contornos (fill=False para não cobrir) ---
    praca_xv = [
        [-27.59570, -48.54980],
        [-27.59570, -48.54860],
        [-27.59620, -48.54860],
        [-27.59620, -48.54980]
    ]
    Polygon(locations=praca_xv, color="#0b6b6a", weight=3, fill=False, tooltip="Praça XV de Novembro").add_to(m)

    praca_fernando = [
        [-27.59895, -48.55190],
        [-27.59895, -48.55090],
        [-27.59795, -48.55090],
        [-27.59795, -48.55190]
    ]
    Polygon(locations=praca_fernando, color="#0b6b6a", weight=3, fill=False, tooltip="Praça Fernando Machado").add_to(m)

    # Adiciona legenda
    draw_legend(m)

    # Exibe Folium com st_folium
    st.markdown("<div class='map-container card'>", unsafe_allow_html=True)
    st_folium(m, width="100%", height=650)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("**Observação:** se tiver GeoJSON com traçado exato das ruas/polígonos, posso importar direto para precisão total.")

elif page == "Equipes":
    st.markdown("## 👥 Distribuição das Equipes")
    st.markdown("10 equipes — sugestão de alocação (2 colaboradores por equipe)")
    st.table({
        "Equipe": [f"Equipe {i}" for i in range(1, 11)],
        "Área": [
            "Correios (Praça XV)",
            "Felipe Schmidt (vasos)",
            "Conselheiro Mafra",
            "Jerônimo Coelho",
            "Trajano",
            "Praça XV (apoio)",
            "Praça Fernando Machado",
            "Tiradentes",
            "Calçadão João Pinto",
            "Saldanha Marinho / Nunes Machado"
        ]
    })

elif page == "Roteiro":
    st.markdown("## 📋 Roteiro Operacional")
    st.markdown("""
    1. Reunião no ponto de apoio (Praça XV) — distribuição de EPIs e materiais.  
    2. Limpeza do prédio dos Correios e entorno (Equipe 1).  
    3. Replantio dos 69 vasos na Rua Felipe Schmidt (Equipe 2).  
    4. Varrição e higienização nas ruas designadas (Equipes 3-5).  
    5. Jardinagem e manutenção nas praças (Equipes 6-7).  
    6. Revisão, registro fotográfico e relatório final.
    """)

elif page == "Recursos":
    st.markdown("## 🧰 Recursos e Materiais")
    st.markdown("""
    **Equipamentos de limpeza:** vassouras, pás, carrinhos, sacos 100L, lavadora de pressão (se disponível).  
    **Jardinagem:** 69 mudas, substrato, adubo, regadores, ferramentas de poda.  
    **EPIs:** luvas, coletes identificadores, bonés, protetor solar, kit primeiros socorros.  
    **Logística:** veículos para transporte, cones, sinalização, rádio/celular para coordenação.
    """)
    st.warning("Checklist de segurança: uso obrigatório de EPIs, hidratação, pausas programadas e sinalização das áreas.")

else:  # Sobre
    st.markdown("## ℹ️ Sobre o Projeto")
    st.markdown("A Aliança por Floripa é uma iniciativa da sociedade civil com apoio da ACIF, CDL, Conseg Centro e Prefeitura de Florianópolis.")
    st.markdown("Objetivo: revitalizar o centro histórico com ações de limpeza, replantio e geração de trabalho digno.")

# ---------------------------
# RODAPÉ
# ---------------------------
st.markdown("---")
st.markdown("<footer>Aliança por Floripa • Projeto de revitalização do Centro Histórico • www.aliancaporfloripa.com.br</footer>", unsafe_allow_html=True)
