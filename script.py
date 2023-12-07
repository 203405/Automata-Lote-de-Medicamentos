class Automata:
    def __init__(self):
        # Definir el alfabeto
        self.alphabet = ['D', 'B', 'C', '0', '1', '4', '5']

        # Definir las transiciones en forma de un diccionario
        self.transitions = {
            'q0': {'D': 'q1', 'B': 'q3'},
            'q1': {'0': 'q4', '1': 'q4', '4': 'q4', '5': 'q4'},
            'q3': {'C': 'q5'},
            'q4': {'0': 'q8', '1': 'q8', '4': 'q8', '5': 'q8'},
            'q5': {'1': 'q6'},
            'q6': {'4': 'q7'},
            'q7': {'0': 'q8'},
            'q8': {}  # Estado final, sin transiciones salientes
        }

        # Definir los estados finales
        self.final_states = ['q8']

        # Estado inicial
        self.initial_state = 'q0'

    def validate_input(self, text):
        current_state = self.initial_state

        for char in text:
            # Verificar si el carácter está en el alfabeto
            if char not in self.alphabet:
                return False

            # Verificar si hay una transición válida desde el estado actual
            if char in self.transitions[current_state]:
                current_state = self.transitions[current_state][char]
            else:
                return False

        # Verificar si el estado actual es un estado final
        if current_state in self.final_states:
            return True
        else:
            return False

# Ejemplo de uso
if __name__ == "__main__":
    automaton = Automata()

    input_string1 = "DB50"
    input_string2 = "BCC140"

    if automaton.validate_input(input_string1):
        print(f'La cadena "{input_string1}" es aceptada por el autómata.')
    else:
        print(f'La cadena "{input_string1}" no es aceptada por el autómata.')

    if automaton.validate_input(input_string2):
        print(f'La cadena "{input_string2}" es aceptada por el autómata.')
    else:
        print(f'La cadena "{input_string2}" no es aceptada por el autómata.')
