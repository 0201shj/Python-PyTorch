import torch

scalar1 = torch.tensor([1.])
scalar2 = torch.tensor([3.])

print(torch.add(scalar1, scalar2))
#tensor.([4.])

print(torch.sub(scalar1, scalar2))
#tensor.([-2.])

print(torch.mul(scalar1, scalar2))
#tensor.([3.])

print(torch.div(scalar1, scalar2))
#tensor.([0.3333])