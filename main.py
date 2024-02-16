"""
    Universidad del Valle de Guatemala
    Análisis de Algoritmos
    Profesor: Paulo Mejía

    Proyecto 1: Máquina de Turing - Secuencia de Fibonacci
    Descripción: Implementación de una máquina de Turing que devuelve el valor de la secuencia de Fibonacci dependiendo del valor ingresado.
    Integrantes:
        - Abner Iván García Alegría - 21285
        - Oscar Esteban Donis Martínez - 21610
        - Astrid Marie Glauser Oliva - 21299
        - Gonzalo Enrique Santizo vega - 21504
        - Jose Daniel Gomez Cabrera - 21429
"""

def read_file():
    # Variables para guardar los datos del archivo
    estados = []
    alfabeto_entrada = []
    alfabeto_cinta = []
    func_transition = {}
    estado_inicial = ""
    sim_blanco = ""
    estados_aceptacion = []

    # Abrir el archivo
    with open('machine.txt', 'r') as file:
        contador = 0

        # Leer el archivo linea por linea
        for line in file:

            # En caso sea las reglas de la función de transición
            if "=" not in line:
                # Eliminar los espacios en blanco y los paréntesis
                line = line.strip().replace('(', '').replace(')', '').replace(' ', '')
                value = [tuple(filter(None, v.split(','))) for v in line.split('->')]
                try:
                    func_transition[value[0]] = value[1]
                except IndexError:
                    print()
                continue

            # En caso contrario, leer la variable y el valor
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()

            if '{' in value and '}' in value:
                value = value.replace('{', '').replace('}', '').replace(' ', '')
                value = value.split(',')

            # Dependiendo de la variable guardamos los datos
            if key == "ESTADOS":
                estados = value
            elif key == "ALFABETO DE ENTRADA":
                alfabeto_entrada = value
            elif key == "ALFABETO DE CINTA":
                alfabeto_cinta = value
            elif key == "ESTADO INICIAL":
                estado_inicial = value
            elif key == "SIMBOLO BLANCO":
                sim_blanco = value
            elif key == "ESTADOS FINALES":
                estados_aceptacion = value

            contador += 1

    return estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion


def maquina_turing(estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion, w, starter):

    # Definimos la posición inicial en la cinta
    input_actual = starter
    flag = False
    print("Transiciones:")
    b = w.copy()
    b[input_actual-1] = ''.join([c + '\u0332' for c in b[input_actual - 1]])
    print(''.join(b))
    print()

    # Mientras no lleguemos al inicio de la cinta, seguimos iterando
    while input_actual != 0 and input_actual != len(w) - 1:
        # Si el estado actual es un estado de aceptación, entonces la cadena es un palíndromo
        if estado_inicial in estados_aceptacion:
            flag = True
            break
        # Si por caso contrario el estado actual no se encuentra en los estados de aceptación, entonces seguimos moviendono en las reglas de la función de transición
        else:
            # Obtenemos la transición
            transition = func_transition[(estado_inicial, w[input_actual])]
            # Imprimimos la transición
            print("(" + estado_inicial + ", " + w[input_actual] + ")","->", transition)
            # Actualizamos el estado actual y el valor de la cinta
            estado_inicial = transition[0]
            w[input_actual] = transition[1]
            # Actualizamos la posición en la cinta
            if transition[2] == "R":
                input_actual += 1
            else:
                input_actual -= 1
            # Imprimimos la cinta
            a = w.copy()
            a[input_actual - 1] = '\n'.join(['('+ c + ')' for c in a[input_actual - 1]])
            print(''.join(a))
            print()

    # Imprimimos valores de salida
    print()
    print("Estado final:", estado_inicial)
    print("Cadena final:")
    print(''.join(w))
    contador = 0
    for i in range(len(w)):
        if w[i] == '|':
            contador += 1

    print("Su número en la secuencia de Fibonacci es:", contador)



def main():
    # Leemos los datos del archivo
    estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion = read_file()

    # Definimos la secuencia de Fibonacci como entrada
    input_sequence = int(input("Ingrese el numero a averiguar en la secuencia de Fibonacci: "))
    numCinta = ""
    i = 0
    while i < input_sequence:
        numCinta += '|'
        i += 1
    # Convertimos la entrada en una cinta con un número definido de blanks
    blank_number = 50
    w = list(sim_blanco * blank_number + numCinta + sim_blanco * (blank_number*4))

    # Le pasamos los datos de la máquina de turing a la función para ejecutarla
    maquina_turing(estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion, w, blank_number)
    print("Número ingresado: ", input_sequence)

main()
