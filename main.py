import PyQt5.QtWidgets as qtw, sys

class MainWindow(qtw.QWidget): #extend QWidget
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Dummy Window")

        self.label = qtw.QLabel("Hello There")
        self.alert = qtw.QMessageBox(text="You clicked on that button I think.")
        self.alert.setWindowTitle("AAAAAAAAAA")
        self.btn = qtw.QPushButton("I change the label.", clicked = lambda : self.label.setText('I got changed!'))
        self.btn2 = qtw.QPushButton("I create an alert.", clicked = lambda : self.alert.exec())
        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.btn)
        self.layout().addWidget(self.btn2)

        #show window
        self.show()

app = qtw.QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())