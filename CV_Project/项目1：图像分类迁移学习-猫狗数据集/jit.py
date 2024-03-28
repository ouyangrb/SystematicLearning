import torch
import torch.nn as nn
from torch import quantization
from torchvision import models

if __name__ == '__main__':
    model = models.resnet18()
    model.fc = nn.Linear(in_features=512, out_features=2, bias=True)
    state_dict = torch.load("./models/best.pth", map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)
    model.eval()

    types_to_quantize = {nn.Conv2d, nn.BatchNorm2d, nn.ReLU}
    quant = quantization.quantize_dynamic(model, types_to_quantize, dtype=torch.qint8)

    scr = torch.jit.script(quant)
    torch.jit.save(scr, './resnet18_dogcat_scriptmodel.pth')  # 转成静态化模型


'''
pytorch 既可以训练模型，也可以通过jit成静态模型，作部署
'''