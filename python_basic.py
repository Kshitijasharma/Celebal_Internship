class Pattern:
    def main(self):
        
        row = int(input("Enter the number of rows: ")) 

        print("Right angle triangle")
        # Task 1: Right angle triangle
        for i in range(row):
            for j in range(i + 1):
                print("* ", end="")
            print()  # New line

        print()
        print("Upper triangle")
        print()
        # Task 2: Upper triangle
        for i in range(row):
            for j in range(row - i):
                print("* ", end="")
            print()

        print()
        print("Diamond shape triangle")
        print()
        for i in range(row):
            # Create space for the * elements
            for j in range(row - i - 1):
                print(" ", end="")

            # Substitute * in those spaces
            for j in range(i + 1):
                print("* ", end="")
            print()

if __name__ == "__main__":
    result = Pattern()
    result.main()  # Access the function result through object
