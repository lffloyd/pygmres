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
        columns_array.append()
  return values_array, columns_array, index_array
