def rev(head):
    p = None
    while head:
        nxt = head.next
        head.next = p
        p = head
        head = nxt
    return p