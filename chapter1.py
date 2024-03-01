import numpy as np

# 예제 1-3

# np.array(): 벡터 또는 행렬을 나타냄
A = np.array([[1,0], [2,1], [4,3]])
B = np.array([[4,3], [1,1], [0,2]])

print('예제 1-3\n')
print(f'A+B = \n {A+B}\n')
print(f'A-B = \n {A-B}\n')
print(f'5B = \n {5*B}\n')

# 예제 1-4

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

# AB
# np.matmul(A, B): 행렬 A와 행렬 B의 행렬곱
AB = np.matmul(A, B)
BA = np.matmul(B, A)

print(f'AB = \n{AB}')
print(f'BA = \n{BA}')

# np.array_equal(A, B): 행렬 A와 행렬 B가 서로 같은지 확인
# 같으면 True, 다르면 False 반환
print(f'AB { "=" if np.array_equal(A, B) else "!=" } BA')

# 예제 1-5

A = np.array([[3,0], [-1,2], [1,1]])
B = np.array([[-3,-1], [2,1], [4,3]])
C = np.array([[1,2,3], [2,0,1]])
D = np.array([[1], [2], [3]])

# A + 2B
# AC
# 3D

print(f'A + 2B =\n{A+2*B}')
print(f'AC =\n{np.matmul(A,C)}')
print(f'3D =\n{3*D}')