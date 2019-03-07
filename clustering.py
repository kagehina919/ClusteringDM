from Scripts.load_dataset import load_dataset
from Scripts.KMeans import KMeans

def main():
    sequences = load_dataset()
    ac = KMeans(sequences)

if __name__ == '__main__':
    main()