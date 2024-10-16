import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox, QWidget
from HandTracking import start

class MainApp(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.initUI()


    def initUI(self):
        
        self.setWindowTitle("Güvenlik Sözleşmesi")
        self.setGeometry(150, 150, 600, 300)

       
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

       
        self.label = QLabel("Lütfen aşağıdaki güvenlik sözleşmesini okuyun ve kabul edin:")
        self.layout.addWidget(self.label)

         
        self.contractText = QLabel("""
Bu yazılımı kullanarak, X platformunda el hareketleri ile gezinebilir ve çeşitli işlemleri gerçekleştirebilirsiniz. 
Ancak, yazılımın kullanımı sırasında meydana gelebilecek herhangi bir yanlış işlem veya hatadan doğacak sorumluluk tamamen kullanıcıya aittir.
Kullanıcı, yazılımı kullanmadan önce tüm talimatları dikkatlice okumalı ve kullanım sırasında gerekli özeni göstermelidir.
Yazılımın kullanımı ile ilgili olarak oluşabilecek herhangi bir veri kaybı, hesap erişim sorunları veya diğer olumsuz durumlarda yazılım geliştiricileri sorumlu tutulamaz.
                                   """)
        self.contractText.setWordWrap(True)
        self.layout.addWidget(self.contractText)

        
        self.checkbox = QCheckBox("Güvenlik sözleşmesini kabul ediyorum")
        self.layout.addWidget(self.checkbox)
 
        self.acceptButton = QPushButton("Kabul Et ve Devam Et")
        self.acceptButton.setEnabled(False)
        self.layout.addWidget(self.acceptButton)

         
        self.checkbox.stateChanged.connect(self.toggleAcceptButton)
 
        self.acceptButton.clicked.connect(self.startProgram)


    def toggleAcceptButton(self):
        if self.checkbox.isChecked():
            self.acceptButton.setEnabled(True)
        else:
            self.acceptButton.setEnabled(False)


    def startProgram(self):
        if self.checkbox.isChecked():
            QMessageBox.information(self, "Onaylandı", "Program başlatılıyor...")
            start()
        else:
            QMessageBox.warning(self, "Uyarı", "Güvenlik sözleşmesini kabul etmelisiniz.")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()