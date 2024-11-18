import sys
import os
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



