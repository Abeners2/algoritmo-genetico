import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from preprocessamento import processar_tsv

# Configurações da página
st.set_page_config(page_title="Análise Genética - GWAS", layout="wide")
sns.set(style="whitegrid")

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
        fig1, ax1 = plt.subplots()
        sns.barplot(x=top_genes.values, y=top_genes.index, palette='viridis', ax=ax1)
        ax1.set_xlabel('Quantidade de SNPs Significativos')
        ax1.set_ylabel('Gene')
        ax1.set_title(f'Top 10 Genes Associados à {condicao}')
        st.pyplot(fig1)

    with col2:
        st.markdown("### 📊 Distribuição dos P-valores")
        fig2, ax2 = plt.subplots()
        sns.histplot(df['p_value'], bins=30, kde=True, color='teal', ax=ax2)
        ax2.set_xlabel('P-valor')
        ax2.set_ylabel('Frequência')
        ax2.set_title('Distribuição dos P-valores Significativos')
        st.pyplot(fig2)

    # Dispersão
    st.markdown("### 🌐 Dispersão dos SNPs vs -log10(P-valor)")
    df['-log10(p_value)'] = -np.log10(df['p_value'])
    fig3, ax3 = plt.subplots(figsize=(14, 5))
    sns.scatterplot(x=range(len(df)), y='-log10(p_value)', data=df, hue='gene', palette='tab10', legend=False, ax=ax3)
    ax3.set_xlabel('Índice do SNP')
    ax3.set_ylabel('-log10(P-valor)')
    ax3.set_title('SNPs Significativos vs -log10(P-valor)')
    st.pyplot(fig3)

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

else:
    st.info("📄 Envie um arquivo `.tsv` do GWAS Catalog para começar a análise.")
