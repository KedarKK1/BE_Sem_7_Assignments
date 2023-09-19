# 5. Write a program to generate binomial coefficients using dynamic programming.
# Author : Kedar Koshti(41435)

class Solution:
    def getRow(self, rowIndex):
        prev = [1]
        for i in range(1, rowIndex + 1):
            curr = [0] * (i + 1)
            for j in range(i + 1):
                left = prev[j - 1] if j > 0 else 0
                right = prev[j] if j < i else 0
                curr[j] = left + right
            prev = curr
        return prev

    def generateBinaryCoefficientsTable(self, rows):
        if(rows <= 0):
            return
        print([1])
        for i in range(1, rows+1):
            row = self.getRow(i)
            print(row)
        return


obj = Solution()
n = int(input("Enter the number of rows you want to generate the coefficients for the solution: "))
obj.generateBinaryCoefficientsTable(n)
