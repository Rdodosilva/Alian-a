import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import sys
import os

# Adicionar o diretório ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data.project_data import *

# Configuração da página
st.set_page_config(
    page_title="Aliança por Floripa",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #009678 0%, #00b8a0 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-number {
        font-size: 2.5em;
        font-weight: bold;
        margin: 10px 0;
    }
    .metric-label {
        font-size: 0.9em;
        opacity: 0.9;
    }
    .phase-card {
        background: white;
        border-left: 5px solid #009678;
        padding: 20px;
        margin: 10px 0;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .phase-number {
        background: #009678;
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-right: 15px;
    }
    .team-card {
        background: white;
        border: 2px solid #e0e0e0;
        padding: 20px;
        margin: 10px 0;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .team-header {
        color: #009678;
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .partner-badge {
        background: #f0f5f5;
        border: 2px solid #009678;
        padding: 15px;
        margin: 10px 5px;
        border-radius: 8px;
        text-align: center;
        display: inline-block;
        min-width: 150px;
    }
    .partner-name {
        color: #009678;
        font-weight: bold;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("assets/logo.png", use_column_width=True)
    st.markdown("---")
    
    page = st.radio(
        "Navegação",
        ["Dashboard", "Mapa de Atuação", "Equipes", "Roteiro Operacional", "Recursos", "Sobre o Projeto"],
        icon_index=0
    )

# PÁGINA: DASHBOARD
if page == "Dashboard":
    st.title("🌿 Aliança por Floripa")
    st.markdown("### Transformando o centro histórico de Florianópolis")
    
    st.markdown("---")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Áreas de Atuação</div>
                <div class="metric-number">{METRICS['areas']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Vasos de Plantas</div>
                <div class="metric-number">{METRICS['plants']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Colaboradores</div>
                <div class="metric-number">{METRICS['collaborators']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Equipes</div>
                <div class="metric-number">{METRICS['teams']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Propósito do projeto
    st.subheader("📋 Propósito do Projeto")
    st.info(PROJECT_INFO['purpose'])
    
    st.markdown("---")
    
    # Missão
    st.subheader("🎯 Nossa Missão")
    cols = st.columns(2)
    for idx, mission in enumerate(MISSION):
        with cols[idx % 2]:
            st.markdown(f"✓ {mission}")
    
    st.markdown("---")
    
    # Status do projeto
    st.subheader("📊 Status do Projeto")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        in_progress = len(AREAS_IN_PROGRESS)
        st.metric("Em Andamento", f"{in_progress} áreas", "🔵 Azul")
    
    with col2:
        planned = len(AREAS_PLANNED)
        st.metric("Planejadas", f"{planned} áreas", "🔴 Vermelho")
    
    with col3:
        st.metric("Concluídas", "0 áreas", "⚪ Nenhuma")
    
    st.markdown("---")
    
    # Link para site oficial
    st.subheader("🌐 Saiba Mais")
    st.markdown(f"[Visite o site oficial do projeto →]({PROJECT_INFO['website']})")

# PÁGINA: MAPA DE ATUAÇÃO
elif page == "Mapa de Atuação":
    st.title("🗺️ Mapa de Atuação")
    st.markdown("Visualize as áreas de atuação do projeto no centro histórico de Florianópolis")
    
    st.markdown("---")
    
    # Criar mapa
    m = folium.Map(
        location=[-27.5945, -48.5475],
        zoom_start=15,
        tiles="OpenStreetMap"
    )
    
    # Adicionar áreas em andamento (Azul)
    for area in AREAS_IN_PROGRESS:
        folium.CircleMarker(
            location=[area['lat'], area['lng']],
            radius=15,
            popup=f"<b>{area['name']}</b><br>{area['location']}<br><em>Em Andamento</em>",
            color="#0099ff",
            fill=True,
            fillColor="#0099ff",
            fillOpacity=0.7,
            weight=2
        ).add_to(m)
    
    # Adicionar áreas planejadas (Vermelho)
    for area in AREAS_PLANNED:
        folium.CircleMarker(
            location=[area['lat'], area['lng']],
            radius=12,
            popup=f"<b>{area['name']}</b><br>{area['location']}<br><em>Planejada</em>",
            color="#ff6b6b",
            fill=True,
            fillColor="#ff6b6b",
            fillOpacity=0.6,
            weight=2
        ).add_to(m)
    
    # Exibir mapa
    st_folium(m, width=1200, height=600)
    
    st.markdown("---")
    
    # Legenda
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🔵 Em Andamento")
        for area in AREAS_IN_PROGRESS:
            st.markdown(f"• **{area['name']}** - {area['location']}")
    
    with col2:
        st.markdown("### 🔴 Planejadas")
        for area in AREAS_PLANNED[:5]:
            st.markdown(f"• **{area['name']}** - {area['location']}")
    
    with col3:
        st.markdown("### 🔴 Planejadas (cont.)")
        for area in AREAS_PLANNED[5:]:
            st.markdown(f"• **{area['name']}** - {area['location']}")

# PÁGINA: EQUIPES
elif page == "Equipes":
    st.title("👥 Equipes")
    st.markdown("Conheça as equipes responsáveis pela execução do projeto")
    
    st.markdown("---")
    
    for idx, team in enumerate(TEAMS, 1):
        st.markdown(f"""
            <div class="team-card">
                <div class="team-header">{team['name']}</div>
                <p><strong>Membros:</strong> {team['members']} colaboradores</p>
                <p><strong>Descrição:</strong> {team['description']}</p>
                <p><strong>Áreas de Responsabilidade:</strong></p>
        """, unsafe_allow_html=True)
        
        for area in team['areas']:
            st.markdown(f"  • {area}")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if idx < len(TEAMS):
            st.markdown("---")

# PÁGINA: ROTEIRO OPERACIONAL
elif page == "Roteiro Operacional":
    st.title("📅 Roteiro Operacional")
    st.markdown("Fases de execução do projeto")
    
    st.markdown("---")
    
    for phase in OPERATIONAL_PHASES:
        with st.container():
            col1, col2 = st.columns([0.15, 0.85])
            
            with col1:
                st.markdown(f"""
                    <div style="background: #009678; color: white; width: 50px; height: 50px; 
                    border-radius: 50%; display: flex; align-items: center; justify-content: center; 
                    font-weight: bold; font-size: 1.2em;">
                    {phase['phase']}
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"### Fase {phase['phase']}: {phase['name']}")
                st.markdown(f"**{phase['description']}**")
                
                st.markdown("**Atividades:**")
                for activity in phase['activities']:
                    st.markdown(f"  ✓ {activity}")
        
        st.markdown("---")

# PÁGINA: RECURSOS
elif page == "Recursos":
    st.title("🛠️ Recursos e Materiais")
    st.markdown("Equipamentos, EPIs e materiais utilizados no projeto")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🔧 Equipamentos")
        for equipment in RESOURCES['equipment']:
            st.markdown(f"• {equipment}")
    
    with col2:
        st.subheader("🦺 EPIs (Equipamentos de Proteção)")
        for ppe in RESOURCES['ppe']:
            st.markdown(f"• {ppe}")
    
    with col3:
        st.subheader("📦 Materiais")
        for material in RESOURCES['materials']:
            st.markdown(f"• {material}")
    
    st.markdown("---")
    
    st.subheader("✅ Checklist de Segurança")
    st.markdown("Antes de iniciar qualquer atividade, verificar:")
    
    for idx, item in enumerate(SAFETY_CHECKLIST, 1):
        st.markdown(f"{idx}. {item}")

# PÁGINA: SOBRE O PROJETO
elif page == "Sobre o Projeto":
    st.title("ℹ️ Sobre o Projeto")
    
    st.markdown("---")
    
    st.subheader("📖 O Projeto Aliança por Floripa")
    st.markdown("""
    O **Projeto Aliança por Floripa** é uma iniciativa colaborativa que visa transformar o centro histórico 
    de Florianópolis através de ações de limpeza, revitalização e reinserção social.
    
    Unindo forças de múltiplas organizações, o projeto trabalha para:
    - Melhorar a qualidade de vida urbana
    - Proporcionar oportunidades de trabalho
    - Reinserir pessoas em vulnerabilidade social
    - Transformar espaços públicos
    """)
    
    st.markdown("---")
    
    st.subheader("🤝 Parceiros")
    
    partners_html = ""
    for partner in PARTNERS:
        partners_html += f"""
        <div class="partner-badge">
            <div class="partner-name">{partner['name']}</div>
            <small>{partner['description']}</small>
        </div>
        """
    
    st.markdown(partners_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("🌐 Links Úteis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"[Site Oficial]({PROJECT_INFO['website']})")
    
    with col2:
        st.markdown("[Entre em Contato](https://www.aliancaporfloripa.com.br/)")
    
    st.markdown("---")
    
    st.info("""
    **Transparência e Impacto**
    
    Este projeto é desenvolvido com total transparência, garantindo que cada contribuição seja 
    aplicada de forma efetiva para transformar a realidade do centro histórico de Florianópolis 
    e reinserir pessoas na sociedade através de capacitação e oportunidades de trabalho.
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em; padding: 20px;">
    <p>Projeto Aliança por Floripa © 2024 | Transformando o centro histórico de Florianópolis</p>
    </div>
""", unsafe_allow_html=True)

