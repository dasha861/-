def get_matrix (m,n,value):
    matrix = []
    for a1 in range(n):
        matrix.append([])
        for a2 in range(m):
            matrix[a1].append(value)
    return matrix

print(get_matrix(2,2,10))
