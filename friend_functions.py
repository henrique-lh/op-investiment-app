def constraints(values):
    if 'Alto' not in values:
        return True
    if values['Médio'] < 2 or values['Baixo'] < 2:
        return True 
    return False

def ceil(df):
    low = df[df['Risco'].isin(['Baixo'])]['Custo de investimento (R$)'].sum() > 1_000_000
    medium = df[df['Risco'].isin(['Médio'])]['Custo de investimento (R$)'].sum() > 1_000_000
    high = df[df['Risco'].isin(['Alto'])]['Custo de investimento (R$)'].sum() > 900_000
    return low or medium or high

def add_in_final_data(final, row):
    final['Opção'].append(row['Opção'])
    final['Descrição'].append(row['Descrição'])
    final['Custo de investimento (R$)'].append(row['Custo de investimento (R$)'])
    final['Retorno esperado (R$)'].append(row['Retorno esperado (R$)'])
    final['Risco'].append(row['Risco'])

def add_info(final, df, mask, counter=1):
    iter = df.sort_values(by='Retorno esperado (R$)', ascending=False).iterrows()
    try:
        while counter:
            row = next(iter)[1]
            add_in_final_data(final, row)
            mask.append(row['Descrição'])
            counter -= 1
    except StopIteration:
        pass