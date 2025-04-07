

# 📘 schedules-ag

**Genetic Algorithm for Optimal Course Scheduling**

This project implements a **Genetic Algorithm (GA)** to select the optimal combination of courses based on time constraints. The goal is to maximize academic utilization within a predefined weekly hour limit.

---

## 🚀 Features

* Binary chromosome representation of courses.
* Fitness function to evaluate time efficiency.
* Parent selection using roulette or tournament method.
* Crossover and mutation operations for genetic variation.
* Detailed output of each generation’s evolution.
* Displays either the exact or the best found solution.

---

## 🧠 How It Works

The genetic algorithm follows these steps:

1. **Initialization:** A random population of possible course combinations is created.
2. **Evaluation:** Each chromosome is evaluated based on total hours and how well it fits within the time constraint.
3. **Selection:** The best-performing individuals are selected as parents.
4. **Crossover:** Parents are combined to produce new offspring.
5. **Mutation:** Random changes are applied to maintain genetic diversity.
6. **Replacement:** The new generation replaces the old one.
7. **Termination:** Stops when an exact solution is found or the generation limit is reached.

---

## 🛠️ Requirements

* Python 3.7+
* No external libraries required (only uses Python's built-in `random` module)

---

## ✅ Example Output

```
✅✅ Exact solution found in generation 6

🧑‍🏫 Selected courses (14 hours):
 - History: 3h
 - English: 3h
 - Programming: 5h
 - Algorithms: 3h
```

---

## 🔧 Possible Improvements

* Allow for customizable constraints (e.g. available days, mandatory courses)
* GUI to visualize and interact with the schedule
* Export results to PDF or Excel

---

## 👨‍💻 Authors

* **Max Saavedra** – *Software Engineering Student*

  📧 [max.saavedra@unmsm.edu.pe](mailto:max.saavedra@unmsm.edu.pe)
* **Jorge Ipanaque** – *Software Engineering Student*

  📧 [jorge.ipanaque@unmsm.edu.pe](mailto:jorge.ipanaque@unmsm.edu.pe)
* **Fabricio Chuquispuma** – *Software Engineering Student*

  📧 [fabricio.chuquispuma@unmsm.edu.pe](mailto:fabricio.chuquispuma@unmsm.edu.pe)
* **Josue Espinoza** – *Software Engineering Student*

  📧 [josue.espinoza@unmsm.edu.pe](mailto:josue.espinoza@unmsm.edu.pe)
* **Geomar Fernandez** – *Software Engineering Student*

  📧 [geomar.fernandez@unmsm.edu.pe](mailto:geomar.fernandez@unmsm.edu.pe)
