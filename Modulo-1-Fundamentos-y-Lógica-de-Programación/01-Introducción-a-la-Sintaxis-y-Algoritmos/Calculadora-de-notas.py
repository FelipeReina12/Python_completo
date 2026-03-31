# Cálculadora de notas que indica si un alumno aprobó el corte según sus calificaciones.
nota_parcial_corte_1_y_2 = 0.15
nota_parcial_corte_3 = 0.20
nota_proyecto_integrador_1 = 0.05
nota_proyecto_integrador_2 = 0.10
nota_proyecto_integrador_3 = 0.15
nota_quiz_1 = 0.10
nota_quiz_2 = 0.05
nota_quiz_3 = 0.05
corte_1 = 0.30
corte_2 = 0.30  
corte_3 = 0.40

print("Primer corte")
parcial_1 =float(input("Ingrese la nota del parcial del primer corte: "))
proyecto_integrador_1 = float(input("Ingrese la nota del proyecto integrador del primer corte: "))
quiz_1 = float(input("Ingrese la nota del quiz del primer corte: "))
total_primer_corte = ((parcial_1 * nota_parcial_corte_1_y_2) + (proyecto_integrador_1 * nota_proyecto_integrador_1) + (quiz_1 * nota_quiz_1)) / corte_1 
print(f"Su nota para el primer corte es: {round(total_primer_corte, 2)}")

print("Segundo corte")
parcial_2 =float(input("Ingrese la nota del parcial del segundo corte: "))
proyecto_integrador_2 = float(input("Ingrese la nota del proyecto integrador del segundo corte: "))
quiz_2 = float(input("Ingrese la nota del quiz del segundo corte: "))
total_segundo_corte = ((parcial_2 * nota_parcial_corte_1_y_2) + (proyecto_integrador_2 * nota_proyecto_integrador_2) + (quiz_2 * nota_quiz_2)) / corte_2 
print(f"Su nota para el segundo corte es: {round(total_segundo_corte, 2)}")

print("Tercer corte")
parcial_3 =float(input("Ingrese la nota del parcial del tercer corte: "))
proyecto_integrador_3 = float(input("Ingrese la nota del proyecto integrador del tercer corte: "))
quiz_3 = float(input("Ingrese la nota del quiz del tercer corte: "))
total_tercer_corte = ((parcial_3 * nota_parcial_corte_3) + (proyecto_integrador_3 * nota_proyecto_integrador_3) + (quiz_3 * nota_quiz_3)) / corte_3 
print(f"Su nota para el tercer corte es: {round(total_tercer_corte, 2)}")

nota_final = (total_primer_corte * corte_1) + (total_segundo_corte * corte_2) + (total_tercer_corte * corte_3)
print(f"Su nota final es: {round(nota_final, 2)}")

if nota_final >= 3.0:
    print("¡Felicidades! Has aprobado el curso.")
else:
    print("Lo siento, no has aprobado el curso. ¡Sigue esforzándote!")
