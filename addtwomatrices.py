matrix1 = [[1,2] , [3,4]]
matrix2 = [[1,2] , [4,5]]

row = len(matrix1)
col = len(matrix1[0])

result  = []

for i in range(row):
    rows = []
    for j in range(col):
        rows.append(matrix1[i][j] + matrix2[i][j])
    result.append(rows)

print("The summation of the matrix is : ", result)
