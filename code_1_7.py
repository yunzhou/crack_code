# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
def setZeros(m):
  zero_rows = [False]*m.shape[0]
  zero_cols = [False]*m.shape[1]
  for i in range(m.shape[0]):
      for j in range(m.shape[1]):
          if m[i,j]==0:
              zero_rows[i]=True
              zero_cols[j] = True
  m[zero_rows, :]=0
  m[:, zero_cols] = 0


if __name__ == '__main__':
    import numpy as np
    m = np.random.rand(4,4)
    m[0, 0] = 0
    m[1, 0] = 0
    m[2, 2] = 0
    print(m)

    print(m)