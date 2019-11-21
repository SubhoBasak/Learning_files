# from PyQt5.QtWidgets import QMainWindow, QApplication
# import sys
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle('Subho')
#         self.setGeometry(100, 100, 600, 400)
#         self.show()
#
# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#     win = MainWindow()
#     sys.exit(App.exec())
#
# from PyQt5.QtWidgets import QMainWindow, QApplication
# import sys
#
# class MainWindow:
#     def __init__(self):
#         self.window = QMainWindow()
#         self.window.setWindowTitle('subho')
#         self.window.setGeometry(100, 100, 600, 400)
#         self.window.show()
#
# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(App.exec())
#
# from PyQt5 import QtWidgets, QtGui
# import sys
# import os
#
# class Mainwindow:
#     def __init__(self):
#         self.application = QtWidgets.QApplication(sys.argv)
#
#         self.main_window = QtWidgets.QMainWindow()
#         self.main_window.setWindowTitle('Subho')
#         self.main_window.setWindowIcon(QtGui.QIcon(os.path.join(
#             os.path.dirname(__file__), 'image.png')))
#         self.main_window.setGeometry(100, 200, 700, 450)
#         self.main_window.show()
#
# if __name__ == '__main__':
#     App = Mainwindow()
#     sys.exit(App.application.exec())
#
# from PyQt5 import QtGui, QtWidgets
# import sys
# import os
#
# class MainWidow:
#     def __init__(self):
#         self.Application = QtWidgets.QApplication(sys.argv)
#
#         self.main_window = QtWidgets.QMainWindow()
#         self.main_window.setWindowIcon(QtGui.QIcon(
#             os.path.join(os.path.dirname(__file__), 'image.png')
#         ))
#         self.main_window.setGeometry(100, 100, 600, 400)
#         self.main_window.show()
#
#         self.button = QtWidgets.QPushButton('Click me', self.main_window)
#         self.button.setText('Again click me')
#         self.button.setGeometry(50, 10, 100, 100)
#         self.button.show()
#
# if __name__ == '__main__':
#     App = MainWidow()
#     sys.exit(App.Application.exec())
#
# from PyQt5 import QtGui, QtWidgets, QtCore
# import sys
# import os
#
# class MainWindow:
#     def __init__(self):
#         self.Application = QtWidgets.QApplication(sys.argv)
#
#         self.main_window = QtWidgets.QMainWindow()
#         self.main_window.setGeometry(100, 100, 700, 500)
#         self.main_window.setWindowIcon(QtGui.QIcon(
#             os.path.join(os.path.dirname(__file__), 'image.png')
#         ))
#         self.main_window.show()
#
#         self.button = QtWidgets.QPushButton('Ok', self.main_window)
#         self.button.setGeometry(10, 10, 200, 200)
#         self.button.setIcon(QtGui.QIcon(
#             os.path.join(os.path.dirname(__file__), 'image.png')
#         ))
#         self.button.setIconSize(QtCore.QSize(100, 100))
#         self.button.show()
#
# if __name__ == '__main__':
#     App = MainWindow()
#     sys.exit(App.Application.exec())
