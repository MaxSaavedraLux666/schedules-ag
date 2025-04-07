""" Algoritmo Genético para seleccionar cursos
    - Autor: Grupo 2"""

import random

# Lista de cursos disponibles (nombre, horas)
cursos = [
    ("Matemáticas", 3),
    ("Física", 4),
    ("Química", 3),
    ("Biología", 3),
    ("Historia", 3),
    ("Inglés", 3),
    ("Literatura", 3),
    ("Programación", 5),
    ("IA", 4),
    ("Algoritmos", 3),
]

# Objetivo de horas
HORAS_OBJETIVO = 14

# =====================
# 1. Inicialización - Max
# =====================
def inicializar_poblacion(tamano_poblacion, longitud_cromosoma):
    """
    Genera una población inicial aleatoria de cromosomas para el algoritmo genético.

    Cada cromosoma está representado por una lista binaria de 0s y 1s,
    donde cada valor indica si un curso ha sido seleccionado (1) o no (0).
    Esta codificación permite simular decisiones de selección de cursos.

    Args:
        tamano_poblacion (int): Cantidad de individuos (cromosomas) que tendrá la población inicial.
        longitud_cromosoma (int): Número de genes por cromosoma, correspondiente al total de cursos disponibles.

    Returns:
        list[list[int]]: Una lista de cromosomas. Cada cromosoma es una lista binaria de longitud igual a `longitud_cromosoma`.

    Ejemplo:
        Supongamos que hay 4 cursos (longitud_cromosoma = 4), y se desea una población de 3 cromosomas:
        >>> inicializar_poblacion(3, 4)
        [[1, 0, 1, 0],
         [0, 1, 1, 1],
         [1, 1, 0, 0]]
    """
    poblacion = []
    for _ in range(tamano_poblacion):
        cromosoma = [random.randint(0, 1) for _ in range(longitud_cromosoma)]
        poblacion.append(cromosoma)
    return poblacion


# 2. Evaluación - Jorge
# =====================
def evaluar(cromosoma, cursos):
    """
    Evalúa un cromosoma calculando su aptitud según el total de horas seleccionadas,
    comparado con el objetivo de horas (HORAS_OBJETIVO). Si el total excede el objetivo,
    se aplica una penalización.

    Args:
        cromosoma (list[int]): Lista binaria indicando los cursos seleccionados.
        cursos (list[tuple]): Lista de cursos con sus horas.

    Returns:
        float: Valor de aptitud. 0 si se excede el objetivo, o inversamente proporcional
               a la diferencia entre el total de horas y el objetivo.

    Ejemplo:
        Si HORAS_OBJETIVO = 14 y cursos = [("Matemáticas", 5), ("Historia", 3), ("Física", 4), ("Arte", 2), ("Programación", 6)],
        y cromosoma = [1, 0, 1, 1, 0], el total es 11, la diferencia es 3, y la aptitud será 1 / (1 + 3) = 0.25.
    """
    total = sum(cursos[i][1] for i in range(len(cromosoma)) if cromosoma[i] == 1)
    diferencia = abs(HORAS_OBJETIVO - total)
    if total > HORAS_OBJETIVO:
        return 0
    return 1 / (1 + diferencia)

# =====================
# 3. Selección - Fabricio
# =====================
def seleccion(poblacion, cursos):
    """
    Selecciona un individuo (cromosoma) de la población para ser padre utilizando el método de selección por torneo 
    (tamaño de torneo = 2). Se eligen aleatoriamente dos individuos distintos de la población actual. Se calcula la aptitud 
    (fitness) de ambos utilizando la función `evaluar`. El individuo con la mayor aptitud es seleccionado como el "ganador" del
    torneo y se devuelve para ser utilizado en la fase de cruce como padre.

    Args:
        poblacion (list[list[int]]): La lista de cromosomas (individuos) que componen la población actual.
        cursos (list[tuple]): La lista de cursos disponibles con sus horas.Es necesaria para poder llamar a 
                            la función `evaluar` y calcular la aptitud de los individuos del torneo.

    Returns:
        list[int]: El cromosoma seleccionado (el 'ganador' del torneo) que será utilizado como padre en la 
                   siguiente generación. En caso de empate en la aptitud, se devuelve el segundo individuo del torneo.
    """
    torneo = random.sample(poblacion, 2)
    fitnesses = [evaluar(ind, cursos) for ind in torneo]
    return torneo[0] if fitnesses[0] > fitnesses[1] else torneo[1]

