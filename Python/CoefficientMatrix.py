class CoefficientMatrix:
    #Static variables defined at this indentation.

    def __init__ (self, list_2d):
        #Instance variables defined as `self.var_name`.
        self.coeff_matrix = list_2d
        self.rows = len(list_2d)
        self.columns = len(list_2d[0])
        return None
    
    def add(self, matrix, reverse_addend_sign = False):
        if not ((len(matrix) == self.rows) and (len(matrix[0]) == self.columns)):
            return ValueError('Left-side matrix must have the same number of rows as columns in the right-side matrix.')
        
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
    

    def multiply(self, matrix):
        # if (self.rows != len(matrix[0])):
        #     return ValueError(f"Input matrix column count {len(matrix[0])} != rows {self.rows}.")
        if (self.columns != len(matrix)):
            return ValueError(f"Input matrix row count {len(matrix)} != columns {self.columns}.")
        
        product_matrix = list()
        for self_row in self.coeff_matrix:
            # Perform operations below for every row in multiplicand.
            dot_product_list = list()
            for matrix_colnum in range(len(matrix[0])):
                # For every column in the multiplier matrix, do the following:
                dot_product = 0
                for self_colnum in range(self.columns):
                    dot_product += (self_row[self_colnum] * matrix[self_colnum][matrix_colnum])
                dot_product_list.append(dot_product)
            
            product_matrix.append(dot_product_list)

        return product_matrix


if __name__ == "__main__":
    import pprint

    #Testing Additon and Subtraction
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

    #Testing Matrix by Matrix Multiplication
    multiplier_list = [
        [7, 8],
        [9, 10],
        [11, 12]        
    ]

    multiplicand = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix_A = CoefficientMatrix(multiplicand)
    pprint.pprint(matrix_A.multiply(multiplier_list))
    