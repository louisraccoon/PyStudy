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

import QtQuick 2.0
import QtQuick.Particles 2.0

Rectangle {
 width: 200
 height: 200
 color: "white"
 
Text {
 text: " 자료형\n
 자료형에는 수치,문자,리스트,튜플,사전,불 등 다양한\n
 자료형이 있다.\n\n
 수치 : int, long, float, compex 등이 있다.\n
 int앞에 0o을 붙이면 8진수, 0b를 붙이면 2진수,\n
 0x를 붙이면 16진수로 인식하게 된다.\n\n
 문자 : 문자는 큰따음표와 작은따음표로 표현한다.\n\n
 리스트 : []를 이용하여 변수들을 한번에 저장할수 있다.\n
 또한 리스트안에 리스트를 쓸수도 있다.\n\n
 튜플 : ()를 사용하며, 리스트와 매우 비슷하다.\n
 단 튜플은 한번 넣은 값을 변경할수 없다.\n\n
 사전 : 사전은 키를 통해 값을 덛는 자료 구조를 가진다.\n
 {}를 이용하며 키:값을 입력하여 키만으로 값을 찾는다.\n\n
 부울 : 부울은 참,거짓을 나타내는데 사용된다.\n
 그렇기 때문에 논리연산, 비교연산등에 사용된다.
 "
 }
}
