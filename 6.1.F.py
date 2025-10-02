import numpy as np

def multiplication_matrix(N):
    m = np.ones((N, N), dtype="int32")
    m[0, :] = np.arange(1, N+1)
    m[:,0] = np.arange(1, N+1)

    for row in m:
        row[1:] = row[0] * m[0,1:]

    # m[1:,1:] = m[1:,0] * m[0,1:] 
    return m

def multiplication_matrix2(N):
    """
    Функция создает матрицу умножения N x N
    
    Args:
        N (int): Размер матрицы
        
    Returns:
        numpy.ndarray: Матрица умножения размером N x N
    """
    row = np.arange(1, N + 1)
    col = np.arange(1, N + 1).reshape(-1, 1)
    return row * col

print(multiplication_matrix2(5))