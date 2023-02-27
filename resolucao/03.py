import json
from locale import LC_MONETARY, currency, setlocale
from statistics import mean


setlocale(LC_MONETARY, 'pt_BR.UTF-8')
C = currency

if __name__ == '__main__':
    with open('data.json', 'r', encoding='UTF-8') as file:
        fixed_data: list[dict] = [x for x in json.load(file) if x['valor'] >= 1]

        min_profit: dict = min(fixed_data, key=lambda x: x['valor'])
        max_profit: dict = max(fixed_data, key=lambda x: x['valor'])
        mean_profit: float = mean(value.get('valor') for value in fixed_data)

        more_than_mean: list[dict] = [profit for profit in fixed_data if profit['valor'] > mean_profit]

    print(
        f'O menor faturamento é do dia {min_profit.get("dia")} '
        f'({C(min_profit.get("valor"), grouping=True)});'
    )
    print(
        f'O maior faturamento é do dia {max_profit.get("dia")} '
        f'({C(max_profit.get("valor"), grouping=True)});'
    )
    print(
        f'\nOs dias com faturamento maior que a média mensal (maiores que {C(mean_profit, grouping=True)}):'
    )
    
    for i in range(len(more_than_mean)):
        print(f'Dia {more_than_mean[i].get("dia")}: {C(more_than_mean[i].get("valor"), grouping=True)}')
