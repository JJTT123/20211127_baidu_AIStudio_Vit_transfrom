class T():
    def __init__(self):
        pass

    def __call__(self, x):
        return self.d(x)

    def d(self, x):
        return x+1

if __name__ == "__main__":
    t = T()
    #print(t.forward(1))
    print(t(1))