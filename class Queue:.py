class Queue:
    def __init__(self):
        self._items = []
    def is_empty(self):
        if len(self._items)==0:
            return True
        else:
            return False
    def enqueue(self,item):
        self._items.insert(0,item)
    def dequeue(self):
        return self._items.pop()
    def size(self):
        return len(self._items)


def hot_potato(name_list,num):
    q = Queue()
    for name in name_list:
        q.enqueue(name)
    while q.size()>1:
        for i in range(num):
            name = q.dequeue()
            q.enqueue(name)
        q.dequeue()
    return q.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))