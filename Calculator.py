from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QVBoxLayout, QHBoxLayout
class Cal(QWidget):
    def __init__(self) -> None:
        super().__init__()
                
        self.setGeometry(200,300,350,300)
        self.collection = ""
        self.edit = QLineEdit("0")
        self.setStyleSheet("font-size : 30px; color : blue ;")

        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btn0 = QPushButton("0")
        self.btnDiv = QPushButton("/")
        self.btnMul = QPushButton("*")
        self.btnMinus = QPushButton("-")
        self.btnAdd = QPushButton("+")
        self.btnEqual = QPushButton("=")
        self.btnClear = QPushButton("AC")


        self.hbtn1 = QHBoxLayout()
        self.hbtn2 = QHBoxLayout()
        self.hbtn3 = QHBoxLayout()
        self.hbtn4 = QHBoxLayout()

        
        self.hbtn1.addWidget(self.btn1)
        self.hbtn1.addWidget(self.btn2)
        self.hbtn1.addWidget(self.btn3)
        self.hbtn1.addWidget(self.btnDiv)
        self.hbtn2.addWidget(self.btn4)
        self.hbtn2.addWidget(self.btn5)
        self.hbtn2.addWidget(self.btn6)
        self.hbtn2.addWidget(self.btnMul)
        self.hbtn3.addWidget(self.btn7)
        self.hbtn3.addWidget(self.btn8)
        self.hbtn3.addWidget(self.btn9)
        self.hbtn3.addWidget(self.btnMinus)
        self.hbtn4.addWidget(self.btnClear)
        self.hbtn4.addWidget(self.btn0)
        self.hbtn4.addWidget(self.btnEqual)
        self.hbtn4.addWidget(self.btnAdd)

        self.vbox = QVBoxLayout()
        
        self.vbox.addWidget(self.edit)
        self.vbox.addLayout(self.hbtn1)
        self.vbox.addLayout(self.hbtn2)
        self.vbox.addLayout(self.hbtn3)
        self.vbox.addLayout(self.hbtn4)

        self.setLayout(self.vbox)
        self.show()
               
        self.btn1.clicked.connect(self.on_click)
        self.btn2.clicked.connect(self.on_click)
        self.btn3.clicked.connect(self.on_click)
        self.btn4.clicked.connect(self.on_click)
        self.btn5.clicked.connect(self.on_click)
        self.btn6.clicked.connect(self.on_click)
        self.btn7.clicked.connect(self.on_click)
        self.btn8.clicked.connect(self.on_click)
        self.btn9.clicked.connect(self.on_click)
        self.btn0.clicked.connect(self.on_click)
        self.btnMul.clicked.connect(self.on_click)
        self.btnMinus.clicked.connect(self.on_click)
        self.btnAdd.clicked.connect(self.on_click)
        self.btnDiv.clicked.connect(self.on_click)
        self.btnEqual.clicked.connect(self.calculate)
        self.btnClear.clicked.connect(self.clear)
    
    def clear(self):
        self.collection = ""
        self.edit.clear()
        
    def on_click(self):
        text = self.sender().text()
        self.collection += text
        self.edit.setText(self.collection)
        
    def calculate(self):
        if self.collection:
            try:
                math_result = eval(self.collection)
                self.edit.setText(str(math_result))
            except ZeroDivisionError:
                self.edit.setText("ZeroDivisionError")
            
        else:
            self.edit.setText("Error: Empty expression")
        
       
calculator = QApplication([])
cal = Cal()
calculator.exec_()