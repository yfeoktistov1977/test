import random
import typing
from typing import Optional
from typing import List

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class MergeListHelper:
	def makeListFromArray(self, lists : list[int]) -> ListNode:
		head = ListNode(lists[0], None)
		current = head
		for i in lists[1:]:
			current.next = ListNode(i, None)
			current = current.next
		return head


	def PrintKListLinked(self, lists : List[Optional[ListNode]]):
		for i in lists:
			next_item = i
			print("Printing next list >>")
			while True:
				print("val = " + str(next_item.val))
				if next_item.next == None:
					break;
				next_item = next_item.next

	def mergeTwoLists(self, l1 : ListNode, l2 : ListNode) -> ListNode:
		dummy = ListNode(0, None)
		current = dummy

		while l1 and l2:
			if l1.val < l2.val:
				current.next = l1
				l1 = l1.next
			else:
				current.next = l2
				l2 = l2.next
			current = current.next
 
    		# Append the remaining nodes of either list
		current.next = l1 if l1 else l2
		return dummy.next

	def merge_k_lists(self, lists: List[ListNode]) -> ListNode:
		if not lists:
			return None
 
		merged_list = None
 
		for i in range(len(lists)):
			merged_list = self.mergeTwoLists(merged_list, lists[i])
 
		return merged_list


