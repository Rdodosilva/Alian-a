import streamlit as st
import folium
from streamlit_folium import folium_static
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Aliança por Floripa",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #E63946 0%, #FF6B35 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #E63946;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .equipe-card {
        background: linear-gradient(135deg, #fff5f2 0%, #ffe8e8 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 6px solid #E63946;
        margin: 1rem 0;
    }
    .stButton>button {
        background: linear-gradient(135deg, #E63946 0%, #FF6B35 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 8px;
    }
    h1, h2, h3 {
        color: #E63946;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>❤️ Aliança por Floripa</h1>
    <p style="font-size: 1.2rem; margin: 0;">Plano de Revitalização do Centro Histórico</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/200x200/E63946/FFFFFF?text=Logo", width=200)
    st.markdown("### 🏛️ Navegação")
    page = st.radio("", [
        "🏠 Início",
        "🗺️ Mapa de Atuação",
        "👥 Equipes",
        "📋 Roteiro Operacional",
        "📊 Recursos",
        "💚 Sobre o Projeto"
    ])
    
    st.markdown("---")
    st.markdown("### 🤝 Parceiros")
    st.markdown("""
    - ACIF
    - CDL Florianópolis
    - Conseg Centro
    - Prefeitura de Florianópolis
    - Projeto Rumo Certo
    """)
    
    st.markdown("---")
    st.markdown("### 🔗 Links")
    st.markdown("[www.aliancaporfloripa.com.br](https://www.aliancaporfloripa.com.br)")

# Páginas
if page == "🏠 Início":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Áreas Prioritárias", "10", "")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Vasos Replantio", "69", "Felipe Schmidt")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Equipes", "2", "Atuação simultânea")
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
        st.success("✓ Baseado no projeto Rumo Certo comprovado")
    with col2:
        st.success("✓ Reinserção social com capacitação profissional")
        st.success("✓ Transparência total com auditoria pública")

elif page == "🗺️ Mapa de Atuação":
    st.markdown("## 🗺️ Mapa de Atuação")
    st.write("Visualize as áreas de trabalho no centro de Florianópolis")
    
    # Criar mapa com Folium
    m = folium.Map(
        location=[-27.5969, -48.5495],
        zoom_start=16,
        tiles='OpenStreetMap'
    )
    
    # Áreas em andamento (AZUL) - Correios e TICEN
    areas_azul = [
        {
            'name': 'Edifício dos Correios',
            'coords': [[-27.5950, -48.5510], [-27.5950, -48.5495], [-27.5960, -48.5495], [-27.5960, -48.5510]]
        },
        {
            'name': 'TICEN - Terminal Centro',
            'coords': [[-27.5990, -48.5515], [-27.5990, -48.5500], [-27.6000, -48.5500], [-27.6000, -48.5515]]
        }
    ]
    
    for area in areas_azul:
        folium.Polygon(
            locations=area['coords'],
            color='#007bff',
            fill=True,
            fillColor='#007bff',
            fillOpacity=0.5,
            weight=4,
            popup=f"<b>⚡ {area['name']}</b><br>Em Andamento"
        ).add_to(m)
    
    # Áreas planejadas (VERMELHO)
    areas_vermelho = [
        {'name': 'Rua Felipe Schmidt', 'coords': [[-27.5955, -48.5520], [-27.5955, -48.5480], [-27.5965, -48.5480], [-27.5965, -48.5520]]},
        {'name': 'Rua Conselheiro Mafra', 'coords': [[-27.5965, -48.5510], [-27.5965, -48.5475], [-27.5975, -48.5475], [-27.5975, -48.5510]]},
        {'name': 'Praça XV', 'coords': [[-27.5975, -48.5505], [-27.5975, -48.5485], [-27.5990, -48.5485], [-27.5990, -48.5505]]},
        {'name': 'Praça Fernando Machado', 'coords': [[-27.5985, -48.5520], [-27.5985, -48.5505], [-27.6000, -48.5505], [-27.6000, -48.5520]]},
        {'name': 'Rua Tiradentes', 'coords': [[-27.5960, -48.5470], [-27.5990, -48.5470], [-27.5990, -48.5480], [-27.5960, -48.5480]]},
        {'name': 'Calçadão João Pinto', 'coords': [[-27.5990, -48.5495], [-27.5990, -48.5475], [-27.6005, -48.5475], [-27.6005, -48.5495]]},
    ]
    
    for area in areas_vermelho:
        folium.Polygon(
            locations=area['coords'],
            color='#dc3545',
            fill=True,
            fillColor='#dc3545',
            fillOpacity=0.3,
            weight=2,
            popup=f"<b>📍 {area['name']}</b><br>Planejada"
        ).add_to(m)
    
    # Áreas concluídas (VERDE) - exemplo
    areas_verde = [
        {'name': 'Área exemplo', 'coords': [[-27.5945, -48.5520], [-27.5945, -48.5505], [-27.5955, -48.5505], [-27.5955, -48.5520]]}
    ]
    
    for area in areas_verde:
        folium.Polygon(
            locations=area['coords'],
            color='#28a745',
            fill=True,
            fillColor='#28a745',
            fillOpacity=0.4,
            weight=3,
            popup=f"<b>✓ {area['name']}</b><br>Concluída"
        ).add_to(m)
    
    # Exibir mapa
    folium_static(m, width=1200, height=600)
    
    # Legenda
    st.markdown("### 📊 Legenda")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("🟢 **Verde**: Áreas Concluídas")
    with col2:
        st.markdown("🔵 **Azul**: Em Andamento (Correios + TICEN)")
    with col3:
        st.markdown("🔴 **Vermelho**: Planejadas")

elif page == "👥 Equipes":
    st.markdown("## 👥 Distribuição das Equipes")
    
    st.markdown('<div class="equipe-card">', unsafe_allow_html=True)
    st.markdown("### 🟠 EQUIPE 1 — Zona Comercial Norte")
    st.write("**Foco:** Revitalização comercial")
    st.markdown("""
    - 📍 **Edifício dos Correios e entorno** *(Em andamento - Azul)*
    - 🌸 **Rua Felipe Schmidt** - Replantio de 69 vasos *(Planejada)*
    - 📍 **Rua Conselheiro Mafra** *(Planejada)*
    - 📍 **Rua Jerônimo Coelho** *(Planejada)*
    - 📍 **Rua Trajano** *(Planejada)*
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="equipe-card">', unsafe_allow_html=True)
    st.markdown("### 🔴 EQUIPE 2 — Praças e Zona Sul")
    st.write("**Foco:** Áreas de convivência")
    st.markdown("""
    - 🌳 **Praça XV de Novembro** *(Planejada)*
    - 🌳 **Praça Fernando Machado** *(Planejada)*
    - 📍 **Rua Tiradentes** *(Planejada)*
    - 📍 **Calçadão João Pinto** *(Planejada)*
    - 📍 **Ruas Saldanha Marinho e Nunes Machado** *(Planejada)*
    - 🏛️ **TICEN - Terminal Centro** *(Em andamento - Azul)*
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
        1. **Limpeza do Edifício dos Correios e entorno** *(EM ANDAMENTO)*
        2. **Replantio dos 69 vasos na Rua Felipe Schmidt** (atividade principal)
        3. **Varrição das Ruas** Conselheiro Mafra, Jerônimo Coelho e Trajano
        """)
    
    with st.expander("🔴 Fase 3: Execução — Equipe 2"):
        st.write("""
        1. **Jardinagem e limpeza da Praça XV de Novembro**
        2. **Manutenção da Praça Fernando Machado**
        3. **Varrição de ruas** Tiradentes, João Pinto, Saldanha Marinho
        4. **Limpeza do TICEN - Terminal Centro** *(EM ANDAMENTO)*
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
        - Substrato e terra
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
                padding: 2rem; border-radius: 10px; text-align: center; color: white;'>
        <h2 style='color: white; margin-bottom: 1rem;'>Faça Parte Desta Transformação</h2>
        <h3 style='color: white; margin-bottom: 1rem;'>www.aliancaporfloripa.com.br</h3>
        <p>Doe via PIX • Acompanhe resultados • Transforme vidas</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>Aliança por Floripa</strong> — Uma iniciativa da sociedade civil</p>
    <p>ACIF • CDL Florianópolis • Conseg Centro • Prefeitura de Florianópolis • Projeto Rumo Certo</p>
    <p style='font-size: 0.9rem; margin-top: 1rem;'>
        Desenvolvido para o projeto de revitalização do centro histórico de Florianópolis
    </p>
</div>
""", unsafe_allow_html=True)
