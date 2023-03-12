#Escribir una función que calcule el máximo común divisor entre dos números.
import sys

sys.path.insert(0, 'D:\Programacion\Python\Django\CAC2023-Django\Codo a Codo Django 2023 1C')


from MaximoDivisorComun import maxDivisor

numero1 = int(input("ingresar numero 1 (mayor a 0): "))
numero2 = int(input("ingresar numero 2 (mayor a 0): "))

respuesta = maxDivisor(numero1,numero2)

print(respuesta)