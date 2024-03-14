import torch
import torch.nn as nn
from torch import optim
from torchvision import models
from torchvision.models import VGG16_BN_Weights, GoogLeNet_Weights, ResNet50_Weights

from dataset import DataSet

import numpy as np

torch.set_printoptions(precision=2, sci_mode=False)


class DogCatClassifier_V1:  # 自定义训练器
    def __init__(self, model, train_data_dir, test_data_dir):
        self.batch_size = 32
        self.num_workers = 0
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = model
        self.train_data_dir = train_data_dir
        self.test_data_dir = test_data_dir
        self.total_epoch = 5
        self.lr = 0.005
        self.loss_fn = nn.CrossEntropyLoss()
        self.opt = optim.SGD(
            params=[p for p in self.model.parameters() if p.requires_grad is True],
            lr=self.lr
        )
        self.print_interval = 2  # 打印的间隔

        self.model = self.model.to(self.device)  # 1、模型要to device

    def train(self):
        # 1. 加载数据
        trainset = DataSet(root_dir=self.train_data_dir,
                           batch_size=self.batch_size,
                           shuffle=True,
                           num_workers=self.num_workers)
        testset = DataSet(root_dir=self.test_data_dir,
                          batch_size=self.batch_size,
                          shuffle=False,
                          num_workers=self.num_workers)

        for epoch in range(self.total_epoch):  # 遍历整个数据集的次数是total_epoch
            self.model.train(True)  # Sets the module in training mode.
            train_loss = []
            batch = 0
            for inputs, labels in trainset:
                inputs = inputs.to(self.device)  # 2、X 要to device
                labels = labels.to(self.device)  # 3、Y 要to device

                # forward
                output = self.model(inputs)
                loss = self.loss_fn(output, labels)

                # backward
                self.opt.zero_grad()
                loss.backward()
                self.opt.step()

                train_loss.append(loss.item())

                if batch % self.print_interval == 0:
                    print(f'{epoch + 1}/{self.total_epoch} {batch} train_loss={loss.item()}')
                batch += 1

            test_loss = []
            batch = 0
            for inputs, labels in testset:
                inputs = inputs.to(self.device)  # 4、测试X 要to device
                labels = labels.to(self.device)  # 5、测试Y 要to device

                # forward
                output = self.model(inputs)
                loss = self.loss_fn(output, labels)

                test_loss.append(loss.item())
                if batch % self.print_interval == 0:
                    print(f'{epoch + 1}/{self.total_epoch} {batch} test_loss={loss.item()}')
                batch += 1

            print(f'{epoch} train mean loss {np.mean(train_loss):.4f} test mean loss {np.mean(test_loss):.4f}')


if __name__ == '__main__':
    vgg = models.vgg16_bn(weights=VGG16_BN_Weights.IMAGENET1K_V1)
    googlenet = models.googlenet(weights=GoogLeNet_Weights.IMAGENET1K_V1)
    resnet = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)

    m = vgg
    train_data_dir = 'datasets/dogcat/train'
    test_data_dir = 'datasets/dogcat/test'
    model = DogCatClassifier_V1(m, train_data_dir, test_data_dir)
    model.train()
