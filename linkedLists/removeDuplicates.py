"""
Given a sorted linkedList remove duplicates from it.

1 -> 2 -> 2 -> 2 -> 3
1 -> 2 -> 2

"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode:
        nextNode = currentNode.next
        while nextNode and nextNode.value == currentNode.value:
            nextNode = nextNode.next
        currentNode.next = nextNode
        currentNode = currentNode.next
    return linkedList


def arrayToList(arr):
    start = None
    node = None
    for i in arr:
        if start == None:
            start = LinkedList(i)
            node = start
        else:
            s = LinkedList(i)
            node.next = s
            node = node.next
    return start


def listToArray(linkedList):
    arr = []
    while linkedList:
        arr.append(linkedList.value)
        linkedList = linkedList.next
    return arr


def test():
    linkedList = arrayToList([1,2,2,3])
    freeFromDups = removeDuplicatesFromLinkedList(linkedList)
    assert(listToArray(freeFromDups) == [1,2,3])

    linkedList = arrayToList([1,2,2])
    freeFromDups = removeDuplicatesFromLinkedList(linkedList)
    assert(listToArray(freeFromDups) == [1,2])
    
    linkedList = arrayToList([1,2])
    freeFromDups = removeDuplicatesFromLinkedList(linkedList)
    assert(listToArray(freeFromDups) == [1,2])
    
    linkedList = arrayToList([1])
    freeFromDups = removeDuplicatesFromLinkedList(linkedList)
    assert(listToArray(freeFromDups) == [1])

test()
