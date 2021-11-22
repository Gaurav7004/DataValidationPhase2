# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets

# class CustomWidget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(CustomWidget, self).__init__(parent)
#         self.button = QtWidgets.QPushButton("button")
#         lay = QtWidgets.QHBoxLayout(self)
#         lay.addWidget(self.button, alignment=QtCore.Qt.AlignRight)
#         lay.setContentsMargins(0, 0, 0, 0)

# class Dialog(QtWidgets.QDialog):
#     def __init__(self, parent=None):
#         super(Dialog, self).__init__(parent=parent)
#         vLayout = QtWidgets.QVBoxLayout(self)
#         hLayout = QtWidgets.QHBoxLayout()
#         self.lineEdit = QtWidgets.QLineEdit()
#         hLayout.addWidget(self.lineEdit)
#         self.filter = QtWidgets.QPushButton("filter", self)
#         hLayout.addWidget(self.filter)
#         self.list = QtWidgets.QListView(self)
#         vLayout.addLayout(hLayout)
#         vLayout.addWidget(self.list)
#         self.model = QtGui.QStandardItemModel(self.list)
#         codes = [
#             'windows',
#             'windows xp',
#             'windows7',
#             'hai',
#             'habit',
#             'hack',
#             'good',
#             'windows',
#             'windows xp',
#             'windows7',
#             'hai',
#             'habit',
#             'hack',
#             'good'
#         ]
#         self.list.setModel(self.model)
#         for code in codes:
#             item = QtGui.QStandardItem(code)
#             self.model.appendRow(item)
#             self.list.setIndexWidget(item.index(), CustomWidget())

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     w = Dialog()
#     w.show()
#     sys.exit(app.exec_())


##########################################################
##########################################################


# import sys 
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QDialog 
# from PyQt5 import QtWidgets, QtGui
# # set up app and GUI  

# app = QApplication(sys.argv) 
  
# mainWindow = QMainWindow() 
# mainWindow.resize(400,200) 
# mainWindow.setWindowTitle("PyQt5 example 3") 
# mainWindow.setCentralWidget(QWidget()) 

# layout = QGridLayout(mainWindow.centralWidget()) 

# button = QPushButton("Open dialog ...") 
# layout.addWidget(button,0,0) 
  
# dialogBox = QDialog() 
# dialogBox.setWindowTitle("The world's weirdest dialog box") 

# lay = QtWidgets.QVBoxLayout(dialogBox)

# listView = QtWidgets.QListWidget()
# label    = QtWidgets.QLabel("Please Select item in the QListView")
# lay.addWidget(listView)
# lay.addWidget(label)

# listView.addItems(['ghh', 'hjjk','ghh', 'hjjk','ghh', 'hjjk','ghh', 'hjjk','ghh', 'hjjk','ghh', 'hjjk'])


# button.clicked.connect(dialogBox.exec_) # invoke dialog modal version 


 
# mainWindow.show() 

# sys.exit(app.exec_()) 


###################################################################################################################3
####################################################################################################################

import sys
from PyQt5 import Qt, QtCore, QtGui, QtWidgets


class ChecklistDialog(QtWidgets.QDialog):

    def __init__(
        self,
        name,
        stringlist=None,
        checked=False,
        icon=None,
        parent=None,
        ):
        super(ChecklistDialog, self).__init__(parent)

        self.name = name
        self.icon = icon
        self.model = QtGui.QStandardItemModel()
        self.listView = QtWidgets.QListView()

        for string in stringlist:
            item = QtGui.QStandardItem(string)
            item.setCheckable(True)
            check = \
                (QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked)
            item.setCheckState(check)
            self.model.appendRow(item)

        self.listView.setModel(self.model)

        self.okButton = QtWidgets.QPushButton('OK')
        self.cancelButton = QtWidgets.QPushButton('Cancel')
        self.selectButton = QtWidgets.QPushButton('Select All')
        self.unselectButton = QtWidgets.QPushButton('Unselect All')

        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)
        hbox.addWidget(self.selectButton)
        hbox.addWidget(self.unselectButton)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.listView)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setWindowTitle(self.name)
        if self.icon:
            self.setWindowIcon(self.icon)

        self.okButton.clicked.connect(self.onAccepted)
        self.cancelButton.clicked.connect(self.reject)
        self.selectButton.clicked.connect(self.select)
        self.unselectButton.clicked.connect(self.unselect)

    def onAccepted(self):
        self.choices = [self.model.item(i).text() for i in
                        range(self.model.rowCount())
                        if self.model.item(i).checkState()
                        == QtCore.Qt.Checked]
        self.accept()

    def select(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Checked)

    def unselect(self):
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(QtCore.Qt.Unchecked)


if __name__ == '__main__':
    fruits = [
        'Banana',
        'Apple',
        'Elderberry',
        'Clementine',
        'Fig',
        'Guava',
        'Mango',
        'Honeydew Melon',
        'Date',
        'Watermelon',
        'Tangerine',
        'Ugli Fruit',
        'Juniperberry',
        'Kiwi',
        'Lemon',
        'Nectarine',
        'Plum',
        'Raspberry',
        'Strawberry',
        'Orange',
        ]
    app = QtWidgets.QApplication(sys.argv)
    form = ChecklistDialog('Fruit', fruits, checked=True)
    if form.exec_() == QtWidgets.QDialog.Accepted:
        print('\n'.join([str(s) for s in form.choices]))