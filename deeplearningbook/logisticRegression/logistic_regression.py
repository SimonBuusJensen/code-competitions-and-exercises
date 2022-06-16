from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_wine

if __name__ == '__main__':

    dataset = load_wine()

    print(dataset)

    model = LogisticRegression()