# this scripts contains code to practice autograd
# lets see how it works

# autograd is powerfull differentiation auto engine that powers neural network training
import torch, torchvision
model = torchvision.models.resnet18(pretrained=True)
data = torch.rand(1,3,64,64)
labels = torch.rand(1,1000)