import sys;
from PyQt5 import QtWidgets;
from controllers.main import appPrincipal;

if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv);
    window = appPrincipal();
    window.show();
    app.exec_();
