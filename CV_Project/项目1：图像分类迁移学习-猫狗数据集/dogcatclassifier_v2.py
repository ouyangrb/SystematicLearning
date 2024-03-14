import torch
import torch.nn as nn
from torch import optim
from torchvision import models
from torchvision.models import VGG16_BN_Weights, GoogLeNet_Weights, ResNet50_Weights

from dataset import DataSet

import numpy as np
import os

torch.set_printoptions(precision=2, sci_mode=False)


class DogCatClassifier_V2:  # 增加了模型的保存与恢复
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
        self.print_interval = 2

        self.model_dir = 'models'
        if not os.path.exists(self.model_dir):  # 如果不存在models文件夹就自动创建一个
            os.makedirs(self.model_dir)
        else:  # 如果存在，就加载最后一个保存的模型
            names = os.listdir(self.model_dir)  # 所有文件的文件名
            if len(names) > 0:
                names.sort()
                name = names[-1]
                print('============loading=======', name)  # # 模型恢复
                missing_keys, unexpected_keys = self.model.load_state_dict(torch.load(os.path.join(self.model_dir, name)))
        self.model = self.model.to(self.device)  # 注意这一行要放在后面

    def save_model(self, epoch):
        # 模型保存
        if epoch == self.total_epoch:
            model_path = os.path.join(self.model_dir, "last.pth")
        else:
            model_path = os.path.join(self.model_dir, f"model_{epoch:04d}.pth")
        torch.save(self.model.state_dict(), model_path)

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

        for epoch in range(self.total_epoch):
            self.model.train(True)  # Sets the module in training mode.
            train_loss = []
            batch = 0
            for inputs, labels in trainset:
                inputs = inputs.to(self.device)
                labels = labels.to(self.device)

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
            for data in testset:
                inputs, labels = data
                inputs = inputs.to(self.device)
                labels = labels.to(self.device)

                # forward
                output = self.model(inputs)
                loss = self.loss_fn(output, labels)

                test_loss.append(loss.item())
                if batch % self.print_interval == 0:
                    print(f'{epoch + 1}/{self.total_epoch} {batch} test_loss={loss.item()}')
                batch += 1
            self.save_model(epoch)  # 1、每个epoch结束 调用模型保存

        print(f'{epoch} train mean loss {np.mean(train_loss):.4f} test mean loss {np.mean(test_loss):.4f}')
        self.save_model(self.total_epoch)  # 2、train结束再调用模型保存


if __name__ == '__main__':
    vgg = models.vgg16_bn(weights=VGG16_BN_Weights.IMAGENET1K_V1)
    googlenet = models.googlenet(weights=GoogLeNet_Weights.IMAGENET1K_V1)
    resnet = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)

    train_data_dir = './datasets/dogcat/training_data'
    test_data_dir = './datasets/dogcat/testing_data'
    model = DogCatClassifier_V2(vgg, train_data_dir, test_data_dir)
    model.train()
