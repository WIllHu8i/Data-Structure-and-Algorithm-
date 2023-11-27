class Deque:
    def __init__(self):
        self._items = []
    def is_empty(self):
        return not bool(self._items)
    def add_front(self, item):
        self._items.append(item)
    def add_rear(self,item):
        self._items.insert(0,item)
    def remove_front(self):
        return self._items.pop()
    def remove_rear(self):
        return self._items.pop(0)
    def size(self):
        return len(self._items)



def pal_checker(a_string):
    d = Deque()
    for char in a_string:
        d.add_rear(char)
    if d.size() %2==0:
        while d.size()>2:
            front = d.remove_front()
            rear = d.remove_rear()
            if front!=rear:
                return False
        if d.remove_front() != d.remove_rear():
            return False
        else:
            return True
    else:
        while d.size()>1:
            front = d.remove_front()
            rear = d.remove_rear()
            if front!=rear:
                return False
        return True
print(pal_checker("lsdkjfskf"))
print(pal_checker("willhukkh"))


