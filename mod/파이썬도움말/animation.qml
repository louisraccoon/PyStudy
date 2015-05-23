/****************************************************************************
**
** Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
** Contact: http://www.qt-project.org/legal
**
** This file is part of the examples of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:BSD$
** You may use this file under the terms of the BSD license as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
**     of its contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick 2.0
import "./" as Examples
//as는 Examples라는 이름으로 대체한다는 뜻

Item {
    height: 480
    width: 320
    LauncherList {
        id: l8
        anchors.fill: parent
        Component.onCompleted: {
            addExample("자료형", "",  Qt.resolvedUrl("text.qml"));
            addExample("문자열", "", Qt.resolvedUrl("text1.qml"));
            addExample("조건문", "", Qt.resolvedUrl("text2.qml"));
            addExample("반복문", "", Qt.resolvedUrl("text3.qml"));
            addExample("함수", "", Qt.resolvedUrl("text4.qml"));
            addExample("클래스", "", Qt.resolvedUrl("text5.qml"));
            addExample("생성자/소멸자", "", Qt.resolvedUrl("text6.qml"));
            addExample("상속", "", Qt.resolvedUrl("text7.qml"));
            addExample("오버로딩", "", Qt.resolvedUrl("text8.qml"));
            addExample("모듈", "", Qt.resolvedUrl("text9.qml"));
            addExample("입출력", "", Qt.resolvedUrl("text10.qml"));
            addExample("예외처리", "", Qt.resolvedUrl("text11.qml"));
        }
    }
}
