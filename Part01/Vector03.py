import torch

vector1 = torch.tensor([1., 2., 3.])
vector2 = torch.tensor([4., 5., 6.])

print(torch.add(vector1, vector2))
#tensor([5., 7., 9.])

print(torch.sub(vector1, vector2))
#tensor([-3., -3., -3.])

print(torch.mul(vector1, vector2))
#tensor([ 4., 10., 18.])

print(torch.div(vector1, vector2))
#tensor([0.2500, 0.4000, 0.5000])

print(torch.dot(vector1, vector2))
#tensor(32.)