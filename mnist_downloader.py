import urllib.request

url_base = 'http://yann.lecun.com/exdb/mnist/'
key_file = {
    'train_img': 'train-images-idx3-ubyte.gz',
    'train_label': 'train-labels-idx1-ubyte.gz',
    'test_img': 't10k-images-idx3-ubyte.gz',
    'test_label': 't10k-labels-idx1-ubyte.gz'
}

dataset_dir = '/home/sai/Desktop/github/zero-deeplearning'

for v in key_file.values():
    file_path = dataset_dir + '/' + v
    print(file_path)
    urllib.request.urlretrieve(url_base + v, file_path)
