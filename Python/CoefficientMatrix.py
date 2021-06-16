class CoefficientMatrix:
    #Static variables defined at this indentation.

    def __init__ (self, list_2d):
        #Instance variables defined as `self.var_name`.
        self.coeff_matrix = list_2d
        self.rows = len(list_2d[0])
        self.columns = len(list_2d)
        return None
    
    def add(self, matrix, reverse_addend_sign = False):
        if not ((len(matrix) == self.rows) and (len(matrix[0]) == self.columns)):
            return ValueError
        
        if reverse_addend_sign:            
            row_index = 0
            while row_index < self.rows:
                column_index = 0
                while column_index < self.columns:
                    matrix[row_index][column_index] = (matrix[row_index][column_index] * -1)
                    column_index += 1
                row_index += 1

        matrix_sum = list()
        row_index = 0
        while (row_index < self.columns):
            row_sum = list()
            column_index = 0
            while (column_index < self.columns):
                row_sum.append(
                    self.coeff_matrix[row_index][column_index] +
                    matrix[row_index][column_index]
                    )
                column_index += 1
            
            matrix_sum.append(row_sum)
            row_index += 1
        
        return matrix_sum

if __name__ == "__main__":
    import pprint

    A_3x3 = CoefficientMatrix(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )

    list_B_3x3 = [
            [3, 3, 3],
            [3, 3, 3],
            [3, 3, 3]
        ]
    B_3x3 = CoefficientMatrix(list_B_3x3)

    pprint.pprint(A_3x3.add(B_3x3.coeff_matrix))
    pprint.pprint(A_3x3.add(B_3x3.coeff_matrix, reverse_addend_sign=True))
