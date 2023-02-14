from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineDownloadRequest
from PySide6.QtCore import QUrl, QFile
from PySide6.QtWidgets import QApplication, QFileDialog
import sys


def callback_function(html):
    print(html)


def on_load_finished():
    print(w.page().runJavaScript("document.documentElement.outerHTML", callback_function))

    
    
app = QApplication(sys.argv)

w = QWebEngineView()
w.load(QUrl("https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&productName=Blue-Eyes+White+Dragon&view=grid"))
# print(w.page().download(QUrl("https://geneni.info"), "test.py"))
# w.loadFinished.connect(on_load_finished())
# w.page().download(QUrl("https://google.com"), QString("tetx.html"))
def save_file():
    filename, _ = QFileDialog.getSaveFileName()

    if filename:
        def write_html_to_file(html):
            with open(filename, 'w') as f:
                f.write(html)

        w.page().toHtml(write_html_to_file)
# print(pagehtml.toString())
save_file()
w.show()

app.exec()
