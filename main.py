import torchvision

if __name__ == '__main__':
    torchvision.datasets.MNIST(root='./data', train=True, download=True)