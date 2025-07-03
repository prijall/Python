class solution:
    def mat(self, matrix:list[list[int]], target:int)->bool:
        rows, cols=len(matrix[1]), len(matrix[0])
        top, down=0, rows-1

        while top<=down:
            row=top + (down-top)//2

            if target>matrix[row][-1]:
                top=row+1
            elif target < matrix[row][0]:
                down=row-1
            else:
                break

        row= top + (down-top)//2

        
        l, r=0, cols-1

        while l<=r:
            m=l + (r-l)//2

            if target> matrix[row][m]:
                l=m+1
            elif target < matrix[row][m]:
                r=m-1
            else:
                return True
            
        if not (top<=down):
            return False
        
        return False
    

s=solution()
print(s.mat(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15))


## Time Complexity: O(log(m) + log(n)) = O(log(m * n)), where m=no of rows, n= no of elements in a rows
## Space Complexity: O(1)