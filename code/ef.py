import timm

ef_model = timm.create_model("resnet50", pretrained = True)
from torchsummary import summary
print(summary(ef_model, (3, 512, 512)))

import torch

torch.save(ef_model.state_dict(), "./pretrained_resNet.pth")