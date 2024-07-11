import sys
from ui import View
from ctrl import Control
from PyQt5.Qtwidgets import QApplication

def main():
	cale = QApplication(sys.argv)
	app = QApplication(sys.argv)
	view = View()
	Control(view=view)
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()