import unittest

class MinHeap:
    def __init__(self) -> None:
        self.values = []
        self.count = 0

    def push(self, value: int) -> None:
        if self.count < len(self.values):
            self.values[self.count] = value
        else:
            self.values.append(value)
        self.count += 1

        # Swap new item up the heap
        index = self.count
        while index > 1:
            parent_index = index // 2
            if self.values[parent_index - 1]  > self.values[index - 1]:
                temp = self.values[index - 1]
                self.values[index - 1] = self.values[parent_index - 1]
                self.values[parent_index - 1] = temp
                index = parent_index
            else:
                break


    def pop(self) -> int:
        if self.count == 0: raise IndexError("Heap is empty")
        
        # Remove top item from the heap 
        ret = self.values[0]
        self.count -= 1

        # Move the last added item to the top of the heap
        # and swap it downwards
        self.values[0] = self.values[self.count]

        # Find the children of the current item
        index = 1
        while index * 2 <= self.count:
            left_index = index * 2
            right_index = index * 2 + 1

            child_index = left_index
            child_val = self.values[left_index - 1]
            if right_index <= self.count and self.values[right_index - 1] < child_val:
                child_index = right_index
                child_val = self.values[right_index - 1]

            # Swap if the child is smaller than the current item
            if child_val < self.values[index - 1]:
                temp = self.values[index - 1]
                self.values[index - 1] = child_val
                self.values[child_index - 1] = temp
                index = child_index
            else:
                break

        return ret

    def peek(self) -> int:
        if self.count == 0: raise IndexError("Heap is empty")
        return self.values[0]

    def isEmpty(self) -> bool:
        return self.count == 0

    def __len__(self) -> int:
        return self.count

class TestMinHeap(unittest.TestCase):
    def test_push(self):
        min_heap = MinHeap()
        min_heap.push(4)
        min_heap.push(3)
        min_heap.push(2)
        min_heap.push(1)
        assert min_heap.values[0] == 1
        assert min_heap.values[1] == 2
        assert min_heap.values[2] == 3
        assert min_heap.values[3] == 4

    def test_push_order(self):
        min_heap = MinHeap()
        min_heap.push(3)
        min_heap.push(1)
        min_heap.push(2)
        min_heap.push(4)
        assert min_heap.values[0] == 1
        assert min_heap.values[1] == 3
        assert min_heap.values[2] == 2
        assert min_heap.values[3] == 4

    def test_pop(self):
        min_heap = MinHeap()
        min_heap.push(4)
        min_heap.push(3)
        min_heap.push(2)
        min_heap.push(1)

        assert min_heap.pop() == 1
        assert min_heap.pop() == 2
        assert min_heap.pop() == 3
        assert min_heap.pop() == 4

    def test_isEmpty(self):
        min_heap = MinHeap()
        assert min_heap.isEmpty()
        
        min_heap.push(1)
        min_heap.push(2)
        min_heap.push(3)
        assert not min_heap.isEmpty()

        min_heap.pop()
        min_heap.pop()
        min_heap.pop()
        assert min_heap.isEmpty()

    def test_peek(self):
        min_heap = MinHeap()

        min_heap.push(3)
        assert min_heap.peek() == 3
        min_heap.push(1)
        assert min_heap.peek() == 1
        min_heap.push(2)
        assert min_heap.peek() == 1
        min_heap.push(4)
        assert min_heap.peek() == 1


if __name__ == '__main__':
    unittest.main()
