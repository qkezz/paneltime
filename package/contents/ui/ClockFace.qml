// SPDX-License-Identifier: GPL-2.0-or-later
import QtQuick

Item {
    id: face
    property string timeText: ""
    property string dateText: ""
    property string widthSample: timeText
    property color textColor: "white"
    property string fontFamily: "Noto Sans"
    property int preferredPixelSize: 15
    property int fontWeight: Font.Normal
    property bool italic: false
    readonly property int pixelSize: preferredPixelSize
    readonly property int lineHeight: Math.ceil(pixelSize * 1.10)
    implicitWidth: Math.ceil(Math.max(timeMetrics.advanceWidth, dateMetrics.advanceWidth)) + 20
    implicitHeight: dateText.length ? lineHeight * 2 : lineHeight

    TextMetrics { id: timeMetrics; font: timeLine.font; text: face.widthSample }
    TextMetrics { id: inkTimeMetrics; font: timeLine.font; text: face.timeText.trim() }
    TextMetrics { id: dateMetrics; font: timeLine.font; text: face.dateText }

    Column {
        anchors.right: parent.right
        anchors.rightMargin: 10
        anchors.verticalCenter: parent.verticalCenter
        spacing: 0
        width: parent.width - 20
        Text {
            id: timeLine
            width: inkTimeMetrics.advanceWidth
            anchors.right: parent.right
            anchors.rightMargin: (inkTimeMetrics.tightBoundingRect.x + inkTimeMetrics.tightBoundingRect.width) - inkTimeMetrics.advanceWidth
            height: face.lineHeight
            text: face.timeText.trim()
            color: face.textColor
            font.family: face.fontFamily
            font.pixelSize: face.pixelSize
            font.weight: face.fontWeight
            font.italic: face.italic
            font.features: ({ "tnum": 1 })
            horizontalAlignment: Text.AlignRight
            verticalAlignment: Text.AlignVCenter
            renderType: Text.NativeRendering
        }
        Text {
            width: dateMetrics.advanceWidth
            anchors.right: parent.right
            anchors.rightMargin: (dateMetrics.tightBoundingRect.x + dateMetrics.tightBoundingRect.width) - dateMetrics.advanceWidth
            height: face.lineHeight
            visible: face.dateText.length > 0
            text: face.dateText.trim()
            color: face.textColor
            font: timeLine.font
            horizontalAlignment: Text.AlignRight
            verticalAlignment: Text.AlignVCenter
            renderType: Text.NativeRendering
        }
    }
}
