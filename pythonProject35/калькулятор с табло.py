from PyQt5.QtWidgets import QWidget, QApplication, QLabel,QPushButton
import sys
import math

class Calculator(QWidget):
      def __init__(self):
            super().__init__()
            self.initUI()
            self.my_input=[] # пишем для ввода инфы
            self.operand_1=[] # пишем для оперАнда
            self.operand_2=[] #тоже самое

      def initUI(self):
            self.setGeometry(100,199,200,200)
            self.setWindowTitle("Мой любимый калькулятор")

            self.label=QLabel(self)
            self.label.setText("0.00")
            self.label.resize(500,50)
            self.label.move(10,0)

            self.num_1=QPushButton("1",self)
            self.num_1.move(0,50)
            self.num_1.resize(40,40)

            self.num_2=QPushButton("2",self)
            self.num_2.resize(40,40)
            self.num_2.move(30,50)

            self.num_3=QPushButton("3",self)
            self.num_3.resize(40,40)
            self.num_3.move(60,50)

            self.num_delenie=QPushButton("/",self)
            self.num_delenie.resize(40,40)
            self.num_delenie.move(120,50)

            self.num_4=QPushButton("4",self)
            self.num_4.resize(40,40)
            self.num_4.move(0,85)

            self.num_5=QPushButton("5",self)
            self.num_5.resize(40,40)
            self.num_5.move(30,85)

            self.num_6=QPushButton("6",self)
            self.num_6.resize(40,40)
            self.num_6.move(60,85)

            self.num_umn=QPushButton("X",self)
            self.num_umn.resize(40,40)
            self.num_umn.move(120,85)

            self.num_7=QPushButton("7",self)
            self.num_7.resize(40,40)
            self.num_7.move(0,120)

            self.num_8=QPushButton("8",self)
            self.num_8.resize(40,40)
            self.num_8.move(30,120)

            self.num_9=QPushButton("9",self)
            self.num_9.resize(40,40)
            self.num_9.move(60,120)

            self.num_stepen=QPushButton("^",self)
            self.num_stepen.resize(40,40)
            self.num_stepen.move(120,120)

            self.num_vit=QPushButton("-",self)
            self.num_vit.resize(40,40)
            self.num_vit.move(90,50)

            self.num_sint=QPushButton(",",self)
            self.num_sint.resize(40,40)
            self.num_sint.move(0,155)

            self.num_0=QPushButton("0",self)
            self.num_0.resize(40,40)
            self.num_0.move(30,155)

            self.num_del=QPushButton("<=",self)
            self.num_del.resize(40,40)
            self.num_del.move(60,155)

            self.num_kvkoren=QPushButton("√",self)
            self.num_kvkoren.resize(40,40)
            self.num_kvkoren.move(120,155)

            self.num_plussik=QPushButton("+",self)
            self.num_plussik.resize(40,75)
            self.num_plussik.move(90,85)

            self.num_ravno=QPushButton("=",self)
            self.num_ravno.resize(40,40)
            self.num_ravno.move(90,155)

            self.num_procent=QPushButton("%",self)
            self.num_procent.resize(40,50)
            self.num_procent.move(150,50)

            self.num_delnacelo=QPushButton("//",self)
            self.num_delnacelo.resize(40,50)
            self.num_delnacelo.move(150,95)

            self.num_vkvadrat=QPushButton("^2",self)
            self.num_vkvadrat.resize(40,55)
            self.num_vkvadrat.move(150,140)

            self.num_1.clicked.connect(self.one) #объединяем с функцией для запуска кнопки
            self.num_2.clicked.connect(self.dva)
            self.num_3.clicked.connect(self.tri)
            self.num_4.clicked.connect(self.chetire)
            self.num_5.clicked.connect(self.pat)
            self.num_6.clicked.connect(self.shest)
            self.num_7.clicked.connect(self.sem)
            self.num_8.clicked.connect(self.vosem)
            self.num_9.clicked.connect(self.devjat)
            self.num_0.clicked.connect(self.zero)
            self.num_plussik.clicked.connect(self.plus_1)
            self.num_vit.clicked.connect(self.minus_1)
            self.num_umn.clicked.connect(self.umnozit)
            self.num_delenie.clicked.connect(self.podelit)
            self.num_stepen.clicked.connect(self.vstepen)
            self.num_kvkoren.clicked.connect(self.sqrt)
            self.num_ravno.clicked.connect(self.ravno)
            self.num_del.clicked.connect(self.clear)
            self.num_sint.clicked.connect(self.sint1)
            self.num_vkvadrat.clicked.connect(self.kvadratik)
            self.num_procent.clicked.connect(self.procent1)
            self.num_delnacelo.clicked.connect(self.delimnacelo)

      def enterValue(self):
            if self.label.text()=="0.00": # функция отвечает за ввод. вводится число,если стоит цифра 0 очищается и производится сумма
                  self.label.setText("")
            self.label.setText(self.label.text()+self.my_input)

      def one(self): # присваиваем кнопкам данные
            self.my_input="1"
            self.enterValue()

      def dva(self):
            self.my_input="2"
            self.enterValue()

      def tri(self):
            self.my_input="3"
            self.enterValue()

      def chetire(self):
            self.my_input="4"
            self.enterValue()

      def pat(self):
            self.my_input="5"
            self.enterValue()

      def shest(self):
            self.my_input="6"
            self.enterValue()

      def sem(self):
            self.my_input="7"
            self.enterValue()

      def vosem(self):
            self.my_input="8"
            self.enterValue()

      def devjat(self):
            self.my_input="9"
            self.enterValue()

      def zero(self):
            self.my_input="0"
            self.enterValue()


      def plus_1(self): #Добавили операцию +, все инфу на табло загнали в операнд1 с пометкой дробное
           self.operation = '+'
           self.operand_1 = float(self.label.text())
           self.label.setText('')

      def minus_1(self):
           self.operation="-"
           self.operand_1=float(self.label.text())
           self.label.setText("")

      def umnozit(self):
           self.operation="*"
           self.operand_1=float(self.label.text())
           self.label.setText("")

      def podelit(self):
            self.operation="/"
            self.operand_1=float(self.label.text())
            self.label.setText("")

      def vstepen(self):
            self.operation="^"
            self.operand_1=float(self.label.text())
            self.label.setText("")

      def sqrt(self):
            self.operation="√"
            self.operand_1=float(self.label.text())
            self.label.setText("")

      def procent1(self):
           self.operation="%"
           self.operand_1=float(self.label.text())
           self.label.setText("")

      def ravno(self):
            self.operand_2=float(self.label.text())
            if self.operation=="+":
                  self.rezult=self.operand_1+self.operand_2

            if self.operation=="-":
                  self.rezult=self.operand_1-self.operand_2

            if self.operation=="*":
                  self.rezult=self.operand_1*self.operand_2

            if self.operation=="/" :
                  if self.operand_2==0:
                        self.rezult="Error"
                  else:
                        self.rezult=self.operand_1/self.operand_2

            if self.operation=="^":
                  self.rezult=self.operand_1**self.operand_2

            if self.operation == "√":
                  self.rezult=self.operand_1**(1/self.operand_2)

            if self.operation == "%":
                  self.rezult = self.operand_1 * (self.operand_2/100)

            if self.operation == "//":
                  self.rezult = self.operand_1 // self.operand_2


            self.label.setText(str(self.rezult))

      def clear(self):
            self.label.setText("")

      def sint1(self):
            self.operation=","
            self.operand_1=(float(self.label.text()))/10
            self.label.setText(str(self.operand_1))

      def kvadratik(self):
            self.operatiom="^2"
            self.operand_1=(float(self.label.text()))**2
            self.label.setText(str(self.operand_1))

      def delimnacelo(self):
            self.operation = "//"
            self.operand_1 = float(self.label.text())
            self.label.setText("")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())





