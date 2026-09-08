def MatrixMultiplication(mat_a,mat_b):  
    m = len(mat_a)
    q = len(mat_b[0])
    n = len(mat_a[0])
    if (n==p):
        print("Condition to perform matrix multiplication is met")
        mat_c = []
        
        for i in range(m):          
            row = []
            for j in range(q):
                cell_sum = 0
                for k in range(n):
                    cell_sum += mat_a[i][k] * mat_b[k][j]
                row.append(cell_sum)
            mat_c.append(row)

        for i in range(m):
            for j in range(q):
                print (mat_c[i][j], end=" ")
            print()
    else:
        print("Condition to perform matrix multiplication is not met")

m = int(input("Enter number of rows (m) MATRIX A: "))
n = int(input("Enter number of columns (n) MATRIX A: "))

mat_a = []
for i in range(m):
    row = []
    for j in range(n):
        val = int(input("Enter element: "))
        row.append(val)
    mat_a.append(row)

for i in range(m):
    for j in range(n):
        print (mat_a[i][j], end=" ")
    print()


p = int(input("Enter number of rows (p) MATRIX B: "))
q = int(input("Enter number of columns (q) MATRIX B: "))

mat_b = []
for i in range(p):
    row = []
    for j in range(q):
        val = int(input("Enter element: "))
        row.append(val)
    mat_b.append(row)

for i in range(p):
    for j in range(q):
        print (mat_b[i][j], end=" ")
    print()

MatrixMultiplication(mat_a,mat_b)