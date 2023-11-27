class Node:
    def __init__(self,node_data):
        self._data = node_data
        self._next = None
    def get_data(self):
        return self._data
    def set_data(self,node_data):
        self._data = node_data
    data = property(get_data, set_data)
    def get_next(self):
        return self._next
    def set_next(self, node_next):
        self._next = node_next
    next = property(get_next, set_next)
    def __str__(self):
        """String"""
        return str(self._data)
temp = Node(93)
temp.data = 100
print(temp)


class UnorderedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head==None
    def add(self,item):
        temp_node = Node(item)
        temp_node.set_next(self.head)
        self.head = temp_node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data ==item:
                return True
            else:
                current = current.next
        return False
    def remove(self,item):
        if self.head is None:
            raise ValueError("{} is not in the list".format(item))
        current = self.head
        if current.data==item:
            self.head = self.head.next
        else:
           while current.next is not None:
               if current.next.data==item:
                   current.next = current.next.next
               else:
                   current = current.next
        raise ValueError("{} is not in the list".format(item))
    def append(self,item):
        if self.head is None:
            self.head = Node(item)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
        current.next = Node(item)
    def insert(self,item, index):
        if self.size()<index:
            raise ValueError("{} is out of the range of index".format(index))
        else:
            if index ==0:
                self.add(item)
            else:
                current = self.head
                for _ in range(index -1):
                    current = current.next
                temp_node = Node(item)
                temp_node.next = current.next
                current.next = temp_node 
                


my_list = UnorderedList()
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)
print(my_list.remove(17))
print(my_list.size())

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next

        return False
    def add(self, item):
        """Add a new node"""
        current = self.head
        previous = None
        temp = Node(item)

        while current is not None and current.data < item:
            previous = current
            current = current.next

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

