from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout
import time
import random
import datetime
from gui.kobert_model.text_classificator import question_classificator
from gui.kogpt2_transformers.text_generator import answer_generator


class AnsWidget(QtWidgets.QWidget):
    def __init__(self,time,tweet, ai_name):
        QtWidgets.QWidget.__init__(self, flags=QtCore.Qt.Widget)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setStretch(1, 2)
        self.layout.setStretch(2, 1)

        self.ai_name = QtWidgets.QLabel()
        self.ai_name.setEnabled(False)
        self.ai_name.setFrameShape(QtWidgets.QFrame.Box)
        self.ai_name.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ai_name.setAlignment(QtCore.Qt.AlignCenter)
        self.ai_name.setObjectName("ai_name")
        self.ai_name.setText(ai_name)
        self.layout.addWidget(self.ai_name)

        self.ans_widget = QtWidgets.QLabel()
        self.ans_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ans_widget.setObjectName("ans_widget")
        self.ans_widget.setText(tweet)
        self.layout.addWidget(self.ans_widget)

        self.horiz_layout = QtWidgets.QHBoxLayout()
        self.horiz_layout.setStretch(0, 0)
        self.horiz_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.get_ans_time = QtWidgets.QLabel()
        self.get_ans_time.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.get_ans_time.setObjectName("get_ans_time")
        self.get_ans_time.setText(time)
        self.horiz_layout.addWidget(self.get_ans_time)

        self.horiz_layout.setStretch(3, 1)

        self.layout.addLayout(self.horiz_layout)
        self.setLayout(self.layout)

        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

class Ui_MainWindow(object):
    def __init__(self):
        self.ans_gen = answer_generator()
        self.q_category = question_classificator()
        self.tmp_q = ""
        self.not_first = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.question = QTextEdit()
        self.question.setAcceptRichText(False)
        self.question.setPlaceholderText("?????? ?????? ????????? ?????? ??????????????? ")
        self.verticalLayout.addWidget(self.question)

        self.finish_btn = QtWidgets.QPushButton(self.centralwidget)
        self.finish_btn.setText('?????? ')
        self.finish_btn.clicked.connect(self.add_tweet_widget)
        self.verticalLayout.addWidget(self.finish_btn)

        self.classif_btn = QtWidgets.QPushButton(self.centralwidget)
        self.classif_btn.setText('    ')
        self.classif_btn.setEnabled(False)
        self.verticalLayout.addWidget(self.classif_btn)


        #font = QtGui.QFont()
        #font.setPointSize(18)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.formLayout = QtWidgets.QHBoxLayout()
        self.formLayout.setStretch(0, 0)

        self.ans_layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom)
        self.ans_layout.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)

        self.formLayout.addLayout(self.ans_layout)


        self.groupbox = QtWidgets.QGroupBox("AI-Emotional-Card")
        self.groupbox.setLayout(self.formLayout)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 690, 414))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.groupbox)

        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setLayout(QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.BottomToTop))

        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 4)
        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_sentence(self, sentence):
        set_sentence = ""
        dot_cnt = 0
        for i,s in enumerate(sentence):
            if dot_cnt == 5: # 5??????????????? ???
                break
            if s != '.': #tmp=??????????????? ?????? , ???????????? ?????????...
                set_sentence += s
            else:
                if i+1 != len(sentence) and sentence[i+1] != '.':
                    dot_cnt += 1
                    set_sentence += '.\n'
                else:
                    set_sentence += s
        return set_sentence

    def set_clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)


    def add_tweet_widget(self):
        q = self.question.toPlainText()
        if self.tmp_q != q and self.not_first: # clear answer layout
            self.set_clear_layout(self.ans_layout)
        self.classif_btn.setText(self.q_category.get_question_category(q))
        yymmdd = time.strftime('%Y??? %m??? %d??? ', time.localtime(time.time()))
        hhmmss = time.strftime('%H??? %M??? %S??? ', time.localtime(time.time()))

        answers = self.ans_gen.get_answers(q)
        for name, ans in answers:
            widget = AnsWidget(yymmdd + hhmmss, self.set_sentence(ans), name)
            self.ans_layout.addWidget(widget)

        #generator_name, ans = self.ans_gen.get_answer(q)
        #widget = AnsWidget(yymmdd+hhmmss, self.set_sentence(ans), generator_name)
        #self.ans_layout.addWidget(widget)
        self.tmp_q = q
        if not self.not_first:
            self.not_first = True

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

