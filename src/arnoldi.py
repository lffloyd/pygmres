import numpy as np


def arnoldi_iteration(A, b, n):
    '''
    Realiza a iteracao de Arnoldi para os dados matrix A e vetor b.

    Recebe:
        - A: instancia CSRMatrix
        - b: instancia np.ndarray
        - n: numero de iteracoes a serem realizadas
    Retorna
        - Q, h
    '''
    dense_A = A.to_dense()
    m = len(dense_A)
    # m = A.shape[0]

    h = np.zeros((n + 1, n), dtype=np.float64)
    Q = np.zeros((m, n + 1), dtype=np.float64)

    q = b / np.linalg.norm(b)
    Q[:, 0] = q

    for k in range(n):
        v = dense_A.dot(q)
        for j in range(k + 1):
            h[j, k] = np.dot(Q[:, j].conj(), v)
            v = v - h[j, k] * Q[:, j]

        h[k + 1, k] = np.linalg.norm(v)
        eps = 1e-12
        if h[k + 1, k] > eps:
            q = v / h[k + 1, k]
            Q[:, k + 1] = q
        else:
            return Q, h
    return Q, h
