# creator: Kenneth Guillont
# LU Decomposition in Python

# Function to perform LU Decomposition
def lu_decomposition(n, a, b):
    l = [[0] * n for _ in range(n)]
    u = [[0] * n for _ in range(n)]
    z = [0] * n
    x = [0] * n

    # LU Factorization
    for k in range(n):
        u[k][k] = 1
        for i in range(k, n):
            # Calculate L matrix
            s = sum(l[i][p] * u[p][k] for p in range(k))
            l[i][k] = a[i][k] - s

        for j in range(k + 1, n):
            # Calculate U matrix
            s = sum(l[k][p] * u[p][j] for p in range(k))
            u[k][j] = (a[k][j] - s) / l[k][k]

    # Display LU matrix
    print("\nLU matrix is:")
    for i in range(n):
        for j in range(n):
            print(l[i][j], end="  ")
        print()

    # Finding Z; LZ = b
    for i in range(n):
        s = sum(l[i][p] * z[p] for p in range(i))
        z[i] = (b[i] - s) / l[i][i]

    # Finding X; UZ = Z
    print("\nSet of solution:")
    for i in range(n):
        s = sum(u[n - 1 - i][p] * x[p] for p in range(n - 1, n - 1 - i, -1))
        x[n - 1 - i] = (z[n - 1 - i] - s) / u[n - 1 - i][n - 1 - i]
        print(x[n - 1 - i])

# Main program
if __name__ == "__main__":
    # Taking input for matrix order and coefficients
    n = int(input("Enter the order of matrix: "))
    a = [[0] * n for _ in range(n)]
    b = [0] * n

    print("Enter all coefficients of matrix:")
    for i in range(n):
        print(f"Row {i + 1}:", end=" ")
        a[i] = list(map(float, input().split()))

    print("Enter elements of b matrix:")
    b = list(map(float, input().split()))

    # Calling LU Decomposition function
    lu_decomposition(n, a, b)