# =====================
# 4. Cruce - Josue
# =====================
def cruce(padre1, padre2):
    """
    Realiza el cruce (crossover) entre dos cromosomas padres para generar dos nuevos cromosomas hijos.

    Este cruce se realiza mediante un punto de corte aleatorio. Los genes del primer hijo son tomados
    desde el inicio de `padre1` hasta el punto de cruce, y desde el punto de cruce hasta el final de `padre2`.
    Para el segundo hijo, se invierte el orden de los padres.

    Args:
        padre1 (list[int]): Cromosoma padre representado como lista de 0s y 1s.
        padre2 (list[int]): Otro cromosoma padre de la misma longitud.

    Returns:
        tuple[list[int], list[int]]: Una tupla con dos listas binarias, que representan los cromosomas hijos generados.

    Ejemplo:
        >>> padre1 = [1, 0, 1, 0]
        >>> padre2 = [0, 1, 0, 1]
        >>> cruce(padre1, padre2)
        ([1, 0, 0, 1], [0, 1, 1, 0])
    """
    punto = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2


# =====================
# 5. Mutación - Willy
# =====================
def mutacion(cromosoma, tasa=0.1):
    """_summary_

    Args:
        cromosoma (_type_): _description_
        tasa (float, optional): _description_. Defaults to 0.1.

    Returns:
        _type_: _description_
    """
    return [1 - gen if random.random() < tasa else gen for gen in cromosoma]

# =====================
# Decodificación final
# =====================
def decodificar(cromosoma, cursos):
    """_summary_

    Args:
        cromosoma (_type_): _description_
        cursos (_type_): _description_

    Returns:
        _type_: _description_
    """
    return [cursos[i] for i in range(len(cromosoma)) if cromosoma[i] == 1]


# =====================
# Algoritmo Genético Principal
# =====================
def algoritmo_genetico():
    """"_Algoritmo Genético para seleccionar cursos """
    tamano_poblacion = 20
    generaciones = 100
    longitud = len(cursos)

    poblacion = inicializar_poblacion(tamano_poblacion, longitud)
    print("🔄 Población Inicial:")
    for idx, crom in enumerate(poblacion):
        print(
            f"  Individuo {idx + 1}: {crom} - Fitness: {evaluar(crom, cursos):.2f}")
    print("="*50)

    for gen in range(generaciones):
        print(f"\n🧬 Generación {gen + 1}")
        nueva_poblacion = []

        for i in range(tamano_poblacion // 2):
            print(f"\n🔗 Selección de padres ({i+1}):")
            padre1 = seleccion(poblacion, cursos)
            padre2 = seleccion(poblacion, cursos)
            print(f" - Padre 1: {padre1}")
            print(f" - Padre 2: {padre2}")

            hijo1, hijo2 = cruce(padre1, padre2)
            print(f" 🧪 Cruce → Hijo 1: {hijo1}, Hijo 2: {hijo2}")

            hijo1 = mutacion(hijo1)
            hijo2 = mutacion(hijo2)
            print(f" 🔀 Mutación → Hijo 1: {hijo1}, Hijo 2: {hijo2}")

            fitness1 = evaluar(hijo1, cursos)
            fitness2 = evaluar(hijo2, cursos)
            print(f" ✅ Fitness → H1: {fitness1:.2f}, H2: {fitness2:.2f}")

            nueva_poblacion.extend([hijo1, hijo2])

        poblacion = nueva_poblacion

        # Verificar si hay solución perfecta
        for crom in poblacion:
            if evaluar(crom, cursos) == 1:
                print(
                    f"\n✅✅ Solución exacta encontrada en generación {gen + 1}")
                print(f"🧬 Cromosoma seleccionado: {crom}")  # <-- esta línea imprime el cromosoma
                seleccionados = decodificar(crom, cursos)
                imprimir_resultado(seleccionados)
                return

    # Si no se encuentra exacta, mostrar la mejor
    mejor = max(poblacion, key=lambda c: evaluar(c, cursos))
    seleccionados = decodificar(mejor, cursos)
    print("\n⚠️ No se encontró una solución exacta, pero esta es la mejor encontrada:")
    imprimir_resultado(seleccionados)


def imprimir_resultado(lista_cursos):
    """
    Imprime los cursos seleccionados junto con el total de horas.

    Args:
        lista_cursos (list of tuples): Lista de cursos seleccionados.
            Cada elemento es una tupla en el formato (nombre_curso, horas).

    Salida:
        Muestra en consola los cursos seleccionados y la suma total de horas.
    """
    total = sum(h for _, h in lista_cursos)
    print(f"\n🧑‍🏫 Cursos seleccionados ({total} horas):")
    for nombre, horas in lista_cursos:
        print(f" - {nombre}: {horas}h")



# =====================
# Ejecutar algoritmo
# =====================
if __name__ == "__main__":
    print("👨‍🏫 Algoritmo Genético para Selección de Cursos")
    print("="*50)
    print("Cursos disponibles:")
    # Imprimir cursos disponibles
    algoritmo_genetico() # Imprimir cursos disponibles