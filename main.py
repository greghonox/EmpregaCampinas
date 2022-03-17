from sobre import sobre
from PyQt5 import QtCore, QtGui, QtWidgets

from threading import Thread
from time import sleep
from openpyxl import Workbook
from openpyxl.styles import colors, Border, Side, Font, Alignment
import emprega_motor
from detalhes import Detalhes

class Empregacampinas(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(451, 547)
        Dialog.setMinimumSize(QtCore.QSize(451, 547))
        Dialog.setMaximumSize(QtCore.QSize(451, 547))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/hiring.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.551, y1:1, x2:0.546, y2:0, stop:0 rgba(206, 190, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(24, 39))
        self.label_4.setMaximumSize(QtCore.QSize(62, 16777215))
        self.label_4.setStyleSheet("image: url(:/newPrefix/img/research.svg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.frame)
        self.janela = QtWidgets.QTabWidget(Dialog)
        self.janela.setStyleSheet("background-color: rgb(217, 205, 58);")
        self.janela.setTabPosition(QtWidgets.QTabWidget.West)
        self.janela.setIconSize(QtCore.QSize(29, 24))
        self.janela.setElideMode(QtCore.Qt.ElideNone)
        self.janela.setTabBarAutoHide(False)
        self.janela.setObjectName("janela")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.tab)
        self.frame_6.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_6)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.palavra_chave = QtWidgets.QLineEdit(self.frame_2)
        self.palavra_chave.setClearButtonEnabled(True)
        self.palavra_chave.setObjectName("palavra_chave")
        self.verticalLayout_4.addWidget(self.palavra_chave)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setEnabled(True)
        self.textEdit.setStyleSheet("background-color: rgb(234, 223, 105);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_6.addWidget(self.frame_6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/img/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.janela.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lista_progresso = QtWidgets.QTableWidget(self.tab_2)
        self.lista_progresso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lista_progresso.setObjectName("lista_progresso")
        self.lista_progresso.setColumnCount(0)
        self.lista_progresso.setRowCount(0)
        self.verticalLayout_7.addWidget(self.lista_progresso)
        self.frame_5 = QtWidgets.QFrame(self.tab_2)
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.exportar_xls = QtWidgets.QPushButton(self.frame_5)
        self.exportar_xls.setStyleSheet("EXPORTE PARA O FORMATO XLSX DO EXCEL PARA ANALISTAR AS OPORTUNIDADES DE EMPREGO!")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/img/excel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportar_xls.setIcon(icon2)
        self.exportar_xls.setIconSize(QtCore.QSize(41, 20))
        self.exportar_xls.setObjectName("exportar_xls")
        self.horizontalLayout_7.addWidget(self.exportar_xls)
        self.exportar = QtWidgets.QPushButton(self.frame_5)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/img/export-file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportar.setIcon(icon3)
        self.exportar.setIconSize(QtCore.QSize(41, 20))
        self.exportar.setObjectName("exportar")
        self.horizontalLayout_7.addWidget(self.exportar)
        self.verticalLayout_7.addWidget(self.frame_5)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/img/goal.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.janela.addTab(self.tab_2, icon4, "")
        self.verticalLayout.addWidget(self.janela)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comecar = QtWidgets.QPushButton(self.frame_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/img/checked.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comecar.setIcon(icon5)
        self.comecar.setIconSize(QtCore.QSize(32, 32))
        self.comecar.setObjectName("comecar")
        self.horizontalLayout.addWidget(self.comecar)
        self.sobre = QtWidgets.QPushButton(self.frame_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/img/question.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sobre.setIcon(icon6)
        self.sobre.setIconSize(QtCore.QSize(32, 32))
        self.sobre.setObjectName("sobre")
        self.horizontalLayout.addWidget(self.sobre)
        self.cancelar = QtWidgets.QPushButton(self.frame_3)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/img/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelar.setIcon(icon7)
        self.cancelar.setIconSize(QtCore.QSize(32, 32))
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout.addWidget(self.cancelar)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Dialog)
        self.janela.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.palavra_chave, self.comecar)
        Dialog.setTabOrder(self.comecar, self.cancelar)
        Dialog.setTabOrder(self.cancelar, self.janela)
        Dialog.setTabOrder(self.janela, self.sobre)
        Dialog.setTabOrder(self.sobre, self.textEdit)
        Dialog.setTabOrder(self.textEdit, self.lista_progresso)
        Dialog.setTabOrder(self.lista_progresso, self.exportar)
        Dialog.setTabOrder(self.exportar, self.exportar_xls)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BUSCA EMPREGO CAMPINAS - GREGÓRIO HONORATO"))
        self.label_3.setText(_translate("Dialog", "BUSCA EMPREGO - GREGHONO"))
        self.label.setText(_translate("Dialog", "PALAVRA CHAVE(VAGA)"))
        self.palavra_chave.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">DESCREVA O QUE ESTA PROCURANDO OU DEIXE EM BRANCO PARA PROCURAR PELAS ULTIMAS VAGAS DE EMPREGO.</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">BUSCA DE EMPREGO NA REGIÃO DE CAMPINAS.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PROGRAMA DESENVOLVIDO PARA AJUDAR, QUEM ESTA EM BUSCA DE SERVIÇO.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">VOCÊ PODE EXPORTA OS E-MAIL\'S PARA MANDAR EM MASSA SEUS DADOS.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CASO PRECISA DE ALGUMA FUNCIONALIDADE EXTRA, ENTRE EM CONTATO:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">TE TODO MEU CORAÇÃO. ESPERO QUE ESSE PROGRAMA AJUDE EM SUA VIDA!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">QUE DEU ILUMINE O CAMINHO DE VOCÊS FORTEMENTE.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">GREGÓRIO HONORATO</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">WHATSAPP:(19) 99250-9913</span></p></body></html>"))
        self.janela.setTabText(self.janela.indexOf(self.tab), _translate("Dialog", "CONFIGURAÇÃO"))
        self.exportar_xls.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">EXPORTE PARA O FORMATO XLSX DO EXCEL PARA ANALISTAR AS OPORTUNIDADES DE EMPREGO!</span></p></body></html>"))
        self.exportar_xls.setText(_translate("Dialog", "Exportar"))
        self.exportar.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">EXPORTE OS E-MAIL PARA ENVIO EM MASSA!</span></p></body></html>"))
        self.exportar.setText(_translate("Dialog", "Exportar"))
        self.janela.setTabText(self.janela.indexOf(self.tab_2), _translate("Dialog", "PROGRESSO"))
        self.comecar.setText(_translate("Dialog", "Começar"))
        self.sobre.setText(_translate("Dialog", "Sobre"))
        self.sobre.setShortcut(_translate("Dialog", "Return, Enter"))
        self.cancelar.setText(_translate("Dialog", "cancelar"))

        self.carregar_janela(Dialog)
    titulo = "BUSCA EMPREGO CAMPINAS - GREGÓRIO HONORATO"
    def carregar_janela(self, Dialog):
        self.comecar.setShortcut("Enter, Return")
        self.palavra_chave.setFocus()
        self.cancelar.clicked.connect(lambda:self.fechar(Dialog))
        self.sobre.clicked.connect(self.abrir_sobre)
        self.comecar.clicked.connect(self.comecar_busca)
        self.exportar_xls.clicked.connect(self.exporta_xls)
        self.exportar.clicked.connect(self.exporta)
        self.lista_progresso.clicked.connect(self.abrir_detalhes)
        self.tabela()

    def abrir_detalhes(self):
        item_selecionado = []
        for selecao in self.lista_progresso.selectedItems():
            item_selecionado.append(selecao.text())
        self.Form = QtWidgets.QDialog()
        self.ui = Detalhes()
        self.ui.setupUi(self.Form, item_selecionado)
        self.Form.exec_()

    rodando = True
    habilita = True
    def comecar_busca(self):
        if(self.habilita):
            msg = QtWidgets.QMessageBox.question(None,self.titulo, "QUER COMEÇAR A BUSCAR?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            if(msg == QtWidgets.QMessageBox.Yes):
                self.janela.setCurrentIndex(1)
                self.comecar.setText("PARAR")
                self.comecar.setStyleSheet("background-color: rgb(255, 255, 127);")
                self.lista_progresso.setRowCount(0)
                self.operacao = emprega_motor.Emprego()
                self.habilita = False
                self.rodando = True
                self.rodar()
        else:
            self.comecar.setText("COMEÇAR")
            self.comecar.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.habilita = True
            self.rodando = False

    def rodar(self):
        Thread(target=self.processar).start()

    def processar(self):
        contador = 0
        while self.rodando:
            self.operacao.navegar(self.palavra_chave.text(), contador)
            self.carregar_progresso(self.operacao.vagas)

            if(len(self.operacao.vagas) == 0):
                self.habilita = True
                self.comecar.setText("COMEÇAR")
                self.comecar.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.rodando = False
                break
            self.operacao.vagas.clear()
            contador += 1

    def carregar_progresso(self, texto):
        for txt in texto:
            linha = self.lista_progresso.rowCount()
            self.lista_progresso.insertRow(self.lista_progresso.rowCount())
            for coluna, dados in enumerate(txt):
                self.lista_progresso.setItem(linha, coluna,QtWidgets.QTableWidgetItem(str(dados)))

    def fechar(self, Dialog):
        self.rodando = False
        self.habilita = False
        Dialog.close()

    def exporta_xls(self):
        QtWidgets.QMessageBox.information(None, self.titulo,
        "<b>AINDA NÃO DISPONIVEL PARA ESSA VERSÃO, ENTRE CONTATO COM DESENVOLVEDOR!</b>")

    def pegar_dados_celula(self, linha):
        linha_dados = []
        for coluna in range(5):
            try:
                linha_dados.append(self.lista_progresso.item(linha, coluna).text())
            except:
                pass
        return linha_dados

    def exporta(self, opcao=0):
        import os
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontConfirmOverwrite
        extensao = ".txt" if(opcao == 0) else ".xlsx"
        nome_arquivo = ""
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None, self.titulo, os.path.expanduser("~/")+
                                                  nome_arquivo, extensao, options=options)

        if(len(fileName) > 0 ):
            self.pegar_lista_progresso(fileName + extensao)

    def pegar_lista_progresso(self, arquivo):
        with open(arquivo, "w") as arq:
            for linha in range(self.lista_progresso.rowCount()):
                try:
                    numero = str(self.lista_progresso.item(linha, 5).text())
                    if(numero != "None"):
                        arq.write(numero+"\n")
                except Exception as erro:
                    pass
        QtWidgets.QMessageBox.information(None, self.titulo, "<b>FEITO A EXPORTAÇÃO COM SUCESSO!</b>")

    def tabela(self):
        self.lista_progresso.setRowCount(0)
        self.lista_progresso.setSelectionBehavior(self.lista_progresso.SelectRows)
        self.lista_progresso.setSelectionMode(self.lista_progresso.SingleSelection)
        self.lista_progresso.setAlternatingRowColors(True)
        self.lista_progresso.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        colunas = ["Clientes", "Sálario", "Beneficio", "Responsabilidade", "Requisitos", "Contato", "Link"]
        self.lista_progresso.clear()
        self.lista_progresso.setColumnCount(len(colunas))
        self.lista_progresso.setHorizontalHeaderLabels(colunas)

    def abrir_sobre(self):
        self.Form = QtWidgets.QDialog()
        self.ui = sobre()
        self.ui.setupUi(self.Form)
        self.Form.exec_()

import recursos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Empregacampinas()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
