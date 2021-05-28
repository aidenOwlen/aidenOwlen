# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\auto.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(915, 839)
        MainWindow.setStyleSheet(_fromUtf8("background:black;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(470, 70, 361, 671))
        self.table.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:black;\n"
"\n"
""))
        self.table.setAlternatingRowColors(False)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        self.table.verticalHeader().setVisible(False)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 70, 381, 671))
        self.groupBox.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.import_2 = QtGui.QPushButton(self.groupBox)
        self.import_2.setGeometry(QtCore.QRect(250, 620, 121, 28))
        self.import_2.setStyleSheet(_fromUtf8("background:black;"))
        self.import_2.setObjectName(_fromUtf8("import_2"))
        self.Status = QtGui.QLabel(self.groupBox)
        self.Status.setGeometry(QtCore.QRect(20, 50, 141, 16))
        self.Status.setStyleSheet(_fromUtf8("color:white;"))
        self.Status.setObjectName(_fromUtf8("Status"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 171, 22))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.Status_2 = QtGui.QLabel(self.groupBox)
        self.Status_2.setGeometry(QtCore.QRect(20, 90, 141, 16))
        self.Status_2.setStyleSheet(_fromUtf8("color:white;"))
        self.Status_2.setObjectName(_fromUtf8("Status_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 90, 171, 22))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.Status_3 = QtGui.QLabel(self.groupBox)
        self.Status_3.setGeometry(QtCore.QRect(20, 130, 141, 16))
        self.Status_3.setStyleSheet(_fromUtf8("color:white;"))
        self.Status_3.setObjectName(_fromUtf8("Status_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 130, 171, 22))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.Status_4 = QtGui.QLabel(self.groupBox)
        self.Status_4.setGeometry(QtCore.QRect(20, 170, 141, 16))
        self.Status_4.setStyleSheet(_fromUtf8("color:white;"))
        self.Status_4.setObjectName(_fromUtf8("Status_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 170, 171, 22))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.Status_5 = QtGui.QLabel(self.groupBox)
        self.Status_5.setGeometry(QtCore.QRect(20, 210, 141, 16))
        self.Status_5.setStyleSheet(_fromUtf8("color:white;"))
        self.Status_5.setObjectName(_fromUtf8("Status_5"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 210, 171, 22))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.Status_6 = QtGui.QLabel(self.groupBox)
        self.Status_6.setGeometry(QtCore.QRect(20, 250, 141, 16))
        self.Status_6.setStyleSheet(_fromUtf8("color:white;"))
        self.Status_6.setObjectName(_fromUtf8("Status_6"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 250, 171, 22))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 290, 171, 22))
        self.lineEdit_7.setText(_fromUtf8(""))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.Status_7 = QtGui.QLabel(self.groupBox)
        self.Status_7.setGeometry(QtCore.QRect(20, 290, 141, 16))
        self.Status_7.setStyleSheet(_fromUtf8("color:white;"))
        self.Status_7.setObjectName(_fromUtf8("Status_7"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 330, 331, 251))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.textEdit = QtGui.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 301, 201))
        self.textEdit.setStyleSheet(_fromUtf8("color:black;"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, -10, 351, 71))
        self.label.setStyleSheet(_fromUtf8("background:transparent;\n"
"color:rgb(152, 0, 0);\n"
"font: 75 15pt  \"Unispace\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 750, 661, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.export_2 = QtGui.QPushButton(self.centralwidget)
        self.export_2.setGeometry(QtCore.QRect(690, 750, 141, 28))
        self.export_2.setStyleSheet(_fromUtf8("font: 75 9pt  \"Unispace\";\n"
"color:white;\n"
"background:rgb(152, 0, 0);"))
        self.export_2.setObjectName(_fromUtf8("export_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Assignment", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Candidates", None))
        self.groupBox.setTitle(_translate("MainWindow", "Option worth", None))
        self.import_2.setText(_translate("MainWindow", "Import excel", None))
        self.Status.setText(_translate("MainWindow", "Business Role 1", None))
        self.Status_2.setText(_translate("MainWindow", "Business Role 2", None))
        self.Status_3.setText(_translate("MainWindow", "Business Role 3", None))
        self.Status_4.setText(_translate("MainWindow", "Pref location 1", None))
        self.Status_5.setText(_translate("MainWindow", "Pref location 2", None))
        self.Status_6.setText(_translate("MainWindow", "Pref location 3", None))
        self.Status_7.setText(_translate("MainWindow", "Per skill match", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Âlgorithm", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Unispace\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1) First if driver license is required, candidates who has no driver license are not matched in any way.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2) Second we look at Major match </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3) Then we compare points ( +1 per skill match, + 0.5 for pref location 1, less for pref 2, even less for pref 3) </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4) If there is no major match skill match we look at business roles and preferred business area and skill match ( business roles are worth more than skill match )</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5) If there is no major match and no skill match we look at business roles and business preferred area . </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For now it matches 100 for 100, if you have a situation where nothing matches how should is it supposed to handle that ? </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Those options above are not working yet, I don\'t know if you would need them, if you see that my points algorithm need some modification or need to be flexible then I may activate those options above so that you could give each option the right worth points.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Automation challenge", None))
        self.export_2.setText(_translate("MainWindow", "Export excel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

