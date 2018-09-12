class HashTable(object):
    """
    Implementation of HashTable that keep doubling in size
    whenever risks of collisions gets too high.
    """
    def __init__(self, length=4, *args, **kwargs):
        self.array = [None] * length

    def hash(self, key, length=None):
        length = len(self.array) if length is None else length
        return hash(key) % length

    def add(self, key, value):
        h = self.hash(key)
        if self.array[h] is not None:
            for kvp in self.array[h]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[h].append([key, value])
        else:
            self.array[h] = []
            self.array[h].append([key, value])

        # If the array is too populated and have
        # too high risk of collissions, we double the length
        # of the array and copy all items over.
        if self.is_full():
            self.dubble()

    def exists(self, key):
        h = self.hash(key)
        if self.array[h] is not None:
            for kvp in self.array[h]:
                if kvp[0] == key:
                    return True

        return False

    def get(self, key):
        h = self.hash(key)
        if self.array[h] is None:
            raise KeyError()
        else:
            for kvp in self.array[h]:
                if kvp[0] == key:
                    return kvp[1]

            raise KeyError()

    def remove(self, key):
        h = self.hash(key)
        if self.array[h] is None:
            raise KeyError()
        else:
            for i in range(len(self.array[h])):
                if key == self.array[h][i][0]:
                    self.array[h].pop(i)
                    # If it is an empty array, reset it to None
                    # which was the original default value.
                    if not self.array[h]:
                        self.array[h] = None
                    return
        raise KeyError()

    def is_full(self):
        items = 0
        for item in self.array:
            if item is not None:
                items += 1

        return items > len(self.array)/2

    def dubble(self):
        ht2 = HashTable(length=len(self.array)*2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue

            for kvp in self.array[i]:
                ht2.add(kvp[0], kvp[1])

        self.array = ht2.array


ht = HashTable()
print(ht.array)
ht.add('id', 1)
ht.add('id', 2)
print(ht.array)
print(ht.get('id'))
print(ht.exists('id'))
print(ht.exists('foo'))
print(ht.remove('id'))
ht.add('id', 1)
ht.add('hello', 2)
ht.add('world', 3)
print(ht.array)
