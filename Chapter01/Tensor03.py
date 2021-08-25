import torch

tensor1 = torch.tensor([[[1.,2.],[3.,4.]], [[5.,6.],[7.,8.]]])
tensor2 = torch.tensor([[[9.,10.],[11.,12.]], [[13.,14.],[15.,16.]]])

print(torch.add(tensor1, tensor2))

print(torch.sub(tensor1, tensor2))

print(torch.mul(tensor1, tensor2))

print(torch.div(tensor1, tensor2))

print(torch.matmul(tensor1, tensor2))
#tensor([[[ 31.,  34.],
#         [ 71.,  78.]],

#        [[155., 166.],
#         [211., 226.]]])