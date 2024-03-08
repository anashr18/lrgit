import torch
from torch import nn


def exists(val):
    return val is not None


class YgXformers(nn.Module):
    def __init__(self):
        super.__init__()

    def forward(self, x):
        return x
