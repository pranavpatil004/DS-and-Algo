

from collections import OrderedDict


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, ele):
        if ele in self.dic:
            self.dic.move_to_end(ele)
            return self.dic[ele]
        else:
            return -1
    
    def set(self, ele):
        self.dic[ele] = ele
        self.dic.move_to_end(ele)
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)
        return self.dic[ele]


l = LRU(2)
l.set(1)
print(l.dic)
l.set(2)
print(l.dic)
l.set(3)
print(l.dic)
print(l.get(2))
print(l.dic)
l.set(4)
print(l.dic)
print(l.dic)