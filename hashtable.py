# hashtable.py

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [None]

    def __len__(self):
        return self.values

    def __setitem__(self, key, value):
        self.values.append(value)
