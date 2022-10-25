## Ex 5-20. QTextEdit.
from model.load_kobert import DialogKoBERT
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout
from model.load_kogpt2 import answer_generator
import string


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.kobert = DialogKoBERT()
        self.kogpt2 = answer_generator()

    def initUI(self):

        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.te.setPlaceholderText("내용을 입력해주세요")

        self.ans_btn = QPushButton(self)
        self.ans_btn.setText('    ')
        self.ans_btn.setEnabled(False)

        self.btn = QPushButton(self)
        self.btn.setText('완료')
        self.btn.clicked.connect(self.set_text)

        self.ans_te = QTextEdit()
        self.ans_te.setAcceptRichText(False)
        self.ans_te.setPlaceholderText("    ")
        self.ans_te.setEnabled(False)

        # self.ans_btn.setVisible(False)
        # self.ans_te.setVisible(False)

        hbox = QHBoxLayout()
        hbox.addWidget(self.ans_btn)
        hbox.addWidget(self.btn)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te)
        vbox.addLayout(hbox)
        vbox.addWidget(self.ans_te)
        self.setLayout(vbox)

        self.setWindowTitle('With U')
        self.setGeometry(300, 300, 400, 500)
        self.show()

    def get_answer(self):
        self.ans_btn.setVisible(True)
        self.ans_te.setVisible(True)
        
    def trim_text(self, text):
        sentence_count = 0
        last = -1
        for idx, char in enumerate(text):
            if char in string.punctuation:
                if char == ',':
                    continue
                last = idx
                sentence_count += 1
                if sentence_count == 1:
                    break
        return text[:last + 1]

    def set_text(self):
        text = self.te.toPlainText()
        self.ans_btn.setText(self.kobert.predict(text))
        
        result = self.kogpt2.get_answer(text)
        self.ans_te.setPlaceholderText(self.trim_text(result))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())