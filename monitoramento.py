import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Configuração da Página
st.set_page_config(page_title="Dashboard Ministerial", layout="wide", page_icon="🏛️")

# 2. Função de carregamento inteligente (Lê Excel ou CSV)
@st.cache_data(ttl=2)
def load_data():
    # Lista de nomes que o ficheiro pode ter (ajustado para o que vimos no teu PC)
    arquivos_possiveis = ["dados.xlsx.xlsx", "dados.xlsx", "dados.csv"]
    
    df = None
    for nome in arquivos_possiveis:
        if os.path.exists(nome):
            try:
                if nome.endswith('.csv'):
                    df = pd.read_csv(nome)
                else:
                    df = pd.read_excel(nome)
                break 
            except Exception:
                continue
    
    if df is not None:
        # Tratamento das colunas conforme a tua planilha real
        df['Progresso'] = pd.to_numeric(df['Progresso'], errors='coerce').fillna(0).astype(int)
        df['Status'] = df['Status'].fillna('A definir')
        return df
    return None

df = load_data()

# Verificação de erro se o arquivo não existir
if df is None:
    st.error("❌ Nenhum ficheiro de dados encontrado (dados.xlsx ou dados.csv).")
    st.info("Certifica-te de que o ficheiro está na mesma pasta que este script no GitHub ou no teu PC.")
    st.stop()

# --- INTERFACE DO DASHBOARD ---

st.title("🏛️ Monitoramento de Projetos Estratégicos")
st.markdown(f"**Status:** Dados carregados com sucesso.")

# 3. Sidebar (Barra Lateral) com Filtros e Download
st.sidebar.title("⚙️ Gestão e Filtros")

# Filtro de Status
status_opcoes = df['Status'].unique().tolist()
status_sel = st.sidebar.multiselect("Filtrar Status:", status_opcoes, default=status_opcoes)

# Aplicar Filtro
df_filtered = df[df['Status'].isin(status_sel)]

# --- BOTÃO DE DOWNLOAD NA SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.subheader("📥 Exportar")
csv = df_filtered.to_csv(index=False).encode('utf-8')

st.sidebar.download_button(
    label="Baixar Relatório (CSV)",
    data=csv,
    file_name='relatorio_projetos_cgdin.csv',
    mime='text/csv',
)
# ------------------------------------

# 4. Indicadores Rápidos (KPIs)
k1, k2, k3 = st.columns(3)
k1.metric("Projetos Ativos", len(df_filtered))
k2.metric("✅ Concluídos", len(df_filtered[df_filtered['Status'] == 'Concluído']))
k3.metric("🚨 Impedimentos", len(df_filtered[df_filtered['Status'] == 'Impedimento']))

# 5. Gráfico de Progresso
st.subheader("🚀 Evolução por Projeto")
fig = px.bar(
    df_filtered, 
    x='Projeto', 
    y='Progresso', 
    color='Status',
    color_discrete_map={
        'Concluído': '#2ecc71', 
        'Em andamento': '#3498db', 
        'Impedimento': '#e74c3c',
        'A definir': '#95a5a6'
    },
    text_auto=True
)
st.plotly_chart(fig, use_container_width=True)

# 6. Tabela Completa (Detalhamento)
st.subheader("📋 Detalhamento Técnico")
st.dataframe(df_filtered, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("Painel de Monitoramento Interno - CGDIN")
