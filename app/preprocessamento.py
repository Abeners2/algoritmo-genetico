import pandas as pd

def processar_tsv(tsv_file, condicao_escolhida=None):
    # Mostrar primeiras linhas do arquivo para debug
    print(tsv_file.read(500))
    tsv_file.seek(0)

    # Leitura do TSV
    df = pd.read_csv(tsv_file, sep='\t')

    # Verifica qual coluna de gene está disponível
    colunas_gene_possiveis = ['GENE', 'REPORTED GENE(S)', 'MAPPED_GENE']
    coluna_gene = next((col for col in colunas_gene_possiveis if col in df.columns), None)

    if not coluna_gene:
        raise KeyError("Nenhuma coluna de gene encontrada no arquivo (esperado: 'GENE', 'REPORTED GENE(S)' ou 'MAPPED_GENE').")

    # Garante que a coluna de interesse para condição está presente
    if 'DISEASE/TRAIT' not in df.columns:
        raise KeyError("A coluna 'DISEASE/TRAIT' não foi encontrada no arquivo.")

    df = df[df['DISEASE/TRAIT'].notna()]

    # Retorna lista de condições disponíveis se nenhuma for selecionada
    if condicao_escolhida is None:
        condicoes_disponiveis = df['DISEASE/TRAIT'].unique().tolist()
        return condicoes_disponiveis

    # Filtra pela condição selecionada
    df_condicao = df[df['DISEASE/TRAIT'] == condicao_escolhida]

    # Define colunas necessárias, substituindo 'GENE' pela encontrada
    colunas_necessarias = ['SNPS', coluna_gene, 'DISEASE/TRAIT', 'P-VALUE', 'STRONGEST SNP-RISK ALLELE']
    df_filtrado = df_condicao[colunas_necessarias].dropna()

    # Aplica filtro de significância estatística
    df_filtrado = df_filtrado[df_filtrado['P-VALUE'] <= 5e-8]

    # Renomeia colunas para manter padrão
    df_filtrado.columns = ['snp_id', 'gene', 'condicao', 'p_value', 'risk_allele']
    df_filtrado['condicao'] = condicao_escolhida

    # Retorna apenas as colunas finais organizadas
    df_final = df_filtrado[['snp_id', 'gene', 'risk_allele', 'p_value', 'condicao']]
    return df_final
