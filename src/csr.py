def parse_csr(matrix):
  
  values_array = [] #values in original matrix
  columns_array = [] #column index of where the value is
  index_array = [] #index of where a new row begins in values_array

  for i in range(len(matrix)):
    if len(values_array) not in index_array:
          index_array.append(len(values_array))
    for j in range(len(matrix[i])):
      if matrix[i][j] != 0:
        values_array.append(matrix[i][j])
        columns_array.append(j)
  return values_array, columns_array, index_array

#Arguments are lists of arrays, in which the first position of the list is the values_array,
#the second is the columns_array 
#and the last one is the index_array

def multiply_matrix(matrix_A, matrix_B):
  values_array = [] #values in original matrix
  columns_array = [] #column index of where the value is
  index_array = [] #index of where a new vector begins in values_array

  for i in range(len(matrix_A[2])):
    index_array.append(matrix_A[2][i])
    if i == len(matrix_A[2])-1:
      vector_init , vector_end = matrix_A[2][i] , len(matrix_A[0])
    else:
      vector_init , vector_end = matrix_A[2][i] , matrix_A[2][i+1]
    A_vector = matrix_A[0][vector_init:vector_end] #Row values
    A_columns =  matrix_A[1][vector_init:vector_end] #Values Columns
    
    B_columns = set(matrix_B[1])
    for j in range(len(B_columns)):
      B_vector = []
      B_rows = []

      for k in range(len(matrix_B[0])):
        row = 0
        if matrix_B[1][k] == j:
          B_vector.append(matrix_B[0][k])
          while row < len(matrix_B[2])-1 and k >= matrix_B[2][row+1] :
            row += 1
          B_rows.append(row)
      
      mult_sum = 0

      try:
        intersection = set(A_columns).intersection(set(B_rows))
        for intersect in intersection:
          index_a = A_columns.index(intersect)
          index_b = B_rows.index(intersect)
          columns_array.append(intersect)
          mult_sum += A_vector[index_a]*B_vector[index_b]
      except:
        pass
      if mult_sum != 0:
        values_array.append(mult_sum)
  return values_array, columns_array, index_array
