import random
import ctypes


def use_clib():
	mylib = ctypes.CDLL('./mylib.so')
	# Function 1
	# Define the argument types and return type of the C function
	mylib.add.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_char_p)
	mylib.add.restype = ctypes.c_int
	ip="10.2.130.129"
	# Call the C function
	result = mylib.add(3, 5, ip.encode('utf-8'))
	print(f"The result is: {result}")

	#function 2
	class Data(ctypes.Structure):
		_fields_ = [("id", ctypes.c_int),
			("value", ctypes.c_double),
			("name", ctypes.c_char * 50)]

	mylib.print_data.argtypes = [ctypes.POINTER(Data)]
	mylib.print_data.restype = None
	data = Data(id=1, value=123.45, name=b"Example")
	mylib.print_data(ctypes.byref(data))

