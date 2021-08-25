import torch

matrix1 = torch.tensor([[1., 2.], [3., 4.]])
matrix2 = torch.tensor([[5., 6.],[7., 8.]])

print(torch.add(matrix1, matrix2))
#tensor([[ 6.,  8.],
#        [10., 12.]])

print(torch.sub(matrix1, matrix2))
#tensor([[-4., -4.],
#        [-4., -4.]])

print(torch.mul(matrix1, matrix2))
#tensor([[ 5., 12.],
#        [21., 32.]])

print(torch.div(matrix1, matrix2))
#tensor([[0.2000, 0.3333],
#        [0.4286, 0.5000]])

print(torch.matmul(matrix1, matrix2))
#tensor([[19., 22.],
#        [43., 50.]])
