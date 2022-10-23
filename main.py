import PyQt5.QtWidgets as qtw, sys

class MainWindow(qtw.QWidget): #extend QWidget
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Dummy Window")

        self.label = qtw.QLabel("Hello There")
        self.btn = qtw.QPushButton("I change the label.", clicked = lambda : self.label.setText('I got changed!'))

        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.btn)

        #show window
        self.show()

app = qtw.QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())