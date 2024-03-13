from torch.utils.data import DataLoader
from torchvision import datasets, transforms


class DataSet:  # 数据集
    def __init__(self, root_dir, batch_size, shuffle, num_workers):
        super(DataSet, self).__init__()
        self.dataset = datasets.ImageFolder(root=root_dir,  # 文件路径
                                            transform=transforms.Compose([transforms.ToTensor(),  # 转成tensor
                                                                          transforms.Resize(size=(224, 224), antialias=True)])  # resize到224*224
                                            )
        self.loader = DataLoader(
            dataset=self.dataset,
            batch_size=batch_size,
            shuffle=shuffle,
            num_workers=num_workers,  # 几个线程
            prefetch_factor=None if num_workers == 0 else num_workers * batch_size
        )

    def __len__(self):
        return len(self.dataset.imgs)  # 数据集里面有几个图片

    def __iter__(self):
        for data in self.loader:
            yield data


if __name__ == '__main__':
    batch_size = 8
    num_workers = 0
    train_dataset = DataSet('./datasets/dogcat/training_data', batch_size, True, num_workers)
    test_dataset = DataSet('./datasets/dogcat/testing_data', batch_size, False, num_workers)
    # print(len(train_dataset))  # 1000个图片
    # print(len(test_dataset))  # 400个图片
    for inputs, labels in train_dataset:  # 调用train_dataset实例里面的__iter__方法
        # print(inputs.shape)  # torch.Size([8, 3, 224, 224])  每次拿8张图片，1000*8=125 次拿完
        # print(labels.shape)  # torch.Size([8]) 类别0代表猫，1代表狗
        print(labels[0].item())

