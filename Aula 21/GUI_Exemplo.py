from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(QtWidgets.QWidget):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(681, 382)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Widget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.in_box = QtWidgets.QTextEdit(Widget)
        self.in_box.setMaximumSize(QtCore.QSize(200, 350))
        self.in_box.setObjectName("in_box")
        self.horizontalLayout.addWidget(self.in_box)
        self.convert = QtWidgets.QPushButton(Widget)
        self.convert.setObjectName("convert")
        self.horizontalLayout.addWidget(self.convert)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.out_box = QtWidgets.QTextEdit(Widget)
        self.out_box.setMaximumSize(QtCore.QSize(200, 350))
        self.out_box.setObjectName("out_box")
        self.gridLayout.addWidget(self.out_box, 6, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Converter"))
        self.convert.setText(_translate("Widget", "Convert"))
        self.convert.clicked.connect(self.convertclick)

    def convertclick(self):
        print('Test')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())