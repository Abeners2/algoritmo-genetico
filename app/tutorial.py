import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def mostrar_tutorial():
    if 'show_tutorial' not in st.session_state:
        st.session_state['show_tutorial'] = False

    def toggle_tutorial():
        st.session_state['show_tutorial'] = not st.session_state['show_tutorial']

    # Botão para o tutorial
    if st.button("❓ Como usar"):
        toggle_tutorial()

    if st.session_state['show_tutorial']:
        st.markdown("### 🧬 Como usar a ferramenta de análise genética")

        with st.expander("1. Acessando o GWAS Catalog e Baixando os Dados"):
            st.subheader("Acesse e baixe os dados do GWAS Catalog")
            st.write("Passo 1: Acesse o [GWAS Catalog](https://www.ebi.ac.uk/gwas/).")
            st.write("Passo 2: Pesquise pela condição de saúde (ex: *Diabetes*).")
            st.write("Passo 3: Baixe os dados no formato `.tsv`.")
            st.image("https://i.imgur.com/1pPZkhh.png", width=300)
            st.image("https://i.imgur.com/s8cUuMA.png", width=300)
            st.image("https://i.imgur.com/HAwOkYi.gif", width=300)

        with st.expander("2. Enviando o Arquivo para o Site"):
            st.subheader("Faça o upload do arquivo .tsv")
            st.write("Passo 4: Use a área de upload na página inicial para carregar o arquivo.")
            st.write("Dica: Aguarde alguns segundos se o arquivo for muito grande.")
            st.image("https://i.imgur.com/OasClbg.png", width=300)
            st.image("https://i.imgur.com/wnspePR.png", width=300)
            st.image("https://i.imgur.com/OdY44EJ.png", width=300)

        with st.expander("3. Escolhendo a Condição de Saúde"):
            st.subheader("Selecione a condição de saúde")
            st.write("Passo 5: Escolha a condição usando a lista.")
            st.image("https://i.imgur.com/qs4Q9rT.png", width=300)

        with st.expander("4. Analisando os Resultados"):
            st.subheader("Interaja com os gráficos")
            st.write("Passo 6: Veja os gráficos interativos gerados.")
            st.write("Passo 7: Passe o mouse sobre os pontos para mais informações.")
            st.image("https://i.imgur.com/uaL1gkL.gif", width=300)

        with st.expander("5. Tabela de SNPs Significativos"):
            st.subheader("Explore a tabela de SNPs")
            st.write("Passo 8: Veja a tabela com os SNPs significativos.")
            st.image("https://i.imgur.com/KHeZ6t5.png", width=300)

        with st.expander("6. Exportando os Resultados"):
            st.subheader("Exporte os dados processados")
            st.write("Passo 9: Clique no botão **Baixar Resultados em CSV** para baixar em CSV.")
            st.image("https://i.imgur.com/yJAOUeR.png", width=300)
            st.image("https://i.imgur.com/N4jMUeN.png", width=300)

