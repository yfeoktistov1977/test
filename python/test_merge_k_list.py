import random
import typing
from typing import Optional
from typing import List

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class MergeListHelper:
	def MergeKList(self, lists : List[List]) -> List:
		for i in lists:
			for j in i:
				print(f"j item= {j}")

	def MergeKListLinked(self, lists : list[Optional[ListNode]]) -> ListNode:
		for i in lists:
			j = i
			while True:
				print("item =" + str(j.val))
				j=j.next
				if j.next == None:
					print("item =" + str(j.val))
					break;
