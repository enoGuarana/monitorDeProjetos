# 🏛️ Painel de Monitoramento de Projetos - CGDIN

Este é um dashboard interativo desenvolvido em Python utilizando a biblioteca **Streamlit**. O objetivo é fornecer uma visão estratégica e em tempo real dos projetos da Coordenação-Geral, permitindo o acompanhamento de prazos, progresso e impedimentos.

🔗 **Acesse o Painel:** [https://monitordeprojetoscgdin.streamlit.app/](https://monitordeprojetoscgdin.streamlit.app/)

## 📊 Funcionalidades
- **Indicadores Rápidos (KPIs):** Total de projetos, projetos concluídos, em andamento e impedimentos.
- **Gráficos Dinâmicos:** Visualização de progresso (%) por projeto através de gráficos de barras interativos.
- **Filtros Personalizados:** Filtragem por Status e Responsável na barra lateral.
- **Detalhamento Técnico:** Tabela completa com informações de equipe, próximas entregas e atualizações semanais.

## 🛠️ Tecnologias Utilizadas
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) (Interface Web)
- [Pandas](https://pandas.pydata.org/) (Tratamento de Dados)
- [Plotly Express](https://plotly.com/python/) (Gráficos Interativos)

## 📂 Estrutura de Arquivos
- `monitoramento.py`: Código-fonte principal da aplicação.
- `dados.csv`: Arquivo de dados (atualizado via download do Excel Web).
- `requirements.txt`: Lista de bibliotecas necessárias para o deploy.

## 🚀 Como Atualizar os Dados
O painel consome os dados diretamente do arquivo `dados.csv` (ou `.xlsx`) presente neste repositório. Para atualizar o dashboard:
1. Edite os dados no seu **Excel Web**.
2. Salve uma cópia como **CSV** ou **Excel** na sua máquina.
3. Faça o upload do arquivo atualizado para este repositório do GitHub.
4. O Streamlit Cloud detectará a mudança e atualizará o site automaticamente.

## 💻 Instalação Local (Para Desenvolvimento)
Caso deseje rodar o projeto localmente:

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSIITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSIITORIO.git)

2. Instale as dependências:
pip install -r requirements.txt

3.Execute a aplicação:
streamlit run monitoramento.py
