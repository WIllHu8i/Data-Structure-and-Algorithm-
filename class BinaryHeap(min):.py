class BinaryHeap:
    def __init__(self):
        self._heap = []
    def __str__(self):
        return str(self._heap)
    
    def _perc_up(self, i):
        while (i-1)//2 >=0:
            parent = self._heap[(i-1)//2]
            if parent >self._heap[i]:
                self._heap[i],self._heap[(i-1)//2] = self._heap[(i-1)//2],self._heap[i]
                i = (i-1)//2
            else:
                break
    
    def insert(self, item):
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)

    def _perc_down(self, i):
        while 2*i+1 < len(self._heap):
            min_child = self._get_min_child(i)
            if self._heap[i]>self._heap[min_child]:
                self._heap[i], self._heap[min_child] =  self._heap[min_child],self._heap[i]
                i = min_child
            else:
                break



    
    def _get_min_child(self, i):
        if 2*i+2>len(self._heap)-1:
            return 2*i+1
        elif self._heap[2*i+1]<self._heap[2*i+2]:
            return 2*i+1
        else:
            return 2*i+2

    def delete(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result
        
    def heapify(self, not_a_heap):
            self._heap = not_a_heap[:]
            cur_idx = len(self._heap) // 2 - 1
            while cur_idx >= 0:
                self._perc_down(cur_idx)
                cur_idx = cur_idx - 1
    
    def is_empty(self):
        return not bool(self._heap)

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)

heap = BinaryHeap()
heap.insert(2)
heap.insert(22)
heap.insert(12)
heap.insert(242)
heap.insert(72)
heap.insert(101)
print(heap)