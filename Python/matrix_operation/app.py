import numpy as np

def input_matrix(name="Matrix"):
    """Function to take matrix input from user"""
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements of {name} row by row (space separated):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("⚠️ Error: Number of elements does not match columns. Try again.")
            return input_matrix(name)
        matrix.append(row)
    return np.array(matrix)


def display_matrix(matrix, title="Result"):
    print(f"\n🔹 {title}:")
    print(matrix)


def menu():
    print("\n=== MATRIX OPERATIONS TOOL ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")


def main():
    while True:
        menu()
        choice = input("\nChoose an operation (1-6): ")

        if choice == "1":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                display_matrix(A + B, "A + B")
            else:
                print("⚠️ Matrices must have the same dimensions for addition.")

        elif choice == "2":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                display_matrix(A - B, "A - B")
            else:
                print("⚠️ Matrices must have the same dimensions for subtraction.")

        elif choice == "3":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape[1] == B.shape[0]:
                display_matrix(A.dot(B), "A × B")
            else:
                print("⚠️ Number of columns in A must equal number of rows in B.")

        elif choice == "4":
            A = input_matrix("Matrix")
            display_matrix(A.T, "Transpose of Matrix")

        elif choice == "5":
            A = input_matrix("Matrix")
            if A.shape[0] == A.shape[1]:
                det = np.linalg.det(A)
                print(f"\n🔹 Determinant: {det:.2f}")
            else:
                print("⚠️ Determinant can only be calculated for square matrices.")

        elif choice == "6":
            print("✅ Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
