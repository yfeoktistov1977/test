import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 600
    height: 125
    title: "Generate core_writeXX apps"


    Column {
        spacing: 10
        anchors.centerIn: parent

        Button {
		text: "Source file"
		onClicked: Property_CaptureButton.on_source_button_clicked()
	}

        Button {
		text: Property_CaptureButton.button_generate_text
		onClicked: Property_CaptureButton.on_generate_button_clicked()
	}

    }

}
