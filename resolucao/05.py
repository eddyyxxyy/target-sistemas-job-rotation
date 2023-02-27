if __name__ == '__main__':
    string: str = input('Informe o texto que será invertido:\n->')
    reverse_string: str = ''

    for i in string:
        reverse_string = i + reverse_string
    
    print(f'Texto invertido:\n{reverse_string}')
