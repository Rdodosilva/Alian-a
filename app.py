import streamlit as st
import folium
from streamlit_folium import folium_static
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Aliança por Floripa",
    page_icon="💚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #E63946 0%, #FF6B35 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 30px rgba(230,57,70,0.3);
    }
    .main-header h1 {
        color: white !important;
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
    }
    .logo-home {
        text-align: center;
        margin: 2rem 0;
    }
    .metric-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        border-left: 6px solid #E63946;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    .equipe-card {
        background: linear-gradient(135deg, #fff5f2 0%, #ffe8e8 100%);
        padding: 2rem;
        border-radius: 12px;
        border-left: 6px solid #E63946;
        margin: 1.5rem 0;
        box-shadow: 0 3px 15px rgba(0,0,0,0.08);
    }
    .stButton>button {
        background: linear-gradient(135deg, #E63946 0%, #FF6B35 100%);
        color: white;
        font-weight: 700;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(230,57,70,0.3);
    }
    h1, h2, h3 {
        color: #E63946;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #fff 0%, #f8f9fa 100%);
    }
    .parceiro-badge {
        background: #f8f9fa;
        padding: 8px 15px;
        border-radius: 20px;
        display: inline-block;
        margin: 5px;
        border: 2px solid #E63946;
        color: #E63946;
        font-weight: 600;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Logo SVG do projeto
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <svg width="150" height="150" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(100,100)">
                <path d="M-15,-60 L-10,-50 L-5,-55 L0,-50 L5,-55 L10,-50 L15,-60 L10,-65 L0,-70 L-10,-65 Z" fill="#FF6B35"/>
                <path d="M60,-15 L50,-10 L55,-5 L50,0 L55,5 L50,10 L60,15 L65,10 L70,0 L65,-10 Z" fill="#D95323"/>
                <path d="M15,60 L10,50 L5,55 L0,50 L-5,55 L-10,50 L-15,60 L-10,65 L0,70 L10,65 Z" fill="#E8737F"/>
                <path d="M-60,15 L-50,10 L-55,5 L-50,0 L-55,-5 L-50,-10 L-60,-15 L-65,-10 L-70,0 L-65,10 Z" fill="#C9525F"/>
            </g>
            <path d="M100 70 C85 70 75 80 75 92 C75 100 80 107 90 117 L100 127 L110 117 C120 107 125 100 125 92 C125 80 115 70 100 70 Z" fill="#E63946" stroke="#fff" stroke-width="3"/>
            <ellipse cx="92" cy="85" rx="10" ry="14" fill="white" opacity="0.5"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: #E63946;'>Aliança por Floripa</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-size: 0.9rem;'>Florianópolis unida para transformar vidas</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🏛️ Navegação")
    page = st.radio("", [
        "🏠 Início",
        "🗺️ Mapa de Atuação",
        "👥 Equipes",
        "📋 Roteiro Operacional",
        "📊 Recursos",
        "💚 Sobre o Projeto"
    ], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("### 🤝 Parceiros")
    st.markdown("""
    <div style='text-align: center;'>
        <span class='parceiro-badge'>ACIF</span>
        <span class='parceiro-badge'>CDL</span>
        <span class='parceiro-badge'>Conseg</span>
        <span class='parceiro-badge'>Prefeitura</span>
        <span class='parceiro-badge'>Rumo Certo</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔗 Site Oficial")
    st.markdown("[www.aliancaporfloripa.com.br](https://www.aliancaporfloripa.com.br)")

# Páginas
if page == "🏠 Início":
    # Logo grande na home
    st.markdown("""
    <div class='logo-home'>
        <svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(100,100)">
                <path d="M-15,-60 L-10,-50 L-5,-55 L0,-50 L5,-55 L10,-50 L15,-60 L10,-65 L0,-70 L-10,-65 Z" fill="#FF6B35"/>
                <path d="M60,-15 L50,-10 L55,-5 L50,0 L55,5 L50,10 L60,15 L65,10 L70,0 L65,-10 Z" fill="#D95323"/>
                <path d="M15,60 L10,50 L5,55 L0,50 L-5,55 L-10,50 L-15,60 L-10,65 L0,70 L10,65 Z" fill="#E8737F"/>
                <path d="M-60,15 L-50,10 L-55,5 L-50,0 L-55,-5 L-50,-10 L-60,-15 L-65,-10 L-70,0 L-65,10 Z" fill="#C9525F"/>
            </g>
            <path d="M100 70 C85 70 75 80 75 92 C75 100 80 107 90 117 L100 127 L110 117 C120 107 125 100 125 92 C125 80 115 70 100 70 Z" fill="#E63946" stroke="#fff" stroke-width="3"/>
            <ellipse cx="92" cy="85" rx="10" ry="14" fill="white" opacity="0.5"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="main-header">
        <h1>💚 Aliança por Floripa</h1>
        <p style="font-size: 1.3rem; margin: 0;">Plano de Revitalização do Centro Histórico</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Áreas Prioritárias", "10", "Centro Histórico")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Vasos para Replantio", "69", "Rua Felipe Schmidt")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Equipes de Trabalho", "2", "Atuação simultânea")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("## 💚 Sobre o Projeto")
    st.write("""
    **A Aliança por Floripa é uma iniciativa da sociedade civil** que reúne a ACIF 
    (Associação Empresarial de Florianópolis), a CDL Florianópolis e o Conseg Centro, 
    com apoio da Prefeitura de Florianópolis e do projeto Rumo Certo da Associação Alberto de Souza.
    """)
    
    st.info("""
    **🎯 Nosso Propósito:**  
    Unir forças para transformar esmolas em oportunidades reais, garantindo que cada 
    contribuição seja aplicada de forma transparente e efetiva para reinserir pessoas 
    na sociedade através de capacitação e oportunidades de trabalho digno.
    """)
    
    st.markdown("### ✓ Como Funciona")
    col1, col2 = st.columns(2)
    with col1:
        st.success("✓ Fundo único gerido por ACIF, CDL e CONSEG Centro")
        st.success("✓ Baseado no projeto Rumo Certo com resultados comprovados")
    with col2:
        st.success("✓ Reinserção social com capacitação profissional")
        st.success("✓ Transparência total com auditoria pública regular")

elif page == "🗺️ Mapa de Atuação":
    st.markdown("## 🗺️ Mapa de Atuação - Centro de Florianópolis")
    st.write("Áreas de trabalho com delimitação precisa das ruas e praças")
    
    # Criar mapa com Folium
    m = folium.Map(
        location=[-27.5950, -48.5490],
        zoom_start=16.5,
        tiles='OpenStreetMap'
    )
    
    # AZUL - Em Andamento: Agência Central dos Correios (Praça XV)
    correios_coords = [
        [-27.5952, -48.5492],
        [-27.5950, -48.5492],
        [-27.5950, -48.5488],
        [-27.5952, -48.5488]
    ]
    
    folium.Polygon(
        locations=correios_coords,
        color='#007bff',
        fill=True,
        fillColor='#007bff',
        fillOpacity=0.6,
        weight=4,
        popup="<b>⚡ Agência Central dos Correios</b><br>Praça XV, 242<br><span style='color: #007bff;'>EM ANDAMENTO</span>"
    ).add_to(m)
    
    # AZUL - Terminal Cidade de Florianópolis (antigo)
    terminal_coords = [
        [-27.5990, -48.5513],
        [-27.5985, -48.5513],
        [-27.5985, -48.5508],
        [-27.5990, -48.5508]
    ]
    
    folium.Polygon(
        locations=terminal_coords,
        color='#007bff',
        fill=True,
        fillColor='#007bff',
        fillOpacity=0.6,
        weight=4,
        popup="<b>⚡ Terminal Cidade de Florianópolis</b><br><span style='color: #007bff;'>EM ANDAMENTO</span>"
    ).add_to(m)
    
    # VERMELHO - Rua Felipe Schmidt (linha da rua)
    felipe_schmidt_coords = [
        [-27.5958, -48.5492],
        [-27.5958, -48.5505],
        [-27.5960, -48.5505],
        [-27.5960, -48.5492]
    ]
    
    folium.Polygon(
        locations=felipe_schmidt_coords,
        color='#dc3545',
        fill=True,
        fillColor='#dc3545',
        fillOpacity=0.4,
        weight=3,
        popup="<b>📍 Rua Felipe Schmidt</b><br>Replantio de 69 vasos<br><span style='color: #dc3545;'>PLANEJADA</span>"
    ).add_to(m)
    
    # VERMELHO - Praça XV de Novembro
    praca_xv_coords = [
        [-27.5952, -48.5495],
        [-27.5952, -48.5485],
        [-27.5958, -48.5485],
        [-27.5958, -48.5495]
    ]
    
    folium.Polygon(
        locations=praca_xv_coords,
        color='#dc3545',
        fill=True,
        fillColor='#dc3545',
        fillOpacity=0.4,
        weight=3,
        popup="<b>📍 Praça XV de Novembro</b><br>Jardinagem e limpeza<br><span style='color: #dc3545;'>PLANEJADA</span>"
    ).add_to(m)
    
    # VERMELHO - Praça Fernando Machado
    praca_fernando_coords = [
        [-27.5970, -48.5515],
        [-27.5970, -48.5505],
        [-27.5980, -48.5505],
        [-27.5980, -48.5515]
    ]
    
    folium.Polygon(
        locations=praca_fernando_coords,
        color='#dc3545',
        fill=True,
        fillColor='#dc3545',
        fillOpacity=0.4,
        weight=3,
        popup="<b>📍 Praça Fernando Machado</b><br>Manutenção de áreas verdes<br><span style='color: #dc3545;'>PLANEJADA</span>"
    ).add_to(m)
    
    # VERMELHO - Rua Conselheiro Mafra (linha da rua)
    mafra_coords = [
        [-27.5962, -48.5495],
        [-27.5962, -48.5480],
        [-27.5964, -48.5480],
        [-27.5964, -48.5495]
    ]
    
    folium.Polygon(
        locations=mafra_coords,
        color='#dc3545',
        fill=True,
        fillColor='#dc3545',
        fillOpacity=0.4,
        weight=3,
        popup="<b>📍 Rua Conselheiro Mafra</b><br>Varrição e higienização<br><span style='color: #dc3545;'>PLANEJADA</span>"
    ).add_to(m)
    
    # VERMELHO - Rua Tiradentes (linha da rua)
    tiradentes_coords = [
        [-27.5945, -48.5485],
        [-27.5945, -48.5470],
        [-27.5947, -48.5470],
        [-27.5947, -48.5485]
    ]
    
    folium.Polygon(
        locations=tiradentes_coords,
        color='#dc3545',
        fill=True,
        fillColor='#dc3545',
        fillOpacity=0.4,
        weight=3,
        popup="<b>📍 Rua Tiradentes</b><br>Limpeza de vias<br><span style='color: #dc3545;'>PLANEJADA</span>"
    ).add_to(m)
    
    # VERMELHO - Calçadão João Pinto
    joao_pinto_coords = [
        [-27.5975, -48.5490],
        [-27.5975, -48.5475],
        [-27.5977, -48.5475],
        [-27.5977, -48.5490]
    ]
    
    folium.Polygon(
        locations=joao_pinto_coords,
        color='#dc3545',
        fill=True,
        fillColor='#dc3545',
        fillOpacity=0.4,
        weight=3,
        popup="<b>📍 Calçadão João Pinto</b><br>Limpeza completa<br><span style='color: #dc3545;'>PLANEJADA</span>"
    ).add_to(m)
    
    # Exibir mapa
    folium_static(m, width=1200, height=650)
    
    # Legenda
    st.markdown("### 📊 Legenda do Mapa")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("🔵 **Azul - Em Andamento:**")
        st.write("• Agência Central dos Correios (Praça XV, 242)")
        st.write("• Terminal Cidade de Florianópolis")
    with col2:
        st.markdown("🔴 **Vermelho - Planejadas:**")
        st.write("• Ruas: Felipe Schmidt, Conselheiro Mafra, Tiradentes, João Pinto")
        st.write("• Praças: XV de Novembro e Fernando Machado")

elif page == "👥 Equipes":
    st.markdown("## 👥 Distribuição das Equipes")
    
    st.markdown('<div class="equipe-card">', unsafe_allow_html=True)
    st.markdown("### 🟠 EQUIPE 1 — Zona Comercial Norte")
    st.write("**Foco:** Revitalização comercial e replantio")
    st.markdown("""
    - 🔵 **Agência Central dos Correios** (Praça XV, 242) - *EM ANDAMENTO*
    - 🌸 **Rua Felipe Schmidt** - Replantio de 69 vasos ornamentais
    - 📍 **Rua Conselheiro Mafra** - Varrição e higienização
    - 📍 **Rua Jerônimo Coelho**
    - 📍 **Rua Trajano**
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="equipe-card">', unsafe_allow_html=True)
    st.markdown("### 🔴 EQUIPE 2 — Praças e Zona Sul")
    st.write("**Foco:** Áreas de convivência e espaços públicos")
    st.markdown("""
    - 🌳 **Praça XV de Novembro** - Jardinagem e limpeza de mobiliário
    - 🌳 **Praça Fernando Machado** - Manutenção de áreas verdes
    - 📍 **Rua Tiradentes** - Varrição
    - 📍 **Calçadão João Pinto** - Limpeza completa
    - 📍 **Ruas Saldanha Marinho e Nunes Machado**
    - 🔵 **Terminal Cidade de Florianópolis** - *EM ANDAMENTO*
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📋 Roteiro Operacional":
    st.markdown("## 📋 Roteiro Operacional")
    
    with st.expander("🔄 Fase 1: Preparação e Briefing", expanded=True):
        st.write("""
        - Encontro de todas as equipes no ponto de reunião central
        - Distribuição de EPIs (luvas, coletes identificados, bonés)
        - Distribuição de materiais, ferramentas e equipamentos
        - Briefing detalhado com orientações de segurança
        - Deslocamento organizado para as áreas de atuação
        """)
    
    with st.expander("🟠 Fase 2: Execução — Equipe 1"):
        st.write("""
        1. **Limpeza da Agência dos Correios** (Praça XV, 242) - *EM ANDAMENTO*
        2. **Replantio dos 69 vasos na Rua Felipe Schmidt** (atividade principal)
        3. **Varrição das Ruas** Conselheiro Mafra, Jerônimo Coelho e Trajano
        """)
    
    with st.expander("🔴 Fase 3: Execução — Equipe 2"):
        st.write("""
        1. **Jardinagem da Praça XV de Novembro**
        2. **Manutenção da Praça Fernando Machado**
        3. **Limpeza do Terminal Cidade** - *EM ANDAMENTO*
        4. **Varrição de ruas** Tiradentes, João Pinto, Saldanha Marinho
        """)
    
    with st.expander("📸 Fase 4: Finalização e Registro"):
        st.write("""
        - Recolhimento de materiais e ferramentas
        - Registro fotográfico "antes e depois"
        - Reunião de avaliação
        - Relatório de atividades
        - Documentação para prestação de contas
        """)

elif page == "📊 Recursos":
    st.markdown("## 📊 Recursos e Materiais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🧹 Equipamentos de Limpeza")
        st.write("""
        - Vassouras profissionais
        - Pás coletoras
        - Carrinhos de recolhimento
        - Sacos de lixo resistentes (100L)
        - Mangueiras de alta pressão
        - Lavadora de alta pressão
        """)
        
        st.markdown("### 🦺 EPIs e Segurança")
        st.write("""
        - Luvas de proteção
        - Coletes identificados
        - Bonés/chapéus
        - Protetor solar
        - Garrafas de água
        - Kit primeiros socorros
        """)
    
    with col2:
        st.markdown("### 🌱 Jardinagem")
        st.write("""
        - **69 mudas/flores** para Felipe Schmidt
        - Substrato e terra de qualidade
        - Adubo orgânico
        - Regadores
        - Ferramentas de jardinagem
        - Tesouras de poda
        """)
        
        st.markdown("### 📋 Apoio Logístico")
        st.write("""
        - Veículos para transporte
        - Sinalização de segurança
        - Cones de trânsito
        - Câmeras fotográficas
        - Coordenação por rádio/celular
        """)
    
    st.warning("""
    **⚠️ Checklist de Segurança Obrigatório:**
    - Uso obrigatório de EPIs durante toda operação
    - Sinalização adequada nas áreas de trabalho
    - Hidratação constante da equipe
    - Pausas regulares programadas
    """)

else:  # Sobre o Projeto
    st.markdown("## 💚 Sobre o Projeto Aliança por Floripa")
    
    st.write("""
    A Aliança por Floripa é uma **iniciativa da sociedade civil** que reúne a ACIF, 
    a CDL e o Conseg Centro, com apoio da Prefeitura de Florianópolis e do projeto 
    Rumo Certo da Associação Alberto de Souza.
    """)
    
    st.info("""
    **🎯 Nosso Propósito**
    
    Unir forças para transformar esmolas em oportunidades reais, garantindo que cada 
    contribuição seja aplicada de forma transparente e efetiva para reinserir pessoas 
    na sociedade através de capacitação e oportunidades de trabalho digno.
    """)
    
    st.markdown("### 📊 Impacto Esperado")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("""
        **🌆 Impacto Urbano**
        - Centro mais limpo e organizado
        - Espaços públicos revitalizados
        - Valorização do comércio local
        - Atração de visitantes
        """)
    
    with col2:
        st.success("""
        **👥 Impacto Social**
        - Oportunidades de trabalho
        - Capacitação profissional
        - Reinserção social efetiva
        - Dignidade e cidadania
        """)
    
    st.markdown("### 🔍 Transparência")
    st.write("""
    - **Gestão Compartilhada**: Fundo gerido por ACIF, CDL e CONSEG Centro
    - **Auditoria Regular**: Prestação de contas pública
    - **Relatórios Periódicos**: Acompanhamento de resultados alcançados
    """)
    
    st.markdown("---")
    st.markdown("### 🔗 Saiba Mais")
    st.markdown("""
    <div style='background: linear-gradient(135deg, #E63946 0%, #FF6B35 100%); 
                padding: 2.5rem; border-radius: 15px; text-align: center; color: white;'>
        <h2 style='color: white; margin-bottom: 1rem;'>💚 Faça Parte Desta Transformação</h2>
        <h3 style='color: white; margin-bottom: 1rem; font-size: 2rem;'>www.aliancaporfloripa.com.br</h3>
        <p style='font-size: 1.1rem;'>Doe via PIX • Acompanhe resultados • Transforme vidas</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p style='font-size: 1.1rem;'><strong>Aliança por Floripa</strong> — Uma iniciativa da sociedade civil</p>
    <p style='margin: 1rem 0;'>ACIF • CDL Florianópolis • Conseg Centro • Prefeitura de Florianópolis • Projeto Rumo Certo</p>
    <p style='font-size: 0.9rem; margin-top: 1.5rem; color: #999;'>
        Desenvolvido para o projeto de revitalização do centro histórico de Florianópolis
    </p>
</div>
""", unsafe_allow_html=True)
