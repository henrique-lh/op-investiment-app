from collections import deque
import numpy as np

def split_solver(W, df):
    wt = np.array(df['Custo de investimento (R$)'].values)
    val = np.array(df['Retorno esperado (R$)'].values)
    items = np.array(df['Opção'].values)
    n = df.shape[0]
    value, selected_items = solution(W, wt, val, n, items)
    return value, selected_items

def solution(W, wt, val, n, my_itens):
    memo = np.full((n + 1, W + 1), -1)
    selected_items = np.full((n + 1, W + 1), False)
    max_value = knapsack(W, wt, val, n, memo, selected_items)
    selected = get_selected_items(wt, selected_items, n, W, my_itens)
    return max_value, selected

def knapsack(W, wt, val, n, memo, selected_items):
    if n == 0 or W == 0:
        return 0

    if memo[n, W] != -1:
        return memo[n, W]

    if wt[n - 1] <= W:
        include_item_value = val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1, memo, selected_items)
        exclude_item_value = knapsack(W, wt, val, n - 1, memo, selected_items)
        if include_item_value > exclude_item_value:
            memo[n, W] = include_item_value
            selected_items[n, W] = True
        else:
            memo[n, W] = exclude_item_value
    else:
        memo[n, W] = knapsack(W, wt, val, n - 1, memo, selected_items)

    return memo[n, W]

def get_selected_items(wt, selected_items, n, W, my_itens):
    selected = deque()
    while n > 0 and W > 0:
        if selected_items[n, W]:
            selected.appendleft(my_itens[n - 1])
            W -= wt[n - 1]
        n -= 1
    return np.array(selected)
