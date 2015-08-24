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
 text: " 조건문\n
 조건문은 조건식을 주어서 조건식을 만족할때에만 \n
 조건식안에 있는 내용을 읽는다.\n\n
 조건식은 if(조건식): 으로 표현하며 조건식\n
 =,==,!=,>,<,>=,<= 을 사용한다.\n\n
 if문은 조건식이 참일때만 수행되어 있다면\n
 거짓일때만 수행하게 할수 있다.\n
 if조건식 아래에 else: 를 이용하여\n
 else 에는 if식이 거짓일경우 else문에 \n
 있는 내용을 읽는다.\n\n
 elif(조건식): 은 if문이 거짓일경우 다른\n
 조건식을 주는방법으로 여러개의 esif를 \n
 사용하여 다양한 조건식들로 나눌수 있다.\n

 예)
 money=1000\n
 if money >= 500; \n
    print(\"돈이 500원 이상 있습니다.\")
 "
 }
}
