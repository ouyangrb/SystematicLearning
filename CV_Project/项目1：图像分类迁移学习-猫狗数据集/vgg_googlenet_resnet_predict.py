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

    # print(vgg)
    model = vgg  # model和vgg都引用指向相同
    model.eval()  # 评估模式

    ts = transforms.ToTensor()  # 类的实例化
    file = r'./test_images/cat.1.jpg'
    with torch.no_grad():
        img = Image.open(file).convert("RGB")  # 转RGB格式
        img = ts(img)  # 实例像函数那样被调用，调用__call__方法，传入图片，返回一个tensor对象
        # print(img.shape)  # [3, 280, 300] [c h w ]
        img = img[None, ...]  # 一定要增加一个维度
        print(img.shape)  # [[1, 3, 280, 300] [n c h w]
        r = model(img)
        # print(r)  # 得到1000个类别的概率值
        print(torch.argmax(r).item())  # 找最大的一个
