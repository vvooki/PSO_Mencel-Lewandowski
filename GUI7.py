from PyQt5 import QtCore, QtGui, QtWidgets
import pso

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1118, 665)
        Dialog.setStyleSheet("background-color:rgb(48, 48, 48); font: 10pt \"Roboto\"; color:rgb(255, 255, 255);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resultBar = QtWidgets.QFrame(Dialog)
        self.resultBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultBar.setObjectName("resultBar")
        self.dataBar = QtWidgets.QFrame(self.resultBar)
        self.dataBar.setGeometry(QtCore.QRect(693, 0, 411, 643))
        self.dataBar.setStyleSheet("background-color:rgb(80, 80, 80)")
        self.dataBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dataBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dataBar.setObjectName("dataBar")
        self.i = QtWidgets.QTextEdit(self.dataBar)
        self.i.setGeometry(QtCore.QRect(180, 60, 181, 41))
        self.i.setStyleSheet("font: 14pt \"Roboto\"; border: 1px solid #b9b9b9;")
        self.i.setObjectName("i")
        self.particles = QtWidgets.QTextEdit(self.dataBar)
        self.particles.setGeometry(QtCore.QRect(180, 140, 181, 41))
        self.particles.setStyleSheet("font: 14pt \"Roboto\"; border: 1px solid #b9b9b9;")
        self.particles.setObjectName("particles")
        self.label = QtWidgets.QLabel(self.dataBar)
        self.label.setGeometry(QtCore.QRect(30, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 12pt \"Roboto\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.dataBar)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 12pt \"Roboto\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.dataBar)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 12pt \"Roboto\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.dataBar)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(230, 370, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setKerning(False)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(49, 142, 255); font: 75 12pt \"Roboto\"; border: 0px solid;")
        self.pushButton.setObjectName("pushButton")
        #self.Animation2D = QtWidgets.QPushButton(self.dataBar)
        #self.Animation2D.setEnabled(True)
        #self.Animation2D.setGeometry(QtCore.QRect(10, 540, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setKerning(False)
        #self.Animation2D.setFont(font)
        #self.Animation2D.setAutoFillBackground(False)
        #self.Animation2D.setStyleSheet("background-color: rgb(0, 85, 0); font: 75 12pt \"Roboto\"; border: 1px dashed white;")
        #self.Animation2D.setObjectName("Animation2D")
        #self.Chart2D = QtWidgets.QPushButton(self.dataBar)
        #self.Chart2D.setEnabled(True)
        #self.Chart2D.setGeometry(QtCore.QRect(260, 540, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setKerning(False)
        #self.Chart2D.setFont(font)
        #self.Chart2D.setAutoFillBackground(False)
        #self.Chart2D.setStyleSheet("background-color: rgb(0, 85, 0);\n"
#"font: 75 12pt \"Roboto\";\n"
#"border: 1px dashed white;\n"
#"")
        #self.Chart2D.setObjectName("Chart2D")
        self.radioButton = QtWidgets.QRadioButton(self.dataBar)
        self.radioButton.setGeometry(QtCore.QRect(30, 290, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("font: 12pt \"Roboto\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.dataBar)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 290, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("font: 12pt \"Roboto\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.dataBar)
        self.radioButton_3.setGeometry(QtCore.QRect(260, 290, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("font: 12pt \"Roboto\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_6 = QtWidgets.QLabel(self.dataBar)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 12pt \"Roboto\";")
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.dataBar)
        self.line_2.setGeometry(QtCore.QRect(0, 210, 411, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.dataBar)
        self.label_5.setGeometry(QtCore.QRect(10, 620, 411, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 10pt \"Roboto\"; background-color: rgb(80, 80, 80);")
        self.label_5.setObjectName("label_5")
        self.solution = QtWidgets.QTextEdit(self.resultBar)
        self.solution.setGeometry(QtCore.QRect(30, 570, 621, 41))
        self.solution.setStyleSheet("font: 14pt \"Roboto\"; border: 1px solid #b9b9b9;")
        self.solution.setObjectName("solution")
        self.i_o = QtWidgets.QLabel(self.resultBar)
        self.i_o.setGeometry(QtCore.QRect(30, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.i_o.setFont(font)
        self.i_o.setStyleSheet("font: 10pt \"Roboto\";")
        self.i_o.setObjectName("i_o")
        self.particles_o = QtWidgets.QLabel(self.resultBar)
        self.particles_o.setGeometry(QtCore.QRect(30, 50, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.particles_o.setFont(font)
        self.particles_o.setStyleSheet("font: 10pt \"Roboto\";")
        self.particles_o.setObjectName("particles_o")
        self.tableWidget = QtWidgets.QTableWidget(self.resultBar)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 621, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnWidth(0,190)
        self.tableWidget.setColumnWidth(1,190)
        self.tableWidget.setColumnWidth(2,190)
        self.tableWidget.setHorizontalHeaderLabels(["Particle Position","Particle Best Position","Particle Local Optimum"])
        
        self.horizontalLayout.addWidget(self.resultBar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #tu pisz nowe rzeczy żeby w razie zmiany designu sie nie pomylić i wiedziec gdzie co wkleić
        self.pushButton.clicked.connect(self.clicked)
        #self.Animation2D.clicked.connect(self.click2dAnimation)
        #self.Chart2D.clicked.connect(self.clickChart)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Iterations"))
        self.label_3.setText(_translate("Dialog", "Particles amount"))
        self.label_4.setText(_translate("Dialog", "SWARM & APP SETTINGS"))
        self.pushButton.setText(_translate("Dialog", "Save and reload"))
        #self.Animation2D.setText(_translate("Dialog", "Generate 2D animation"))
        #self.Chart2D.setText(_translate("Dialog", "Generate 2D chart"))
        self.radioButton.setText(_translate("Dialog", "Rastrign"))
        self.radioButton_2.setText(_translate("Dialog", "Ackley"))
        self.radioButton_3.setText(_translate("Dialog", "Eggholder"))
        self.label_6.setText(_translate("Dialog", "PICK THE FUNCTION"))
        self.label_5.setText(_translate("Dialog", "Łukasz Mencel & Jakub Lewandowski | 2021 | Sztuczna Inteligencja"))
        self.i_o.setText(_translate("Dialog", "Current Iterations:"))
        self.particles_o.setText(_translate("Dialog", "Current amount of Particles:"))

    def clicked(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
        checked = 0
        
        self.solution.setStyleSheet("font: 12pt \"Roboto\";border: 1px solid rgb(49, 142, 255);")

        if(self.radioButton.isChecked()):
                checked = 1
        elif(self.radioButton_2.isChecked()):
                checked = 2
        elif(self.radioButton_3.isChecked()):
                checked = 3

        self.solution.setText(pso.main(int(self.i.toPlainText()), int(self.particles.toPlainText()),checked))
        self.i_o.setText("Current Iterations: " + self.i.toPlainText())
        self.particles_o.setText("Current Amount of Particles: " + self.particles.toPlainText())
        
        self.tableWidget.setHorizontalHeaderLabels(["Particle Position","Particle Best Position","Particle Local Optimum"])
        
        self.tableWidget.setRowCount(len(pso.tabParticlePosition))
        for i in range(0, len(pso.tabParticlePosition)):
              self.tableWidget.setItem(i,0, QtWidgets.QTableWidgetItem(pso.tabParticlePosition[i]))
              self.tableWidget.setItem(i,1, QtWidgets.QTableWidgetItem(pso.tabPbestPosition[i]))
              self.tableWidget.setItem(i,2, QtWidgets.QTableWidgetItem(pso.tabLocalOptimum[i]))

        pso.tabParticlePosition.clear()
        pso.tabLocalOptimum.clear()
        pso.tabPbestPosition.clear()

    def click2dAnimation(self):
        pso.plotingAnimation(int(self.i.toPlainText()), int(self.particles.toPlainText()))

    def clickChart(self):
        pso.plotingChart(int(self.i.toPlainText()), int(self.particles.toPlainText())) 



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())