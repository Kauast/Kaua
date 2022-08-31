print('-----------------------------------------')
print('Seja bem vindo!')
print('-----------------------------------------')

flag = True

while flag:
    iniciar = str(
        input('Você quer iniciar o programa [S] ou [N]?\n\nDigite aqui: ')).upper()

    if iniciar == 'S':
        iniciar = True
        while iniciar:
            n1 = float(input('\nDigite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            operacao = int(input(
                '\n [1] Somar \n [2] Subtrair \n [3] Multiplicar \n [4] Dividir\n [5] Encerrar programa\n\nDigite aqui: '))

            if operacao == 1:
                resultado = n1 + n2
                print('O resultado é: ', resultado)
                continuar = input(
                    'Você quer continuar [S] ou [N]?\nDigite aqui: ')
                if continuar == 'S':
                    continue

                else:
                    print('\nPrograma encerrado!')
                    iniciar = False
                    flag = False

            elif operacao == 2:
                resultado = n1 - n2
                print('O resultado é: ', resultado)
                continuar = input(
                    'Você quer continuar [S] ou [N]?\nDigite aqui: ')
                if continuar == 'S':
                    continue
                else:
                    print('\nPrograma encerrado!')
                    iniciar = False
                    flag = False

            elif operacao == 3:
                resultado = n1 * n2
                print('O resultado é: ', resultado)
                continuar = input(
                    'Você quer continuar [S] ou [N]?\nDigite aqui: ')
                if continuar == 'S':
                    continue
                else:
                    print('\nPrograma encerrado!')
                    iniciar = False
                    flag = False

            elif operacao == 4:
                resultado = n1 / n2
                print('O resultado é: ', resultado)
                continuar = input(
                    'Você quer continuar [S] ou [N]?\nDigite aqui:\n ')
                if continuar == 'S':
                    continue
                else:
                    print('\nPrograma encerrado!')
                    iniciar = False
                    flag = False

            elif operacao == 5:
                print('\nPrograma encerrado!')
                iniciar = False
                flag = False

    elif iniciar == 'N':
        print('\nPrograma encerrado!')
        flag = False
    else:
        print('Valor invalido!')
