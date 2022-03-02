from PySide2 import QtWidgets, QtCore


class OdbijDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Odbij porudzbinu")
        self.vbox_layout = QtWidgets.QVBoxLayout()
        self.form_layout = QtWidgets.QFormLayout()
        self.inputNapomena = QtWidgets.QPlainTextEdit(self)
        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok
                                                     | QtWidgets.QDialogButtonBox.Cancel, parent=self)
        self.form_layout.addRow("Napomena za odbijanje :", self.inputNapomena)

        self.vbox_layout.addLayout(self.form_layout)
        self.vbox_layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.setLayout(self.vbox_layout)

    def get_napomena(self):

        return self.inputNapomena.toPlainText()
