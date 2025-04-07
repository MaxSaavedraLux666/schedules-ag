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
    """_summary_

    Args:
        cromosoma (_type_): _description_
        cursos (_type_): _description_

    Returns:
        _type_: _description_
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
    """_summary_

    Args:
        poblacion (_type_): _description_
        cursos (_type_): _description_

    Returns:
        _type_: _description_
    """
    torneo = random.sample(poblacion, 2)
    fitnesses = [evaluar(ind, cursos) for ind in torneo]
    return torneo[0] if fitnesses[0] > fitnesses[1] else torneo[1]

# =====================
# 4. Cruce - Josue
# =====================
def cruce(padre1, padre2):
    """_summary_

    Args:
        padre1 (_type_): _description_
        padre2 (_type_): _description_

    Returns:
        _type_: _description_
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