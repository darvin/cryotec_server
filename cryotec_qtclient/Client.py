# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtCore, QtGui  # подключает основные модули PyQt
import mainform  # подключает модуль описания формы
 
 
def main():
    app = QtGui.QApplication(sys.argv)  # создаёт основной объект программы
    form = mainform.MainForm()  # создаёт объект формы
    form.show()  # даёт команду на отображение объекта формы и содержимого
    app.exec_()  # запускает приложение
 
 
if __name__ == "__main__":
    sys.exit(main())