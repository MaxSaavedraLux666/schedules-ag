import random

# Lista de cursos disponibles (nombre, horas)
cursos = [
    ("Matemáticas", 3),
    ("Física", 4),
    ("Química", 2),
    ("Biología", 3),
    ("Historia", 2),
    ("Inglés", 3),
    ("Literatura", 2),
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
    poblacion = []
    for _ in range(tamano_poblacion):
        cromosoma = [random.randint(0, 1) for _ in range(longitud_cromosoma)]
        poblacion.append(cromosoma)
    return poblacion

# 2. Evaluación - Jorge
# =====================
def evaluar(cromosoma, cursos):
    total = sum(cursos[i][1] for i in range(len(cromosoma)) if cromosoma[i] == 1)
    diferencia = abs(HORAS_OBJETIVO - total)
    if total > HORAS_OBJETIVO:
        return 0
    return 1 / (1 + diferencia)

# =====================
# 4. Cruce - Josue
# =====================
def cruce(padre1, padre2):
    punto = random.randint(1, len(padre1) - 1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2


# =====================
# 5. Mutación - Willy
# =====================
def mutacion(cromosoma, tasa=0.1):
    return [1 - gen if random.random() < tasa else gen for gen in cromosoma]

# =====================
# Decodificación final
# =====================
def decodificar(cromosoma, cursos):
    return [cursos[i] for i in range(len(cromosoma)) if cromosoma[i] == 1]


# =====================
# Ejecutar algoritmo
# =====================
# algoritmo_genetico()
