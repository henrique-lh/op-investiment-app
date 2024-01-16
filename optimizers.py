from friend_functions import ceil, constraints
import numpy as np
import pandas as pd
from solver import split_solver

def optimizer_1(df, non_selected_data, LIMIT):

    # Copiando variáveis e definindo constantes
    copy_non_selected_data = non_selected_data.copy()
    max_cost = df['Custo de investimento (R$)'].max()
    max_profit = df['Retorno esperado (R$)'].sum()
    risk_type = df[df['Custo de investimento (R$)'] == max_cost]['Risco'].values[0]
    new_possible_sum = LIMIT - df['Custo de investimento (R$)'].sum() + max_cost # capacidade máxima nova
    df_copy = df[df['Custo de investimento (R$)'] != max_cost]

    # Checando tipo de dado
    if constraints(df_copy.value_counts()):
        high_copy = copy_non_selected_data[copy_non_selected_data['Risco'] == risk_type]
        min_cost_row = high_copy[high_copy['Custo de investimento (R$)'] == high_copy['Custo de investimento (R$)'].min()]
        max_cost -= min_cost_row['Custo de investimento (R$)'].min()
        new_possible_sum -= min_cost_row['Custo de investimento (R$)'].min()
        df_copy = pd.concat([df_copy, min_cost_row], ignore_index=True)
        copy_non_selected_data = copy_non_selected_data[~copy_non_selected_data['Opção'].isin(min_cost_row['Opção'])]

    if new_possible_sum <= copy_non_selected_data['Custo de investimento (R$)'].min():
        return df

    # Aplicando knapsack problem
    v, i = split_solver(new_possible_sum, copy_non_selected_data)
    filtered_data = non_selected_data[non_selected_data['Opção'].isin(i)]

    # Selecionando novos dados e retornando
    new_data = pd.concat([df_copy, filtered_data], ignore_index=True)

    if ceil(new_data): 
        risks_types = ['Baixo', 'Médio', 'Alto']
        capacity_constraints = [1_000_000, 1_000_000, 900_000]
        selected_items = np.array([])
        for W_df, risk in zip(capacity_constraints, risks_types):
            df_risk = new_data[new_data['Risco'].isin([risk])]
            value, items = split_solver(W_df, df_risk)
            selected_items = np.append(selected_items, items)

    if new_data['Retorno esperado (R$)'].sum() > max_profit:
        return new_data
    return df