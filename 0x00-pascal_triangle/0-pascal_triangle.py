def pascal_triangle(n):
  """
  This function generates Pascal's Triangle of size n.

  Args:
      n: An integer representing the number of rows in the triangle.

  Returns:
      A list of lists of integers representing Pascal's Triangle.
      Returns an empty list if n <= 0.
  """

  if n <= 0:
    return []

  
  triangle = [[1]]


  for i in range(1, n):

    new_row = [1] + [triangle[i - 1][j - 1] + triangle[i - 1][j] for j in range(1, i)] + [1]
    triangle.append(new_row)

  return triangle

triangle = pascal_triangle(5)
print(triangle)

