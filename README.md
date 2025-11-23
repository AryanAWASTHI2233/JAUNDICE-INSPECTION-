**Project Title**

Health Symptom Analyzer with Risk Pie Chart


---

**Overview of the Project**

The Health Symptom Analyzer is a Python-based interactive program that evaluates a user’s health risk level based on common symptoms. The user answers a series of yes/no questions, and the system calculates a score to determine their risk category. It also generates a visual pie chart using Matplotlib to show the percentage of “Safe” and “In Danger” conditions. This project demonstrates user input handling, decision-making logic, and data visualization in Python.


---

**Features**

User name input and welcome response

Interactive symptom questionnaire (10 symptoms)

Automatic risk scoring

Health status classification (Fine / Rest Needed / Visit Doctor)

Pie chart visualization of danger vs safe percentage

Clean modular code using functions

Beginner-friendly and easy to run



---

**Technologies / Tools Used**

Python 3.x

Matplotlib (for pie chart visualization)

Standard Python libraries: input(), conditionals, lists, loops



---

**Steps to Install & Run the Project**

1. Install Python (if not installed)

Download from: https://www.python.org/downloads/

2. Install Matplotlib

Open terminal / CMD and run:

pip install matplotlib

3. Create a Python file

Save your code as:

health_checker.py

4. Run the project

Open terminal/CMD in the file’s folder and run:

python health_checker.py

5. Follow the on-screen instructions

Enter your name

Answer each symptom using y/n

View your health status and pie chart



---

**Instructions for Testing**

Test the program by entering different combinations of symptoms:

0 symptoms → expect “GOOD, YOU ARE FINE”

1–3 symptoms → expect “TAKE REST”

5 symptoms → expect “AVOID SOCIAL CONTACT, SEE A DOCTOR”

More than 5 → expect “VISIT A DOCTOR QUICKLY”


Test case-insensitivity: y/Y/n/N

Test invalid inputs to ensure the program doesn’t crash

Verify the pie chart always shows correct percentages

Confirm no repeated questions (function called once)
