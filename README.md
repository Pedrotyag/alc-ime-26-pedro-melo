# Álgebra Linear Computacional — Questão 5

Resolução da questão 5 (prova 1) por decomposição LU sem pivotamento.

O script monta a fatoração `A = LU`, resolve `Ly = b` por substituição progressiva e `Ux = y` por substituição regressiva.

## Sistema

```text
A = | 2  1  1 |     b = |  7 |
    | 4  3  3 |         | 19 |
    | 8  7  9 |         | 49 |
```

## Como executar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 alc-p1-05-pedro-melo.py
```

## Saída esperada

```text
Matriz L:
[[1. 0. 0.]
 [2. 1. 0.]
 [4. 3. 1.]]

Matriz U:
[[2. 1. 1.]
 [0. 1. 1.]
 [0. 0. 2.]]

Solucao x:
[1. 2. 3.]
```

A verificação imprime `L @ U`, que recupera `A`, e `A @ x`, que recupera `b = [7, 19, 49]`.

## Funções

| Função | Papel |
| --- | --- |
| `decompoe_lu` | Fatora `A` em `L` (triangular inferior, com 1 na diagonal) e `U` (triangular superior) |
| `forward_substitution` | Resolve `Ly = b` |
| `back_substitution` | Resolve `Ux = y` |
| `resolve_lu` | Encadeia a fatoração e as duas substituições e devolve `(L, U, x)` |

A matriz precisa ser quadrada e os pivôs da eliminação não podem ser nulos. Se algum pivô for zero, o script interrompe e indica que é preciso um método com pivotamento.
