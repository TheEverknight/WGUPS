
class hashTable:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash% self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for group in self.map[key_hash]:
                if group[0] == key:
                    group.append(value)

                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for group in self.map[key_hash]:
                if group[0] == key:
                    return group
        return self.map[key_hash]

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] ==key:
                self.map[key_hash].pop(i)





    def print(self):
        print('--------Package_ID & Destination--------')
        for item in self.map:
            if item is not None:
                print(str(item))



class HashTable:
    # Hashtable made to a capacity of 99 to avoid any collisions
    def __init__(self, capacity = 99):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # put() that allows the packages to be placed into buckets
    def put(self, package):
        key = package.package_id
        index = hash(key) % len(self.table)
        self.table[index].append(package)

# Hashtable initiated for later retrieval
table = HashTable()