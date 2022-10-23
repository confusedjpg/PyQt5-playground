import PyQt5.QtWidgets as qtw, sys, random as rd

class MainWindow(qtw.QWidget): #extend QWidget
    def __init__(self):
        #steal qtw.QWidget.__init__() lol
        super(MainWindow, self).__init__()
        self.setWindowTitle("Dummy Window")
        self.hello = ['hello', 'hi', 'howdy', 'sup', 'hello there', 'greetings']

        #create widgets and configure them
        self.label = qtw.QLabel("buenos dias")
        self.alert = qtw.QMessageBox(text="You clicked on that button I think.")
        self.alert.setWindowTitle("AAAAAAAAAA")
        self.btn = qtw.QPushButton("I change the label.", clicked = lambda : self.label.setText(rd.choice(self.hello)))
        self.btn2 = qtw.QPushButton("I create an alert.", clicked = lambda : self.alert.exec())
        
        #set layout and add widgets
        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.btn)
        self.layout().addWidget(self.btn2)

        self.show()

app = qtw.QApplication(sys.argv)
app.setStyle("Windows") #change style to something nicer
mw = MainWindow()
sys.exit(app.exec_())