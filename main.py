from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QCheckBox, QRadioButton, QLineEdit

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

        self.isStart = True

        self.initUI()

        self.show()

    def initUI(self):
        # Define
        self.te_message = self.findChild(QTextEdit, 'te_message')
        self.pbtn_connection = self.findChild(QPushButton, 'pbtn_connection')
        self.lb_connection = self.findChild(QLabel, 'lb_connection')

        self.cb_isSelectAfterAssigning = self.findChild(QCheckBox, 'cb_isSelectAfterAssigning')
        
        self.pbtn_releaseI = self.findChild(QPushButton, 'pbtn_releaseI')
        self.pbtn_releaseJ = self.findChild(QPushButton, 'pbtn_releaseJ')
        self.pbtn_releaseIJ = self.findChild(QPushButton, 'pbtn_releaseIJ')
        self.pbtn_releaseNone = self.findChild(QPushButton, 'pbtn_releaseNone')

        self.pbtn_torsionReduction = self.findChild(QPushButton, 'pbtn_torsionReduction')
        self.pbtn_nonsway = self.findChild(QPushButton, 'pbtn_nonsway')
        self.pbtn_modelChecker = self.findChild(QPushButton, 'pbtn_modelChecker')

        self.rb_joint = self.findChild(QRadioButton, 'rb_joint')
        self.rb_frame = self.findChild(QRadioButton, 'rb_frame')
        self.rb_area = self.findChild(QRadioButton, 'rb_area')
        self.pbtn_selection = self.findChild(QPushButton, 'pbtn_selection')
        self.le_unique_name = self.findChild(QLineEdit, 'le_unique_name')

        # Connect
        self.msg_signal.new_msg.connect(self.show_msg_update)
        self.pbtn_connection.clicked.connect(self.connect_etabs)

        self.pbtn_selection.clicked.connect(self.select_objects)

        self.update_button_connect()

        # OTHER
        self.cb_isSelectAfterAssigning.stateChanged.connect(self.update_button_connect)


    def update_button_connect(self) :
        #### If Add new Buttons, It MUST add following list ####
        pbtns = [self.pbtn_releaseI, self.pbtn_releaseJ, self.pbtn_releaseIJ, self.pbtn_releaseNone, 
                 self.pbtn_torsionReduction, self.pbtn_nonsway, self.pbtn_modelChecker]
        for pbtn in pbtns :
            pbtn.disconnect()

        self.isSelectAfterAssigning = self.cb_isSelectAfterAssigning.isChecked()
        isStart = self.isStart

        if self.etabs != None :
            self.pbtn_releaseI.clicked.connect(lambda : self.TedChu.release(release_end = "Mi", isSelectAfterAssigning = self.isSelectAfterAssigning))
            self.pbtn_releaseJ.clicked.connect(lambda : self.TedChu.release(release_end = "Mj", isSelectAfterAssigning = self.isSelectAfterAssigning))
            self.pbtn_releaseIJ.clicked.connect(lambda : self.TedChu.release(release_end = "Mij", isSelectAfterAssigning = self.isSelectAfterAssigning))
            self.pbtn_releaseNone.clicked.connect(lambda : self.TedChu.release(isSelectAfterAssigning = self.isSelectAfterAssigning))

            self.pbtn_torsionReduction.clicked.connect(lambda : self.TedChu.torsion_reduction(isSelectAfterAssigning = self.isSelectAfterAssigning))
            self.pbtn_nonsway.clicked.connect(lambda : self.TedChu.set_nonsway(isSelectAfterAssigning = self.isSelectAfterAssigning))

            print_log("The Buttons are Connected!!", self.msg_signal)

        else :
            self.pbtn_releaseI.clicked.connect(self.do_not_connect_msg)
            self.pbtn_releaseJ.clicked.connect(self.do_not_connect_msg)
            self.pbtn_releaseIJ.clicked.connect(self.do_not_connect_msg)
            self.pbtn_releaseNone.clicked.connect(self.do_not_connect_msg)

            self.pbtn_torsionReduction.clicked.connect(self.do_not_connect_msg)
            self.pbtn_nonsway.clicked.connect(self.do_not_connect_msg)

            if not isStart :
                print_log("The Buttons don't be Connected!!", self.msg_signal)


    def show_msg_update(self, msg):
        s = self.te_message.toPlainText()

        self.te_message.setPlainText(f'{s}\n{msg}')

        self.te_message.verticalScrollBar().setValue(self.te_message.verticalScrollBar().maximum())

    def do_not_connect_msg(self) :
        self.show_msg_update("The Button is not Connected!!")

    def connect_etabs(self):
        print_log("Clicked Connect Button", self.msg_signal)

        if self.etabs == None :
            etabs = ETABS(isTedChu = True, msg_signal = self.msg_signal, print_log = print_log)
            self.etabs = etabs
            self.TedChu = TedChuMethods(etabs, print_log)
            self.pbtn_connection.setText(f' Connected to {self.etabs.EDB_name}!! ')
            self.lb_connection.setText(f'Path : {self.etabs.EDB_path}')

            self.isStart = False

        else :
            self.pbtn_connection.setText(f" Disconnect to EABS!! ")
            self.etabs = None
            self.TedChu = None
            self.lb_connection.setText('尚未連接ETABS\n(連接前需確認 Tools -> Acitve instant for API')

        self.update_button_connect()

    def select_objects(self) :
        unique = self.le_unique_name.text()

        if unique == "" :
            print_log("Nothing is selected", self.msg_signal)
            return

        uniqueNames = unique.split()



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
