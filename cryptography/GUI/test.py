from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
combo = QComboBox()
combo.addItem("AES")
combo.addItem("DES")
combo.addItem("RSA")
combo.addItem("MD5")
combo.addItem("SHA1s")
layout.addWidget(combo)

window.setLayout(layout)
window.show()
app.exec_()