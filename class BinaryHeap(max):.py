class BinaryHeap:
    def __init__(self):
        self._heap = []
    
    def _perc_up(self, cur_idx):

        while (cur_idx-1)//2 >=0:
            parent_index = (cur_idx-1)//2
            if self._heap[parent_index] < self._heap[cur_idx]:
                self._heap[parent_index],self._heap[cur_idx] = self._heap[cur_idx],self._heap[parent_index]
                cur_idx = parent_index
            else:
                break


    def insert(self, item):
        self._heap.append(item)
        self._perc_up(len(self._heap)-1)
    
    def _get_max_child(self, parent_idx):
        if 2*parent_idx+2 > len(self._heap)-1:
            return 2*parent_idx+1
        elif self._heap[2*parent_idx+2] <self._heap[2*parent_idx+1]:
            return 2*parent_idx+1
        else:
            return 2*parent_idx+2
        
    def _perc_down(self, cur_idx):

        while 2*cur_idx+1 <= len(self._heap)-1:
            max_child = self._get_max_child(cur_idx)
            if self._heap[cur_idx]<self._heap[max_child]:
                self._heap[cur_idx],self._heap[max_child] = self._heap[max_child],self._heap[cur_idx]
                cur_idx = max_child
            else:
                break

    def delete(self, index):
        self._heap[index],self._heap[-1] = self._heap[-1], self._heap[index]
        result = self._heap.pop
        self._perc_down(index)
        return result
    
    def heapify(self, not_a_heap):
        self._heap =  not_a_heap[:]
        cur_idx = len(self._heap)//2 -1
        while cur_idx<=0:
            self._perc_down(cur_idx)
            cur_idx-=1

    def is_empty(self):
        return not bool(self._heap)
    
    def __len__(self):
        return len(self._heap)
    def __str__(self):
        return str(self._heap)
    

a_heap = BinaryHeap()
a_heap.heapify([9, 5, 6, 2, 3])
print(a_heap)

heap = BinaryHeap()
heap.insert(2)
heap.insert(22)
heap.insert(12)
heap.insert(242)
heap.insert(72)
heap.insert(101)
print(heap)