import random
import typing
from typing import Optional
from typing import List

def array_buble_sort(array):
	for i in range(0, len(array)):
		for j in range(0, len(array) - i - 1):
			print(" i = " + str(i) + " j = " + str(j))
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]


	return 0

def param_test_func(mylist : Optional[str]):
	print(" param_test_func test mylist=" + mylist);
	age: Optional[int] = None  # age может быть числом или None
	age2: int | None  # age может быть числом или None
	age2 = None
	if age2 is None:
		print("Age 2 is NONE");

	age = 25
	age = "yy25"
	print(f"mylist={mylist} Age=" + age)
