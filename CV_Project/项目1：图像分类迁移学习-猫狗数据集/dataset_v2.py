from torch.utils.data import DataLoader
from torchvision import datasets, transforms


class DataSet_V2:  # 数据集 版本2(对训练数据做了数据增强）
    def __init__(self, root_dir, batch_size, shuffle, num_workers, istrainning):
        super(DataSet_V2, self).__init__()
        self.istrainning = istrainning
        self.dataset = datasets.ImageFolder(root=root_dir,
                                            transform=self.get_transforms())  # 自定义了transform格式
        self.loader = DataLoader(
            dataset=self.dataset,
            batch_size=batch_size,
            shuffle=shuffle,
            num_workers=num_workers,
            prefetch_factor=None if num_workers == 0 else num_workers * batch_size
        )

    def get_transforms(self):
        if not self.istrainning:  # 推理的时候
            return transforms.Compose([
                transforms.Lambda(self.convert_img),  # 读入的图片转RGB，因为读入的图片有可能是RGBA，把A透明度通道去掉
                transforms.ToTensor(),
                transforms.Resize(size=(224, 224), antialias=True)
            ])
        else:  # 训练的时候
            return transforms.Compose([
                transforms.Lambda(self.convert_img),
                # 随机水平翻转输入图像
                transforms.RandomHorizontalFlip(p=0.4),  # 概率是0.4
                # 随机改变图像的亮度、对比度、饱和度和色调等属性，从而增加数据样本的多样性
                transforms.ColorJitter(),
                # 将给定图像随机裁剪为不同的大小和宽高比，然后缩放所裁剪得到的图像为指定的大小；（即先随机采集，然后对裁剪得到的图像缩放为同一大小）
                # 默认scale = (0.08, 1.0)
                transforms.RandomResizedCrop(size=224, scale=(0.7, 1.0)),
                transforms.ToTensor()
            ])

    @staticmethod
    def convert_img(img):
        return img.convert("RGB")

    def __len__(self):
        return len(self.dataset.imgs)

    def __iter__(self):
        for data in self.loader:
            yield data


if __name__ == '__main__':
    batch_size = 8
    num_workers = 0
    train_dataset = DataSet_V2('datasets/dogcat/train', batch_size, True, num_workers, True)
    test_dataset = DataSet_V2('datasets/dogcat/test', batch_size, False, num_workers, False)
    # print(len(train_dataset))
    # print(len(test_dataset))
    # print(len(test_small_dataset))
    for inputs, labels in train_dataset:
        # print(inputs.shape)
        # print(labels.shape)
        print(labels[0].item())
        # for img in inputs:
        #     img_PIL = transforms.ToPILImage()
        #     picture = img_PIL(img)
        #     picture.save('11.jpg')
        #     break
        # break
