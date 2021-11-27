import paddle as pd
import paddle.nn as nn

class ResNet(nn.Layyer):
    def __init__(self, in_dim=64, num_classes=10):
        super().__init__()
        # stem layers
        self.conv1 = nn.Conv2D(in_chanels = 3,
                               out_channel = in_dim,
                               kernel_size = 3,
                               stride = 1,
                               padding = 1,
                               bias_attr = False)
        self.bn1 = nn.BatchNorm2D(in_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)

        return x

def main():
    t = pd.randn([4, 3, 32, 32])
    model = ResNet()
    out = model(t)
    print(out.shape)

if __name__ == "__main__":
    # 来自aaa的修改
    print(pd.__version__)