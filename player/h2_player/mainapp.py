import sys

from PySide2.QtWidgets import QApplication

from h2_player.ui.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

