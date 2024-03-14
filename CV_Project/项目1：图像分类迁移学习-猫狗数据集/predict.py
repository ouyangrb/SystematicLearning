import torch
from PIL import Image
from torchvision import models, transforms
import numpy as np
import torch.nn as nn
np.set_printoptions(precision=4, suppress=True)

def softmax(z):
    # 计算softmax函数
    e_z = np.exp(z - np.max(z))
    return e_z / np.sum(e_z)


if __name__ == '__main__':
    ts = transforms.ToTensor()
    resnet = models.resnet18()
    resnet.fc = nn.Linear(in_features=512, out_features=2, bias=True)
    state_dict = torch.load("./models/best.pth")  # 加载训练好的参数
    # 如果是在GPU上训练保存的best.pth,在CPU上预测就要用下面的代码
    # state_dict = torch.load("./models/best.pth", map_location=torch.device('cpu'))
    resnet.load_state_dict(state_dict)
    resnet.eval()

    with torch.no_grad():
        img = Image.open("./test_images/dog.1000.jpg").convert("RGB")
        img = ts(img)
        img = img[None, ...]  # 加一个维度
        r = resnet(img)
        print(r.shape)  # torch.Size([1, 2])
        print(r)
        # print(r[0][:5])
        print(softmax(r[0].numpy()))
        print(torch.argmax(r).item())