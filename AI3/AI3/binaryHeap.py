class Heap:
    def __init__(self):
        self.heap = []
        self.lastIndex = -1

    def push(self, value):
        self.lastIndex += 1
        if self.lastIndex < len(self.heap):
            self.heap[self.lastIndex] = value
        else:
            self.heap.append(value)
        self.siftUp(self.lastIndex)

    #returns the node with min fCost
    def pop(self):
        if self.lastIndex == -1:
            raise IndexError('pop from empty heap')

        min_value = self.heap[0]

        self.heap[0] = self.heap[self.lastIndex]
        self.lastIndex -= 1
        self.siftDown(0)

        return min_value

    def siftUp(self, index):
        while index > 0:
            parentIndex, parentValue = self.getParent(index)

            if parentValue <= self.heap[index].fCost:
                break

            self.heap[parentIndex], self.heap[index] =\
                self.heap[index], self.heap[parentIndex]

            index = parentIndex

    def siftDown(self, index):
        while True:
            indexVal = self.heap[index].fCost

            leftChildIndex, leftChildVal = self.getLeftChild(index, indexVal)
            rightChildIndex, rightChildValue = self.getRightChild(index, indexVal)

            if indexVal <= leftChildVal and indexVal <= rightChildValue:
                break

            if leftChildVal < rightChildValue:
                new_index = leftChildIndex
            else:
                new_index = rightChildIndex

            self.heap[new_index], self.heap[index] =\
                self.heap[index], self.heap[new_index]

            index = new_index

    def getParent(self, index):
        if index == 0:
            return None, None

        parentIndex = (index - 1) // 2

        return parentIndex, self.heap[parentIndex]

    def getLeftChild(self, index, defaultValue):
        leftChildIndex = 2 * index + 1

        if leftChildIndex > self.lastIndex:
            return None, defaultValue

        return leftChildIndex, self.heap[leftChildIndex].fCost

    def getRightChild(self, index, defaultValue):
        rightChildIndex = 2 * index + 2

        if rightChildIndex > self.lastIndex:
            return None, defaultValue

        return rightChildIndex, self.heap[rightChildIndex].fCost

    def __len__(self):
        return self.lastIndex + 1

    def getMin(self):
        if len(self) > 0:
            # print len(self)
            a = self.pop()
            fval = a.fCost
            self.push(a)
            return fval
        return None
    

