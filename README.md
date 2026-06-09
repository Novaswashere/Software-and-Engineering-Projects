# 💻 Python Object-Oriented Programming (OOP) Portfolio

**Author:** Anjum Saeed  
**Language:** Python 3.x  
**License:** MIT  

Welcome to my Python engineering portfolio. This repository contains a collection of terminal-based software applications developed to demonstrate advanced Object-Oriented Programming (OOP) concepts, including encapsulation, state mutation, multi-agent interactions, and data logic modeling.

---

## 📂 Featured Projects

### 1. Multi-Agent Turn-Based RPG Arena Engine
A fully automated combat simulation engine built using strict OOP principles. It features independent character agents that dynamically interact with one another within a terminal-logged combat loop.

* **Core Concepts Demonstrated:**
  * **Object Composition:** Passing object instances (target agents) into class methods to trigger interactions.
  * **State Mutation:** Dynamically altering internal variables (HP, Attack, Defense) based on randomized game logic and defense algorithms.
  * **Method Encapsulation:** Keeping combat math and critical-hit algorithms isolated within specific class behaviors.

### 2. Digital Library Inventory System
A backend terminal tracker that manages a central entity controlling an array of distinct, mutable objects. It prevents data conflicts and ensures logical state flow.

* **Core Concepts Demonstrated:**
  * **Data Architecture:** Managing an inventory array consisting of instantiated `Book` objects.
  * **Logic Modeling:** Preventing conflicting data mutations (e.g., stopping a user from checking out a book that is already marked as checked out).
  * **Centralized State Management:** Using a master `Library` class to view, filter, and interact with the child objects.

### 3. Virtual Pet Shelter Simulator
A Tamagotchi-style simulation engine that runs a real-time terminal menu to manage the state degradation of multiple independent entities simultaneously.

* **Core Concepts Demonstrated:**
  * **Independent Object Instantiation:** Generating multiple unique simulated entities from the same base class, guaranteeing isolated data encapsulation.
  * **Algorithmic State Degradation:** Implementing loops that actively decay variables (hunger, happiness) to simulate the passage of time.
  * **Batch Processing:** Iterating through object arrays to apply global actions (e.g., "Feed All").

---

## 🚀 How to Run Locally (Step-by-Step Guide)

**Prerequisite:** Ensure you have [Python 3.x](https://www.python.org/downloads/) installed on your machine. No external libraries are required.

**Step 1: Clone the repository** Open your terminal (Mac/Linux) or Command Prompt/Git Bash (Windows) and run:
```bash
git clone [https://github.com/Novaswashere/Software-and-Engineering-Projects.git](https://github.com/Novaswashere/Software-and-Engineering-Projects.git)
```
Step 2: Enter the master directory 
```bash
python Software-and-Engineering-Projects
```
**Step 3: Execute the application** Run the script using the Python command (Note: Use `python3` on macOS/Linux if `python` defaults to an older version):
```bash
python arena_engine.py
```
Alternatively, You may use: `python library_inventory.py` or `python pet_simulator.py`
