################### brute force approach ###########################################
# this is brute force aproach
class Solution:
    # Function to set entire row and column to 0 if an element in the matrix is 0
    def setZeros(self, matrix):
          # Get number of rows
        m=len(matrix)
          # Get number of cols
        n=len(matrix[0])
        # First pass: mark rows and columns
        for i in range(m):
            for j in range(n):
                # If current cell is zero
                if matrix[i][j]==0:
                    # Mark entire row
                    for col in range(n):
                        matrix[i][col]!=0
                        matrix[i][col]=-1
                        # Mark entire col
                    for row in range(m):
                        matrix[row][j]!=0
                        matrix[row][j]=-1
         # Second pass: replace -1 with 0                
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==-1:
                    matrix[i][j]=0
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [
    [1, 2, 0, 4],
    [5, 6, 7, 8],
    [9, 0, 11, 12],
    [13, 14, 15, 16]
]
sol=Solution()   
sol.setZeros(matrix) 
for row in matrix:
    print(row)                               

####################### better approach solution #####################
class Solution:
     # Function to set entire row and column to 0 if an element in the matrix is 0
    def setZeroes(self, matrix):
         # Get number of rows
        m=len(matrix)
         # Get number of col
        n=len(matrix[0])
          # Create row marker array
        row=[0]*m
          # Create col marker array
        col=[0]*n
        # First pass: mark rows and columns that need to be zeroed
        for i in range(m):
            for j in range(n):
                # If element is zero, mark its row and column
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
          # Second pass: set cells to zero based on markers            
        for i in range(m):
            for j in range(n):
                 # If the row or column is marked, set cell to zero
                if row[i]==1 or col[j]==1:
                    matrix[i][j]=0
    def printmatrix(self,matrix):
        print("resultant matrix is: ")
        for row in matrix:
            print(row)                
matrix = [[1,1,1],[1,0,1],[1,1,1]]  
matrix2= [
    [1, 2, 0, 4],
    [5, 6, 7, 8],
    [9, 0, 11, 12],
    [13, 14, 15, 16]
]
sol=Solution()
sol.setZeroes(matrix)
sol.printmatrix(matrix)

sol.setZeroes(matrix2)
sol.printmatrix(matrix2)

########################### optimal approach ###############################
class Solution :
        # Function to set entire row and column to 0 if an element in the matrix 
    def setZeroes(self,matrix):
        # Get dimensions of matrix
        m=len(matrix)
        n=len(matrix[0])
        
          # Flag to track if first row should be zeroed
        first_row_zero=False
          # Flag to track if first col should be zeroed
        first_col_zero=False

         # Check if first row has any zero
        for col in range(n):
            if matrix[0][col]==0:
                first_row_zero=True
                break
             # Check if first col has any zero
        for row in range(m):
            if matrix[row][0]==0:
                first_col_zero=True
                break

              # Use first row/column as markers
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0

             # Set cells to zero based on markers
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
         # Zero the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
                
        #print resultant matrix
    def printmatrix(self,matrix):
        print("resultant matrix is :")
        for row in matrix:
            print(row)
matrix = [[1,1,1],[1,0,1],[1,1,1]]  
matrix2= [
    [1, 2, 0, 4],
    [5, 6, 7, 8],
    [9, 0, 11, 12],
    [13, 14, 15, 16]
]
sol=Solution()
sol.setZeroes(matrix)
sol.printmatrix(matrix)

sol.setZeroes(matrix2)
sol.printmatrix(matrix2)                                        
                    

