import torch
from PIL import Image
from torchvision import models, transforms
from torchvision.models import VGG16_BN_Weights, GoogLeNet_Weights, ResNet50_Weights, ResNet18_Weights
import torch.nn as nn


if __name__ == '__main__':
    '''
    图片分类学一个的话，学resnet50，其次vgg16_bn，再次googlenet
    '''
    vgg = models.vgg16_bn(weights=VGG16_BN_Weights.IMAGENET1K_V1)  # 在imagenet数据集上训练好的模型
    googlenet = models.googlenet(weights=GoogLeNet_Weights.IMAGENET1K_V1)
    resnet50 = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
    resnet18 = models.resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)

    print(resnet50)
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
