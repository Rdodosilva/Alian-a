# Dados do Projeto Aliança por Floripa

PROJECT_INFO = {
    "name": "Projeto Aliança por Floripa",
    "tagline": "Transformando o centro histórico de Florianópolis",
    "purpose": "Unir forças para transformar esmolas em oportunidades reais, garantindo que cada contribuição seja aplicada de forma transparente e efetiva para reinserir pessoas na sociedade através de capacitação e oportunidades de trabalho.",
    "website": "https://www.aliancaporfloripa.com.br/",
}

PARTNERS = [
    {"name": "ACIF", "description": "Associação Empresarial de Florianópolis"},
    {"name": "CDL Florianópolis", "description": "Câmara de Dirigentes Lojistas"},
    {"name": "Conseg Centro", "description": "Conselho de Segurança do Centro"},
    {"name": "Prefeitura de Florianópolis", "description": "Apoio institucional"},
    {"name": "Projeto Rumo Certo", "description": "Associação Alberto de Souza"},
]

MISSION = [
    "Realizar limpeza e revitalização do centro histórico",
    "Proporcionar capacitação e oportunidades de trabalho",
    "Transformar espaços públicos",
    "Reinserção social de pessoas em vulnerabilidade",
]

METRICS = {
    "areas": 10,
    "plants": 69,
    "collaborators": 20,
    "teams": 2,
}

# Áreas em andamento (Azul)
AREAS_IN_PROGRESS = [
    {
        "name": "Edifício dos Correios",
        "location": "Praça XV de Novembro, 242",
        "status": "em_andamento",
        "lat": -27.5948,
        "lng": -48.5476,
        "description": "Agência Central - Limpeza e revitalização da fachada e entorno"
    },
    {
        "name": "Terminal Cidade de Florianópolis",
        "location": "Centro - Antigo Terminal",
        "status": "em_andamento",
        "lat": -27.5960,
        "lng": -48.5460,
        "description": "Limpeza e revitalização do terminal antigo"
    }
]

# Áreas planejadas (Vermelho)
AREAS_PLANNED = [
    {
        "name": "Rua Felipe Schmidt",
        "location": "Centro",
        "status": "planejada",
        "lat": -27.5945,
        "lng": -48.5470,
        "description": "Replantio de 69 vasos de plantas"
    },
    {
        "name": "Praça XV de Novembro",
        "location": "Centro",
        "status": "planejada",
        "lat": -27.5948,
        "lng": -48.5476,
        "description": "Limpeza e revitalização da praça histórica"
    },
    {
        "name": "Praça Fernando Machado",
        "location": "Centro",
        "status": "planejada",
        "lat": -27.5955,
        "lng": -48.5485,
        "description": "Revitalização e limpeza da praça"
    },
    {
        "name": "Rua Conselheiro Mafra",
        "location": "Centro",
        "status": "planejada",
        "lat": -27.5950,
        "lng": -48.5465,
        "description": "Limpeza e revitalização da rua"
    },
    {
        "name": "Rua Jerônimo Coelho",
        "location": "Centro",
        "status": "planejada",
        "lat": -27.5940,
        "lng": -48.5480,
        "description": "Limpeza e revitalização da rua"
    },
    {
        "name": "Rua Trajano",
        "location": "Centro",
        "status": "planejada",
        "lat": -27.5935,
        "lng": -48.5475,
        "description": "Limpeza e revitalização da rua"
    },
    {
        "name": "Rua Tiradentes",
        "location": "Centro",
        "status": "planejada",
        "lat": -27.5930,
        "lng": -48.5490,
        "description": "Limpeza e revitalização da rua"
    },
    {
        "name": "Calçadão João Pinto",
        "location": "Centro",
        "status": "planejada",
        "lat": -27.5925,
        "lng": -48.5470,
        "description": "Limpeza e revitalização do calçadão"
    },
    {
        "name": "Rua Saldanha Marinho",
        "location": "Centro",
        "status": "planejada",
        "lat": -27.5920,
        "lng": -48.5485,
        "description": "Limpeza e revitalização da rua"
    },
    {
        "name": "Rua Nunes Machado",
        "location": "Centro",
        "status": "planejada",
        "lat": -27.5915,
        "lng": -48.5495,
        "description": "Limpeza e revitalização da rua"
    }
]

TEAMS = [
    {
        "name": "Equipe 1 - Zona Comercial Norte",
        "members": 10,
        "description": "Responsável pela limpeza e revitalização da zona comercial norte do centro",
        "areas": ["Edifício dos Correios", "Rua Felipe Schmidt", "Praça XV de Novembro"],
    },
    {
        "name": "Equipe 2 - Praças e Zona Sul",
        "members": 10,
        "description": "Responsável pelas praças e zona sul do centro histórico",
        "areas": ["Terminal Cidade de Florianópolis", "Praça Fernando Machado", "Rua Conselheiro Mafra"],
    }
]

OPERATIONAL_PHASES = [
    {
        "phase": 1,
        "name": "Preparação e Planejamento",
        "description": "Mobilização de recursos, treinamento de equipes e planejamento detalhado",
        "activities": [
            "Reunião de alinhamento com parceiros",
            "Treinamento de segurança e operacional",
            "Levantamento de materiais e equipamentos",
            "Definição de cronograma"
        ]
    },
    {
        "phase": 2,
        "name": "Limpeza Profunda",
        "description": "Limpeza intensiva das áreas prioritárias",
        "activities": [
            "Limpeza de fachadas e calçadas",
            "Remoção de detritos e lixo",
            "Limpeza de áreas verdes",
            "Higienização geral"
        ]
    },
    {
        "phase": 3,
        "name": "Revitalização e Plantio",
        "description": "Plantio de vasos e revitalização de espaços",
        "activities": [
            "Replantio de 69 vasos de plantas",
            "Preparação de canteiros",
            "Revitalização de áreas verdes",
            "Manutenção de plantas"
        ]
    },
    {
        "phase": 4,
        "name": "Manutenção Contínua",
        "description": "Manutenção periódica e acompanhamento",
        "activities": [
            "Limpeza semanal das áreas",
            "Manutenção de plantas",
            "Monitoramento de qualidade",
            "Relatórios de progresso"
        ]
    }
]

RESOURCES = {
    "equipment": [
        "Varredoras mecânicas Kärcher",
        "Pás e vassouras profissionais",
        "Sacos para coleta de lixo",
        "Carrinhos de coleta",
        "Mangueiras e bombas de água",
        "Ferramentas de jardinagem"
    ],
    "ppe": [
        "Coletes de segurança",
        "Luvas de proteção",
        "Botas de segurança",
        "Bonés/chapéus",
        "Óculos de proteção",
        "Máscaras respiratórias"
    ],
    "materials": [
        "Plantas e vasos (69 unidades)",
        "Terra e adubo",
        "Sacos de lixo",
        "Produtos de limpeza",
        "Água para limpeza",
        "Materiais de sinalização"
    ]
}

SAFETY_CHECKLIST = [
    "Verificar condições climáticas",
    "Inspecionar equipamentos",
    "Distribuir EPIs adequados",
    "Fazer briefing de segurança",
    "Verificar sinalização de área",
    "Confirmar comunicação entre equipes",
    "Verificar primeiros socorros disponíveis",
    "Definir zona de trabalho segura"
]

