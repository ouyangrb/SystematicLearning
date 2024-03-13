import torch
from PIL import Image
from torchvision import models,transforms
from torchvision.models import VGG16_BN_Weights, GoogLeNet_Weights, ResNet50_Weights
import torch.nn as nn


if __name__ == '__main__':

    vgg = models.vgg16_bn(weights=VGG16_BN_Weights.IMAGENET1K_V1)
    googlenet = models.googlenet(weights=GoogLeNet_Weights.IMAGENET1K_V1)
    resnet = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)

    print(resnet)
    # model = resnet
    # model.eval()
    #
    # ts = transforms.ToTensor()
    # file = r'./test_images/cat.1.jpg'
    # with torch.no_grad():
    #     img = Image.open(file).convert("RGB")
    #     img = ts(img)
    #     img = img[None, ...]
    #     r = model(img)
    #     print(torch.argmax(r).item())
