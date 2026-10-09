
import numpy as np

A = np.array([
    [2, 1, 1],
    [4, 3, 3],
    [8, 7, 9],
])

b = np.array([
    [7],
    [19],
    [49]
])


def decompoe_lu(A):
    """
    Decompoe a matriz A em L e U.

    Retorna (U, L)
    """

    U = np.array(A, copy=True, dtype=float)

    # verifica se A é quadrada
    if U.ndim != 2 or U.shape[0] != U.shape[1]:
        raise ValueError("A matriz A deve ser quadrada.")

    n = U.shape[0]
    L = np.eye(n)

    # percorre os pivos
    for i in range(n):
        p = U[i, i]

        if p == 0:
            raise ValueError("Use um método alternativo com pivotamento.")

        # percorre as linhas abaixo dos pivos
        for j in range(i + 1, n):
            m = U[j, i] / p

            L[j, i] = m

            # percorre as colunas da linha abaixo do pivo
            for k in range(i, n):
                U[j, k] -= U[i, k] * m

    return U, L


def forward_substitution(L, b):
    """
    Resolve Ly = b por substituicao progressiva.
    """

    n = L.shape[0]
    y = np.zeros(n)

    # percorre as linhas de cima para baixo
    for i in range(n):
        soma = 0

        # soma os termos que ja conhecemos
        for j in range(i):
            soma += L[i, j] * y[j]

        y[i] = (b[i] - soma) / L[i, i]

    return y


def back_substitution(U, y):
    """
    Resolve Ux = y por substituicao regressiva.
    """

    n = U.shape[0]
    x = np.zeros(n)

    # percorre as linhas de baixo para cima
    for i in range(n - 1, -1, -1):
        soma = 0

        # soma os termos que ja conhecemos
        for j in range(i + 1, n):
            soma += U[i, j] * x[j]

        if U[i, i] == 0:
            raise ValueError("Pivo nulo na substituicao regressiva.")

        x[i] = (y[i] - soma) / U[i, i]

    return x


def resolve_lu(A, b):
    """
    Resolve Ax = b usando decomposicao LU.

    Retorna (L, U, x)
    """

    b = np.array(b, copy=True, dtype=float).reshape(-1)

    U, L = decompoe_lu(A)

    if len(b) != L.shape[0]:
        raise ValueError("Dimensoes de A e b incompativeis.")

    # primeiro resolve Ly = b
    y = forward_substitution(L, b)

    # depois resolve Ux = y
    x = back_substitution(U, y)

    return L, U, x


if __name__ == "__main__":
    L, U, x = resolve_lu(A, b)

    print("Matriz L:")
    print(L)

    print("\nMatriz U:")
    print(U)

    print("\nSolucao x:")
    print(x)

    print("\nVerificacao L @ U:")
    print(L @ U)

    print("\nVerificacao A @ x:")
    print(A @ x)
