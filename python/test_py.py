import random
import test_windows
import test_py_clib
import test_py_if_for
import os
import sys

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


#test_py_clib.use_clib()
#display("234234234");
#print("Global variable(place2) = ",  gvalue)
#test_windows.show_window_class()

ask_yes_no()

#if test_py_if_for.test_if() !=0:
#       sys.exit(0)
#else:
#	print("Access granted !");

#test_py_if_for.test_loops()
