
def preeenche_vetor(vetor: int) -> int:
    vetor = []
    for i in range(0,5, 1):
        vetor.append(int(input("Digite o valor: ")))







def exibe_vetor(vetor: list) -> None:
    for i in range(5):
        print(f"v[{i}] = {vetor[i]}")

def primeiro_elemento(vetor: list) -> int:
    primeiro = len(vetor)
    return vetor[primeiro - 5]


def val_negativo(vetor: list) -> None:
    for i in range (5):
        if vetor[i] < 0:
            print(vetor[i])


def exibe_vetor(vetor: list) -> None:
    for i in range(len(vetor)):
        print(f"v[{i}] = {vetor[i]}")

def soma(vetor: list) -> int:
    soma = 0
    for i in range(len(vetor)):
        soma = soma + vetor[i]
    return soma


def exibe_vetor(vetor: list) -> None:
    for i in range(len(vetor)):
        print(f"v[{i}] = {vetor[i]}")

def media(vetor: list) -> int :
    soma = 0
    for i in range(len(vetor)):
        soma = soma + vetor[i]
    media = 0
    for i in range(len(vetor)):
        media = soma / 5
    return media


def exibe_vetor(vetor: list) -> None:
    for i in range(len(vetor)):
        print(f"v[{i}] = {vetor[i]}")

def impares(vetor: list) -> None:
    for i in range(len(vetor)):
        if vetor[i]%2 != 0 :
            print(vetor[i])



def exibe_vetor(vetor: list) -> None:
    for i in range(len(vetor)):
        print(f"v[{i}] = {vetor[i]}")

def primeiro_ultimo(vetor: list) -> None:
        ultimo = len(vetor)
        print(vetor[0],vetor[ultimo - 1])


def indice_par(vetor: list) -> None:
    for i in range(len(vetor)):
        if i % 2 == 0:
            print(vetor[i])


def existe(vetor: list) -> str:
    for i in range (len(vetor)):
        valor = int(input("Digite o valor: "))
        if valor in vetor:
            return True
        else:
            return False


def ordenar(vetor: list) -> int:
    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            if vetor[i] > vetor[j]:
                temp = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = temp
    return vetor


#Nivel 2

v1 = [3, 4, 5, 6, 7]
v2 = [0, 0, 0, 0, 0]

def copia_vetor(v1: list, v2: list) -> None:
    for i in range (len(v1)):
        v2[i]=v1[i]
    print(v2)

def inverte_vetor(v1, v2: int) -> None:
    w=0
    for i in range(len(v1)):
        w+=1
        v2[i] = v1[len(v1)-w]
    print(v2)


def ordena_vetor_crescente(v: list) -> None:
    for i in range(len(v)):
        for j in range(i, len(v)):
            if v[i] > v[j]:
                temp = v[i]
                v[i] = v[j]
                v[j] = temp
    print (v)

def ordena_vetor_decrescente(v: list) -> None:
    for i in range(len(v)):
        for j in range(i, len(v)):
            if v[i] < v[j]:
                temp = v[i]
                v[i] = v[j]
                v[j] = temp
    print (v)

def ordena_vetor(v: list) -> None:
    forma = str(input("tecle [c] para crescente e [d] para decrescente: "))

    if forma == 'c':
        for i in range(len(v)):
            for j in range(i, len(v)):
                if v[i] > v[j]:
                    temp = v[i]
                    v[i] = v[j]
                    v[j] = temp
        print(v)
    else:
        for i in range(len(v)):
            for j in range(i, len(v)):
                if v[i] < v[j]:
                    temp = v[i]
                    v[i] = v[j]
                    v[j] = temp
        print(v)

def separa_vetor(v: list) -> None:
    for i in range(len(v)):
        if v[i] % 2 == 0:
            print(v[i], end=" ", flush=True)
    for i in range(len(v)):
        if v[i] % 2 != 0:
            print(v[i], end=" ", flush=True)