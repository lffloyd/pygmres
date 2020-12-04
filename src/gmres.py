import numpy as np
from numpy.linalg import lstsq
from src.arnoldi import arnoldi_iteration
from src.csr import CSRMatrix


def generate_e(n):
    '''
    Gera o vetor e1 de tamanho n+1, onde e1=(1 0 0 0 0 ...)
    e |e1|=n+1.
    Tal vetor eh empregado na minimizacao para obtencao de y 
    e no calculo do residual entre o y obtido a resposta real
    do sistema

    Recebe:
        - n: sera usado para calcular o tamanho n+1 do vetor
    Retorna
        - np.ndarray com todas as componentes exceto a primeira zeradas
    '''
    arr = [0] * (n+1)
    arr[0] = 1
    return np.array(arr)


def gmres(A, b, max_iter=50, min_residual=1e-8):
    '''
    Calcula a solucao de um sistema linear Ax=b via algoritmo
    GMRES.

    Recebe:
        - A: np.ndarray 2D, matrix A de coeficientes
        - b: np.ndarray 1D, vetor solucao da matriz
        - max_iter: numero maximo de iteracoes a serem realizadas
        - min_residual: residual minimo considerado suficiente para uma boa resposta
    Retorna
        - np.ndarray representando a solucao x do sistema linear
    '''
    A_csr = CSRMatrix(A)

    Q_values = []
    y = np.random.rand(1, len(b))

    for n in range(1, max_iter+1):
        Qn, hn = arnoldi_iteration(A_csr, b, n)
        Q_values.append(Qn)

        y = minimize(hn, b, n)

        rn = calculate_residual(hn, b, y, n)
        if rn < min_residual:
            return Qn.mult(y)

    return Q_values[:-1].mult(y)


def calculate_residual(hn, b, y, n):
    '''
    Calcula o residuo da solucao y encontrada.
    Formula do residuo aplicada: ||hn*y-||b||_2*e1||_2 / ||b||_2

    Recebe:
        - hn: np.ndarray
        - b: np.ndarray 1D, vetor solucao da matriz
        - y: solucao atual do sistema
        - n: numero da iteracao corrente
    Retorna
        - float representando o residuo calculado
    '''
    e1 = generate_e(n)
    b_norm = np.linalg.norm(b)
    return np.linalg.norm(hn.mult(y) - (b_norm*e1)) / b_norm


def minimize(hn, b, n):
    '''
    Minimiza o problema de minimos quadrados ||hn*y-||b||_2*e1||_2
    encontrando um y que eh a solucao candidata atual
    do sistema linear inicial

    Recebe:
        - hn: np.ndarray
        - b: np.ndarray 1D, vetor solucao da matriz
        - n: numero da iteracao corrente
    Retorna
        - np.ndarray representando y, a solucao encontrada atualmente do sistema
    '''
    e1 = generate_e(n)
    b_norm = np.linalg.norm(b)
    negated_b_norm = np.negative(b_norm)
    negated_hn = hn.negative()
    negated_b_times_e1 = negated_b_norm * e1
    x, residuals, _, _ = lstsq(
        negated_hn.to_dense(), negated_b_times_e1, rcond=-1)
    return x
