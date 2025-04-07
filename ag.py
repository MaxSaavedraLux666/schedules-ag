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

# =====================
# 2. Evaluación - Jorge
# =====================
def evaluar(cromosoma, cursos):
    total = sum(cursos[i][1] for i in range(len(cromosoma)) if cromosoma[i] == 1)
    diferencia = abs(HORAS_OBJETIVO - total)
    if total > HORAS_OBJETIVO:
        return 0
    return 1 / (1 + diferencia)

# =====================
# Ejecutar algoritmo
# =====================
# algoritmo_genetico()
