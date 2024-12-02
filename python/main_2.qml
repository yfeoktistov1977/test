import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Call Python from QML"

    Column {
        spacing: 10
        anchors.centerIn: parent

        TextField {
            id: inputField
            placeholderText: "Enter your name"
        }

        Button {
            text: "Greet"
            onClicked: {
                // Call Python function and display the result
                const greeting = backend.greet(inputField.text);
                resultText.text = greeting;
            }
        }

        Text {
            id: resultText
            text: ""
        }
    }
}
