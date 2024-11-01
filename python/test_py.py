import random
import test_windows
import test_py_clib
import test_py_if_for
import test_merge_k_list
import test_func
import os
import sys
from test_merge_k_list import MergeListHelper
from test_merge_k_list import ListNode

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

test_list = [[1,3], [5,7], [2,6]]
testMergeClass = MergeListHelper()
testMergeClass.MergeKList(test_list)

A2 = ListNode(3, None)
A1 = ListNode(1, A2)
B2 = ListNode(7, None)
B1 = ListNode(5, B2)
C2 = ListNode(6, None)
C1 = ListNode(2, C2)

Main_list = [A1, B1, C1]
testMergeClass.MergeKListLinked(Main_list)

print(f" End of program !")