✔ Problem Statement

Jaundice is a condition that often goes unnoticed in its early stages due to lack of awareness and confusion about symptoms. Many individuals are unable to identify whether the symptoms they experience are serious enough to require medical attention. There is a need for a simple, accessible tool that can quickly analyze user-reported symptoms and provide an initial risk estimation.

This project aims to offer a lightweight, interactive system that helps users determine their potential jaundice risk based on common symptoms, without requiring medical expertise or complex devices.


---

✔ Scope of the Project

The project provides a command-line interface (CLI) tool for assessing jaundice risk.

It focuses on collecting basic symptoms through simple yes/no inputs.

The system calculates risk levels based on the number of symptoms selected.

It stores results in a text file report for record-keeping.

It provides a visual representation of the risk through a pie chart.

It does not diagnose jaundice medically—its goal is preliminary assessment only.

It is a small-scale, educational project demonstrating Python fundamentals like:

Input handling

Conditional checks

File operations

Object-oriented programming

Basic data visualization




---

✔ Target Users

General users who want to self-check symptoms quickly.

Students and beginners learning Python and building simple projects.

Individuals monitoring health symptoms for early detection.

Healthcare learners who want to understand symptom-based assessment tools.

Users without technical knowledge, since the system requires only simple y/n inputs.



---

✔ High-Level Features

1️⃣ Symptom-Based Assessment

Users answer a series of jaundice-related symptoms.

Each "yes" increases the risk score.


2️⃣ Risk Level Classification

Categorizes the risk into five stages:

Fine

Mild

Moderate

High

Critical



3️⃣ Automatic Report Generation

Saves user name, symptoms, score, and result into report.txt.


4️⃣ Visual Health Analysis (Pie Chart)

Uses matplotlib to display “Safe Zone vs Danger Zone” analysis.


5️⃣ Interactive CLI Input System

Simple yes/no questions

Validates incorrect user inputs

Provides clean console output


6️⃣ Modular, OOP-Based Architecture

Core logic organized inside JaundiceDetector class

Easier to extend or modify
