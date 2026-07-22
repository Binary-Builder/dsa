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

#For upside down pyramid
#Run an outer loop (i) from 0 to N-1 for rows.
#Print i spaces before the stars.
#Print 2 * N - (2 * i + 1) stars.
#Print i spaces after the stars (optional for symmetry in visualization).
