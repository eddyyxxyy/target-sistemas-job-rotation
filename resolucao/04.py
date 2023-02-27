if __name__ == '__main__':
    profits: dict = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53,
    }
    
    total: float = sum(profits.values())
    
    print('Percentual de representação de cada estado (aproximado):')
    for i in range(len(profits)):
        print(
            f'{tuple(profits.keys())[i]}: {(tuple(profits.values())[i] / total) * 100:.2f}%'
        )
