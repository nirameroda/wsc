QT += core
QT -= gui
QT += widgets

TARGET = nodeImportanceLPA
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG += qt

TEMPLATE = app

SOURCES += main.cpp \
    network.cpp \
    src\node.cpp

HEADERS += \
    src\network.h \
    node.h

QMAKE += core
