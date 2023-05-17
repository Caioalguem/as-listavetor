from exerc_vetor import *

opcao = int(input("Escolhoa o nivel [1] ou [2]: "))

match opcao:
    case 1:
        print("------------------NIVEL 1-------------------")
        print("1 - Exibe o primeiro elemento")
        print("2 - Exibe os valores negativos")
        print("3 - Soma os valores do vetor")
        print("4 - Calcula a média do vetor")
        print("5 - Exibe os valores ímpares")
        print("6 - Exibe o primeiro e o último valor do vetor")
        print("7 - Exibe os alores contidos em posições pares")
        print("8 - Verifica se o valor solicitado existe no vetor")
        print("9 - Ordena os valores")
        nv1 = int(input("Digite uma opção: "))

        v = [9, 5, 3, 66, 7]

        match nv1:
            case 1:
                exibe_vetor(v)
                resp = primeiro_elemento(v)
                print(resp)

            case 2:
                exibe_vetor(v)
                val_negativo(v)

            case 3:
                exibe_vetor(v)
                resp = soma(v)
                print(resp)

            case 4:
                exibe_vetor(v)
                resp = media(v)
                print(resp)

            case 5:
                exibe_vetor(v)
                impares(v)

            case 6:
                exibe_vetor(v)
                primeiro_ultimo(v)

            case 7:
                exibe_vetor(v)
                indice_par(v)

            case 8:
                exibe_vetor(v)
                resp = existe(v)
                print(resp)

            case 9:
                resp = ordenar(v)
                print(resp)
    case 2:
        print("------------------NIVEL 2-------------------")
        print("1 - Copiar valor em outro")
        print("2 - Inverte o valor de duas listas")
        print("3 - Ordena a lista na ordem crescente")
        print("4 - Ordena a lista na ordem decrescente")
        print("5 - Ordena a lista de acordo com a sua opção")
        print("6 - Separa a lista em pares e ímpares")


        nv2 = int(input("Digite uma opção: "))

        v = [9, 5, 3, 66, 7]

        match nv2:
            case 1:
                copia_vetor(v1, v2)
                resp = v2
                print(resp)

            case 2:
                inverte_vetor(v1, v2)
                resp= v2
                print(resp)

            case 3:
                ordena_vetor_crescente(v)

            case 4:
                ordena_vetor_decrescente(v)

            case 5:
                ordena_vetor(v)

            case 6:
                separa_vetor(v)













