import torch

scalar1 = torch.tensor([1.])
scalar2 = torch.tensor([3.])

add_scalar = scalar1 + scalar2
print(add_scalar)
# tensor([4.])

sub_scalar = scalar1 - scalar2
print(sub_scalar)
# tensor([-2.])

mul_scalar = scalar1 * scalar2
print(mul_scalar)
# tensor([3.])

div_scalr = scalar1 / scalar2
print(div_scalr)
# tensor([0.3333])