## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        self.conv1 = nn.Conv2d(1, 32, 5)
        self.mp1 = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(32, 64, 5)
        self.mp2 = nn.MaxPool2d(2,2)
        self.conv3 = nn.Conv2d(64, 128, 5)
        self.mp3 = nn.MaxPool2d(2,2)
        self.conv4 = nn.Conv2d(128, 256, 5)
        self.mp4 = nn.MaxPool2d(2,2)
        self.d = nn.Dropout(p=0.2)
        self.l = nn.Linear(256*10*10,136)
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        x = self.mp1(F.relu(self.conv1(x)))
        x = self.mp2(F.relu(self.conv2(x)))
        x = self.mp3(F.relu(self.conv3(x)))
        x = self.mp4(F.relu(self.conv4(x)))
        x = self.d(x)
        x = x.view(x.shape[0],-1)
        x = self.l(x)
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
