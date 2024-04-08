"""
Aufgabe:
Schreibe ein Programm das alle Zahlen von 1 bis 100 ausgibt. 
1) Wenn die Zahl allerdings ein Vielfaches von 3 ist, soll statt der Zahl das Wort "Fizz" ausgegeben werden.
2) Wenn die Zahl ein Vielfaches von 5 ist, soll statt der Zahl das Wort "Buzz" ausgegeben werden. 
3) Ist die Zahl sowohl ein Vielfaches von 3 als auch von 5, soll statt der Zahl das Wort "FizzBuzz" ausgegeben werden.

"""

"""
Wie ist das Programm in Pseudo-Code aufgebaut?

Schleife die die Zahlen von 1 bis 100 durchläuft. 
    - Ausgabe der Zahlen
1) 
    - Bedingung: Zahl durch 3 Teilbar -> Ausgabe: "Fizz"
        - Modulo Funktion -> Rest = 0
2) 
    - Bedingung: Zahl durch 5 Teilbar -> Ausgabe: "Buzz"
        - Modulo Funktion -> Rest = 0
3) 
    - Bedingung:  Zahl durch 3 und 5 Teilbar -> Ausgabe: "FizzBuzz"
        - Modulo Funktion -> Rest = 0
"""

# Ausgabe
print("Hello World")

# While-Schleife
a = 0 
while(a < 5):
    a += 1
    print(a)

# For-Schleife
# range(Startwert, Endwert -1, Schritte)
# - Startwert und Schritte Optional 
# --> Default: Startwert = 0 und Schritte = 1
for i in range(2, 20, 4):
    print(i)

# if-Bedingung
zahl1 = 1
zahl2 = 1
zahl3 = 1
if(zahl1 == zahl2):
    print("wir sind gleich! :)")

# if-Bedingung mit logischer Verknüpfung
if(zahl1 == zahl2 and zahl1 == zahl3): #Alternativ: or
    print("Die Zahlen sind alle gleich!")

# if & else
zahl1 = 1
zahl2 = 2
if (zahl1 < zahl2):
    print("zahl eins: " + str(zahl1) + " ist kleiner als zahl zwei: " + str(zahl2))
else:
    print("Die Zahl eins ist größer als die Zahl 2")

# elif
zahl1 = 5
zahl2 = -5000
zahl3 = 1
if (zahl1 < zahl2):
    print("zahl eins: " + str(zahl1) + " ist kleiner als zahl zwei: " + str(zahl2))
elif (zahl1 < zahl3):
    print("zahl eins: " + str(zahl1) + " ist kleiner als zahl drei: " + str(zahl3))
else:
    print("Die Bedingungen sind nicht als true ausgewertet")
    print("zahl eins: " + str(zahl1) + " ist größer als zahl zwei: " + str(zahl2) + " und als zahl drei: " + str(zahl3))

# Modulo
print("Modulo:")
print(zahl1 % zahl3)