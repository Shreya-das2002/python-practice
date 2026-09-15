# Object-Oriented Student Directory System

A robust, terminal-based Student Registry application built in Python. This project transitions traditional dictionary-based data handling into clean Object-Oriented Programming (OOP), utilizing a dedicated controller layout to manage data entry, storage operations, and input safety guards.

---

## Problem Statement
Managing student records using plain text files or raw nested dictionaries often leads to fragile code. Without proper structures:
* Data fields become inconsistent and difficult to track.
* Rogue inputs (like typing letters for an age) cause immediate program crashes.
* Close-down procedures result in absolute data loss unless a persistent storage layout is linked.

**The Solution:** This project implements the **Separation of Concerns** principle. It wraps data attributes within independent `Student` instances, controls operations through a centralized `StudentManager` engine, enforces robust data validation loops, and uses JSON serialization to maintain an indestructible, permanent record book on disk.

---

