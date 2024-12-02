import sys
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

class Backend(QObject):
    @Slot(str, result=str)
    def greet(self, name):
        """A Python function callable from QML."""
        return f"Hello, {name} from Python!"

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the backend object
    backend = Backend()

    # Set up the QML engine
    engine = QQmlApplicationEngine()

    # Expose the backend object to QML
    engine.rootContext().setContextProperty("backend",  backend)

    # Load the QML file
    engine.load("main_2.qml")

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

