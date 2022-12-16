# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 387)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mian_res/resource/icons/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget{\n"
"    color: white;\n"
"    background: qlineargradient( x1:0.5 y1:0, x2:0.5 y1:1, stop:0 #db8504, stop:1 black);\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QLabel{\n"
"    background: transparent;\n"
"    border: None;\n"
"}\n"
"\n"
"QListWidget{\n"
"    color: black;\n"
"    background: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: black;\n"
"    background: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: black;\n"
"    background: white;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.btn_refresh_category_list = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_refresh_category_list.sizePolicy().hasHeightForWidth())
        self.btn_refresh_category_list.setSizePolicy(sizePolicy)
        self.btn_refresh_category_list.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_refresh_category_list.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_refresh_category_list.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mian_res/resource/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_refresh_category_list.setIcon(icon1)
        self.btn_refresh_category_list.setIconSize(QtCore.QSize(16, 16))
        self.btn_refresh_category_list.setFlat(False)
        self.btn_refresh_category_list.setObjectName("btn_refresh_category_list")
        self.horizontalLayout_4.addWidget(self.btn_refresh_category_list)
        self.btn_add_category = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_category.sizePolicy().hasHeightForWidth())
        self.btn_add_category.setSizePolicy(sizePolicy)
        self.btn_add_category.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_add_category.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_category.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mian_res/resource/icons/tab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_category.setIcon(icon2)
        self.btn_add_category.setFlat(False)
        self.btn_add_category.setObjectName("btn_add_category")
        self.horizontalLayout_4.addWidget(self.btn_add_category)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.lis_wid_category = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lis_wid_category.sizePolicy().hasHeightForWidth())
        self.lis_wid_category.setSizePolicy(sizePolicy)
        self.lis_wid_category.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lis_wid_category.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lis_wid_category.setObjectName("lis_wid_category")
        self.verticalLayout.addWidget(self.lis_wid_category)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.btn_refresh_task_list = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_refresh_task_list.sizePolicy().hasHeightForWidth())
        self.btn_refresh_task_list.setSizePolicy(sizePolicy)
        self.btn_refresh_task_list.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_refresh_task_list.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_refresh_task_list.setText("")
        self.btn_refresh_task_list.setIcon(icon1)
        self.btn_refresh_task_list.setIconSize(QtCore.QSize(16, 16))
        self.btn_refresh_task_list.setFlat(False)
        self.btn_refresh_task_list.setObjectName("btn_refresh_task_list")
        self.horizontalLayout_5.addWidget(self.btn_refresh_task_list)
        self.btn_add_task = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_task.sizePolicy().hasHeightForWidth())
        self.btn_add_task.setSizePolicy(sizePolicy)
        self.btn_add_task.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_add_task.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_task.setText("")
        self.btn_add_task.setIcon(icon2)
        self.btn_add_task.setFlat(False)
        self.btn_add_task.setObjectName("btn_add_task")
        self.horizontalLayout_5.addWidget(self.btn_add_task)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.lis_wid_task = QtWidgets.QListWidget(self.centralwidget)
        self.lis_wid_task.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lis_wid_task.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lis_wid_task.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lis_wid_task.setObjectName("lis_wid_task")
        self.verticalLayout_2.addWidget(self.lis_wid_task)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.led_name_task = QtWidgets.QLineEdit(self.centralwidget)
        self.led_name_task.setText("")
        self.led_name_task.setFrame(False)
        self.led_name_task.setObjectName("led_name_task")
        self.horizontalLayout.addWidget(self.led_name_task)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.ted_description_task = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ted_description_task.setFont(font)
        self.ted_description_task.setStyleSheet("font-size: 10pt;\n"
"fornt-weight: 600;\n"
"background: white;\n"
"color: black;")
        self.ted_description_task.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ted_description_task.setObjectName("ted_description_task")
        self.verticalLayout_4.addWidget(self.ted_description_task)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setMinimumSize(QtCore.QSize(105, 0))
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setDefault(False)
        self.btn_cancel.setFlat(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 0, 5, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(105, 0))
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setAutoDefault(False)
        self.btn_save.setDefault(False)
        self.btn_save.setFlat(False)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 0, 4, 1, 1)
        self.btn_complete_task = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_complete_task.sizePolicy().hasHeightForWidth())
        self.btn_complete_task.setSizePolicy(sizePolicy)
        self.btn_complete_task.setMinimumSize(QtCore.QSize(105, 0))
        self.btn_complete_task.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_complete_task.setAutoDefault(False)
        self.btn_complete_task.setDefault(False)
        self.btn_complete_task.setFlat(False)
        self.btn_complete_task.setObjectName("btn_complete_task")
        self.gridLayout.addWidget(self.btn_complete_task, 0, 3, 1, 1)
        self.btn_del_task = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del_task.sizePolicy().hasHeightForWidth())
        self.btn_del_task.setSizePolicy(sizePolicy)
        self.btn_del_task.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_del_task.setObjectName("btn_del_task")
        self.gridLayout.addWidget(self.btn_del_task, 0, 2, 1, 1)
        self.btn_edit_task = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_edit_task.sizePolicy().hasHeightForWidth())
        self.btn_edit_task.setSizePolicy(sizePolicy)
        self.btn_edit_task.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_edit_task.setObjectName("btn_edit_task")
        self.gridLayout.addWidget(self.btn_edit_task, 0, 1, 1, 1)
        self.btn_save_edit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_edit.sizePolicy().hasHeightForWidth())
        self.btn_save_edit.setSizePolicy(sizePolicy)
        self.btn_save_edit.setMinimumSize(QtCore.QSize(105, 0))
        self.btn_save_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_edit.setAutoDefault(False)
        self.btn_save_edit.setDefault(False)
        self.btn_save_edit.setFlat(False)
        self.btn_save_edit.setObjectName("btn_save_edit")
        self.gridLayout.addWidget(self.btn_save_edit, 0, 6, 1, 1)
        self.btn_cancel_edit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel_edit.sizePolicy().hasHeightForWidth())
        self.btn_cancel_edit.setSizePolicy(sizePolicy)
        self.btn_cancel_edit.setMinimumSize(QtCore.QSize(105, 0))
        self.btn_cancel_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel_edit.setAutoDefault(False)
        self.btn_cancel_edit.setDefault(False)
        self.btn_cancel_edit.setFlat(False)
        self.btn_cancel_edit.setObjectName("btn_cancel_edit")
        self.gridLayout.addWidget(self.btn_cancel_edit, 0, 7, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Категории:"))
        self.label_2.setText(_translate("MainWindow", "Список задач:"))
        self.label_3.setText(_translate("MainWindow", "Название задачи:"))
        self.label_4.setText(_translate("MainWindow", "Описание задачи:"))
        self.ted_description_task.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.btn_cancel.setText(_translate("MainWindow", "Отмена"))
        self.btn_save.setText(_translate("MainWindow", "Сохранить"))
        self.btn_complete_task.setText(_translate("MainWindow", "Выполнено"))
        self.btn_del_task.setText(_translate("MainWindow", "Удалить задачу"))
        self.btn_edit_task.setText(_translate("MainWindow", "Изменить задачу"))
        self.btn_save_edit.setText(_translate("MainWindow", "Сохранить"))
        self.btn_cancel_edit.setText(_translate("MainWindow", "Отмена"))
import file_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
