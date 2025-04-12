# 🧬 Identificação de Padrões Genéticos - GWAS Catalog

Este projeto é um sistema interativo desenvolvido com **Python** e **Streamlit** que permite a análise de dados genéticos provenientes do [GWAS Catalog](https://www.ebi.ac.uk/gwas/), com foco na identificação de SNPs significativamente associados a condições de saúde, como **Diabetes Tipo 2**.

## 🎯 Objetivo

Facilitar a visualização e identificação de **padrões genéticos** em condições específicas, usando arquivos `.tsv` fornecidos pelo GWAS Catalog.

## ⚙️ Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Streamlit](https://streamlit.io/)

## 🧪 Funcionalidades

- 📁 Upload de arquivos `.tsv` brutos do GWAS Catalog
- 🔍 Filtro por condição de saúde (ex: Diabetes Tipo 2)
- 🧠 Identificação de SNPs com p-valor ≤ 5e-8
- 📊 Visualizações interativas:
  - Top 10 genes associados
  - Distribuição de p-valores
  - Dispersão dos SNPs por cromossomo
- 📥 Exportação dos resultados em `.csv`

## 🧾 Exemplo de Arquivo

Utilize arquivos `.tsv` baixados diretamente do GWAS Catalog:
🔗 [GWAS Catalog Download](https://www.ebi.ac.uk/gwas/)

## 🧰 Como Executar Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/Abeners2/algoritmo-genetico.git
cd algoritmo-genetico

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o aplicativo
streamlit run app/interface.py
```

## 👨‍👩‍👧‍👦 Equipe

- **Abner** – Desenvolvimento, lógica de análise, integração Streamlit
- **Ana Júlia** – Apoio biomédico e validação científica
- **Evie** – Apoio biomédico e levantamento de dados

## 🌍 Licença

Este projeto é de código aberto, voltado para fins educacionais e comunitários. Licenciado sob a **MIT License**.
