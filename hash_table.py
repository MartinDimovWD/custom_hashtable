
class HashTable:
    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def __setitem__(self, key, value):
        if key in self.__keys:
            index = self.__keys.index(key)
            self.__values[index] = value
            return
        """ If the max capacity is reached, we double the size of the table by adding slots with 'None'.
         Otherwise, the recursion in get_index will reach its max depth and become useless. """
        if self.max_capacity == self.size():
            self.__resize()
        """ Attributes will be set in the hash table on random basis.
         the index of the key-value pair is defined in the __calc_index method.
         Linear approach: if the 'slot' is taken, we will put the element in
         the next available slot. """
        index = self.__calc_index(key)
        index = self.__get_index(index)
        self.__keys[index] = key
        self.__values[index] = value

    def __calc_index(self, key):
        index = sum([ord(char) for char in key]) % self.max_capacity
        return index

    def __get_index(self, index):
        """ The index might collide as there could already be an element at that
        index. With recursion, we will find the next possible index where the
        element is 'None'. If the index is at max capacity, we return to the
        start of the list and search for the next empty slot."""
        if index == self.max_capacity:
            index = 0
        if self.__keys[index] is None:
            return index
        return self.__get_index(index+1)

    def size(self):
        return len([el for el in self.__keys if el is not None])

    def __resize(self):
        self.__keys = self.__keys+[None]*self.max_capacity
        self.__values = self.__values + [None] * self.max_capacity
        self.max_capacity *= 2

    def hash(self, key):
        pass

    def add(self, key, value):
        pass

    def get(self, key):
        pass


table = HashTable()
table['name'] = 'Peter'
table['age'] = 25

print(table)
print(table.get('name'))