
class Automata():
    
    # Constructor de la clase con parámetros
    def __init__(self,alphabet, transitionsTable, initialState, finalState):
        self.alphabet = alphabet ;
        self.transitionsTable = transitionsTable;
        self.initialState = initialState;
        self.finalState = finalState;
        
    # Constructor de la clase sin parámetros        
    def __init__(self):
        self.alphabet = ['0', '4', 'J', '9', 'A', '6', 'M', 'T', 'N', '2', 'V', 'B', 'L', 'D', 'U', '3', 'C', '5', '1', '8', 'X', 'S'];
        self.transitionsTable = [
            ["q0", "B", "q1"],
            ["q1", "A", "q2"],
            ["q2", "L", "q4"],
            ["q4", "0", "q5"],
            ["q5", "3", "q11"],            
            ["q1", "C", "q3"],
            ["q3", "C", "q8"],
            ["q8", "1", "q10"],
            ["q10", "4", "q11"],
            ["q11", "0", "q12"],
            ["q3", "D", "q9"],
            ["q9", "0", "q13"],
            ["q13", "8", "q14"],
            ["q14", "6", "q15"],
            ["q0", "D", "q6"],
            ["q6", "B", "q7"],
            ["q7", "5", "q11"],
            ["q0", "S", "q16"],
            ["q16", "0", "q17"],
            ["q17", "J", "q18"],
            ["q18", "1", "q19"],
            ["q19", "3", "q20"],
            ["q20", "8", "q21"],
            ["q0", "T", "q22"],
            ["q22", "M", "q23"],
            ["q23", "2", "q24"],
            ["q24", "3", "q25"],
            ["q25", "0", "q26"],
            ["q26", "3", "q27"],
            ["q27", "0", "q28"],
            ["q28", "1", "q20"],
            ["q0", "N", "q29"],
            ["q29", "3", "q30"],
            ["q30", "C", "q31"],
            ["q31", "9", "q32"],
            ["q32", "6", "q33"],
            ["q33", "4", "q34"],
            ["q0", "X", "q35"],
            ["q35", "2", "q36"],
            ["q36", "5", "q37"],
            ["q37", "4", "q38"],
            ["q38", "3", "q39"],
            ["q39", "V", "q40"],
            ["q0", "A", "q41"],
            ["q41", "U", "q42"],
            ["q42", "2", "q43"],
            ["q43", "8", "q38"],            
            ["q39", "3", "q46"],
        ];
        self.initialState = "q0";
        self.finalStates = ["q12", "q15", "q21", "q34", "q40", "q46"];  
        self.route = [];              
        
    # Valida la si la entrada cumple con el automata
    def validateInput(self, text): 
            
        currentState = self.initialState;

        for letter in text:
            foundTransition = False;
            for transition in self.transitionsTable:
                if transition[0] == currentState and transition[1] == letter:                    
                    self.route.append(currentState);
                    self.route.append(letter);
                    currentState = transition[2];
                    foundTransition = True;
                    break;
            
            if not foundTransition:                            
                return False;  # No se encontró ninguna transición para el símbolo actual   
            else:
                self.route.append(currentState);                  
                          
        self.route.append(currentState);      
        return currentState in self.finalStates;
    
    def getRoute(self):
        
        route = self.route
        
        stringRoute = "";
        for i in range(0, len(route)):
            try:
                if(i % 3 == 0):
                    stringRoute = stringRoute + route[i] + " = " + route[i + 1] + " => " + route[i + 2] + ", "
            except:
                break                 
        
        return stringRoute[:-2];