import sys

from design_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui

from sqlquery import SqlQuery


class lis_todo(QMainWindow):
	def __init__(self):
		super(lis_todo, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
		sql_query.db_disconnect()

	def showEvent(self, a0: QtGui.QShowEvent) -> None:
		sql_query.db_connect()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = lis_todo()

	sql_query = SqlQuery()


	window.show()
	sys.exit(app.exec())



