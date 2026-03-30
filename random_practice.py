class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    @staticmethod
    def mergeTwoLists(list1, list2):
        output = None
        tail = None
        prev = None
        while list1 and list2:
            if list1.val >= list2.val:
                if not tail:
                    output = tail = list2
                    list2 = list2.next
                    tail.next = list1
                    list1 = list1.next
                    prev = tail
                    tail = tail.next
                    continue
                elif tail.val > list1.val:
                    prev.next = list1
                    tail.next = list1.next
                    list1.next = tail
                    prev = tail
                    tail = tail.next
                else:
                    tail.next = list2
                    prev = tail
                    tail = tail.next
                    list2 = list2.next
                    tail.next = list1
                    list1 = list1.next
                    continue

            else:
                if not tail:
                    output = tail = list1
                    list1 = list1.next
                    tail.next = list2
                    list2 = list2.next
                    prev = tail
                    tail = tail.next
                    continue
                elif tail.val > list2.val:
                    prev.next = list2
                    tail.next = list2.next
                    list2.next = tail
                    prev = tail
                    tail = tail.next
                else:
                    tail.next = list1
                    prev = tail
                    tail = tail.next
                    list1 = list1.next
                    tail.next = list1
                    list2 = list2.next
                    continue
            list2 = list2.next
            list1 = list1.next
        print(output)
listt1 = ListNode(1)
listt1.next = ListNode(2)
listt1.next.next = ListNode(4)
listt2 = ListNode(1)
listt2.next = ListNode(3)
listt2.next.next = ListNode(4)
Solution.mergeTwoLists(listt1, listt2)