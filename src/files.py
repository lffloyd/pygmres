import numpy as np


def read_system_of_lineq_from_file(filename):
    '''
    Lê um sistema de equacoes lineares (Ax=b) a partir de um arquivo.
    No arquivo, as linhas da matriz A e os elementos do vetor b devem estar armazenados
    em sequencia.
    Primeiramente as linhas da matriz, como exemplo:
        2 4 5
        6 2 9
        1 0 8
    E logo abaixo os elementos de B:
        1 8 7
    
    Recebe:
        - filename: path do arquivo
    Retorna:
        tupla com A, b onde ambos sao do tipo np.array
    '''
    elements = []
    with open(filename, "r") as file:
        for line in file:
            elements.append(list(map(lambda x: float(x), line.split())))
    
    A = np.array(elements[:-1])
    b = np.array(elements[-1])
    return A, b
