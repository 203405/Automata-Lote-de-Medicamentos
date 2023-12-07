from views.main import Ui_MainWindow as windowsMain
from PyQt5.QtWidgets import QMessageBox
from models.Automata import Automata;
from colorama import Fore, Style
from PyQt5 import QtWidgets

class appPrincipal(QtWidgets.QMainWindow, windowsMain):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self);
        windowsMain.__init__(self);
        self.setupUi(self);
        
        self.setFixedSize(620, 528);
        self.input.setFocus();
        self.validated.clicked.connect(self.startProcess);
        self.cancel.clicked.connect(self.cancelEverything);
        
    def startProcess(self):
        
        # Obtenemos el texto del input
        text = self.input.toPlainText();

        if not self.validateInput(text) : return;

        # Instancia de la clase Automata
        automata = Automata();

        # Verificar si la cadena es aceptada por el autómata
        value = automata.validateInput(text);
        
        route = automata.getRoute();
        
        if value:
            print(Fore.GREEN + f"La cadena '{text}' es aceptada por el autómata.");
            self.result.setText(f"La cadena '{text}'\nes aceptada por el autómata.");
            self.result.setStyleSheet("color: green;  border: 1px solid green;");
        else:    
            print(Fore.RED + f"La cadena '{text}' no es aceptada por el autómata.");
            self.result.setText(f"La cadena '{text}'\nno es aceptada por el autómata.");
            self.result.setStyleSheet("color: red; border: 1px solid red;");
        print(Style.RESET_ALL, end="");  
        
        print(route);  
        self.lblRoute.setText(route);
        self.input.setFocus();
        
    def validateInput(self, text):
        
        if(len(text) == 0):            
            message = QMessageBox();
            message.setWindowTitle("¡Atención!");
            message.setText("No has escrito nada para validar.");
            message.setIcon(QMessageBox.Warning);
            message.addButton(QMessageBox.Ok);
            message.exec_();
            
            self.input.setFocus();            
            return False;        
        else:            
            return True;
        
    def cancelEverything(self):
        self.result.setText("");
        self.input.setText("");
        self.lblRoute.setText("");
        self.result.setStyleSheet("color: rgb(0, 0, 0); border: 1px solid rgb(52, 165, 201);");
        self.input.setFocus();    