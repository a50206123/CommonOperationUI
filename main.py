from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit

from yc_etabs_api.etabs import ETABS
from yc_etabs_api.apps.tedchu import TedChuMethods

from yc_print import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/main_windows.ui', self)

        self.setWindowTitle("ETABS TOOLS")

        self.msg_signal = msg_signal
        self.etabs = None
        self.TedChu = None

        self.initUI()

        self.show()

    def initUI(self):
        # Define
        self.te_message = self.findChild(QTextEdit, 'te_message')
        self.pbtn_connection = self.findChild(QPushButton, 'pbtn_connection')
        self.lb_connection = self.findChild(QLabel, 'lb_connection')
        
        self.pbtn_releaseI = self.findChild(QPushButton, 'pbtn_releaseI')
        self.pbtn_releaseJ = self.findChild(QPushButton, 'pbtn_releaseJ')
        self.pbtn_releaseIJ = self.findChild(QPushButton, 'pbtn_releaseIJ')
        self.pbtn_releaseNone = self.findChild(QPushButton, 'pbtn_releaseNone')

        self.pbtn_torsionReduction = self.findChild(QPushButton, 'pbtn_torsionReduction')
        self.pbtn_nonsway = self.findChild(QPushButton, 'pbtn_nonsway')

        # Connect
        self.msg_signal.new_msg.connect(self.show_msg_update)
        self.pbtn_connection.clicked.connect(self.connect_etabs)
        self.update_button_connect()


        # OTHER

    def update_button_connect(self) :

        if self.etabs != None :
            self.pbtn_releaseI.clicked.connect(lambda : self.TedChu.release(release_end = "Mi"))
            self.pbtn_releaseJ.clicked.connect(lambda : self.TedChu.release(release_end = "Mj"))
            self.pbtn_releaseIJ.clicked.connect(lambda : self.TedChu.release(release_end = "Mij"))
            self.pbtn_releaseNone.clicked.connect(lambda : self.TedChu.release())

            self.pbtn_torsionReduction.clicked.connect(lambda : self.TedChu.torsion_reduction())
            self.pbtn_nonsway.clicked.connect(lambda : self.TedChu.set_nonsway())

            self.pbtn_releaseI.clicked.disconnect(self.do_not_connect_msg)
            self.pbtn_releaseJ.clicked.disconnect(self.do_not_connect_msg)
            self.pbtn_releaseIJ.clicked.disconnect(self.do_not_connect_msg)
            self.pbtn_releaseNone.clicked.disconnect(self.do_not_connect_msg)

            self.pbtn_torsionReduction.clicked.disconnect(self.do_not_connect_msg)
            self.pbtn_nonsway.clicked.disconnect(self.do_not_connect_msg)


            print_log("The Buttons are Connected!!", msg_signal)
        else :
            self.pbtn_releaseI.clicked.connect(self.do_not_connect_msg)
            self.pbtn_releaseJ.clicked.connect(self.do_not_connect_msg)
            self.pbtn_releaseIJ.clicked.connect(self.do_not_connect_msg)
            self.pbtn_releaseNone.clicked.connect(self.do_not_connect_msg)

            self.pbtn_torsionReduction.clicked.connect(self.do_not_connect_msg)
            self.pbtn_nonsway.clicked.connect(self.do_not_connect_msg)


    def show_msg_update(self, msg):
        s = self.te_message.toPlainText()

        self.te_message.setPlainText(f'{s}\n{msg}')

        self.te_message.verticalScrollBar().setValue(self.te_message.verticalScrollBar().maximum())

    def do_not_connect_msg(self) :
        self.show_msg_update("The Button is not Connected!!")

    def connect_etabs(self):
        print_log("Clicked Connect Button", self.msg_signal)

        if self.etabs == None :
            etabs = ETABS(isTedChu = True, msg_signal = msg_signal, print_log = print_log)
            self.etabs = etabs
            self.TedChu = TedChuMethods(etabs, print_log)
            self.pbtn_connection.setText(f' Connected to {self.etabs.EDB_name}!! ')
            self.lb_connection.setText(f'Path : {self.etabs.EDB_path}')


        else :
            self.pbtn_connection.setText(f" Disconnect to EABS!! ")
            self.etabs = None
            self.TedChu = None
            self.lb_connection.setText(' ')

        self.update_button_connect()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
