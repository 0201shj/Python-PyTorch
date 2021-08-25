import torch

matrix1 = torch.tensor([[1., 2.], [3., 4.]])
matrix2 = torch.tensor([[5., 6.],[7., 8.]])

sum_matrix = matrix1 + matrix2
print(sum_matrix)
#tensor([[ 6.,  8.],
#        [10., 12.]])

sub_matrix = matrix1 - matrix2
print(sub_matrix)
#tensor([[-4., -4.],
#        [-4., -4.]])

mul_matrix = matrix1 * matrix2
print(mul_matrix)
#tensor([[ 5., 12.],
#        [21., 32.]])

div_matrix = matrix1 / matrix2
print(div_matrix)
#tensor([[0.2000, 0.3333],
#        [0.4286, 0.5000]])