import random
import test_windows
import test_py_clib
import test_py_if_for
import test_merge_k_list
import test_func
import os
import sys

import kivy
from kivy import *
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Rectangle
from kivy.uix.button import Label

class MyWidget(Widget):
	pass

class MainLayoutApp(App):
	def build(self):
		return Label()

if __name__ == "__main__":
	print(f"Starting program")
	myApp = MainLayoutApp()
	myApp.run()