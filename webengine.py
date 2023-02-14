from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineDownloadRequest
from PySide6.QtCore import QUrl, QFile
from PySide6.QtWidgets import QApplication, QFileDialog
import sys

    
    
app = QApplication(sys.argv)

w = QWebEngineView()
w.load(QUrl("https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&productName=Blue-Eyes+White+Dragon&view=grid"))
# print(w.page().download(QUrl("https://geneni.info"), "test.py"))
# w.loadFinished.connect(on_load_finished())
# w.page().download(QUrl("https://google.com"), QString("tetx.html"))

def getresponse(html):
    
    with open("test3.html", 'w') as f:
        f.write(html)
        
    # print(html)

def save_file():
    # w.page().runJavaScript("document.getElementsByTagName('html')[0].innerHTML", 0, getresponse)
    w.page().toHtml(getresponse)
# print(pagehtml.toString())e

w.loadFinished.connect(save_file)
# save_file()
w.show()

app.exec()
