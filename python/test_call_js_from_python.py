import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject
from PySide6.QtCore import QMetaObject
from PySide6.QtCore import Qt, Q_ARG


def print_children(obj, depth=0):
    """Recursively print the object tree with indentation."""
    if obj is None:
        return

    # Print the current object
    print("  " * depth + f"{obj.metaObject().className()} (id: {obj.objectName()})")

    # Recursively print children
    for child in obj.children():
        print_children(child, depth + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load the QML file
    engine = QQmlApplicationEngine()
    engine.load("main_3.qml")

    # Check if the QML file loaded successfully
    if not engine.rootObjects():
        sys.exit(-1)

    # Get the root object of the QML file
    root_object = engine.rootObjects()[0]
    #root_objects = engine.rootObjects()

    #for root in root_objects:
     #   print("Root Object:")
      #  print_children(root)

    #print (root_object.children())

    # Find the Button object by its ID
    my_button = root_object.findChild(QObject, "buttonOne")

    if my_button:
        print("Button object found!")
        # Call the 'greet' function defined in QML
        QMetaObject.invokeMethod(my_button, "greet")
        QMetaObject.invokeMethod(my_button, "greet2", Qt.DirectConnection,  Q_ARG("QVariant", "Yura"), Q_ARG("QVariant", 99))
    else:
        print("Button object not found!")

    sys.exit(app.exec())
