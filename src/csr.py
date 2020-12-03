import numpy as np


class CSRMatrix():
    '''
    Armazena a representacao CSR de uma matriz
    '''

    def __getitem__(self, index):
      row = self.index_array[index[0]]
      next_row = row
      if index[0] < len(self.index_array)-1:
        next_row = self.index_array[index[0]+1]
        columns = self.columns_array[row:next_row]
      else: 
        columns = self.columns_array[row:]
      print(columns)
      if index[1] in list(columns):
        return self.values_array[row+list(columns).index(index[1])]
      else:
        return 0

      
    def __setitem__(self,pos,value):
      row, column = pos[0],pos[1]
      
      if(self[row,column] != 0):
        print("oie")
    
    def __init__(self, matrix, from_csr=False):
        '''
        Recebe uma matriz completa e transforma ela no formato CSR, 
        ou tres conjuntos com valores, colunas e indices ja no formato CSR.
        '''
        if from_csr != True:
            self.__to_csr(matrix)
            return

        self.values_array = np.array(matrix[0])
        self.columns_array = np.array(matrix[1])
        self.index_array = np.array(matrix[2])

    def __str__(self):
        return f'\nValues: {self.values_array}\nColumns: {self.columns_array}\nIndexes: {self.index_array}\n'

    def __to_csr(self, matrix):
        '''
        Cria a representacao CSR a partir de uma matriz completa no formato:
          2 4 5
          6 2 9
          1 0 8
        '''
        self.values_array = []  # values in original matrix
        self.columns_array = []  # column index of where the value is
        self.index_array = []  # index of where a new row begins in values_array

        idx = 0
        for i in range(len(matrix)):
          self.index_array.append(idx)
          idx += np.count_nonzero(matrix[i])

          for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    self.values_array.append(matrix[i][j])
                    self.columns_array.append(j)
            
        self.values_array = np.array(self.values_array)
        self.columns_array = np.array(self.columns_array)
        self.index_array = np.array(self.index_array)
    
    def to_dense(self):
      '''
      Retorna uma representacao densa (completa) da matriz CSR.

      Retorna:
        - np.ndarray com a matriz densa
      '''
      maximum_idx = len(self.index_array)-1
      total_of_values = len(self.values_array)

      cols = max(list(self.columns_array))+1
      rows = len(self.index_array)

      dense_mtx = [[0]*cols for i in range(rows)]
      for idx in range(rows):
        line_start = self.index_array[idx]
        line_end = self.index_array[idx+1] \
          if idx < maximum_idx else total_of_values

        for n in range(line_start, line_end):
          an = self.values_array[n]
          column = self.columns_array[n]
          dense_mtx[idx][column] = an

      return np.array(dense_mtx)

    def __mult_by_vector(self, other):
        '''
        Multiplica esta matriz CSR por um vetor

        Recebe:
          - other: instancia de np.ndarray
        Retorna
          - instancia de np.ndarray com o resultado da multiplicacao
        '''
        maximum_idx = len(self.index_array)-1
        total_of_values = len(self.values_array)

        result = []
        for idx in range(len(self.index_array)):
          line_start = self.index_array[idx]
          line_end = self.index_array[idx+1] \
            if idx < maximum_idx else total_of_values

          acc = 0
          t = 0
          for n in range(line_start, line_end):
            an = self.values_array[n]
            column = self.columns_array[n]
            acc += an*other[column]
      
          result.append(acc)

        return np.array(result)

    def mult(self, other):
        '''
        Multiplica esta matriz CSR por outra ou por um vetor (completo)

        Recebe:
          - other: instancia CSRMatrix ou np.ndarray
        Retorna
          - instancia CSRMatrix ou np.ndarray com o resultado da multiplicacao
        '''
        if isinstance(other, np.ndarray):
          return self.__mult_by_vector(other)

        values_array = []
        columns_array = []
        index_array = []

        for i in range(len(self.index_array)):
            index_array.append(len(values_array))
            if i == len(self.index_array)-1:
                vector_init, vector_end = self.index_array[i], len(
                    self.values_array)
            else:
                vector_init, vector_end = self.index_array[i], self.index_array[i+1]
            A_vector = self.values_array[vector_init:vector_end]
            A_columns = self.columns_array[vector_init:vector_end]

            B_columns = set(other.columns_array)
            column = 0
            for j in range(len(B_columns)):
                B_vector = []
                B_rows = []

                for k in range(len(other.values_array)):
                    row = 0
                    if other.columns_array[k] == j:
                        B_vector.append(other.values_array[k])
                        while row < len(other.index_array)-1 and k >= other.index_array[row+1]:
                            row += 1
                        B_rows.append(row)

                mult_sum = 0
                
                intersection = set(A_columns).intersection(set(B_rows))
                for intersect in sorted(intersection):
                    index_a = list(A_columns).index(intersect)
                    index_b = list(B_rows).index(intersect)
                    mult_sum += A_vector[index_a]*B_vector[index_b]

                if mult_sum != 0:
                    values_array.append(mult_sum)
                    columns_array.append(column)
                column += 1

        return CSRMatrix(
            [values_array, columns_array, index_array],
            from_csr=True
        )
