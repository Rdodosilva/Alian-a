# 🚀 Guia de Deploy - Aliança por Floripa

## 📋 Pré-requisitos

- Conta no GitHub
- Python 3.8+ instalado (para testes locais)

## 🔧 Estrutura de Arquivos Necessários

Crie a seguinte estrutura no seu repositório:

```
alianca-por-floripa/
│
├── app.py                    # Código principal (já fornecido)
├── requirements.txt          # Dependências (já fornecido)
├── README.md                # Documentação (já fornecido)
└── .streamlit/
    └── config.toml          # Configurações (já fornecido)
```

## 📦 Passo 1: Criar Repositório no GitHub

1. Acesse [github.com](https://github.com)
2. Clique em **"New repository"**
3. Nome: `alianca-por-floripa`
4. Descrição: `Dashboard do projeto Aliança por Floripa`
5. Escolha **Public** ou **Private**
6. **NÃO** inicialize com README (vamos adicionar manualmente)
7. Clique em **"Create repository"**

## 📤 Passo 2: Fazer Upload dos Arquivos

### Opção A: Via Interface Web do GitHub

1. No repositório criado, clique em **"Add file" > "Upload files"**
2. Arraste os 4 arquivos:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - Crie pasta `.streamlit` e adicione `config.toml`
3. Commit: "Initial commit - Aliança por Floripa dashboard"
4. Clique em **"Commit changes"**

### Opção B: Via Git Command Line

```bash
# Inicializar repositório local
git init
git add .
git commit -m "Initial commit - Aliança por Floripa dashboard"

# Conectar ao GitHub (substitua SEU-USUARIO)
git remote add origin https://github.com/SEU-USUARIO/alianca-por-floripa.git
git branch -M main
git push -u origin main
```

## 🌐 Passo 3: Deploy no Streamlit Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io)

2. Clique em **"New app"**

3. Configure:
   - **Repository**: `seu-usuario/alianca-por-floripa`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: `alianca-floripa` (ou nome desejado)

4. Clique em **"Deploy!"**

5. Aguarde 2-3 minutos para o deploy completar

6. Seu app estará disponível em:
   ```
   https://alianca-floripa.streamlit.app
   ```

## ✅ Verificação do Deploy

Após o deploy, verifique se:

- ✅ O app carrega sem erros
- ✅ O mapa é exibido corretamente
- ✅ As cores estão corretas (verde, azul, vermelho)
- ✅ Correios e TICEN estão destacados em azul
- ✅ Todas as páginas funcionam
- ✅ A navegação no sidebar funciona

## 🔄 Atualizações Futuras

Para atualizar o app:

1. Edite os arquivos no GitHub
2. Faça commit das mudanças
3. O Streamlit Cloud irá automaticamente fazer redeploy

Ou via Git:
```bash
git add .
git commit -m "Descrição das mudanças"
git push origin main
```

## 🎨 Personalização de Cores

Para alterar as cores do projeto, edite `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#E63946"          # Cor principal (vermelho Aliança)
backgroundColor = "#FFFFFF"        # Fundo branco
secondaryBackgroundColor = "#F8F9FA"  # Fundo secundário cinza claro
textColor = "#333333"              # Texto cinza escuro
```

## 🗺️ Personalização do Mapa

Para adicionar/remover áreas, edite em `app.py`:

```python
# Áreas em andamento (AZUL)
areas_azul = [
    {
        'name': 'Nome da Área',
        'coords': [[lat1, lon1], [lat2, lon2], [lat3, lon3], [lat4, lon4]]
    }
]

# Áreas planejadas (VERMELHO)
areas_vermelho = [...]

# Áreas concluídas (VERDE)
areas_verde = [...]
```

## 📊 Adicionar Logo Customizada

1. Adicione a logo na pasta do projeto: `logo.png`

2. Atualize em `app.py`:
```python
with st.sidebar:
    st.image("logo.png", width=200)
```

3. Commit e push:
```bash
git add logo.png app.py
git commit -m "Adiciona logo customizada"
git push origin main
```

## 🐛 Solução de Problemas

### Erro: "Module not found"
- Verifique se `requirements.txt` está correto
- Redeploy manualmente no Streamlit Cloud

### Mapa não carrega
- Verifique conexão com internet
- Confirme que `streamlit-folium` está no requirements

### Cores erradas
- Limpe cache do navegador
- Verifique arquivo `config.toml`

### App muito lento
- Otimize coordenadas do mapa
- Reduza número de polígonos
- Use cache do Streamlit: `@st.cache_data`

## 📱 Compartilhamento

Após deploy bem-sucedido:

1. Copie a URL: `https://alianca-floripa.streamlit.app`
2. Compartilhe com:
   - Equipes do projeto
   - Parceiros (ACIF, CDL, Conseg)
   - Site oficial Aliança por Floripa
   - Redes sociais

## 🔒 Segurança

- O código é público (transparência do projeto)
- Não adicione senhas ou chaves de API no código
- Use Streamlit Secrets para dados sensíveis

## 📈 Analytics (Opcional)

Para adicionar Google Analytics:

1. Crie arquivo `index.html` na pasta `.streamlit`
2. Adicione código de tracking
3. Configure no Streamlit Cloud

## 🎉 Pronto!

Seu dashboard está no ar! 

Qualquer dúvida:
- Documentação Streamlit: [docs.streamlit.io](https://docs.streamlit.io)
- Fórum Streamlit: [discuss.streamlit.io](https://discuss.streamlit.io)

---

**Desenvolvido para o projeto Aliança por Floripa**
💚 Florianópolis unida para transformar vidas
