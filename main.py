from controller import *



def main():
    app = QApplication([])
    Window = Controller()
    Window.show()
    app.exec_()

if __name__ == "__main__":
    main()