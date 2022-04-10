import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm # Displays a progress bar

import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchsummary import summary
from torchvision import datasets, transforms
from torch.utils.data import Dataset, Subset, DataLoader, random_split

if torch.cuda.is_available():
    print("Using the GPU. You are good to go!")
    device = 'cuda'
else:
    print("Using the CPU. Overall speed may be slowed down")
    device = 'cpu'


# Code to load dataset and create dataloaders


# Code to preprocess images if needed 


# Code to get labels for images 


# Code to create CNN model


# Code to set hyperparameters 


# Code for baseline solution using nearest neighbour. 


# Code to train model 


# Code to evaluate model 



