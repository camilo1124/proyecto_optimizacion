
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import data_processing as dp
import model as md

import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.state = 0
        self.res_money = None
        self.res_hec = None
        self.res_tiempo = None
        self.elements_index = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 611, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(240, 30, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 371, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(240, 130, 171, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(230, 170, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(440, 330, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda :self.button_next_func())
        self.pushButton2 = QtWidgets.QPushButton(self.tab)
        self.pushButton2.setGeometry(QtCore.QRect(320,330,111,31))
        self.pushButton2.setObjectName("pushButton2")
        self.table = QtWidgets.QTableWidget(len(dp.get_field("Cultivo")),1,self.tab)
        self.table.setGeometry(35,40,150,300)
        self.table.hide()
        self.table2 = None
        self.table3 = None
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(50, 50, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(50, 100, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(50, 140, 47, 13))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(90, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(490, 50, 61, 21))
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(300, 100, 130, 21))
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(270, 135, 150, 21))
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(300, 60, 157, 21))
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(440,100,50,21))
        self.lineEdit2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit2.setGeometry(QtCore.QRect(440, 135, 50, 21))
        self.checkBox = QtWidgets.QCheckBox(" Añadir tiempo ",self.tab)
        self.checkBox.setGeometry(330,170,180,21)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 80, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(480, 80, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuInfo.addSeparator()
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        if self. state == 0:
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "AgroColLP"))
            self.label.setText(_translate("MainWindow", "AgroColLP"))
            self.label_2.setText(_translate("MainWindow", "Aplicación para la optimización de resursos del agro colombiano"))
            self.label_3.setText(_translate("MainWindow", "Escoja el modelo que desee:"))
            self.comboBox.setCurrentText(_translate("MainWindow", "Maximizar Produccion(Ton)"))
            self.comboBox.setItemText(0, _translate("MainWindow", "Maximizar Produccion(Ton)"))
            self.comboBox.setItemText(1, _translate("MainWindow", "Minimizar Costo"))
            self.comboBox.setItemText(2, _translate("MainWindow", "Maximizar Ganancias"))
            self.comboBox.setItemText(3, _translate("MainWindow", "Maximizar Utilidades"))
            self.pushButton.setText(_translate("MainWindow", "Siguiente"))
            self.pushButton2.setText(_translate("MainWindow", "Anterior"))
            self.pushButton2.hide()
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Optimizacion de recursos"))
            self.label_6.setText(_translate("MainWindow", "Lugar 1"))
            self.label_7.setText(_translate("MainWindow", "Lugar 1"))
            self.label_8.setText(_translate("MainWindow", "Lugar 1"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Problema de transporte"))
            self.label_4.setText(_translate("MainWindow", "Origen"))
            self.label_5.setText(_translate("MainWindow", "Destino"))
            self.label_9.setText(_translate("MainWindow", "Hectarias Disponibles"))
            self.label_10.setText(_translate("MainWindow", "Dinero Disponibles(mill)"))
            self.checkBox.setCheckState(False)
            self.label_9.hide()
            self.label_10.hide()
            self.label_11.hide()
            self.lineEdit.hide()
            self.lineEdit2.hide()
            self.checkBox.hide()
            self.tabWidget.removeTab(1)
            self.tabWidget.removeTab(1)
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Ruta menos costosa"))
            self.menuInfo.setTitle(_translate("MainWindow", "Info"))

    def hide_elements_init(self):

        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.comboBox.hide()

    def hide_elements_stage_one(self):
        self.label_9.hide()
        self.label_10.hide()
        self.lineEdit.hide()
        self.lineEdit2.hide()
        self.checkBox.hide()
        self.table.hide()





    def stage_cero(self):

        print("Estado cero")

    def button_next_func(self):
        if self.state == 0:
            self.stage_one()




    def stage_one(self):
        self.checkBox.setCheckState(False)
        selected_model = self.comboBox.currentText()

        self.hide_elements_init()
        self.state = 1
        cultivos = dp.get_field("Cultivo")
        for i in range(len(cultivos)):
            item = QtWidgets.QTableWidgetItem(cultivos[i])
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.table.setItem(i,0,item)
        self.label_9.show()
        if selected_model == "Minimizar Costo":
            self.label_10.setText("Toneladas min")
            self.label_10.setGeometry(QtCore.QRect(300, 135, 150, 21))
        self.label_10.show()
        self.label_11.setText(selected_model)
        self.label_11.show()
        self.lineEdit.show()
        self.lineEdit2.show()
        self.pushButton2.show()
        self.checkBox.show()
        self.table.setHorizontalHeaderLabels(["Cultivos"])
        self.table.show()
        self.pushButton.clicked.connect(lambda : self.stage_two())

    def stage_two(self):
        self.res_hec = int(self.lineEdit.text())
        self.res_money = int(self.lineEdit2.text())
        self.res_tiempo = bool(self.checkBox.checkState())
        self.hide_elements_stage_one()
        nRows = 0
        indexes = []
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0).checkState() > 0:
                nRows += 1
                indexes.append(row)

        self.label_11.setGeometry(270,30,157,21)
        self.table2 = QtWidgets.QTableWidget(nRows,3,self.tab)
        self.table2.setGeometry(35, 60, 500, 200)
        cultivos = dp.get_field("Cultivo")
        item3 = []
        comboBox_arr = []
        diccionarios = []
        for i in range(nRows):
            item1 = QtWidgets.QTableWidgetItem(cultivos[indexes[i]])
            mercados = dp.get_markets(i)
            precios = dp.get_prices(i)
            dic = {mercados[i]: precios[i] for i in range(len(precios))}
            diccionarios.append(dic)
            comboBox_arr.append(QtWidgets.QComboBox())
            for j in mercados:
                comboBox_arr[i].addItem(j)
            item3.append(QtWidgets.QTableWidgetItem(str(dic[comboBox_arr[i].currentText()])))
            self.table2.setItem(i, 0, item1)
            self.table2.setCellWidget(i,1,comboBox_arr[i])
            self.table2.setItem(i, 2, item3[i])
            header = self.table2.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            self.table2.cellWidget(i,1).currentTextChanged.connect(lambda state, x=i:self.table2.item(x,2).setText(str(diccionarios[x][comboBox_arr[x].currentText()])))
            #comboBox_arr[i].currentTextChanged.connect(lambda state, x=i: print(x))
            #comboBox_arr[i].currentTextChanged.connect(lambda state ,x=i : item3[x].setText(str(dic[comboBox_arr[x].currentText()])))
            self.table2.setHorizontalHeaderLabels(["Cultivos","Mercados", "Precio promedio"])
        self.pushButton.setText("Resolver")
        final_prices = []
        for i in range(self.table2.rowCount()):
            final_prices.append(int(self.table2.item(i,2).text()))
        self.pushButton.clicked.connect(lambda : self.state_tree(indexes,final_prices))
        self.table2.show()

    def state_tree(self,indexes,prices):

        self.table2.hide()
        model = self.label_11.text()

        if model == "Maximizar Produccion(Ton)":
            resultado,fo = md.max_prod_model(self.res_hec,self.res_money,self.res_tiempo,indexes,prices)
            self.table3 = QtWidgets.QTableWidget(len(resultado)+1,1,self.tab)
            self.table3.setGeometry(35, 60, 500, 200)
            self.table3.setHorizontalHeaderLabels(["Resultados"])
            for i in range(len(resultado)):
                item = QtWidgets.QTableWidgetItem(resultado[i])
                self.table3.setItem(i,0,item)
            item = QtWidgets.QTableWidgetItem(fo)
            self.table3.setItem(len(resultado),0,item)
            header = self.table3.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            self.table3.show()



        elif model == "Minimizar Costo":
            resultado,fo =md.min_cost_model(self.res_hec,self.res_money,self.res_tiempo,indexes,prices)
            self.table3 = QtWidgets.QTableWidget(len(resultado) + 1, 1, self.tab)
            self.table3.setGeometry(35, 60, 500, 200)
            self.table3.setHorizontalHeaderLabels(["Resultados"])
            for i in range(len(resultado)):
                item = QtWidgets.QTableWidgetItem(resultado[i])
                self.table3.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem(fo)
            self.table3.setItem(len(resultado), 0, item)
            header = self.table3.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            self.table3.show()
        elif model == "Maximizar Ganancias":
            resultado,fo =md.max_profit_model(self.res_hec,self.res_money,self.res_tiempo,indexes,prices)
            self.table3 = QtWidgets.QTableWidget(len(resultado) + 1, 1, self.tab)
            self.table3.setGeometry(35, 60, 500, 200)
            self.table3.setHorizontalHeaderLabels(["Resultados"])
            for i in range(len(resultado)):
                item = QtWidgets.QTableWidgetItem(resultado[i])
                self.table3.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem(fo)
            self.table3.setItem(len(resultado), 0, item)
            header = self.table3.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            self.table3.show()
        elif model == "Maximizar Utilidades":
            resultado,fo =md.max_util_model(self.res_hec,self.res_money,self.res_tiempo,indexes,prices)
            self.table3 = QtWidgets.QTableWidget(len(resultado) + 1, 1, self.tab)
            self.table3.setGeometry(35, 60, 500, 200)
            self.table3.setHorizontalHeaderLabels(["Resultados"])
            for i in range(len(resultado)):
                item = QtWidgets.QTableWidgetItem(resultado[i])
                self.table3.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem(fo)
            self.table3.setItem(len(resultado), 0, item)
            header = self.table3.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            self.table3.show()








def Programa():
    app = QApplication([])
    instancia_vent = QtWidgets.QMainWindow()
    mw = Ui_MainWindow()
    mw.setupUi(instancia_vent)
    instancia_vent.show()




    app.exec_()