import sys
import os
import re
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtQml import *
from PySide6 import *
from PySide6.QtCore import QObject, Slot, Property, Signal
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFileDialog

class SourceDestinationButton(QObject):
	button_text_changed = Signal()

	def __init__(self):
		super().__init__()
		self._button_text = "Generate: "

	def txt_convert(self):
		inputfile = self.file_path_src
		outputfile = self.file_path_dst

		# check input file
		try:
			fi = open(inputfile, "r")
		except IOError as e:
			print(e)
			sys.exit(e.errno)
		# check output file
		try:
			fo = open(outputfile, "w")
		except IOError as e:
			print(e)
			fi.close()
			sys.exit(e.errno)
		# convert + write to output file
		for line in fi:
			m = re.match(r'.*Запись регистра №(\d+) чипа №\d+ ячейки №\d+: значение = \dx([0-9, A-F]+) \((\d+) байт.*\)', line, re.IGNORECASE)
			if m:
				addr = m.group(1)
				value = m.group(2).lower()
				reg_width = int(m.group(3))*8
				fo.write("core_write" + str(reg_width) + "(core, " + addr + ", 0x" + value + ");\n")
			else:
				m = re.match(r'.*Чтение регистра №(\d+) чипа №\d+ ячейки №\d+: значение = \dx([0-9, A-F]+) \((\d+) байт.*\)', line, re.IGNORECASE)
				if m:
					addr = m.group(1)
					value = m.group(2).lower()
					reg_width = int(m.group(3))*8
					fo.write("core_read" + str(reg_width) + "(core, " + addr + ");\n")
				else:
					fo.write(line)

		fo.close()
		fi.close()			


	@Slot()
	def on_source_button_clicked(self):
		print("Src Button clicked from QML!")
		current_dir = os.getcwd()
		self.file_path_src, _ = QFileDialog.getOpenFileName(None, "Select a File", current_dir, "All Files (*.*)")
		self.file_path_dst = self.file_path_src + "_out"
		print(f"SourceFile = {self.file_path_src}")
		print(f"DestinationFile = {self.file_path_dst}")
		self._button_text = "Generate : " + self.file_path_dst
		self.button_text_changed.emit()
		self.txt_convert();

	@Property(str, notify=button_text_changed)
	def button_generate_text(self):
		return self._button_text	
	@button_generate_text.setter
	def button_generate_text(self, value):
		self._button_text = value	

	@Slot()
	def on_generate_button_clicked(self):
		print("Destination button clicked from QML!")

if __name__ == "__main__":
	CaptureButton = SourceDestinationButton()

	# Create the application
	app = QApplication(sys.argv)
	engine = QQmlApplicationEngine()
	engine.rootContext().setContextProperty("Property_CaptureButton", CaptureButton)

	engine.load("main.qml")  # Replace with your QML file
	sys.exit(app.exec())



