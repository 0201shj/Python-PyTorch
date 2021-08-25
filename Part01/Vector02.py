import torch

vector1 = torch.tensor([1., 2., 3.])
vector2 = torch.tensor([4., 5., 6.])

add_vector = vector1 + vector2
print(add_vector)
#tensor([5., 7., 9.])

sub_vector = vector1 - vector2
print(sub_vector)
#tensor([-3., -3., -3.])

mul_vector = vector1 * vector2
print(mul_vector)
#tensor([ 4., 10., 18.])

div_vector = vector1 / vector2
print(div_vector)
#tensor([0.2500, 0.4000, 0.5000])
