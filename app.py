import streamlit as st
import folium
from streamlit_folium import folium_static
import json

# Configuração da página
st.set_page_config(
    page_title="Aliança por Floripa - Dashboard Operacional",
    page_icon="💚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS avançado - Cores do site oficial
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
        padding: 0;
    }
    
    .block-container {
        padding: 2rem 3rem !important;
        max-width: 100% !important;
    }
    
    /* Header Premium */
    .premium-header {
        background: linear-gradient(135deg, #FF4655 0%, #FF6B6B 50%, #FFA07A 100%);
        padding: 3rem 4rem;
        border-radius: 20px;
        margin-bottom: 3rem;
        box-shadow: 0 20px 60px rgba(255, 70, 85, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .premium-header::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: pulse 4s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    .logo-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .header-title {
        color: white;
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        margin: 1rem 0;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.3);
        letter-spacing: -2px;
    }
    
    .header-subtitle {
        color: rgba(255,255,255,0.95);
        font-size: 1.5rem;
        text-align: center;
        font-weight: 400;
    }
    
    /* Navigation Modern */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    
    .nav-button {
        background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
        color: white;
        padding: 1rem 2.5rem;
        border-radius: 15px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s;
        border: 2px solid #FF4655;
        cursor: pointer;
        box-shadow: 0 5px 20px rgba(255, 70, 85, 0.3);
    }
    
    .nav-button:hover {
        background: linear-gradient(135deg, #FF4655 0%, #FF6B6B 100%);
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 70, 85, 0.5);
    }
    
    .nav-button.active {
        background: linear-gradient(135deg, #FF4655 0%, #FF6B6B 100%);
        box-shadow: 0 10px 30px rgba(255, 70, 85, 0.6);
    }
    
    /* Cards Premium */
    .stat-card {
        background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
        padding: 2.5rem;
        border-radius: 20px;
        border-left: 6px solid #FF4655;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        transition: all 0.4s;
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: radial-gradient(circle, rgba(255,70,85,0.2) 0%, transparent 70%);
    }
    
    .stat-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 60px rgba(255, 70, 85, 0.4);
        border-left-width: 10px;
    }
    
    .stat-number {
        font-size: 4rem;
        font-weight: 900;
        color: #FF4655;
        line-height: 1;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1.2rem;
        color: #aaa;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .stat-description {
        font-size: 0.95rem;
        color: #888;
        margin-top: 0.5rem;
    }
    
    /* Mapa Container */
    .map-container {
        background: #1a1a1a;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.6);
        margin: 2rem 0;
    }
    
    .map-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Legend Modern */
    .legend-container {
        background: #2d2d2d;
        padding: 2rem;
        border-radius: 15px;
        margin-top: 2rem;
        border: 2px solid #FF4655;
    }
    
    .legend-title {
        color: #FF4655;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin: 1rem 0;
        padding: 1rem;
        background: #1a1a1a;
        border-radius: 10px;
    }
    
    .legend-color {
        width: 40px;
        height: 40px;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }
    
    .legend-text {
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
    }
    
    .legend-description {
        color: #888;
        font-size: 0.9rem;
    }
    
    /* Team Cards */
    .team-card {
        background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
        padding: 3rem;
        border-radius: 20px;
        margin: 2rem 0;
        border-left: 8px solid #FF4655;
        box-shadow: 0 15px 50px rgba(0,0,0,0.5);
        position: relative;
        overflow: hidden;
    }
    
    .team-card::after {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,70,85,0.05) 0%, transparent 70%);
    }
    
    .team-number {
        position: absolute;
        top: 2rem;
        right: 2rem;
        font-size: 6rem;
        font-weight: 900;
        color: rgba(255,70,85,0.2);
        line-height: 1;
    }
    
    .team-title {
        color: #FF4655;
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 1rem;
    }
    
    .team-focus {
        color: #aaa;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 500;
    }
    
    .area-item {
        background: #1a1a1a;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 12px;
        border-left: 4px solid #FF6B6B;
        transition: all 0.3s;
    }
    
    .area-item:hover {
        transform: translateX(10px);
        background: #252525;
        border-left-width: 6px;
    }
    
    .area-title {
        color: white;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .area-description {
        color: #888;
        font-size: 0.95rem;
    }
    
    .status-badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-left: 1rem;
    }
    
    .status-andamento {
        background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(0, 180, 219, 0.4);
    }
    
    .status-planejada {
        background: linear-gradient(135deg, #FF4655 0%, #FF6B6B 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(255, 70, 85, 0.4);
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%);
        padding: 2.5rem;
        border-radius: 20px;
        border: 2px solid #FF4655;
        margin: 2rem 0;
        box-shadow: 0 15px 50px rgba(255, 70, 85, 0.3);
    }
    
    .info-title {
        color: #FF4655;
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
    }
    
    .info-text {
        color: #ccc;
        font-size: 1.1rem;
        line-height: 1.8;
    }
    
    /* Esconder elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Scrollbar Dark */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0a0a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #FF4655;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #FF6B6B;
    }
