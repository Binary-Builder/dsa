class solution:
    def pattern(self, n):

        for i in range (n):
            for j in range(n-i-1):
               print(" ", end="")

            for j in range(2*i+1):
             print("*", end="")

            for j in range(n-i-1):
                print(" ", end="")

            print()
        

if __name__ == "__main__":
    sol = solution()
    N=5
    sol.pattern(N)

