import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QLabel, QListWidget, QMessageBox
)
from models import (
    get_all_mahasiswa, add_mahasiswa_db, delete_mahasiswa_db,
    update_mahasiswa_db, get_mahasiswa_by_id
)

class MahasiswaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Manajemen Mahasiswa")
        self.setGeometry(100, 100, 400, 400)

        self.list_widget = QListWidget()
        self.nama_input = QLineEdit()
        self.nim_input = QLineEdit()
        self.id_label = QLabel("")

        self.add_button = QPushButton("Tambah")
        self.update_button = QPushButton("Update")
        self.delete_button = QPushButton("Hapus")
        self.load_button = QPushButton("Refresh")

        layout = QVBoxLayout()
        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Nama"))
        form_layout.addWidget(self.nama_input)
        form_layout.addWidget(QLabel("NIM"))
        form_layout.addWidget(self.nim_input)

    def add_mahasiswa(self):
        nama = self.nama_input.text()
        nim = self.nim_input.text()
        if not nama or not nim:
            QMessageBox.warning(self, "Peringatan", "Nama dan NIM tidak boleh kosong.")
            return

        if add_mahasiswa_db(nama, nim):
            QMessageBox.information(self, "Sukses", "Mahasiswa ditambahkan.")
            self.load_data()
        else:
            QMessageBox.warning(self, "Gagal", "NIM sudah ada atau input tidak valid.")

    def update_mahasiswa(self):
        if not self.id_label.text():
            QMessageBox.warning(self, "Error", "Pilih mahasiswa terlebih dahulu.")
            return

        mahasiswa_id = int(self.id_label.text())
        nama = self.nama_input.text()
        nim = self.nim_input.text()

        if update_mahasiswa_db(mahasiswa_id, nama, nim):
            QMessageBox.information(self, "Sukses", "Data mahasiswa diperbarui.")
            self.load_data()
        else:
            QMessageBox.warning(self, "Gagal", "Gagal memperbarui data.")

    def delete_mahasiswa(self):
        if not self.id_label.text():
            QMessageBox.warning(self, "Error", "Pilih mahasiswa terlebih dahulu.")
            return

        mahasiswa_id = int(self.id_label.text())
        delete_mahasiswa_db(mahasiswa_id)
        QMessageBox.information(self, "Sukses", "Mahasiswa dihapus.")
        self.nama_input.clear()
        self.nim_input.clear()
        self.id_label.clear()
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MahasiswaApp()
    window.show()
    sys.exit(app.exec_())