# Projeto Aliança por Floripa

## Descrição

Aplicação Streamlit interativa para o **Projeto Aliança por Floripa**, uma iniciativa colaborativa de revitalização do centro histórico de Florianópolis.

O projeto une forças de múltiplas organizações para:
- Realizar limpeza e revitalização do centro histórico
- Proporcionar capacitação e oportunidades de trabalho
- Transformar espaços públicos
- Reinserir pessoas em vulnerabilidade social

## Funcionalidades

### 📊 Dashboard
- Métricas principais do projeto (áreas, vasos, colaboradores)
- Propósito e missão do projeto
- Status atual das atividades
- Link para o site oficial

### 🗺️ Mapa de Atuação
- Mapa interativo com as áreas de atuação
- Visualização de áreas em andamento (azul) e planejadas (vermelho)
- Informações detalhadas de cada localidade

### 👥 Equipes
- Informações sobre as 2 equipes de trabalho
- Áreas de responsabilidade
- Número de colaboradores

### 📅 Roteiro Operacional
- 4 fases de execução do projeto
- Atividades detalhadas de cada fase
- Cronograma de implementação

### 🛠️ Recursos e Materiais
- Lista de equipamentos utilizados
- EPIs (Equipamentos de Proteção Individual)
- Materiais necessários
- Checklist de segurança

### ℹ️ Sobre o Projeto
- Informações gerais do projeto
- Parceiros envolvidos
- Links úteis
- Compromisso com transparência

## Instalação

### Pré-requisitos
- Python 3.8+
- pip

### Passos

1. Clone ou baixe o projeto:
```bash
cd alianca-floripa
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
streamlit run app.py
```

4. A aplicação abrirá automaticamente em seu navegador (geralmente em `http://localhost:8501`)

## Estrutura do Projeto

```
alianca-floripa/
├── app.py                    # Aplicação principal do Streamlit
├── requirements.txt          # Dependências do projeto
├── README.md                 # Este arquivo
├── .streamlit/
│   └── config.toml          # Configurações do Streamlit
├── assets/
│   └── logo.png             # Logo do projeto
└── data/
    └── project_data.py      # Dados do projeto
```

## Dados do Projeto

### Áreas de Atuação

#### Em Andamento (Azul)
- Edifício dos Correios - Agência Central (Praça XV de Novembro, 242)
- Terminal Cidade de Florianópolis (antigo terminal)

#### Planejadas (Vermelho)
- Rua Felipe Schmidt (replantio de 69 vasos)
- Praça XV de Novembro
- Praça Fernando Machado
- Rua Conselheiro Mafra
- Rua Jerônimo Coelho
- Rua Trajano
- Rua Tiradentes
- Calçadão João Pinto
- Rua Saldanha Marinho
- Rua Nunes Machado

### Equipes

**Equipe 1 - Zona Comercial Norte**
- 10 colaboradores
- Responsável pela zona comercial norte do centro

**Equipe 2 - Praças e Zona Sul**
- 10 colaboradores
- Responsável pelas praças e zona sul do centro

### Parceiros

- ACIF (Associação Empresarial de Florianópolis)
- CDL Florianópolis
- Conseg Centro
- Prefeitura de Florianópolis (apoio)
- Projeto Rumo Certo (Associação Alberto de Souza)

## Configuração

As configurações do Streamlit estão em `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#009678"
backgroundColor = "#f0f5f5"
secondaryBackgroundColor = "#ffffff"
textColor = "#1a1a1a"
```

## Desenvolvimento

Para modificar os dados do projeto, edite o arquivo `data/project_data.py`.

### Adicionar uma nova área
```python
AREAS_PLANNED.append({
    "name": "Nome da Área",
    "location": "Localização",
    "status": "planejada",
    "lat": -27.5945,
    "lng": -48.5475,
    "description": "Descrição"
})
```

### Adicionar uma nova equipe
```python
TEAMS.append({
    "name": "Nome da Equipe",
    "members": 10,
    "description": "Descrição",
    "areas": ["Área 1", "Área 2"]
})
```

## Deploy

### Streamlit Cloud

1. Faça push do código para um repositório GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório GitHub
4. Selecione o arquivo `app.py` como ponto de entrada

### Heroku

1. Crie um arquivo `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Deploy:
```bash
git push heroku main
```

### Docker

1. Crie um `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

2. Build e execute:
```bash
docker build -t alianca-floripa .
docker run -p 8501:8501 alianca-floripa
```

## Contribuindo

Para contribuir com melhorias:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto é de código aberto e disponível sob a licença MIT.

## Contato

Para mais informações sobre o Projeto Aliança por Floripa:
- Website: https://www.aliancaporfloripa.com.br/
- Email: contato@aliancaporfloripa.com.br

## Changelog

### v1.0.0 (2024-10-31)
- Versão inicial da aplicação
- Dashboard com métricas
- Mapa interativo
- Seção de equipes
- Roteiro operacional
- Recursos e materiais
- Informações sobre o projeto

---

**Projeto Aliança por Floripa** © 2024 | Transformando o centro histórico de Florianópolis

