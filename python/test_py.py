import random
import test_windows
import test_py_clib
import test_py_if_for
import test_merge_k_list
import test_func
import os
import sys
#from test_merge_k_list import MergeListHelper
#from test_merge_k_list import ListNode
from test_merge_k_list import *

gvalue = 125

############### just functions #################################
def display(message, voice = "1234"):
        #global gvalue
        gvalue = 32
        print(message + " " + voice)
        print("Global variable(place1) = ",  gvalue)
        return 9

def ask_yes_no(question = "Do you want ? (y/n)"):
        response = None
        while response not in ("y", "n"):
                response = input(question).lower()
        return response

#program -------------------------
if __name__ == "__main__":
	data_array = [8, 3, 10, 14, 1]
	data_array1 = list(data_array)
	data_array1[0] = 155

	data_dict = { 1 : 1, 2 : 333}


	#data_array1 = [[4,5,6], [1,3], [4,5] , [1,1], [1,3]]

	#test_py_clib.use_clib()
	#display("234234234");
	#print("Global variable(place2) = ",  gvalue)
	#test_windows.show_window_class()

	#ask_yes_no()

	#if test_py_if_for.test_if() !=0:
	#       sys.exit(0)
	#else:
	#	print("Access granted !");

	#test_py_if_for.test_loops()

	#test_func.array_buble_sort(data_array)
	#print(data_array)

	#test_func.param_test_func("888")

	#------- start>> merge k linked lists sorted by accend
	test_list = [[1,3], [5,7], [2,6]]
	testMergeClass = MergeListHelper()
	Main_list = [testMergeClass.makeListFromArray(test_list[0]),
              	testMergeClass.makeListFromArray(test_list[1]),
                testMergeClass.makeListFromArray(test_list[2])]
	print(f"(2)------------------")
	Merged_List = testMergeClass.merge_k_lists(Main_list)
	next_item = Merged_List
	while True:
		print(f"Next.item {next_item.val}");
		next_item = next_item.next
		if not next_item.next:
			break
	#------- end merge k linked lists sorted by accend

	print(f" End of program !")