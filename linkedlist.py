class ListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList: 
    """
    Technically a doubly linked list
    """

    def __init__(self) -> None:
        self.start = None
        self.end = None

    def addFirst(self, value):
        temp = self.start
        self.start = ListNode(value)
        self.start.next = temp

        if self.end is None:
            self.end = self.start
    
    def addLast(self, value):
        temp = self.end
        self.end = ListNode(value)

        if temp is not None:
            temp.next = self.end

        if self.start is None:
            self.start = self.end

    def findValue(self, value):
        """
        Returns the first ListNode that contains the specified value.
        Returns None if no such node exists.
        """

        curr = self.start
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next

        return None

    def removeValue(self, value):
        """
        Removes the first ListNode that contains the specified value.
        """
        prev = None
        curr = self.start
        while curr is not None:
            if curr.value == value:
                if curr == self.start:
                    self.start = curr.next
                if curr == self.end:
                    self.end = prev
                if prev is not None:
                    prev.next = curr.next

                return curr


            prev = curr
            curr = curr.next
        return None


    def removeFirst():
        temp = self.start

        if self.start:
            self.start = self.start.next

        if temp == self.end:
            self.end = None

        return temp

    def removeLast():
        prev = None
        curr = self.start
        while curr is not None and curr.next is not None:
            prev = curr
            curr = curr.next

        self.end = prev
        if prev is not None:
            prev.next = None
        if curr == self.start:
            self.start = None


        return curr
