import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
from preprocessamento import processar_tsv
from tutorial import mostrar_tutorial

# Configurações da página
st.set_page_config(page_title="Análise Genética - GWAS", layout="wide")
sns.set(style="whitegrid")
mostrar_tutorial()
# Título e descrição
st.title("🔬 Identificação de Padrões Genéticos - GWAS Catalog")
st.markdown(
    "Este app permite analisar dados do GWAS Catalog para identificar SNPs associados a condições de saúde. "
    "Faça upload de um arquivo `.tsv` bruto do [GWAS Catalog](https://www.ebi.ac.uk/gwas/)."
)

# Upload do arquivo
uploaded_file = st.file_uploader("📂 Envie o arquivo `.tsv` bruto do GWAS Catalog", type="tsv")

if uploaded_file:
    with st.spinner("🔄 Processando o arquivo..."):
        try:
            resultado = processar_tsv(uploaded_file)
        except Exception as e:
            st.error(f"❌ Erro ao processar o arquivo: {e}")
            st.stop()

    # Se ainda não foi escolhida uma condição, mostrar as disponíveis
    if isinstance(resultado, list):
        condicao = st.selectbox("🧬 Selecione a condição de saúde que deseja analisar:", resultado)
        if not condicao:
            st.stop()

        with st.spinner(f"🔎 Filtrando para: {condicao}..."):
            try:
                df = processar_tsv(uploaded_file, condicao_escolhida=condicao)
            except Exception as e:
                st.error(f"❌ Erro ao filtrar pela condição: {e}")
                st.stop()
    else:
        df = resultado
        condicao = df['condicao'].iloc[0] if 'condicao' in df.columns else "Condição Genética"

    # Subtítulo
    st.subheader(f"📈 Resultados para: **{condicao}**")

    # Gráficos
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧬 Top 10 Genes mais associados")
        top_genes = df['gene'].value_counts().nlargest(10)
        top_genes_df = top_genes.sort_values().reset_index()
        top_genes_df.columns = ['gene', 'count']

        fig_bar = px.bar(
            top_genes_df,
            x='count',
            y='gene',
            orientation='h',
            labels={'count': 'Quantidade de SNPs Significativos', 'gene': 'Gene'},
            title=f'Top 10 Genes Associados à {condicao}',
            color='count',
            color_continuous_scale='viridis'
        )

    fig_bar.update_layout(height=400, margin=dict(l=40, r=40, t=60, b=40), coloraxis_showscale=False)
    st.plotly_chart(fig_bar, use_container_width=True)


    with col2:
            fig_hist = px.histogram(
        df,
        x='p_value',
        nbins=30,
        title='Distribuição dos P-valores Significativos',
        labels={'p_value': 'P-valor'},
        color_discrete_sequence=['teal']
    )
    fig_hist.update_layout(height=400, margin=dict(l=40, r=40, t=60, b=40))
    st.plotly_chart(fig_hist, use_container_width=True)


    # Dispersão
    st.markdown("### 🌐 Dispersão dos SNPs vs -log10(P-valor) (Interativo)")

    df['-log10(p_value)'] = -np.log10(df['p_value'])

    fig_plotly = px.scatter(
        df,
        x=df.index,
        y='-log10(p_value)',
        color='gene',
        hover_data={
            'snp_id': True,
            'gene': True,
            'p_value': True,
            '-log10(p_value)': ':.2f',
            'condicao': True
        },
        labels={'x': 'Índice do SNP', '-log10(p_value)': '-log10(P-valor)'},
        title='SNPs Significativos vs -log10(P-valor)'
    )

    fig_plotly.update_layout(
        height=500,
        showlegend=False,
        margin=dict(l=40, r=40, t=60, b=40)
    )

    st.plotly_chart(fig_plotly, use_container_width=True)

    # Tabela de dados
    st.markdown("### 🔍 Visualização da Tabela de SNPs Significativos")
    st.dataframe(df)

    # Download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar Resultados em CSV",
        data=csv,
        file_name="resultados_significativos.csv",
        mime='text/csv'
    )
    if btn:
        st.toast("Resultados baixados com sucesso!", icon="✅")

else:
    pass
