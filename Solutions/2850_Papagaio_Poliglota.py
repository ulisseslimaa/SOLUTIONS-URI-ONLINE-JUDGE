while True:
    try:
        a = str(input())
        if a == 'nenhuma':
            print('portugues')
        if a == 'direita':
            print('frances')
        if a == 'esquerda':
            print('ingles')
        if a == 'as duas':
            print('caiu')
    except EOFError:
        break