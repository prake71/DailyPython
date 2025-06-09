'''
https://www.w3resource.com/python-exercises/python-basic-exercises.php

Write a Python program to compute the future value of a specified
principal amount, rate of interest, and number of years.

Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
'''

# Wie wird der Future Value (Zukunftswert) berechnet?
# Der Future Value wird berechnet, indem du den aktuellen Wert der
# Investition (PV) mit (1 + Zinssatz/Anzahl der Zinsperioden) hoch
# (Anzahl der Zinsperioden * Anzahl der Jahre) multiplizierst.

pv = 10000
zinssatz = 3.5
anz_perioden = 7

fv = round(pv * (1 + zinssatz/100) ** anz_perioden,2)
print(fv)





