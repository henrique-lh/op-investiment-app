from friend_functions import add_info, add_in_final_data, constraints
import numpy as np
from optimizers import optimizer_1
import pandas as pd
from solver import split_solver

class Investments:

    def __init__(self, path: str, W) -> None:
        if W <= 0:
            raise ValueError
        self.data = pd.read_csv(path)
        self.opt_data: pd.DataFrame = None
        self.W = W

    def validate_solution(self):
        values = self.opt_data.value_counts()
        if constraints(values):
            self.find_suboptimal_solution_by_risk()
        self.save()

    def find_best_solution_at_all(self):     # W = 2.400.000
        value, selected_items = split_solver(self.W, self.data)
        self.opt_data = self.data[self.data['Opção'].isin(selected_items)]
        self.validate_solution()

    def find_suboptimal_solution_by_risk(self):
        risks_types = ['Baixo', 'Médio', 'Alto']
        capacity_constraints = [1_000_000, 1_000_000, 900_000]
        selected_items = np.array([])

        for W_df, risk in zip(capacity_constraints, risks_types):
            df_risk = self.data[self.data['Risco'].isin([risk])]
            value, items = split_solver(W_df, df_risk)
            selected_items = np.append(selected_items, items)
        filtered_data = self.data[self.data['Opção'].isin(selected_items)]

        # Variável final
        final = {
            'Opção': [], 'Descrição': [], 'Custo de investimento (R$)': [],
            'Retorno esperado (R$)': [], 'Risco': []
        }

        # Ações que serão excluídas
        mask = []

        # Adicionando dados
        counters = [2, 2, 1]

        for counter, risk in zip(counters, risks_types):
            df = filtered_data[filtered_data['Risco'] == risk]
            add_info(final, df, mask, counter)

        selected_data = filtered_data[~filtered_data['Opção'].isin(mask)]

        for index, row in selected_data.sort_values(by='Retorno esperado (R$)', ascending=False).iterrows():
            if sum(final['Custo de investimento (R$)']) + row['Custo de investimento (R$)'] > self.W:
                continue
            add_in_final_data(final, row)
            mask.append(row['Opção'])

        # Atualizando dados
        non_selected_data = self.data[~self.data['Opção'].isin(mask)]
        self.opt_data = optimizer_1(pd.DataFrame(final), non_selected_data, self.W)

    def save(self):
        self.opt_data.to_csv('MyInvestiments/resultado.csv', index=False)

    def get_sum_of_low_invests(self):
        return self.opt_data[self.opt_data['Risco'] == 'Baixo']['Custo de investimento (R$)'].sum()

    def get_sum_of_medium_invests(self):
        return self.opt_data[self.opt_data['Risco'] == 'Médio']['Custo de investimento (R$)'].sum()

    def get_sum_of_high_invests(self):
        return self.opt_data[self.opt_data['Risco'] == 'Alto']['Custo de investimento (R$)'].sum()

    def get_sum_of_all_investiments(self):
        return self.opt_data['Retorno esperado (R$)'].sum()
