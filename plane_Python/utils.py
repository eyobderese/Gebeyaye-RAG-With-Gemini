import pickle


def load_embedded_data(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)


def save_embedded_data(file_path, data):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)
