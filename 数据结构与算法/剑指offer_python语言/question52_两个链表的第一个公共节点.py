class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def solution(head1:Node, head2:Node):
    length1 = get_list_length(head1)
    length2 = get_list_length(head2)

    if length1>length2:
        node1 = head1
        node2 = head2
        diff = length1-length2
    else:
        node1 = head1
        node2 = head2
        diff = length2 - length1
    while diff>0:
        node1 = node1.next
        diff -= 1
    while node1.val != node2.val and node1 is not None and node2 is not None:
        node1 = node1.next
        node2 = node2.next

    return node1


def get_list_length(head:Node):
    length = 0
    node = head
    while node is not None:
        length += 1
        node = node.next
    return length
