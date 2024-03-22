import markdown
import pypandoc
from ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys
import os

def BabyMode():
    os.system("pip3 install pypandoc_binary")
    os.system("pip3 install PySide6")
    os.system("pip3 install markdown")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdopener.clicked.connect(self.opener)
        self.ui.transform.clicked.connect(self.trans)
        self.ui.trword.clicked.connect(self.tr2word)
        
    def opener(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "打开Markdown文件", ".", "*")
        self.file = filePath
        
    def trans(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            html = markdown.markdown(f.read())
        with open(self.file+".html","w") as f1:
            f1.write(html)
        QMessageBox.information(self, "完成！", "完成", QMessageBox.Ok)
    
    def tr2word(self):
        pypandoc.convert_file(self.file, 'docx', 'md', outputfile=self.file+'.docx')
        QMessageBox.information(self, "完成！", "完成", QMessageBox.Ok)
    
    def tr2pdf(self):
        pypandoc.convert_file(self.file, 'docx', 'pdf', outputfile=self.file+'.pdf')
        QMessageBox.information(self, "完成！", "完成", QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())