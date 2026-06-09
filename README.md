# 💻 Python Object-Oriented Programming (OOP) Portfolio

**Author:** Anjum Saeed  
**Language:** Python 3.x  
**License:** MIT  

Welcome to my Python engineering portfolio. This repository contains a collection of terminal-based software applications developed to demonstrate Object-Oriented Programming (OOP) concepts, including controller classes, state mutation, parallel data structures, and terminal-based logic modeling.

---

## 📂 Featured Projects

### 1. Multi-Agent Turn-Based RPG Arena Engine
A terminal-based combat simulation engine built using OOP. It features independent character objects passed into a centralized controller to manage a combat loop.

* **Core Concepts Demonstrated:**
  * **Object Instantiation:** Generating distinct `Player` objects with unique starting parameters.
  * **Controller Classes:** Using a `Battle` class to accept player objects and manage the interaction between them.
  * **State Mutation:** Dynamically altering internal variables (Health) based on calculated attack and defense logic loops.

### 2. Digital Library Inventory System
A CLI-based inventory tracker that utilizes a central library class to manage and mutate parallel data lists securely. 

* **Core Concepts Demonstrated:**
  * **Parallel Data Structures:** Synchronizing multiple arrays (titles, authors, availability) to act as a unified database.
  * **Logic Modeling & Safety:** Using custom class methods to prevent conflicting data mutations (e.g., stopping a user from checking out a book that is already marked as unavailable).
  * **Interactive CLI Menu:** Building a continuous `while` loop interface for user-driven data querying.

### 3. Virtual Pet Shelter Simulator
A Tamagotchi-style simulation engine that runs a real-time terminal menu to manage the state degradation of multiple independent pets simultaneously.

* **Core Concepts Demonstrated:**
  * **Independent Object Encapsulation:** Generating multiple unique simulated entities from the same base `pet` class, guaranteeing isolated data tracking.
  * **Algorithmic State Degradation:** Implementing methods that actively decay variables (hunger, happiness) to simulate the passage of time.
  * **User-Driven Actions:** Updating object states based on targeted CLI menu selections.
---

## 🚀 How to Run Locally (Step-by-Step Guide)

**Prerequisite:** Ensure you have [Python 3.x](https://www.python.org/downloads/) installed on your machine. No external libraries are required.

**Step 1: Clone the repository** Open your terminal (Mac/Linux) or Command Prompt/Git Bash (Windows) and run:
```bash
git clone [https://github.com/Novaswashere/Software-and-Engineering-Projects.git](https://github.com/Novaswashere/Software-and-Engineering-Projects.git)
```
Step 2: Enter the master directory 
```bash
cd Software-and-Engineering-Projects
```

**Step 3: Enter the directory** You want to execute. For Example if we want to acess rpg-arena-engine we will run:
```bash
cd rpg-arena-engine
```
Alternatively, You may use: `cd digital-library-system` or `cd virtual-pet-simulator` 

**Step 4: Execute the application** Run the script using the Python command (Note: Use `python3` on macOS/Linux if `python` defaults to an older version):
```bash
python arena_engine.py
```
Alternatively, You may use: `python library_inventory.py` or `python pet_simulator.py`
