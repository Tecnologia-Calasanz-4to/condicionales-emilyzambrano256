Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def suma(num1,num2):
...     sumar= num1+num2
...     return sumar
... 
>>> def division(num1,num2):
...     dividir= num1/num2
...     return dividir
... 
>>> def multiplicar(num1,num2):
...     multiplicar= num1*num2
...     return multiplicar
... 
>>> def resta(num1,num2):
...     restar= num1-num2
...     return restar
... 
>>> n1=int(input("Dame un num: "))
Dame un num: 6
>>> n2=int(input("Dame otro num: "))
Dame otro num: 2
>>> resultadoSuma= suma(n1,n2)
>>> print (resultadoSuma)
8
>>> resultadoDivision= division(n1,n2)
>>> print (resultadoDivision)
3.0
>>> resultadoMultiplicar= multiplicar(n1,n2)
>>> print (resultadoMultiplicar)
12
>>> resultadoResta= resta(n1,n2)
>>> print (resultadoResta)
4
