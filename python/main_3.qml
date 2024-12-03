import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Find QML Button from Python"

    Button {
        id: myButton1
        objectName: "buttonOne"
        text: "Click Me"

        // Define a function in QML
        function greet() {
            console.log("Hello, " +  "!")
        }

        function greet2(name, age) {
            console.log("Hello :" + "name" + " Age = " + age )
        }

    }
}