</style>
""", unsafe_allow_html=True)

# Header com Logo
st.markdown("""
<div class="premium-header">
    <div class="logo-container">
        <img src="https://aliancaporfloripa.com.br/wp-content/uploads/2024/12/logo-alianca.png" 
             style="height: 120px;" 
             onerror="this.style.display='none'">
    </div>
    <h1 class="header-title">💚 Aliança por Floripa</h1>
    <p class="header-subtitle">Dashboard Operacional de Revitalização do Centro Histórico</p>
</div>
""", unsafe_allow_html=True)

# Sistema de navegação moderno
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("📊 Dashboard", use_container_width=True):
        st.session_state.page = 'dashboard'
with col2:
    if st.button("🗺️ Mapa Operacional", use_container_width=True):
        st.session_state.page = 'mapa'
with col3:
    if st.button("👥 Equipes", use_container_width=True):
        st.session_state.page = 'equipes'
with col4:
    if st.button("📋 Roteiro", use_container_width=True):
        st.session_state.page = 'roteiro'
with col5:
    if st.button("💚 Sobre", use_container_width=True):
        st.session_state.page = 'sobre'

st.markdown("<br>", unsafe_allow_html=True)

# PÁGINA: DASHBOARD
if st.session_state.page == 'dashboard':
    # Métricas principais
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">10</div>
            <div class="stat-label">Áreas Prioritárias</div>
            <div class="stat-description">Centro Histórico de Florianópolis</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">69</div>
            <div class="stat-label">Vasos Ornamentais</div>
            <div class="stat-description">Replantio na Rua Felipe Schmidt</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">20</div>
            <div class="stat-label">Colaboradores</div>
            <div class="stat-description">2 Equipes de 10 pessoas</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Info principal
    st.markdown("""
    <div class="info-box">
        <div class="info-title">🎯 Sobre o Projeto</div>
        <div class="info-text">
            <p><strong>A Aliança por Floripa é uma iniciativa da sociedade civil</strong> que reúne a ACIF (Associação Empresarial de Florianópolis), a CDL Florianópolis e o Conseg Centro, com apoio da Prefeitura de Florianópolis e do projeto Rumo Certo da Associação Alberto de Souza.</p>
            <br>
            <p><strong>Nosso propósito é simples e poderoso:</strong> unir forças para transformar esmolas em oportunidades reais, garantindo que cada contribuição seja aplicada de forma transparente e efetiva para reinserir pessoas na sociedade.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-box">
            <div class="info-title">🌆 Impacto Urbano</div>
            <div class="info-text">
                ✓ Centro mais limpo e organizado<br>
                ✓ Espaços públicos revitalizados<br>
                ✓ Valorização do comércio local<br>
                ✓ Atração de visitantes
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <div class="info-title">👥 Impacto Social</div>
            <div class="info-text">
                ✓ Oportunidades de trabalho digno<br>
                ✓ Capacitação profissional<br>
                ✓ Reinserção social efetiva<br>
                ✓ Transformação de vidas
            </div>
        </div>
        """, unsafe_allow_html=True)

# PÁGINA: MAPA
elif st.session_state.page == 'mapa':
    st.markdown('<div class="map-title">🗺️ Mapa Operacional - Centro de Florianópolis</div>', unsafe_allow_html=True)
    
    # Criar mapa avançado
    m = folium.Map(
        location=[-27.5950, -48.5490],
        zoom_start=16.5,
        tiles='CartoDB positron',
        attr='CartoDB'
    )
    
    # Estilo personalizado para os polígonos
    style_andamento = {
        'fillColor': '#00B4DB',
        'color': '#0083B0',
        'weight': 3,
        'fillOpacity': 0.6
    }
    
    style_planejada = {
        'fillColor': '#FF4655',
        'color': '#FF6B6B',
        'weight': 2,
        'fillOpacity': 0.4
    }
    
    # EM ANDAMENTO - Correios (forma real do prédio)
    correios_geo = {
        "type": "Feature",
        "properties": {
            "name": "Agência Central dos Correios",
            "address": "Praça XV de Novembro, 242",
            "status": "EM ANDAMENTO"
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [-48.5492, -27.5950],
                [-48.5488, -27.5950],
                [-48.5488, -27.5952],
                [-48.5492, -27.5952],
                [-48.5492, -27.5950]
            ]]
        }
    }
    
    folium.GeoJson(
        correios_geo,
        style_function=lambda x: style_andamento,
        tooltip="Agência Central dos Correios",
        popup=folium.Popup("<b>⚡ Agência Central dos Correios</b><br>Praça XV de Novembro, 242<br><span style='color: #00B4DB; font-weight: bold;'>EM ANDAMENTO</span>", max_width=300)
    ).add_to(m)
    
    # EM ANDAMENTO - Terminal Cidade
    terminal_geo = {
        "type": "Feature",
        "properties": {
            "name": "Terminal Cidade de Florianópolis",
            "status": "EM ANDAMENTO"
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [-48.5513, -27.5985],
                [-48.5508, -27.5985],
                [-48.5508, -27.5990],
                [-48.5513, -27.5990],
                [-48.5513, -27.5985]
            ]]
        }
    }
    
    folium.GeoJson(
        terminal_geo,
        style_function=lambda x: style_andamento,
        tooltip="Terminal Cidade de Florianópolis",
        popup=folium.Popup("<b>⚡ Terminal Cidade de Florianópolis</b><br><span style='color: #00B4DB; font-weight: bold;'>EM ANDAMENTO</span>", max_width=300)
    ).add_to(m)
    
    # PLANEJADAS - Ruas e Praças com nomes
    areas_planejadas = [
        {
            "name": "Rua Felipe Schmidt",
            "coords": [[-48.5492, -27.5958], [-48.5505, -27.5958], [-48.5505, -27.5960], [-48.5492, -27.5960]],
            "desc": "Replantio de 69 vasos ornamentais"
        },
        {
            "name": "Praça XV de Novembro",
            "coords": [[-48.5495, -27.5952], [-48.5485, -27.5952], [-48.5485, -27.5958], [-48.5495, -27.5958]],
            "desc": "Jardinagem e limpeza de mobiliário"
        },
        {
            "name": "Praça Fernando Machado",
            "coords": [[-48.5515, -27.5970], [-48.5505, -27.5970], [-48.5505, -27.5980], [-48.5515, -27.5980]],
            "desc": "Manutenção de áreas verdes"
        },
        {
            "name": "Rua Conselheiro Mafra",
            "coords": [[-48.5495, -27.5962], [-48.5480, -27.5962], [-48.5480, -27.5964], [-48.5495, -27.5964]],
            "desc": "Varrição e higienização"
        },
        {
            "name": "Rua Tiradentes",
            "coords": [[-48.5485, -27.5945], [-48.5470, -27.5945], [-48.5470, -27.5947], [-48.5485, -27.5947]],
            "desc": "Limpeza de vias"
        },
        {
            "name": "Calçadão João Pinto",
            "coords": [[-48.5490, -27.5975], [-48.5475, -27.5975], [-48.5475, -27.5977], [-48.5490, -27.5977]],
            "desc": "Limpeza completa"
        }
    ]
    
    for area in areas_planejadas:
        area_geo = {
            "type": "Feature",
            "properties": {"name": area["name"]},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[coord[0], coord[1]] for coord in area["coords"]]]
            }
        }
        
        folium.GeoJson(
            area_geo,
            style_function=lambda x: style_planejada,
            tooltip=area["name"],
            popup=folium.Popup(f"<b>📍 {area['name']}</b><br>{area['desc']}<br><span style='color: #FF4655; font-weight: bold;'>PLANEJADA</span>", max_width=300)
        ).add_to(m)
    
    # Adicionar marcadores com nomes das ruas
    for area in areas_planejadas:
        center_lat = sum([c[1] for c in area["coords"]]) / len(area["coords"])
        center_lon = sum([c[0] for c in area["coords"]]) / len(area["coords"])
        
        folium.Marker(
            location=[center_lat, center_lon],
            icon=folium.DivIcon(html=f'<div style="background: rgba(255,70,85,0.9); color: white; padding: 5px 10px; border-radius: 5px; font-weight: bold; font-size: 11px; white-space: nowrap;">{area["name"]}</div>')
        ).add_to(m)
    
    folium_static(m, width=1400, height=700)
    
    # Legenda
    st.markdown("""
    <div class="legend-container">
        <div class="legend-title">📊 Legenda do Mapa</div>
        <div class="legend-item">
            <div class="legend-color" style="background: linear-gradient(135deg, #00B4DB 0%, #0083B0 100%);"></div>
            <div>
                <div class="legend-text">🔵 Em Andamento</div>
                <div class="legend-description">Agência Central dos Correios • Terminal Cidade</div>
            </div>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background: linear-gradient(135deg, #FF4655 0%, #FF6B6B 100%);"></div>
            <div>
                <div class="legend-text">🔴 Planejadas</div>
                <div class="legend-description">Ruas e Praças aguardando início dos trabalhos</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# PÁGINA: EQUIPES
elif st.session_state.page == 'equipes':
    st.markdown('<div class="map-title">👥 Distribuição das Equipes</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="team-card">
        <div class="team-number">01</div>
        <div class="team-title">🟦 EQUIPE 1 — Zona Comercial Norte</div>
        <div class="team-focus">10 Colaboradores • Foco: Revitalização comercial e replantio</div>
        
        <div class="area-item">
            <div class="area-title">🔵 Terminal Cidade de Florianópolis <span class="status-badge status-andamento">Em Andamento</span></div>
            <div class="area-description">Limpeza e organização da área do terminal</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# PÁGINA: ROTEIRO
elif st.session_state.page == 'roteiro':
    st.markdown('<div class="map-title">📋 Roteiro Operacional</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <div class="info-title">🔄 Fase 1: Preparação e Briefing</div>
        <div class="info-text">
            • Encontro de todas as equipes no ponto de reunião central<br>
            • Distribuição de EPIs (luvas, coletes identificados, bonés)<br>
            • Distribuição de materiais, ferramentas e equipamentos<br>
            • Briefing detalhado com orientações de segurança e responsabilidades<br>
            • Deslocamento organizado para as áreas de atuação
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="team-card">
            <div class="team-number">01</div>
            <div class="team-title">🟦 Fase 2: Execução — Equipe 1</div>
            
            <div class="area-item">
                <div class="area-title">1. Agência dos Correios</div>
                <div class="area-description">Limpeza completa da área externa, calçadas e entorno imediato</div>
            </div>
            
            <div class="area-item">
                <div class="area-title">2. Replantio Felipe Schmidt</div>
                <div class="area-description">Atividade principal: replantio dos 69 vasos com flores ornamentais</div>
            </div>
            
            <div class="area-item">
                <div class="area-title">3. Varrição de Ruas</div>
                <div class="area-description">Conselheiro Mafra, Jerônimo Coelho e Trajano</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="team-card">
            <div class="team-number">02</div>
            <div class="team-title">🟥 Fase 3: Execução — Equipe 2</div>
            
            <div class="area-item">
                <div class="area-title">1. Praças XV e Fernando Machado</div>
                <div class="area-description">Jardinagem, limpeza de bancos e manutenção de áreas verdes</div>
            </div>
            
            <div class="area-item">
                <div class="area-title">2. Terminal Cidade</div>
                <div class="area-description">Limpeza e organização da área do terminal</div>
            </div>
            
            <div class="area-item">
                <div class="area-title">3. Varrição de Ruas</div>
                <div class="area-description">Tiradentes, João Pinto, Saldanha Marinho e Nunes Machado</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <div class="info-title">📸 Fase 4: Finalização e Registro</div>
        <div class="info-text">
            • Recolhimento e organização de materiais e ferramentas<br>
            • Registro fotográfico completo do "antes e depois"<br>
            • Reunião rápida de avaliação com coordenadores de equipe<br>
            • Elaboração de relatório de atividades realizadas<br>
            • Documentação de resultados para prestação de contas pública
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box" style="border-color: #FFD700;">
        <div class="info-title" style="color: #FFD700;">⚠️ Checklist de Segurança Obrigatório</div>
        <div class="info-text">
            ✓ Uso obrigatório de EPIs durante toda a operação<br>
            ✓ Sinalização adequada em todas as áreas de trabalho<br>
            ✓ Hidratação constante de toda a equipe<br>
            ✓ Pausas regulares programadas a cada 2 horas<br>
            ✓ Kit de primeiros socorros sempre acessível<br>
            ✓ Coordenador de segurança disponível em campo<br>
            ✓ Comunicação direta com equipe de apoio
        </div>
    </div>
    """, unsafe_allow_html=True)

# PÁGINA: SOBRE
elif st.session_state.page == 'sobre':
    st.markdown('<div class="map-title">💚 Sobre o Projeto Aliança por Floripa</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <div class="info-title">🎯 Nossa Missão</div>
        <div class="info-text">
            <p>A Aliança por Floripa é uma <strong>iniciativa da sociedade civil</strong> que reúne a ACIF (Associação Empresarial de Florianópolis), a CDL Florianópolis e o Conseg Centro, com apoio da Prefeitura de Florianópolis e do projeto Rumo Certo da Associação Alberto de Souza.</p>
            <br>
            <p><strong>Nosso propósito é simples e poderoso:</strong> unir forças para transformar esmolas em oportunidades reais, garantindo que cada contribuição seja aplicada de forma transparente e efetiva para reinserir pessoas na sociedade.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <div class="info-title">🌆 Impacto Urbano</div>
            <div class="info-text">
                <strong>✓ Centro mais limpo e organizado</strong><br>
                Varrição completa de vias e praças<br><br>
                
                <strong>✓ Espaços públicos revitalizados</strong><br>
                Jardinagem e manutenção de áreas verdes<br><br>
                
                <strong>✓ Valorização do comércio local</strong><br>
                Ambiente mais atrativo para clientes<br><br>
                
                <strong>✓ Atração de visitantes</strong><br>
                Centro histórico mais acolhedor
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <div class="info-title">👥 Impacto Social</div>
            <div class="info-text">
                <strong>✓ Oportunidades de trabalho digno</strong><br>
                Contratação formal de pessoas em vulnerabilidade<br><br>
                
                <strong>✓ Capacitação profissional</strong><br>
                Treinamento em jardinagem e limpeza urbana<br><br>
                
                <strong>✓ Reinserção social efetiva</strong><br>
                Metodologia comprovada do Projeto Rumo Certo<br><br>
                
                <strong>✓ Transformação de vidas</strong><br>
                Dignidade e cidadania restauradas
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <div class="info-title">🔍 Transparência Total</div>
        <div class="info-text">
            <p><strong>Gestão Compartilhada:</strong> O fundo é gerido em conjunto pela ACIF, CDL e Conseg Centro, com apoio institucional da Prefeitura e metodologia do projeto Rumo Certo.</p>
            <br>
            <p><strong>Auditoria Regular:</strong> Todas as movimentações passam por auditoria e prestação de contas pública, garantindo que cada recurso seja aplicado corretamente.</p>
            <br>
            <p><strong>Relatórios Periódicos:</strong> Parceiros e doadores terão acesso a relatórios periódicos com os resultados alcançados e o impacto gerado no centro histórico.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box" style="background: linear-gradient(135deg, #FF4655 0%, #FF6B6B 100%); border: none;">
        <div class="info-title" style="color: white; text-align: center; font-size: 2.5rem;">💚 Faça Parte Desta Transformação</div>
        <div class="info-text" style="color: white; text-align: center; font-size: 1.3rem;">
            <br>
            <p style="font-size: 2rem; font-weight: 800; margin: 1rem 0;">www.aliancaporfloripa.com.br</p>
            <p style="font-size: 1.2rem;">Doe via PIX • Acompanhe resultados • Transforme vidas</p>
            <br>
            <p style="font-size: 1rem; font-weight: 600;">Quem ontem usava as praças para dormir,<br>amanhã poderá estar preservando elas.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Parceiros
    st.markdown('<br><br>', unsafe_allow_html=True)
    st.markdown('<div class="map-title" style="font-size: 2rem;">🤝 Parceiros</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    parceiros = [
        ("ACIF", "Associação Empresarial"),
        ("CDL", "CDL Florianópolis"),
        ("Conseg", "Conseg Centro"),
        ("Prefeitura", "Florianópolis"),
        ("Rumo Certo", "Projeto Social")
    ]
    
    for col, (nome, desc) in zip([col1, col2, col3, col4, col5], parceiros):
        with col:
            st.markdown(f"""
            <div class="stat-card" style="text-align: center; padding: 1.5rem;">
                <div class="stat-label" style="font-size: 1.1rem; color: #FF4655;">{nome}</div>
                <div class="stat-description" style="margin-top: 0.5rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #666; padding: 3rem 0; border-top: 2px solid #FF4655; margin-top: 3rem;">
    <p style="font-size: 1.3rem; color: #FF4655; font-weight: 700; margin-bottom: 1rem;">Aliança por Floripa</p>
    <p style="font-size: 1rem; color: #aaa;">Uma iniciativa da sociedade civil para transformar o centro de Florianópolis</p>
    <p style="font-size: 0.9rem; color: #888; margin-top: 1.5rem;">
        ACIF • CDL Florianópolis • Conseg Centro • Prefeitura de Florianópolis • Projeto Rumo Certo
    </p>
    <p style="font-size: 0.8rem; color: #666; margin-top: 2rem;">
        Dashboard Operacional desenvolvido para gestão e acompanhamento do projeto
    </p>
</div>
""", unsafe_allow_html=True)
            <div class="area-title">🔵 Agência Central dos Correios <span class="status-badge status-andamento">Em Andamento</span></div>
            <div class="area-description">Praça XV de Novembro, 242 • Limpeza completa da área externa e entorno</div>
        </div>
        
        <div class="area-item">
            <div class="area-title">🌸 Rua Felipe Schmidt <span class="status-badge status-planejada">Planejada</span></div>
            <div class="area-description">Replantio de 69 vasos com flores e plantas ornamentais</div>
        </div>
        
        <div class="area-item">
            <div class="area-title">📍 Rua Conselheiro Mafra <span class="status-badge status-planejada">Planejada</span></div>
            <div class="area-description">Varrição, coleta de resíduos e higienização de calçadas</div>
        </div>
        
        <div class="area-item">
            <div class="area-title">📍 Rua Jerônimo Coelho <span class="status-badge status-planejada">Planejada</span></div>
            <div class="area-description">Limpeza de vias e manutenção de áreas públicas</div>
        </div>
        
        <div class="area-item">
            <div class="area-title">📍 Rua Trajano <span class="status-badge status-planejada">Planejada</span></div>
            <div class="area-description">Varrição e organização de espaços públicos</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="team-card">
        <div class="team-number">02</div>
        <div class="team-title">🟥 EQUIPE 2 — Praças e Zona Sul</div>
        <div class="team-focus">10 Colaboradores • Foco: Áreas de convivência e espaços públicos</div>
        
        <div class="area-item">
            <div class="area-title">🌳 Praça XV de Novembro <span class="status-badge status-planejada">Planejada</span></div>
            <div class="area-description">Jardinagem, limpeza de bancos e mobiliário urbano</div>
        </div>
        
        <div class="area-item">
            <div class="area-title">🌳 Praça Fernando Machado <span class="status-badge status-planejada">Planejada</span></div>
            <div class="area-description">Manutenção de áreas verdes e limpeza geral</div>
        </div>
        
        <div class="area-item">
            <div class="area-title">📍 Rua Tiradentes <span class="status-badge status-planejada">Planejada</span></div>
            <div class="area-description">Varrição e higienização de calçadas</div>
        </div>
        
        <div class="area-item">
            <div class="area-title">📍 Calçadão João Pinto <span class="status-badge status-planejada">Planejada</span></div>
            <div class="area-description">Limpeza completa do calçadão e áreas de convivência</div>
        </div>
        
        <div class="area-item">
            <div class="area-title">📍 Ruas Saldanha Marinho e Nunes Machado <span class="status-badge status-planejada">Planejada</span></div>
            <div class="area-description">Varrição fina, recolhimento de resíduos e manutenção</div>
        </div>
        
        <div class="area-item">
