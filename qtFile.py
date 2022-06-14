import sys
from PyQt5.QtWidgets import QMainWindow, QColorDialog, QRadioButton, QComboBox, QHBoxLayout, QInputDialog
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel, QLineEdit, QAction, QPushButton, QFileDialog
from XLMethods import createMatrixWithXlElement, writef
from gramSchmidt import *


class MenuBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Path = False
        self.hboxLBL = False
        self.RBG = False
        self.RBL = False
        self.setUI()

    def setUI(self):
        # ==============  ..:: mainWindow::.. ==============
        self.setWindowTitle('..:: QR ::..')
        self.setGeometry(100, 100, 400, 300)
        self.setMinimumSize(100, 200)
        self.setMaximumSize(600, 400)

        # ==============  ..:: Actions::.. ==============
        mainMenuBar = self.menuBar()

        fileActionExit = QAction('Exit', self)
        viewActionChBC = QAction('Change background color', self)

        addMenuFile = mainMenuBar.addMenu('File')
        addMenuView = mainMenuBar.addMenu('View')

        addMenuFile.addAction(fileActionExit)
        addMenuView.addAction(viewActionChBC)

        fileActionExit.triggered.connect(self.exitApp)
        viewActionChBC.triggered.connect(self.changegColor)

        # ==============  ..:: radio button::.. ==============
        self.radioBG = QRadioButton(self)
        self.radioBG.setText('Solving Ax=b using QR factorization')
        self.radioBG.setGeometry(20, 20, 500, 28)
        self.radioBG.clicked.connect(self.rbg)

        self.radioBL = QRadioButton(self)
        self.radioBL.setText('Solving Least-Squares Problem using QR')
        self.radioBL.setGeometry(20, 50, 500, 28)
        self.radioBL.clicked.connect(self.rbl)

        # ==============  ..:: Labels::.. ==============

        self.hboxLBL = QLabel('', self)
        self.hboxLBL.setGeometry(100, 100, 100, 100)
        # ==============  ..:: Buttons::.. ==============

        btn = QPushButton(self, text='set file Path')
        btn.setGeometry(30, 100, 100, 26)
        btn.clicked.connect(lambda: self.getPath())

        runBtn = QPushButton(self, text='Run')
        runBtn.setGeometry(30, 140, 100, 26)
        runBtn.clicked.connect(lambda :self.run())

        exitbtn = QPushButton(self, text='Exit')
        exitbtn.setGeometry(30, 220, 100, 26)
        exitbtn.clicked.connect(self.exitApp)

        self.show()

    def run(self):
        if self.Path:
            matrix, b, matrixLength = createMatrixWithXlElement(self.Path)
            if self.radioBG:
                vector = AXb(matrix, b).getX()
                writef(vector)

            elif self.radioBL:
                vector = LeastSquares(matrix, b).process()
                writef(vector)

    def rbg(self):
        self.RBG = True

    def rbl(self):
        self.RBL = True

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Exel Files (*.xlsx);;ods file (*.ods)",
                                                  options=options)
        if fileName:
            return fileName

    def getPath(self):
        self.Path = self.openFileNameDialog()


    def changegColor(self):
        var1 = QColorDialog()
        colorName = var1.getColor().name()
        self.setStyleSheet(f'background-color: {colorName}')

    def exitApp(self):
        qmb = QMessageBox.question(self, '..:: Exit ::..',
                                   'are you sure you want to exit?',
                                   QMessageBox.Cancel | QMessageBox.Yes)

        if qmb == QMessageBox.Yes:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    WindowOne = MenuBar()
    sys.exit(app.exec_())
