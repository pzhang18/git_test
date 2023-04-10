import torch
import numpy as np

print(torch.__version__)
x = torch.rand(5,3)
matrix = torch.tensor([[5,6],[7,8]])
print("x=", x, "matrix=", matrix)
print(x.ndim, matrix.ndim)
print(x.shape, matrix.shape)