class ClassName:
    # Klassenattribute und Methoden
    pass
class ErsteKlasse:
    def initialisieren(self):
        self.name = "Meine Klasse"
    
    def ausgabe(self):
        print(f"Der Name ist {self.name}")

        meine_klasse = ErsteKlasse()



class ErsteKlasse:
    def initialisieren(self, name):
        self.name = name


class ErsteKlasse:
    zaehler = 0  # Klassenattribut
    
    def __init__(self, name):
        self.name = name
        ErsteKlasse.zaehler += 1

class Fahrzeug:

    def __init__(self, name, richtung, geschwindigkeit, raeader, farbe, leistung):
        self.name = name
        self.richtung = richtung
        self.geschwindigkeit = geschwindigkeit
        self.reader = raeader
        self.farbe = farbe
        self.name = leistung
        self.motor_laeuft  = False

    def sarten(self):
        self.motor_laeuft = True

    def stoppen(self):
        self.motor_laeuft = False
        
    def beschleunigen(self, wert):
        if self.motor_laeuft:
            self.geschwindigkeit += wert



class Fahrzeug:
    def __init__(self, name, farbe):
        self.name = name
        self.farbe = farbe
auto = Fahrzeug("Auto", "Rot")


def __del__(self):
    print(f"{self.name} wurde zerstört.")

class Fahrzeug:
    def __init__(self, name, farbe):
        self.name = name
        self.farbe = farbe

    def __str__(self):
        return f"Fahrzeug: {self.name}, Farbe: {self.farbe}"

# Instanz der Klasse Fahrzeug erstellen
mein_auto = Fahrzeug("VW Golf", "Blau")

# Gibt die benutzerdefinierte Zeichenkette zurück
print(mein_auto)

class ParentClass:
    def method(self):
        print("From Parent")

class ChildClass(ParentClass):
    pass

obj = ChildClass()
obj.method()  # Ausgabe: From Parent


class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class A:
    def method(self):
        print("From A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.method()  # Ausgabe: From A



class Base:
    def __init__(self):
        print("Base init")

class Derived(Base):
    pass

obj = Derived()  # Ausgabe: Base init


class Fahrzeug:
    def __init__(self, name, richtung, geschwindigkeit, farbe, leistung):
        self.name = name
        self.richtung = richtung
        self.geschwindigkeit = geschwindigkeit
        self.farbe = farbe
        self.leistung = leistung

class Kraftwagen(Fahrzeug):
    def __init__(self, name, richtung, geschwindigkeit, farbe, leistung, tueren):
        super().__init__(name, richtung, geschwindigkeit, farbe, leistung)
        self.tueren = tueren

class Pkw(Kraftwagen):
    def __init__(self, name, richtung, geschwindigkeit, farbe, leistung, tueren, kofferraum):
        super().__init__(name, richtung, geschwindigkeit, farbe, leistung, tueren)
        self.kofferraum = kofferraum


class Test:
    def ausgabe(self):
        print("Methode aus Test")

class Versuch(Test):
    def ausgabe(self):
        super().ausgabe()  # Ruft die Methode der Elternklasse Test auf
        print("Methode aus Versuch")

versuch = Versuch()
versuch.ausgabe()


class Test:
    def __init__(self, wert):
        self.__wert = wert

    def get_wert(self):
        return self.__wert

objekt = Test(10)
print(objekt.get_wert())  # Gibt 10 aus
# print(objekt.__wert)  # Führt zu einem Fehler


class Test:
    def __init__(self):
        self.__versteckt = 42

obj = Test()
# Direkter Zugriff schlägt fehl:
# print(obj.__versteckt)  # AttributeError

# Zugriff über Name Mangling:
print(obj._Test__versteckt)  # Ausgabe: 42

print(f"Die Zahl {target_number} wurde zuletzt an der Position {last_index} gefunden.")




class Person:
    def __init__(self, alter):
        self.__alter = alter

    def get_alter(self):
        return self.__alter

    def set_alter(self, neues_alter):
        if neues_alter > 0:
            self.__alter = neues_alter
        else:
            print("Ungültiges Alter")



class Rechteck:
    def __init__(self, breite, hoehe):
        self.__breite = breite
        self.__hoehe = hoehe

    @property
    def flaeche(self):
        return self.__breite * self.__hoehe

    @flaeche.setter
    def flaeche(self, wert):
        print("Flaeche kann nicht direkt gesetzt werden.")

prop = property(get_prop, set_prop)

# Eine Methode zur Ausgabe der Liste
def ausgabe(meine_liste):
    print("Die Liste enthält folgende Werte:")
    for wert in meine_liste:
        print(wert, end=" ")
    print("\n")

# Eine Liste erstellen
liste = []
for i in range(1, 10):
    liste.append(i)

ausgabe(liste)

# Ein Element löschen
element = int(input("Welches Element soll gelöscht werden? "))
liste.remove(element)
ausgabe(liste)

#--------------------
# Zwei Werte einlesen
dividend = int(input("Geben Sie den Dividend ein: "))
divisor = int(input("Geben Sie den Divisor ein: "))

# Berechnen und ausgeben
if divisor != 0:
    print("Das Ergebnis ist:", dividend / divisor)
else:
    print("Division durch 0 ist nicht erlaubt!")

#-------------------
if element in liste:
    liste.remove(element)
if divisor != 0:
    ergebnis = dividend / divisor

#--------------------
def pruefeZahl(wert):
    if wert.isnumeric():
        return True
    else:
        return False

wert = wert.replace(".", "")
if wert.isnumeric():
    return True

try:
    # Code, der eine Ausnahme auslösen könnte
except:
    # Code zur Fehlerbehandlung


try:
    wert = int(input("Geben Sie eine Zahl ein: "))
    print("Das Ergebnis ist:", 10 / wert)
except ValueError:
    print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
except ZeroDivisionError:
    print("Division durch 0 ist nicht erlaubt.")

#--------
try:
    ergebnis = dividend / divisor
except ZeroDivisionError:
    print("Eine Division durch 0 ist nicht definiert.")


except (ZeroDivisionError, ValueError):
    print("Fehler: Ungültige Eingabe oder Division durch 0.")

except BaseException as e:
    print("Es hat ein Problem gegeben:", e)


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Fehler: Division durch 0!")



# Eigene Ausnahme definieren
class EigeneAusnahme(Exception):
    pass

# Nutzung der eigenen Ausnahme
def pruefen(wert):
    if wert < 0:
        raise EigeneAusnahme("Der Wert darf nicht negativ sein!")

try:
    pruefen(-5)
except EigeneAusnahme as e:
    print("Fehler:", e)


#------

class ZuVielError(Exception):
    def __init__(self, vorhanden, menge, volumen):
        self.vorhanden = vorhanden
        self.menge = menge
        self.volumen = volumen
    def __str__(self):
        return f"Das Fass enthält {self.vorhanden} Liter. Mit {self.menge} wird das Volumen überschritten."
#-----------

def befuellen(self, menge):
    if self.vorhanden + menge > self.volumen:
        raise ZuVielError(self.vorhanden, menge, self.volumen)


#------------

try:
    ergebnis = dividend / divisor
except ZeroDivisionError:
    print("Eine Division durch 0 ist nicht definiert.")
else:
    print(f"Das Ergebnis ist: {ergebnis}")


#---------

try:
    datei = open("daten.txt", "r")
    inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden.")
finally:
    datei.close()  # Datei wird immer geschlossen, auch bei Fehlern




# Prüfen mit str.isnumeric()
string1 = "123"
print(string1.isnumeric())  # True, da nur numerische Zeichen enthalten sind

string2 = "3.14"
print(string2.isnumeric())  # False, da Gleitkommazahl

# Allgemeine Prüfung für Zahlen mit float()
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

print(is_number("3.14"))  # True, Gleitkommazahl erkannt
print(is_number("-42"))   # True, negative Zahl erkannt
print(is_number("abc"))   # False, keine Zahl


try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 10 / zahl
except ValueError:
    print("Ungültige Eingabe! Bitte eine ganze Zahl eingeben.")
except ZeroDivisionError:
    print("Division durch 0 ist nicht erlaubt.")
except Exception as e:  # Allgemeiner Block, der alle übrigen Ausnahmen abfängt
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")


try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 10 / zahl
except ZeroDivisionError as e:  # Zugriff auf die Instanz der Ausnahmeklasse
    print(f"Fehler: {e}")  # Ausgabe der Fehlermeldung
except ValueError as e:
    print(f"Ungültige Eingabe: {e}")


try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 10 / zahl
except ZeroDivisionError:
    print("Division durch 0 ist nicht erlaubt!")
except ValueError:
    print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
else:
    print(f"Das Ergebnis ist: {ergebnis}")  # Nur wenn kein Fehler auftritt

# Benutzerdefinierte Ausnahmeklasse, die von Exception abgeleitet ist
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    # Ausnahme manuell auslösen
    raise CustomError("Das ist ein benutzerdefinierter Fehler!")
except CustomError as e:
    print(f"Ein Fehler ist aufgetreten: {e.message}")


mein_dict = {"a": 1, "b": 2}

try:
    wert = mein_dict["c"]  # Schlüssel 'c' existiert nicht
except KeyError as e:
    print(f"Fehler: Der Schlüssel '{e}' ist im Dictionary nicht vorhanden.")

datei = open("datei.txt", "w")
datei.close()


with open("datei.txt", "w") as datei:
    datei.write("Hallo Welt\n")
print("Datei erstellt.")

# Erzeugung eines Dateiobjekts im Schreibmodus
datei = open("beispiel.txt", "w")

# Datei wird geschrieben
datei.write("Hallo, Welt!")

# Datei wird geschlossen
datei.close()


with open("datei.txt", "w") as datei:
    for i in range(1, 6):
        datei.write(f"Zeile {i}\n")
print("Datei erfolgreich geschrieben.")

with open("datei.txt", "w") as datei:
    datei.write("Beispieltext\n")

with open("beispiel.txt", "w") as datei:
    datei.write("Hallo, Welt!")  # Datei wird beschrieben
# Sobald der Block endet, wird die Datei automatisch geschlossen


with open("datei.txt", "r") as datei:
    for zeile in datei:
        print(zeile, end="")


# Dateiinhalt: 
# Zeile 1
# Zeile 2
# Zeile 3

with open("beispiel.txt", "r") as datei:
    print("Mit readline():")
    print(datei.readline())  # Liest nur die erste Zeile
    
    datei.seek(0)  # Zurück zum Anfang der Datei
    
    print("\nMit readlines():")
    print(datei.readlines())  # Liest alle Zeilen und gibt sie als Liste zurück



with open("datei.txt", "r+") as datei:
    print(datei.tell())  # Position ausgeben
    datei.seek(0)        # An den Anfang springen
    datei.truncate()     # Datei kürzen



with open("demo.txt", "w") as datei:
    datei.writelines(["Eins\n", "Zwei\n", "Drei\n"])


import os
print("Aktuelles Verzeichnis:", os.getcwd())
os.mkdir("neues_verzeichnis")
os.chdir("neues_verzeichnis")
print("Neues Verzeichnis:", os.getcwd())

import gzip
with gzip.open("gepackt.gz", "wb") as datei:
    for i in range(1, 100000):
        datei.write(f"Zeile {i}\n".encode())
print("Gepackte Datei erstellt.")


with open("example.txt", "w") as datei:
    datei.write("Hallo, Welt!")
# Datei wird automatisch geschlossen


# Öffnen einer Datei im Lesemodus:
with open("beispiel.txt", "r", encoding="utf-8") as datei:
    inhalt = datei.read()
    print(inhalt)


with open("example.txt", "w+") as datei:
    datei.write("Hallo, Welt!")  # Schreiben in die Datei
    datei.seek(0)                # Zurück an den Anfang der Datei
    print(datei.read())          # Lesen aus der Datei


try:
    with open("example.txt", "x") as datei:
        datei.write("Hallo, Welt!")
except FileExistsError:
    print("Fehler: Die Datei existiert bereits!")


with open("example.txt", "w") as datei:
    datei.write("Hallo, Welt!")  # Speichert Text

with open("daten.txt", "a") as datei:
    # Konvertierung in einen String, um den Wert anzuhängen
    datei.write(str(42) + "\n")


with open("test.txt", "w") as datei:
    datei.write("Hallo, Welt!")  # Speichert Text



with open("test.txt", "r") as datei:
    for zeile in datei:
        print(zeile, end="")

import os

# Liste aller Dateien und Unterverzeichnisse im aktuellen Verzeichnis
inhalt = os.listdir()
print("Inhalt des aktuellen Verzeichnisses:", inhalt)

# Optional: Inhalt eines spezifischen Verzeichnisses
verzeichnis = "/pfad/zum/verzeichnis"
inhalt_spezifisch = os.listdir(verzeichnis)
print(f"Inhalt von {verzeichnis}:", inhalt_spezifisch)

import gzip

# Komprimierte Datei erstellen und schreiben
with gzip.open("example.gz", "wb") as datei:
    datei.write(b"Das ist ein komprimierter Text.")



# Metainformationen oder Kommentare
"""
Dieses Skript demonstriert den Import von Modulen.
"""

# Import von Modulen (direkt am Anfang)
import os
import math

# Restlicher Code
print("Aktuelles Verzeichnis:", os.getcwd())
print("Quadratwurzel von 16:", math.sqrt(16))


# Modul: grundrechenarten.py
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

import grundrechenarten
print(grundrechenarten.add(3, 5))


import math
print(math.factorial(5))  # Ausgabe: 120

import random
print(random.randint(1, 10))  # Zufällige Zahl zwischen 1 und 10

import math as mathematik

# Verwendung des Alias
print(mathematik.sqrt(16))  # Ausgabe: 4.0

import math as mathematik
print(math.factorial(10))

#Fehlermeldung NameError: name 'math' is not defined

from math import pi

from meinpaket import meinmodul


import sys

# Liste der Suchverzeichnisse ausgeben
print(sys.path)

try:
    x = int("abc")  # Führt zu einem ValueError
except (ValueError, TypeError) as e:
    print(f"Eine Ausnahme wurde ausgelöst: {e}")
try:
    # Code, der eine Ausnahme auslösen könnte
except (Exception1, Exception2):
    pass

with open("vorhanden.txt", "a") as datei:
    datei.write("Zusätzlicher Inhalt wird angehängt.\n")

if os.path.exists("test.txt"):
    file_size = os.path.getsize("test.txt")
    print(f"Die Größe der Datei beträgt {file_size} Bytes.")
else:
    print("Die Datei 'test.txt' existiert nicht.")


# eine Zeichenkette erstellen
zeichenkette = "Ich bin eine Zeichenkette."
# einen Wert einlesen
eingabe = input("Wonach soll gesucht werden? ")

try:
    # Versucht, die erste Position zu finden
    position = zeichenkette.index(eingabe) + 1
    anzahl = zeichenkette.count(eingabe)
    print("Die erste Position ist", position)
    print("Der Wert", eingabe, "wurde", anzahl, "-mal gefunden.")
except ValueError:
    # Ausnahmebehandlung, falls der Wert nicht gefunden wird
    print("Der Wert", eingabe, "wurde nicht gefunden.")


import time

# Aktuelle Zeit als Zeitstempel
current_time = time.time()
print(f"Aktuelle Zeit (Zeitstempel): {current_time}")

import numpy as np

# Ein Array mit Zahlen
array = np.array([1, 2, 3, 4, 5])
print(array)  # Ausgabe: [1 2 3 4 5]


import numpy as np

# Erstellen eines großen Arrays
data = np.random.rand(1000, 1000)

# Matrixmultiplikation (schnell und effizient)
result = np.dot(data, data)

print("Matrixmultiplikation abgeschlossen.")

import numpy as np

# Eine Liste definieren
liste = [1, 2, 3, 4, 5]

# Liste in ein NumPy-Array umwandeln
array = np.array(liste)

print(array)  # Ausgabe: [1 2 3 4 5]

import numpy as np

# Ein NumPy-Array erstellen
np_array = np.array([10, 20, 30, 40, 50])

# Jedes Element des Arrays durch 2 teilen
np_array = np_array / 2

print(np_array)  # Ausgabe: [ 5. 10. 15. 20. 25.]

import numpy as np

# Zwei NumPy-Arrays erstellen
np_array = np.array([1, 2, 3])
np_array_2 = np.array([4, 5, 6])

# Elementweise Multiplikation
werte = np_array * np_array_2

print(werte)  # Ausgabe: [ 4 10 18 ]


import numpy as np

# Integer-Array mit 32-Bit
int_array = np.array([1, 2, 3], dtype=np.int32)
print(int_array.dtype)  # Ausgabe: int32

# Gleitkomma-Array mit einfacher Genauigkeit (float32)
single_array = np.array([1.5, 2.3, 3.7], dtype=np.float32)
print(single_array.dtype)  # Ausgabe: float32

# Gleitkomma-Array mit doppelter Genauigkeit (float64)
double_array = np.array([1.5, 2.3, 3.7], dtype=np.float64)
print(double_array.dtype)  # Ausgabe: float64


import numpy as np

# Ganzzahlen-Array ohne Angabe eines Datentyps
int_array = np.array([1, 2, 3])
print(int_array.dtype)  # Ausgabe: int64 (auf 64-Bit-Systemen)

# Nachkommazahlen-Array ohne Angabe eines Datentyps
float_array = np.array([1.5, 2.5, 3.5])
print(float_array.dtype)  # Ausgabe: float64


import numpy as np

# Werte außerhalb des Bereichs von int8
array = np.array([300, -300], dtype=np.int8)
print(array)  # Ausgabe: [44 -44] (Fehler durch Überlauf)

# Korrekte Wahl des Datentyps
array_correct = np.array([300, -300], dtype=np.int16)
print(array_correct)  # Ausgabe: [ 300 -300]


import numpy as np

# Array mit int8-Werten
array = np.array([-128, 0, 127], dtype=np.int8)
print(array)  # Ausgabe: [-128    0  127]

# Überschreiten des Wertebereichs führt zu Überlauf
overflow_array = np.array([128], dtype=np.int8)
print(overflow_array)  # Ausgabe: [-128] (Überlauf)


import numpy as np

# Ein Array mit einem spezifischen Datentyp erstellen
array = np.array([1, 2, 3], dtype=np.int32)

# Den Datentyp des Arrays abrufen
print(array.dtype)  # Ausgabe: int32


import numpy as np
liste = [10, 20, 30]
np_array = np.array(liste)
print(np_array)

np_array = np.zeros(5)  # Array mit 5 Nullen

np_array = np.arange(0, 10, 2)  # Werte von 0 bis 8 in 2er-Schritten


np_array = np.linspace(0, 1, 10)  # 10 Werte von 0 bis 1

import numpy as np

# Ein eindimensionales Array (Vektor)
vektor = np.array([1, 2, 3, 4, 5])
print(vektor)  # Ausgabe: [1 2 3 4 5]


np.full(shape, fill_value, dtype=None)

import numpy as np

# 2x3-Array mit dem Wert 7 erstellen
array = np.full((2, 3), 7)
print(array)


import numpy as np

# Eindimensionales Array mit 5 Nullen
array = np.zeros(5)
print(array)  # Ausgabe: [0. 0. 0. 0. 0.]


np.arange(start, stop, step, dtype=None)


import numpy as np
array = np.arange(1, 10, 2)
print(array)  # Ausgabe: [1 3 5 7 9]


np.empty(shape, dtype=float)


array = np.empty((2, 3))
print(array)
# Ausgabe: Zufällige Werte im Speicher, z. B.
# [[0.00000000e+000 0.00000000e+000 4.94065646e-324]
#  [0.00000000e+000 0.00000000e+000 0.00000000e+000]]

import numpy as np
array = np.arange(0, 3)
print(array)


np.linspace(start, stop, num=50, endpoint=True, dtype=None)



import numpy as np

# Erzeugt 5 gleichmäßig verteilte Werte von 0 bis 10
array = np.linspace(0, 10, 5)
print(array)  # Ausgabe: [ 0.   2.5  5.   7.5 10. ]


np_2darray = np.array([[1, 2, 3], [4, 5, 6]])
np_3darray = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

import numpy as np

# Ein 2D-numpy-Array erstellen
array = np.array([[1, 2, 3], [4, 5, 6]])

# Anzahl der Elemente im Array ermitteln
anzahl_elemente = array.size
print("Anzahl der Elemente:", anzahl_elemente)


array = np.array([[1, 2, 3], [4, 5, 6]])
print(array.size)   # 6
print(array.ndim)   # 2
print(array.shape)  # (2, 3)

print(np_array[0])  # Erstes Element
print(np_2darray[1, 0])  # Element in Zeile 1, Spalte 0


import numpy as np

# Zwei Arrays mit der gleichen Form
mein_array_1 = np.array([1, 2, 3])
mein_array_2 = np.array([4, 5, 6])

# Elementweise Addition
ergebnis = mein_array_1 + mein_array_2
print(ergebnis)  # Ausgabe: [5 7 9]


np.dot(array1, array2)
np.sum(array)


import numpy as np

# Zwei Matrizen definieren
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrizenmultiplikation
result = np.dot(matrix1, matrix2)  # Oder: matrix1 @ matrix2
print(result)


array = np.array([1, 2, 3])
array = np.append(array, 4)  # [1, 2, 3, 4]


import numpy as np

# Ursprüngliches Array
array = np.array([1, 2, 3])

# Werte am Ende einfügen
neues_array = np.append(array, [4, 5])
print(neues_array)

import numpy as np

# Mehrdimensionales Array
array = np.array([[1, 2, 3], [4, 5, 6]])

# Mit np.ravel()
eindimensional_ravel = np.ravel(array)
print("Ravel:", eindimensional_ravel)  # Ausgabe: [1 2 3 4 5 6]

# Mit .flatten()
eindimensional_flatten = array.flatten()
print("Flatten:", eindimensional_flatten)  # Ausgabe: [1 2 3 4 5 6]

struktur = np.dtype([("name", np.str_, 10), ("alter", np.int32)])
daten = np.array([("Max", 25), ("Anna", 30)], dtype=struktur)

np_array['name']

import numpy as np

# Eine Liste definieren
meine_liste = [1, 2, 3,]

# Liste in ein NumPy-Array umwandeln
mein_array = np.array(meine_liste)
print(mein_array)  # Ausgabe: [1 2 3]


import numpy as np

# Direktes Erstellen eines Arrays aus einer Liste
mein_array = np.array([1, 2, 3])
print(mein_array)  # Ausgabe: [1 2 3]


import numpy as np

# Erstellen eines 2x3-Arrays ohne Initialisierung
array = np.empty((2, 3))
print(array)

import numpy as np

# Array mit Werten von 5 bis 50 (exklusive) und Schrittweite 5
mein_array = np.arange(5, 55, 5)
print(mein_array)


import numpy as np

# Ein 2D-numpy-Array erstellen
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Dimensionen des Arrays abrufen
dimensionen = array.shape
print("Dimensionen des Arrays:", dimensionen)


import numpy as np

# Ein 2D-numpy-Array erstellen
array = np.array([[1, 2, 3], [4, 5, 6]])

# Shape (Form) abrufen
print("Shape des Arrays:", array.shape)


import numpy as np

# Ein 3D-Array erstellen
mein_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Zweiter Wert in der dritten Dimension des Arrays
wert = mein_array[0, 1, 1]  # Zugriff auf das Element in [0, 1, 1]
print("Zweiter Wert in der dritten Dimension:", wert)


import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a * b)  # Ausgabe: [ 4 10 18 ]


a = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
b = np.array([1, 2, 3])               # Shape: (3,)
print(a * b)
# Ausgabe:
# [[ 1  4  9]
#  [ 4 10 18]]


import numpy as np

# Zwei Matrizen definieren
A = np.array([[1, 2], [3, 4]])  # 2x2-Matrix
B = np.array([[5, 6], [7, 8]])  # 2x2-Matrix

# Matrizenmultiplikation
C = np.dot(A, B)  # Oder: A @ B
print(C)


import numpy as np

# Ursprüngliches Array
array = np.array([1, 2, 3, 4, 5])

# Löschen des Elements an Index 2
neues_array = np.delete(array, 2)
print(neues_array)  # Ausgabe: [1 2 4 5]


# Mehrdimensionales Array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Löschen der zweiten Spalte (Index 1)
neues_array_2d = np.delete(array_2d, 1, axis=1)
print(neues_array_2d)


import numpy as np

# Ursprüngliches Array
array = np.array([1, 2, 3])

# Verwenden von append()
neues_array = np.append(array, [4, 5])
print("Neues Array:", neues_array)  # Ausgabe: [1 2 3 4 5]
print("Originales Array:", array)   # Ausgabe: [1 2 3]


import numpy as np

# Ursprüngliches Array
array = np.array([1, 2, 3, 4, 5, 6])

# Array in eine 2x3-Matrix umformen
neues_array = np.reshape(array, (2, 3))
print(neues_array)



import numpy as np

# Zwei Arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Verbinden der Arrays
result = np.concatenate((array1, array2))
print(result)  # Ausgabe: [1 2 3 4 5 6]


array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6]])

# Verbinden entlang der Zeilen
result = np.concatenate((array1, array2), axis=0)
print(result)


array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5], [6]])

# Verbinden entlang der Spalten
result = np.concatenate((array1, array2), axis=1)
print(result)


import numpy as np

np_array = np.arange(1, 6)  # Array mit Werten [1, 2, 3, 4, 5]

# Prüfen, ob ein Wert gleich 4 ist
print(np_array == 4)  # [False False False True False]

# Werte größer als 2
print(np_array > 2)  # [False False True True True]

# Werte zwischen 2 und 4
print((np_array > 2) & (np_array < 4))  # [False False True False False]

# Werte gleich 2 oder 4
print((np_array == 2) | (np_array == 4))  # [False True False True False]


# Werte gleich 4
print(np_array[np_array == 4])  # [4]

# Ungerade Werte
print(np_array[np_array % 2 != 0])  # [1, 3, 5]


print(np.nonzero(np_array > 2))  # (array([2, 3, 4]),)


import numpy as np

# Ein Array mit Werten von 1 bis 5
np_array = np.array([1, 2, 3, 4, 5])

# Bedingung: Werte größer als 3
direkte_werte = np_array[np_array > 3]
print(direkte_werte)


np_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(np_2darray[0, :])  # Erste Zeile
print(np_2darray[:, 1])  # Zweite Spalte


indices = [0, 2, 4]
print(np_array[indices])  # [1, 3, 5] 4

mask = np_array > 3
print(np_array[mask])  # Werte größer als 3


import numpy as np
daten = np.loadtxt("daten.txt", delimiter=",")
print(daten)


import numpy as np
data = np.loadtxt("daten.csv", delimiter=",")
print(data)


data = np.genfromtxt("daten.csv", delimiter=",", missing_values="?", filling_values=0)
print(data)


np.savetxt("output.csv", data, delimiter=",", fmt="%.2f")


np.save("daten.npy", data)


data = np.load("daten.npy")
print(data)



mmap_array = np.memmap("daten.bin", dtype='float32', mode='r', shape=(1000, 1000))
print(mmap_array[0, 0])



import numpy as np

# Create array with values 5, 6, 7, 8, 9 and define the type uint32
array = np.array([5, 6, 7, 8, 9], dtype=np.uint32)

# Divide the array's total values by two.
result = array / 2

# Output results
print(f"Ursprüngliches Array: {array}")
print(f"Resultate nach Teilung durch 2: {result}")



import numpy as np

# Erstellen eines Arrays mit 20 Elementen, alle mit dem Wert 100
array = np.full(20, 100)

# Ausgabe des Arrays
print(array)




# Import the NumPy library
import numpy as np

# Example of an array
mein_array = np.array([[1, 2, 3], [4, 5, 6]])

# Determine the number of elements in each dimension
dimensions = mein_array.shape

# Print the dimensions
print(f"Anzahl der Elemente in jeder Dimensio: {dimensions}")




import numpy as np

# Example of a multidimensional array
mein_array = np.array([[1, 2, 3], [1, 4, 6]])

# Sum values along the rows (dimension 0)
sum_lines = mein_array.sum(axis=0)

# Sum values along the columns (dimension 1)
sum_columns = mein_array.sum(axis=1)

print(f"Summe entlang der Zeilen: {sum_lines}")
print(f"Summe entlang der Spalten: {sum_columns}")


import numpy as np

# Create the first two-dimensional matrix
first_array = np.array([[1, 2, 3], [1, 4, 6]])
second_array = np.array([[7, 8], [14, 16], [28, 32]])

# Perform matrix multiplication
result = np.dot(first_array, second_array)

# Output results
print("Array 1 (Matrix A):")
print(first_array)

print("\nArray 2 (Matrix B):")
print(second_array)

print("\nErgebnis der Matrizenmultiplikation (Matrix C):")
print(result)


import numpy as np

# Definition of the structured array with specific data types
dtype = [('text', 'U10'),  # Unicode text with max. 10 characters
         ('zahl1', 'i4'),  # 32-bit integer (corresponds to np.int32)
         ('zahl2', 'f4')]  # 32-bit floating point number (corresponds to np.float32)

# Initialisierung des Arrays mit Beispielwerten
meine_struktur = np.array([('Beispiel', 42, 3.14),
                           ('Test', 7, 2.71)],
                          dtype=dtype)

# Initialization of the array with sample value
print("Strukturiertes Array:")
print(meine_struktur)

# Access to individual elements and columns
print("\nErster Eintrag:")
print(meine_struktur[0]) 

print("\nText im zweiten Eintrag:")
print(meine_struktur[1]['text'])  




import numpy as np

# Definition of the structured array with specific data types
dtype = [('text', 'U10'),  # Unicode text with max. 10 characters
         ('zahl1', 'i4'),  # 32-bit integer (corresponds to np.int32)
         ('zahl2', 'f4')]  # 32-bit floating point number (corresponds to np.float32)

# Initialization of the array with sample values
meine_struktur = np.array([('Beispiel', 42, 3.14),
                           ('Test', 7, 2.71)],
                          dtype=dtype)

# Initialization of the array with sample value
print("Strukturiertes Array:")
print(meine_struktur)

# Access to individual elements and columns
print("\nErster Eintrag:")
print(meine_struktur[0])

print("\nText im zweiten Eintrag:")
print(meine_struktur[1]['text'])


import numpy as np

# Create an empty array for integer values
array = np.array([], dtype=int)

# Read in ten integer values and add them to the array
for i in range(10):
    while True:
        try:
            value = int(input(f"Geben Sie den {i + 1}. Wert ein (nur Zahlen erlaubt): "))
            array = np.append(array, value)  # Korrektur: value statt values
            break
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

# Output of the array after adding the values            
print("\nArray nach dem Hinzufügen der Werte:")
print(array)

# Remove the first element
array = np.delete(array, 0)

# Output of the array after removing the first element
print("\nArray nach dem Entfernen des ersten Elements:")
print(array)


import numpy as np

# Beispielarray
mein_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Letzte fünf Elemente in umgekehrter Reihenfolge
ergebnis = mein_array[-1:-6:-1]

print("Letzte fünf Elemente in umgekehrter Reihenfolge:", ergebnis)



import numpy as np

# Example for an array
mein_array = np.array([1.234, -5.678, 9.012, 3.456, -7.890])

# Save the data in a text file with the specified formatting
np.savetxt("meine_datei.txt", mein_array, fmt="%+5.3f")

print("Daten wurden erfolgreich gespeichert.")




#----------------------

import matplotlib.pyplot as plt

werte = [10, 15, 20, 25, 30]
figur, achse = plt.subplots()
achse.plot(werte)


import matplotlib.pyplot as plt
import numpy as np

array = np.arange(5, 20)
plt.plot(array)


import matplotlib.pyplot as plt
import numpy as np
array = np.linspace(0, 2 * np.pi, 30)
plt.plot(np.sin(array))
plt.show()



import matplotlib.pyplot as plt
import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([2, 4, 6, 8, 10])

plt.plot(array1 / array2)  # Division der Arrays und Plot
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Arrays definieren
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([2, 4, 6, 8, 10])

# Erstellen einer Figur mit einem Zeichenbereich (subplots)
fig, ax = plt.subplots()

# Division der Arrays und Darstellung
ax.plot(array1 / array2)

# Diagramm anzeigen
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Daten erstellen
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Subplots erstellen: 1 Zeile, 2 Spalten
fig, (ax1, ax2) = plt.subplots(1, 2)

# Erstes Subplot
ax1.plot(x, y1)
ax1.set_title("Sinus")

# Zweites Subplot
ax2.plot(x, y2)
ax2.set_title("Kosinus")

plt.show()



"""
Werte für die x-Achse
"""
# Pyplot aus Matplotlib als plt importieren
import matplotlib.pyplot as plt
# eine Liste mit Werten erstellen
werte = [10, 15, 12, 11, 30, 10, 9]
# die Beschriftungen für die x-Achse festlegen
x_achse =["Montag", "Dienstag", "Mittwoch", "Donnerstag",
"Freitag", "Samstag", "Sonntag"]
# die Werte ausgeben
plt.plot(x_achse, werte)
plt.show()




"""
Wertebereiche für die Achsen setzen
"""
# Pyplot aus Matplotlib als plt importieren
import matplotlib.pyplot as plt
# eine Liste mit Werten erstellen
werte = [10, 15, 12, 11]
# die Werte für die x-Achse festlegen
x_achse =[1, 2, 3, 4]
# die Werte für Minimum und Maximum setzen
xmin = 1
xmax = 4
ymin = 0
ymax = 20
# die Wertebereiche der Achsen anpassen
plt.axis([xmin, xmax, ymin, ymax])
# die Werte ausgeben
plt.plot(x_achse, werte)
plt.show()




import matplotlib.pyplot as plt

werte = [10, 15, 12, 11]
plt.plot(werte)
plt.show()

# Wertebereich der Achsen ermitteln
wertebereich = plt.axis()
print(f"Wertebereiche der Achsen: {wertebereich}")

"""
Diagramm speichern
"""
# Pyplot aus Matplotlib als plt importieren
import matplotlib.pyplot as plt
# eine Liste mit Werten erstellen
werte = [10, 15, 12, 11]
# die Werte für die x-Achse festlegen
x_achse =[1, 2, 3, 4]
# die Werte für Minimum und Maximum setzen
xmin = 1
xmax = 4
ymin = 0
ymax = 20
# die Wertebereiche der Achsen anpassen
plt.axis([xmin, xmax, ymin, ymax])
# die Werte ausgeben
plt.plot(x_achse, werte)
# das Diagramm in verschiedenen Formaten speichern
plt.savefig("diagramm.png")
plt.savefig("diagramm.tif")
plt.savefig("diagramm.jpg")



import matplotlib.pyplot as plt

# Beispiel-Daten
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Diagramm erstellen
plt.plot(x, y)

# Diagramm speichern
plt.savefig("diagramm.png")

# Diagramm anzeigen
plt.show()


daten = np.loadtxt("testdaten.txt")
np.count_nonzero(daten == wert)



import matplotlib.pyplot as plt

# Beispiel-Daten
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Diagramm mit Formatzeichenfolge: rote gestrichelte Linie mit Kreismarkern
plt.plot(x, y, 'r--o')

# Diagramm anzeigen
plt.show()


x_achse = [1, 2, 3, 4]  # Eigene Werte für die x-Achse
werte = [10, 15, 12, 11]  # Werte für die y-Achse

plt.plot(x_achse, werte)  # x-Werte und y-Werte an plot() übergeben
plt.show()


werte = [10, 15, 12, 11]  # Array mit Werten
plt.plot(werte, 'r:')  # Werte mit gepunkteter roter Linie darstellen
plt.show()


x_achse = [1, 2, 3, 4]  # Liste für die x-Werte
werte = [10, 15, 12, 11]  # Liste für die y-Werte

plt.plot(x_achse, werte)  # Beide Listen gleich lang
plt.show()


#-----------
x_achse = [1, 20, 3, 4]  # Werte für die x-Achse
werte = [10, 15, 12, 11]  # Werte für die y-Achse

plt.plot(x_achse, werte)  # Diagramm mit den x-Werten erstellen
plt.show()


werte = [10, 15, 12, 11]  # Werte für die y-Achse
plt.plot(werte)  # x-Werte werden automatisch generiert (0, 1, 2, 3)
plt.show()


#------------
werte = [5, 6, 7, 8]  # Beispielwerte
x_achse = [10, 12, 15, 18]  # x-Werte im Bereich 10-20

plt.plot(x_achse, werte)
plt.axis([10, 20, 1, 10])  # x_min, x_max, y_min, y_max
plt.show()


#---------
import matplotlib.pyplot as plt

# Beispiel-Diagramm erstellen
plt.plot([1, 2, 3], [4, 5, 6])

# Diagramm als PNG-Datei speichern
plt.savefig("diagramm.png")  # Das Dateiformat wird durch '.png' angegeben


#--------------
import matplotlib.pyplot as plt

# Beispiel-Diagramm erstellen
plt.plot([10, 20, 30], [5, 15, 25])

# Diagramm im PDF-Format speichern
plt.savefig("meindiagramm.pdf")  # '.pdf' gibt das Dateiformat an


import matplotlib.pyplot as plt
import numpy as np
array = np.arange(5, 20)
plt.plot(array, color="red", linestyle="--", linewidth=2, marker="o")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Beispielwerte
x = np.arange(5)
y = x ** 2

# Diagramm mit Markierungen und angepasster Größe
plt.plot(x, y, marker="o", markersize=10)
plt.show()


plt.text(6, 10, "Demotext")
plt.annotate("Wichtig!", xy=(2, 7), xytext=(4, 7), 
             arrowprops=dict(color="red"))


font = {"family": "serif", "color": "blue", "size": 12}
plt.title("Diagramm", fontdict=font)


plt.text(10, 10, r"$\alpha \beta$")


font = {"family": "serif", "color": "blue", "size": 12, "weight": "bold"}
plt.title("Diagramm", fontdict=font)


import matplotlib.pyplot as plt

daten = [1, 2, 3, 4, 5]
plt.plot(daten, linewidth=3, marker='D', markersize=5)
plt.show()

plt.title("Durchschnittswerte")

plt.ylabel("Ausgaben")


plt.plot(daten, label="Daten")
plt.legend()
plt.show()


plt.text(3, 6, "Achtung")
plt.annotate("Hinweis", xy=(3, 6), xytext=(2, 8), arrowprops=dict(facecolor='black', shrink=0.05))

font_dict = {"weight": "bold", "color": "red"}

plt.text(2, 2, r'$\pi$', fontsize=12)


import matplotlib.pyplot as plt
import numpy as np

# Daten erstellen
array = np.linspace(0, 2 * np.pi, 30)
sinus = np.sin(array)
kosinus = np.cos(array)

# Plots erstellen
plt.plot(sinus, color="red", linestyle=":", label="Sinus")
plt.plot(kosinus, color="blue", label="Kosinus")

# Legende und Titel hinzufügen
plt.legend()
plt.title("Sinus und Kosinus")
plt.show()


figur, achsen = plt.subplots(2)
achsen[0].plot(sinus, color="red", linestyle=":", label="Sinus")
achsen[1].plot(kosinus, color="blue", label="Kosinus")


figur, achsen = plt.subplots(1, 2)
achsen[0].plot(sinus, color="red", linestyle=":", label="Sinus")
achsen[1].plot(kosinus, color="blue", label="Kosinus")


figur, achsen = plt.subplots(2, 2)
achsen[0, 0].plot(sinus, color="red", label="Sinus")
achsen[1, 0].plot(kosinus, color="blue", label="Kosinus")
achsen[0, 1].plot(array1, color="green")
achsen[1, 1].plot(array2, color="orange")

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Mehrere Plots in einem Diagramm
plt.plot(x, y1, label="Sinus", color="blue")
plt.plot(x, y2, label="Kosinus", color="red")
plt.title("Mehrere Plots in einem Diagramm")
plt.legend()
plt.show()


fig, axes = plt.subplots(nrows=2, ncols=2)

# Beschriftung der Plots
axes[0, 0].set_title("Plot 1")
axes[0, 1].set_title("Plot 2")
axes[1, 0].set_title("Plot 3")
axes[1, 1].set_title("Plot 4")

plt.tight_layout()
plt.show()



fig, axes = plt.subplots(2, 1)  # Zwei Plots untereinander

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Zugriff auf die Zeichenbereiche
axes[0].plot(x, y1, color="green", label="Sinus")
axes[0].legend()
axes[0].set_title("Plot 1: Sinus")

axes[1].plot(x, y2, color="purple", label="Kosinus")
axes[1].legend()
axes[1].set_title("Plot 2: Kosinus")

plt.tight_layout()
plt.show()


fig, axes = plt.subplots(3, 3)  # 3x3-Tabelle

for i in range(3):
    for j in range(3):
        axes[i, j].plot(np.random.rand(10))  # Zufällige Daten für jeden Plot
        axes[i, j].set_title(f"Plot {i+1},{j+1}")

plt.tight_layout()
plt.show()



fig, axes = plt.subplots(2, 2)

# Zugriff auf den Bereich unten links
axes[1, 0].plot([1, 2, 3], [4, 5, 6], color="orange")
axes[1, 0].set_title("Unten Links")

plt.tight_layout()
plt.show()


fig, axes = plt.subplots(2, 2)

# Titel für die gesamte Figur
fig.suptitle("Gesamttitel für die Figur")

plt.tight_layout()
plt.show()



import matplotlib.pyplot as plt

kategorien = ['A', 'B', 'C']
werte = [10, 15, 7]

plt.bar(kategorien, werte, color='blue')
plt.title("Beispiel für ein Säulendiagramm")
plt.show()


labels = ['Äpfel', 'Bananen', 'Kirschen']
größen = [20, 30, 50]
explode = (0, 0.1, 0)  # Hebt das zweite Segment hervor

plt.pie(größen, labels=labels, explode=explode, autopct='%1.1f%%', startangle=140)
plt.title("Beispiel für ein Kreisdiagramm")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# exmaple array
daten = np.array([1, 3, 5, 7, 9])

# plot with the settings from the fifth task
plt.plot(
    daten,
    color='black',       
    linestyle='-.',      
    linewidth=2,         
    marker='D',          
    markerfacecolor='red', 
    markersize=5         
)

# displaying the plot
plt.show()






import matplotlib.pyplot as plt

# data for the pie chart 
labels = ['Frau Müller', 'Herr Meier', 'Herr Schmitz']
percentage = [61.6, 22.9, 15.5]
colors = ['gold', 'lightblue', 'lightgreen']
explode = (0.1, 0.01, 0.01)

# create pie chart
plt.figure(figsize=(6, 6))
plt.pie(percentage, labels=labels, autopct='%1.1f%%', colors=colors, explode=explode, startangle=90)
plt.title('Wahlergebnisse')

# save diagram
plt.savefig('Wahlergebnisse.jpeg', format='jpeg')

# displaying the plot
plt.show()







import matplotlib.pyplot as plt

# Data for the plots
x_labels = ['Messung 1', 'Messung 2', 'Messung 3', 'Messung 4']
y_values_1 = [10, 20, 30, 40]
y_values_2 = [40, 30, 20, 10]

# Create multiple plot
plt.figure(figsize=(8, 6))
plt.plot(x_labels, y_values_1, label='Daten 1', color='red')
plt.plot(x_labels, y_values_2, label='Daten 2', color='black')

# Adjust axis range
plt.ylim(0, 50)

# Title, axis labels and legend
plt.title('Mehrfachplot mit zwei Plots')
plt.xlabel('Messungen')
plt.ylabel('Werte')
plt.legend()

# Save diagram
plt.savefig('Mehrfachplot.jpeg', format='jpeg')

# Show diagram
plt.show()








import matplotlib.pyplot as plt

# Data for the plots 
labels = ['A', 'B', 'C', 'D', 'E']
values = [10, 5, 20, 12, 47]

# Create subplots (2 rows, 2 columns)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Titel für die gesamte Figur
fig.suptitle('Diagramme', fontsize=16)

# Title for the entire figure
axes[0, 0].plot(labels, values, marker='o', linestyle='-', color='blue')
axes[0, 0].set_title('Liniendiagramm')

# Bar chart (top right)
axes[0, 1].bar(labels, values, color='green')
axes[0, 1].set_title('Balkendiagramm')

# Bar chart (bottom left)
axes[1, 0].barh(labels, values, color='orange')
axes[1, 0].set_title('Säulendiagramm')

# Pie chart (bottom right)
axes[1, 1].pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
axes[1, 1].set_title('Kreisdiagramm')

# Customize layout and save diagram
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Platz für den Figur-Titel lassen
plt.savefig('Mehrfachplot_Diagramme.jpeg', format='jpeg')

# Show diagram 
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Load data from the file (sample data)
daten_aus_datei = np.array([3, 8, 1, 10])  # Example values, replace with np.loadtxt(“testdaten.txt”)

# Creation of the x-axis
x_achse = np.arange(len(daten_aus_datei))

# Creation of the x-axis
plt.bar(x_achse, daten_aus_datei, color='skyblue', label="Häufigkeiten")

# Add a note for the value 8
plt.annotate(
    'Hier ist der Wert 8',  
    xy=(1, 8),   # Position of the note (bar index 1, value 8)
    xytext=(1.3, 9),  # Position of the text
    arrowprops=dict(facecolor='black', arrowstyle='->')  # Arrow format
)

# Add axis labels and titles
plt.xlabel('Kategorien')
plt.ylabel('Werte')
plt.title('Balkendiagramm mit Hinweis')

# Add legend
plt.legend()

# Save diagram
plt.savefig('Balkendiagramm.jpeg', format='jpeg')

# Show diagram
plt.show()



import pandas as pd
liste = pd.Series([10, 15, 20, 25, 30])
print(liste)


zeitreihe = pd.date_range("1.1.2024", "31.1.2024")
print(zeitreihe)

tabelle = pd.DataFrame([[10, 15, 20], [5, 10, 15]])
print(tabelle)


import matplotlib.pyplot as plt

# Eine Liste von Zahlen
werte = [1, 3, 2, 5, 7, 6]

# Liniendiagramm erstellen
plt.plot(werte)

# Diagramm anzeigen
plt.show()



import pandas as pd

# Erstellen einer Series mit gemischten Datentypen
serie = pd.Series([1, "Text", 3.14, True])
print(serie)

import pandas as pd
import numpy as np
liste = pd.Series(np.arange(10, 60, 10))
print(liste)

liste = pd.Series({
    'Filiale Nord': 100000,
    'Filiale Ost': 200000,
    'Filiale Süd': 300000,
    'Filiale West': 400000
})
print(liste)

import pandas as pd

# Dictionary erstellen
data = {"Name": ["Anna", "Ben", "Chris"], "Alter": [25, 30, 35]}

# Umwandlung in ein DataFrame
df = pd.DataFrame(data)

print(df)


import pandas as pd

# Erstellen einer Zeitreihe mit jährlicher Frequenz
zeitreihe = pd.date_range(start="2020-01-01", periods=5, freq="Y")

print(zeitreihe)


import pandas as pd

# Erstellen einer Zeitreihe mit einer definierten Anzahl von Perioden
zeitreihe = pd.date_range(start="2023-01-01", periods=5, freq="D")

print(zeitreihe)


import pandas as pd

# Erstellen einer Zeitreihe
zeitreihe = pd.date_range(start="2023-01-01", periods=5, freq="D")

# Formatieren der Zeitreihe
formatierte_zeitreihe = zeitreihe.strftime("%d-%m-%Y")

print(formatierte_zeitreihe)


liste = pd.Series([100, 200, 300], index=['A', 'B', 'C'])
print(liste)


index = [1, 2, 3]
werte = [100, 200, 300]
liste = pd.Series(werte, index=index)
print(liste[1])  # Gibt 100 zurück

print(liste[liste > 100])


import pandas as pd

# Erstellen einer Liste mit benutzerdefiniertem Index
data = [10, 20, 30]
index = ["a", "b", "c"]

df = pd.DataFrame(data, index=index, columns=["Werte"])
print(df)


liste = pd.Series([1, 2, None])
print(liste.isnull())  # Gibt True für NaN zurück

liste = liste.dropna()
print(liste)


liste = liste.fillna(0)
print(liste)


import pandas as pd
import numpy as np

# Erstellen eines DataFrames mit fehlenden Werten
data = {"A": [1, 2, np.nan], "B": [4, np.nan, 6]}
df = pd.DataFrame(data)
print(df)

# Beispiel einer Liste
meine_liste = [10, 20, 30, 40]

# Zugriff auf das letzte Element
letztes_element = meine_liste[-1]
print(f"Das letzte Element ist: {letztes_element}")


import pandas as pd
import numpy as np

# Beispiel-Liste
meine_liste = [1, 2, np.nan, 4]

# Prüfen, ob ein Element NaN ist
ist_nan = pd.isna(meine_liste)
print(ist_nan)

import pandas as pd
liste = pd.Series([1, 3, 5])
print(liste)

import numpy as np
import pandas as pd
werte = pd.Series(np.arange(1, 102, 5))
print(werte)

import pandas as pd
zeitreihe = pd.date_range(start="2024-12-01", end="2024-12-31", freq="B")
print(zeitreihe)


zeitreihe = pd.date_range(start="2022-02-01", periods=10)
print(zeitreihe)


zeitreihe = pd.date_range(start="2022-01-01", periods=5)
formatiert = zeitreihe.strftime("%d/%m/%Y")
print(formatiert)


import pandas as pd
umsaetze = pd.Series([10.10, 20.20, 30.30, 40.40])
tabelle = pd.DataFrame(umsaetze)
print(tabelle)


import pandas as pd
quartale = ["Quartal 1", "Quartal 2", "Quartal 3", "Quartal 4"]
index_filialen = ["Filiale 1", "Filiale 2", "Filiale 3"]
filiale_1 = pd.Series([10.10, 20.20, 30.30, 40.40], index=quartale)
filiale_2 = pd.Series([100.10, 200.20, 300.30, 400.40], index=quartale)
filiale_3 = pd.Series([1000.10, 2000.20, 3000.30, 4000.40], index=quartale)
tabelle = pd.DataFrame([filiale_1, filiale_2, filiale_3], index=index_filialen)
print(tabelle)

import pandas as pd
umsaetze = [
    {"Quartal 1": 10.10, "Quartal 2": 20.20, "Quartal 3": 30.30, "Quartal 4": 40.40},
    {"Quartal 1": 100.10, "Quartal 2": 200.20, "Quartal 3": 300.30, "Quartal 4": 400.40},
    {"Quartal 1": 1000.10, "Quartal 2": 2000.20, "Quartal 3": 3000.30, "Quartal 4": 4000.40}
]
tabelle = pd.DataFrame(umsaetze)
print(tabelle)



import numpy as np
struktur = np.dtype([
    ("Standort", str, 15),
    ("Quartal 1", np.float32),
    ("Quartal 2", np.float32),
    ("Quartal 3", np.float32),
    ("Quartal 4", np.float32)
])
umsaetze = np.array([("Bonn", 10.10, 20.20, 30.30, 40.40),
                     ("Berlin", 100.10, 200.20, 300.30, 400.40)], struktur)
tabelle = pd.DataFrame(umsaetze)
print(tabelle)


tabelle = pd.DataFrame([filiale_1, filiale_2, filiale_3], columns=["Quartal 1", "Quartal 4"])
print(tabelle["Quartal 1"])
print(tabelle.loc["Filiale 1"])
print(tabelle.iloc[0])
print(tabelle["Quartal 1"]["Filiale 1"])
print(tabelle.iloc[1][1])
print(tabelle[tabelle["Quartal 1"] > 500])


import pandas as pd

# Erstellen eines DataFrames aus einem Dictionary
data = {
    "Name": ["Anna", "Ben", "Charlie"],
    "Alter": [28, 34, 25],
    "Stadt": ["Berlin", "München", "Hamburg"]
}

df = pd.DataFrame(data)

# Ausgabe des DataFrames
print(df)


import pandas as pd

# Erstellen eines DataFrames
data = {
    "Name": ["Anna", "Ben", "Charlie"],
    "Alter": [28, 34, 25],
    "Stadt": ["Berlin", "München", "Hamburg"]
}

df = pd.DataFrame(data)

# Darstellung bestimmter Spalten
selected_columns = df[["Name", "Stadt"]]

# Ausgabe der ausgewählten Spalten
print(selected_columns)


print(tabelle.sum())  # Spaltensumme
print(tabelle.mean(axis=1))  # Durchschnitt pro Zeile


gefiltert = tabelle.dropna()
print("\nNach Entfernen fehlender Werte:")
print(gefiltert)

# Fehlende Werte ersetzen
ersetzt = tabelle.fillna(0)
print("\nNach Ersetzen fehlender Werte mit 0:")
print(ersetzt)


arrays = [
    ["a", "a", "b", "b"],
    [1, 2, 1, 2]
]
index = pd.MultiIndex.from_arrays(arrays, names=("Group", "Subgroup"))
df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], index=index, columns=["X", "Y"])
print(df)



import pandas as pd

# Erstellen eines DataFrames
data = {
    "Name": ["Anna", "Ben", "Charlie"],
    "Alter": [28, 34, 25],
    "Stadt": ["Berlin", "München", "Hamburg"]
}

df = pd.DataFrame(data)

# Löschen einer Spalte
df_ohne_stadt = df.drop(columns=["Stadt"])

# Löschen einer Zeile
df_ohne_ben = df.drop(index=1)

# Ausgabe nach Löschen
print("Ohne Spalte 'Stadt':")
print(df_ohne_stadt)

print("\nOhne Zeile mit Index 1:")
print(df_ohne_ben)



import pandas as pd

# Erstellen von zwei DataFrames
data1 = {
    "ID": [1, 2, 3],
    "Name": ["Anna", "Ben", "Charlie"]
}

data2 = {
    "ID": [1, 2, 4],
    "Alter": [28, 34, 30]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Tabellen verbinden
result = pd.merge(df1, df2, on="ID", how="inner")

# Ausgabe des Ergebnisses
print("Verbundenes DataFrame:")
print(result)



import pandas as pd

# Listen erstellen
liste_1 = [1, 2, 3]
liste_2 = [4, 5, 6]
liste_3 = [7, 8, 9]
mein_index = ['A', 'B', 'C']

# Tabelle erzeugen
tabelle = pd.DataFrame({
    "Spalte 1": liste_1,
    "Spalte 2": liste_2,
    "Spalte 3": liste_3
}, index=mein_index)

print(tabelle)

#------------------
# Tabelle erzeugen
tabelle = pd.DataFrame({
    "Spalte 1": liste_1,
    "Spalte 2": liste_2,
    "Spalte 3": liste_3
}, index=mein_index)

# Nur bestimmte Spalten übernehmen
tabelle_reduziert = tabelle[["Spalte 1", "Spalte 3"]]

print(tabelle_reduziert)

print(tabelle["Spalte 1"])
print(tabelle.loc["Zeile 1"])

print(tabelle.iloc[0, 0])
print(tabelle.loc[:, "Spalte 1":"Spalte 10"])


tabelle["Neue Spalte"] = [10, 20, 30]
print(tabelle)

tabelle = tabelle.drop("Spalte 1", axis=1)

print(tabelle.shape)
# Ausgabe: (Zeilen, Spalten)

index = pd.MultiIndex.from_tuples([("Gruppe 1", "A"), ("Gruppe 1", "B"), ("Gruppe 2", "A")])
tabelle = pd.DataFrame({"Wert": [10, 20, 30]}, index=index)
print(tabelle)

import pandas as pd
data = pd.read_csv('daten.csv', sep=';', header=0)
print(data.head())

# Excel-Datei einlesen
excel_data = pd.read_excel("daten.xlsx", sheet_name="Tabelle1")
print(excel_data)

data = pd.read_json('daten.json')

# Daten in eine CSV-Datei schreiben
data.to_csv("export.csv", sep=";", index=False)

# Daten in eine Excel-Datei schreiben
data.to_excel("export.xlsx", sheet_name="Ergebnisse")

import sqlite3
conn = sqlite3.connect('datenbank.db')
df = pd.read_sql('SELECT * FROM tabelle', conn)

df.to_sql('tabelle', conn, if_exists='replace', index=False)


import pandas as pd

# CSV-Datei laden, ohne die erste Zeile als Spaltenbeschriftung zu verwenden
df = pd.read_csv("datei.csv", header=None)

# Ausgabe der geladenen Daten
print(df)


import pandas as pd

# Beispiel-Daten
daten = {"Name": ["Alice", "Bob", "Charlie"], "Alter": [25, 30, 35]}
df = pd.DataFrame(daten)

# Daten in eine CSV-Datei schreiben
df.to_csv("output.csv", index=False)

print("Die Daten wurden erfolgreich in 'output.csv' gespeichert.")

import pandas as pd

# CSV-Datei öffnen und in der Variablen speichern
test = pd.read_csv("test.csv")

import pandas as pd

# CSV-Datei laden und eigene Spaltenüberschriften setzen
test = pd.read_csv("test.csv", names=["A", "B", "C"], header=None)

import pandas as pd

# Pandas-Optionen ändern, um alle Zeilen auszugeben
pd.set_option("display.max_rows", None)

import pandas as pd

# CSV-Datei laden und die erste Spalte als Index verwenden
test = pd.read_csv("test.csv", index_col=0)
df.to_csv("output.csv", index=False)

# CSV-Datei mit Semikolon als Trennzeichen laden
df = pd.read_csv("test.csv", sep=";")


#---------------
import pandas as pd
# Example list with NaN values
liste = pd.Series([1, 2, None, 4, None, 6])
# Replace non-existent values with 0
liste.fillna(0, inplace=True)
print(liste)

#---------------
import pandas as pd
# Create a sample table
tabelle = pd.DataFrame({
    "Spalte1": [1, 2, 3],
    "Spalte3": [10, 20, 30]
})
# Add new column with values
tabelle.insert(1, "Buchstabe", ["A", "B", "C"])
print(tabelle)

import pandas as pd
# Definition of the indices
index_1 = ["A", "B", "C", "D"]
index_2 = ["A", "B", "E", "F"]
# Values for the two lists
werte_1 = [1, 2, 3, 4]
werte_2 = [9, 8, 7, 6]
# Creation of the Pandas series with the indices
liste_1 = pd.Series(werte_1, index=index_1)
liste_2 = pd.Series(werte_2, index=index_2)
# Multiplication of the two lists
result = liste_1 * liste_2
print(result)




# Dictionary with the days of the week and their indices
tage = {1: "Montag", 2: "Dienstag", 3: "Mittwoch", 4: "Donnerstag", 5: "Freitag", 6: "Samstag", 7: "Sonntag"}
# List of weekdays based on the indices
wochentage_liste = [tage[i] for i in range(1, 8)]
print("Liste der Wochentage:")
print(wochentage_liste)


import pandas as pd
# Creation of the list with the values and index
werte = [100, 200, 300, 400, 500]
index = ["A", "B", "C", "D", "E"]
# Creation of the pandas Series
liste = pd.Series(werte, index=index)
print(liste)


import pandas as pd
import numpy as np
# Create first line with numpy
erste_zeile = np.arange(1, 11)
# Create DataFrame with the first line
tabelle = pd.DataFrame([erste_zeile])
# Create further lines in a loop
for i in range(2, 11):
    neue_zeile = erste_zeile * i
    tabelle = pd.concat([tabelle, pd.DataFrame([neue_zeile])], ignore_index=True)
# Customize row and column labels
tabelle.index = [f"{i}-mal" for i in range(1, 11)]
tabelle.columns = [f"{i}" for i in range(1, 11)]
print(tabelle)


import pandas as pd
# Import CSV file
data = pd.read_csv("pth08_aufgabe11.csv")
# Totalize, calculate minimum and maximum
total = data.sum().sum()  
min_value = data.min().min()  
max_value = data.max().max()
# Sort values
sorted_values = data.values.flatten()  
sorted_values = sorted(sorted_values)
# Output first 25 values
first_values = sorted_values[:25]
# Output
print(f"Gesamtsumme der Werte: {total}")
print(f"Minimum der Werte: {min_value}")
print(f"Maximum der Werte: {max_value}")
print("Erste 25 Werte der sortierten Liste:", first_values)




import pandas as pd
import matplotlib.pyplot as plt
# Read file
datei_name = "pth08_aufgabe11.csv" 
daten = pd.read_csv(datei_name, header=None)
# Merge values into a single column
werte = daten.stack()
# Create the histogram
plt.hist(werte, bins=20, color='blue', edgecolor='black')
# Label diagram
plt.title("Histogramm der Werte aus der Datei") 
plt.xlabel("Wertebereich")  
plt.ylabel("Häufigkeit")
# Show diagram
plt.show()


import pandas as pd
# Import data from the CSV file
datei_name = "pth08_aufgabe13.csv"
daten = pd.read_csv(datei_name)
# Add new column with the sum of the rows
daten['Summe'] = daten.sum(axis=1)
# Output complete table
print("Vollständige Tabelle mit Summenspalte:")
print(daten)
# Save table in a new CSV file (without index)
export_datei = "pth08_aufgabe13_edit.csv"
daten.to_csv(export_datei, index=False)
print(f"\nDie bearbeitete Tabelle wurde in der Datei '{export_datei}' gespeichert.")


import statistics
daten = [5, 8, 9, 9, 5]
print("Mittelwert:", statistics.mean(daten))
print("Median:", statistics.median(daten))
print("Standardabweichung:", statistics.stdev(daten))


import numpy as np
daten = [5, 8, 9, 9, 5]
print("Mittelwert:", np.mean(daten))
print("Standardabweichung:", np.std(daten))


import pandas as pd
daten = {'Werte': [5, 8, 9, 9, 5]}
df = pd.DataFrame(daten)
print(df.describe())
print("Korrelation:", df.corr())


import numpy as np
import statistics

# Beispiel-Daten
daten = [10, 20, 30, 40, 50, 60, 70]

# Berechnung des Medians
median = statistics.median(daten)

# Berechnung weiterer statistischer Werte
mittelwert = np.mean(daten)
spannweite = np.ptp(daten)  # Range (Maximum - Minimum)
minimum = np.min(daten)
maximum = np.max(daten)
standardabweichung = np.std(daten)

# Ausgabe der Ergebnisse
print(f"Datensatz: {daten}")
print(f"Median: {median}")
print(f"Mittelwert: {mittelwert}")
print(f"Spannweite: {spannweite}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Standardabweichung: {standardabweichung}")


import statistics
dezile = [statistics.quantiles(meine_liste, n=10)]

import random
wert = random.normalvariate(50, 10)

import numpy as np
werte = np.random.normal(30, 2, 20)

import numpy as np
werte = np.random.default_rng().normal(loc=30, scale=2, size=20)


import numpy as np

# Beispiel-Daten
meine_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Erstellung einer Stichprobe mit 5000 Elementen (mit oder ohne Zurücklegen)
stichprobe = np.random.choice(meine_liste, size=5000, replace=True)
# Ausgabe der ersten 10 Elemente der Stichprobe
print(stichprobe[:10])


from itertools import permutations
liste = ["A", "B", "C"]
permutationen = permutations(liste)
for p in permutationen:
    print(p)


import itertools
# Beispiel: Permutationen einer Liste
objekte = ['A', 'B', 'C']
permutationen = list(itertools.permutations(objekte))
print(permutationen)


import itertools
# Beispiel: Kombinationen von 2 Elementen aus einer Liste
objekte = ['A', 'B', 'C', 'D']
kombinationen = list(itertools.combinations(objekte, 2))
print(kombinationen)

from itertools import combinations
liste = ["A", "B", "C"]
kombinationen = combinations(liste, 2)
for k in kombinationen:
    print(k)

import itertools
# Beispiel: Variation mit Wiederholung
objekte = ['A', 'B', 'C']
variationen = list(itertools.product(objekte, repeat=2))
print(variationen)

from itertools import product
liste = ["A", "B", "C"]
variationen = product(liste, repeat=2)
for v in variationen:
    print(v)
    

import statistics
# Example data list
my_list = [3, 7, 8, 5, 12, 14, 21, 13, 18]
# Sort list
sorted_list = sorted(my_list)
# Calculate quartiles (n=4 for quartiles)
q1, q2, q3 = statistics.quantiles(sorted_list, n=4)
print(f"Q1: {q1}, Q2 (Median): {q2}, Q3: {q3}")

#--------------


import itertools

# Set of elements
elements = ['A', 'B', 'C', 'D']

# Permutations (all possible orders)
permutations_no_repetition = list(itertools.permutations(elements, 4))
permutations_with_repetition = list(itertools.product(elements, repeat=4))

# Combinations (order does not matter)
combinations_no_repetition = list(itertools.combinations(elements, 4))
combinations_with_repetition = list(itertools.combinations_with_replacement(elements, 4))

# Variations (ordered subsets)
variations_no_repetition = list(itertools.permutations(elements, 4))
variations_with_repetition = list(itertools.product(elements, repeat=4))

# Output results with count
print("Permutationen ohne Wiederholung:")
for p in permutations_no_repetition:
    print(p)
print(f"Anzahl: {len(permutations_no_repetition)}\n")

print("\nPermutationen mit Wiederholung:")
for p in permutations_with_repetition:
    print(p)
print(f"Anzahl: {len(permutations_with_repetition)}\n")

print("\nKombinationen ohne Wiederholung:")
for k in combinations_no_repetition:
    print(k)
print(f"Anzahl: {len(combinations_no_repetition)}\n")

print("\nKombinationen mit Wiederholung:")
for k in combinations_with_repetition:
    print(k)
print(f"Anzahl: {len(combinations_with_repetition)}\n")

print("\nVariationen ohne Wiederholung:")
for v in variations_no_repetition:
    print(v)
print(f"Anzahl: {len(variations_no_repetition)}\n")

print("\nVariationen mit Wiederholung:")
for v in variations_with_repetition:
    print(v)
print(f"Anzahl: {len(variations_with_repetition)}\n")


#----------

import random

def draw_lottery_numbers():
    # Draw 6 unique numbers from the range 1..49
    numbers = random.sample(range(1, 50), 6)
    # Sort for better readability
    numbers.sort()
    return numbers

# Output a draw
result = draw_lottery_numbers()
print("Die gezogenen Lottozahlen lauten:", result)


#--------------
def code_cracker_time():
    # User input
    characters = input("Geben Sie die verfügbaren Zeichen ein (z.B. abc123!?): ")
    
    length = int(input("Geben Sie die Länge des Kennworts ein: "))

    # Number of entered characters
    num_characters = len(characters)

    # Number of possible combinations (characters^length)
    possible_combinations = num_characters ** length

    # 10 ms (= 0.01 s) per attempt
    time_in_seconds = possible_combinations * 0.01
    
    print(f"\nMögliche Kombinationen: {possible_combinations}")
    print(f"Benötigte Zeit: {time_in_seconds} Sekunden")

if __name__ == "__main__":
    code_cracker_time()

#-------------------
import pandas as pd
# Load file
file_path = "pth08_aufgabe13.csv"
data = pd.read_csv(file_path)
# Calculate row sums, summing only numeric columns and rounding to 2 decimal places
data["Summe"] = data.sum(axis=1, numeric_only=True).round(2)
# Display result
print(data)
# Save without index
export_file = "pth08_aufgabe13_edit.csv"
data.to_csv(export_file, index=False)
print(f"\nDie bearbeitete Tabelle wurde gespeichert: {export_file}")



import pandas as pd
# Example list with NaN values
example_list = pd.Series([1, 2, None, 4, None, 6])
# Replace NaN values with 0
example_list = example_list.fillna(0)
print(example_list)

data["Summe"] = data.select_dtypes(include=["number"]).sum(axis=1).round(2)

#-----------
import pandas as pd
import numpy as np
# Creates the multiplication table using list comprehension
table = pd.DataFrame(
    [[i * j for j in range(1, 11)] for i in range(1, 11)]
)
# Sets appropriate row and column labels
table.index = [f"{i}-times" for i in range(1, 11)]
table.columns = [f"{i}" for i in range(1, 11)]
# Print table
print(table)


import pandas as pd
# Load file
file_path = "pth08_aufgabe13.csv"
data = pd.read_csv(file_path)
# Calculate row sums, summing only numeric columns and rounding to 2 decimal places
data["Summe"] = data.select_dtypes(include=["number"]).sum(axis=1).round(2)
# Display result
print(data)
# Save without index
export_file = "pth08_aufgabe13_edit.csv"
data.to_csv(export_file, index=False)
print(f"\nDie bearbeitete Tabelle wurde gespeichert: {export_file}")


import numpy as np

# Ursprüngliche Daten
daten = np.array([1, 10, 100, 1000, 10000])

# Logarithmische Transformation (Basis 10)
transformierte_daten = np.log10(daten)

print("Originale Daten:", daten)
print("Transformierte Daten:", transformierte_daten)

import pandas as pd

datum = pd.to_datetime("2025-01-29")
print(datum)

import pandas as pd

# Erster DataFrame
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})

# Zweiter DataFrame
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Alter': [25, 30, 35]})

# Verbindung der Tabellen über die Spalte "ID"
df_merged = pd.merge(df1, df2, on='ID')

print(df_merged)

text = "Hallo Welt, Welt ist schön."
# Ersetze alle Vorkommen von "Welt" durch "Erde"
neuer_text = text.replace("Welt", "Erde")
print(neuer_text)  # Ausgabe: "Hallo Erde, Erde ist schön."

# Ersetze nur das erste Vorkommen von "Welt"
neuer_text = text.replace("Welt", "Erde", 1)
print(neuer_text)  # Ausgabe: "Hallo Erde, Welt ist schön."




#-------------
import pandas as pd

# Einlesen der Kundendaten
kunden_tabelle = pd.read_csv("kunden.csv", sep=";")
print(kunden_tabelle.head())

# Einlesen der Bestellungen
bestellungen_tabelle = pd.read_csv("bestellungen.csv", sep=";")
print(bestellungen_tabelle.head())


# Überprüfung auf fehlende Werte
if bestellungen_tabelle.isnull().any(axis=None):
    print("Es gibt leere Einträge:")
    print(bestellungen_tabelle[bestellungen_tabelle.isnull().any(axis=1)])
    # Entfernen der fehlerhaften Zeilen
    bestellungen_tabelle = bestellungen_tabelle.dropna()

bestellungen_tabelle["KNR"] = bestellungen_tabelle["KNR"].astype(int)

max_knr = kunden_tabelle["KNR"].max()
check = bestellungen_tabelle[bestellungen_tabelle["KNR"] > max_knr]
if not check.empty:
    print("Es gibt ungültige Kundennummern, diese werden entfernt.")
    bestellungen_tabelle.drop(check.index, inplace=True)

# Konvertierung der Datumsangaben in das datetime-Format
bestellungen_tabelle["DATUM"] = pd.to_datetime(bestellungen_tabelle["DATUM"])

# Beispiel: Entfernen von Bestellungen außerhalb des Jahres 2021
check = bestellungen_tabelle[
    (bestellungen_tabelle["DATUM"] < "2021-01-01") | (bestellungen_tabelle["DATUM"] > "2021-12-31")
]
if not check.empty:
    bestellungen_tabelle.drop(check.index, inplace=True)

kunden_bestellungen_tabelle = pd.merge(left=kunden_tabelle, right=bestellungen_tabelle, on="KNR")
kunden_bestellungen_tabelle.to_csv("kunden_bestellungen.csv", index=False, sep=";")

tabelle.drop(["KNR", "NAME", "DATUM"], axis=1, inplace=True)

# Entfernen von Leerzeichen und Aufteilen der Artikel-Spalte
tabelle["ARTIKEL"] = tabelle["ARTIKEL"].str.replace(" ", "")
tabelle[["ARTIKEL1", "ARTIKEL2", "ARTIKEL3"]] = tabelle["ARTIKEL"].str.split(",", expand=True)

# Umwandeln der Artikelnummern in Integer
tabelle["ARTIKEL1"] = tabelle["ARTIKEL1"].astype(int)
tabelle["ARTIKEL2"] = tabelle["ARTIKEL2"].astype(int)
tabelle["ARTIKEL3"] = tabelle["ARTIKEL3"].astype(int)
tabelle.to_csv("region_bestellungen.csv", index=False, sep=";")

liste_region = pd.unique(tabelle["REGION"])
liste_artikel1 = pd.unique(tabelle["ARTIKEL1"])
liste_artikel2 = pd.unique(tabelle["ARTIKEL2"])
liste_artikel3 = pd.unique(tabelle["ARTIKEL3"])

werte = []
for region in liste_region:
    for artikel in liste_artikel1:
        anzahl = len(tabelle[(tabelle["REGION"] == region) & (tabelle["ARTIKEL1"] == artikel)])
        werte.append([region, artikel, anzahl])

kumuliert = pd.DataFrame(werte, columns=["REGION", "ARTIKEL", "ANZAHL"])

gruppe = kumuliert.groupby(["ARTIKEL"]).sum()
print(gruppe)

for region in liste_region:
    tabelle_region = kumuliert[kumuliert["REGION"] == region]
    gruppe = tabelle_region.groupby(["ARTIKEL"]).sum()
    gruppe.plot(kind="bar", y="ANZAHL", title="Region " + str(region))

import matplotlib.pyplot as plt

figur, achsen = plt.subplots(1)
for region in liste_region:
    tabelle_region = kumuliert[kumuliert["REGION"] == region]
    gruppe = tabelle_region.groupby(["ARTIKEL"]).sum()
    plt.plot(gruppe["ANZAHL"], label="Region " + str(region))

plt.title("Zusammenfassung der Verkaufszahlen")
plt.legend()
plt.show()

import pandas as pd
# Erstellen einer pandas-Serie mit doppelten Werten
serie = pd.Series([1, 2, 2, 3, 4, 4, 5])
# Anwenden der unique()-Funktion
einzigartige_werte = serie.unique()
print(einzigartige_werte)


import pandas as pd
# Erstellen eines DataFrame
df = pd.DataFrame({
    'Kategorie': ['A', 'B', 'A', 'B', 'A'],
    'Wert': [10, 20, 30, 40, 50]
})
# Gruppieren nach 'Kategorie' und Berechnen der Summe der Werte
gruppiert = df.groupby('Kategorie')['Wert'].sum()
print(gruppiert)


import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [0, 0, 1], 'B': [False, False, True]})
print(df.any())

pruef = tabelle[tabelle['Nummer'] > 100]  # Filterung der Zeilen

# Überprüfen, ob die Tabelle Werte enthält
if not pruef.empty:
    print("Die Tabelle enthält Werte.")
else:
    print("Die Tabelle ist leer.")
    
tabelle_3 = pd.merge(tabelle_1, tabelle_2, on='Nummer')

tabelle['Name'] = tabelle['Name'].str.replace(" ", "")
 

import pandas as pd
tag = pd.to_datetime("31.12.2021")
print(tag)  # Ausgabe: 2021-12-31 00:00:00
print(tag.day_name())  # Ausgabe: Friday

print(tag.strftime("%d.%m.%Y"))  # Ausgabe: 31.12.2021

tag = tag + pd.Timedelta("1 w")  # Eine Woche addieren
tag = tag - pd.Timedelta("3 d")  # Drei Tage subtrahieren
print(tag)  # Neue Datumsangabe

tage = pd.date_range("02.01.2021", "02.07.2021")
print(tage)

import pandas as pd

datum = pd.to_datetime("2025-01-29")
print(type(datum))  # Ausgabe: <class 'pandas._libs.tslibs.timestamps.Timestamp'>

import pandas as pd
# Erzeugung einer Zeitreihe vom 1. Januar 2025 bis zum 10. Januar 2025 mit täglicher Frequenz
zeitreihe = pd.date_range(start="2025-01-01", end="2025-01-10", freq="D")
print(zeitreihe)

zeitreihe = pd.date_range("1.1.2022", periods=365, freq="D")
print(zeitreihe)

uhrzeit = pd.to_datetime("31.12.2021 13:00")
uhrzeit = uhrzeit + pd.Timedelta("17 h")  # 17 Stunden addieren
print(uhrzeit)  # Ausgabe: 2022-01-01 06:00:00

differenz = uhrzeit_2 - uhrzeit_1
print(differenz)  # 0 days 17:00:00

import numpy as np
zeitreihe = pd.date_range("1.1.2022", periods=365, freq="D")
rng = np.random.default_rng()
werte = rng.integers(1, 101, 365)  # 365 zufällige Werte
serie = pd.Series(werte, index=zeitreihe)
print(serie)

import numpy as np
rng = np.random.default_rng()
werte = rng.integers(1, 101, 365)
zeitreihe = pd.Series(werte, index=zeitreihe)
print(zeitreihe)

gruppe = serie.groupby(pd.Grouper(freq="M")).mean()

import pandas as pd
import matplotlib.pyplot as plt

# Wetterdaten einlesen
tabelle_1 = pd.read_csv("mpi_roof_2020a.csv", encoding="ANSI")
tabelle_2 = pd.read_csv("mpi_roof_2020b.csv", encoding="ANSI")
tabelle = pd.concat([tabelle_1, tabelle_2])

# Spalten löschen
tabelle.drop(["p (mbar)"], axis=1, inplace=True)
tabelle["Date Time"] = pd.to_datetime(tabelle["Date Time"])

# Durchschnittswerte pro Monat berechnen
gruppe = tabelle.groupby(pd.Grouper(key="Date Time", freq="M")).mean()

# Diagramme erzeugen
gruppe.plot(kind="bar", y="T (degC)", title="Durchschnittstemperatur")
gruppe.plot(kind="bar", y="rain (mm)", title="Durchschnittsniederschlag")
plt.show()

# Berechnung der Korrelation zwischen Temperatur und Niederschlag
print(tabelle.corr())

import pandas as pd
datum = pd.Timestamp("2025-01-29")
print(datum.day_name())  # Ausgabe: Mittwoch
import pandas as pd
datum = pd.to_datetime("29.01.2025", format="%d.%m.%Y")
print(datum)  # Ausgabe: 2025-01-29 00:00:00

import pandas as pd
datum = pd.Timestamp("2025-01-29")
neues_datum = datum + pd.Timedelta(weeks=2)
print(neues_datum)  # Ausgabe: 2025-02-12 00:00:00

import pandas as pd
zeitreihe = pd.date_range(start="2022-01-01", end="2022-03-31", freq="D")
print(zeitreihe)

import pandas as pd
arbeitstage = pd.date_range(start="2024-04-01", end="2024-04-30", freq="B")
print(arbeitstage)

import pandas as pd
datum1 = pd.Timestamp("2023-12-31")
datum2 = pd.Timestamp("2024-02-14")
differenz = datum2 - datum1
print(differenz)  # Ausgabe: 45 days 00:00:00

import pandas as pd
# Beispiel-Daten erstellen
daten = {'Datum': pd.date_range(start="2025-01-01", periods=10, freq="D"),
         'Wert': [5, 3, 8, 6, 7, 2, 9, 1, 4, 5]}

reihe = pd.DataFrame(daten)
# Nach Tagen gruppieren und Summe berechnen
ergebnis = reihe.groupby(reihe['Datum'].dt.date)['Wert'].sum()
print(ergebnis)


import pandas as pd
import matplotlib.pyplot as plt
# Textdatei einlesen
with open("textdatei.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()
# Sonderzeichen entfernen
for zeichen in [",", ".", ":", ";", "!", "?"]:
    text = text.replace(zeichen, "")
# Stoppwörter entfernen
stoppwörter = ["der", "die", "das", "und", "ist", "ein", "zu", "mit"]
wörter = [wort for wort in text.split() if wort not in stoppwörter]
# Häufigkeit berechnen
wort_freq = pd.Series(wörter).value_counts()
# Top 10 häufigste Wörter ausgeben
print(wort_freq.head(10))
# Diagramm erstellen
wort_freq.head(10).plot(kind="bar", title="Häufigste Wörter")
plt.show()

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
# Kassendaten einlesen
df = pd.read_csv("kassendaten.csv", sep=";")
# Spalte mit Produktnummern aufteilen
df["Produkte"] = df["Produkte"].str.split(",")
# Erstellen der Matrix mit 0 und 1 (Produkt vorhanden oder nicht)
produkte_set = set(item for sublist in df["Produkte"] for item in sublist)
for produkt in produkte_set:
    df[produkt] = df["Produkte"].apply(lambda x: 1 if produkt in x else 0)
# Apriori-Algorithmus zur Ermittlung häufig gekaufter Produktkombinationen
frequente_muster = apriori(df.drop(columns=["Produkte"]), min_support=0.05, use_colnames=True)
# Ermittlung der Assoziationsregeln
regeln = association_rules(frequente_muster, metric="lift", min_threshold=1.0)
# Ausgabe der wichtigsten Regeln
print(regeln[["antecedents", "consequents", "support", "confidence", "lift"]])


import pandas as pd
# Example DataFrame with a column "Text"
table = pd.DataFrame({
    'Text': ['Hallo;Welt', 'Hello;World']
})
# Split the "Text" column into "Text1" and "Text2" at each semicolon
table[['Text1', 'Text2']] = table['Text'].str.split(';', expand=True)
print(table)

#-------

import pandas as pd
# Create date 1.1.2030
date = pd.to_datetime("2030-01-01")
# Output weekday for 1.1.2030
print("Datum:", date)
print("Wochentag:", date.day_name())
# Add 10 days
new_date = date + pd.Timedelta(days=10)
# Output new date and weekday
print("Neues Datum:", new_date)
print("Neuer Wochentag:", new_date.day_name())

#-------

import pandas as pd
# List of the last days of each month in the year 2022
last_days = pd.date_range(start="2022-01-31", end="2022-12-31", freq="ME")
# Add 14 days
new_dates = last_days + pd.Timedelta(days=14)
# Output the original and new dates with weekdays
result = pd.DataFrame({
    "Letzter Tag": last_days,
    "Wochentag (alt)": last_days.day_name(),
    "Neues Datum (+14 Tage)": new_dates,
    "Wochentag (neu)": new_dates.day_name()
})
print(result)

#--------
"""
Vorbereiten der Daten
"""
# pandas als pd importieren
import pandas as pd

# die Kunden in eine Tabelle lesen
kunden_tabelle = pd.read_csv("kunden.csv", sep=";")
# die ersten fünf Einträge ausgeben
print(kunden_tabelle.head())

# die Bestellungen in eine Tabelle lesen
bestellungen_tabelle = pd.read_csv("bestellungen.csv", sep=";")
# die ersten fünf Einträge ausgeben
print(bestellungen_tabelle.head())

# nach dem Wert NaN suchen
if bestellungen_tabelle.isnull().any(axis=None):
    print("Es gibt leere Einträge.")
    # die Einträge ausgeben
    print(bestellungen_tabelle[bestellungen_tabelle.isnull().any(axis=1)])
    # die Einträge löschen
    bestellungen_tabelle = bestellungen_tabelle.dropna()

# den Wert für die Kundennummer umbauen
bestellungen_tabelle["KNR"] = bestellungen_tabelle["KNR"].astype(int)

# **** Änderung: Prüfung, ob alle Kundennummern größer als 0 sind ****
invalid_knr = bestellungen_tabelle[bestellungen_tabelle["KNR"] <= 0]
if not invalid_knr.empty:
    print("Es gibt Kundennummern, die kleiner oder gleich 0 sind:")
    print(invalid_knr)
    # diese ungültigen Einträge löschen
    bestellungen_tabelle.drop(invalid_knr.index, inplace=True)
# **************************************************************

# und zur Kontrolle ausgeben
print(bestellungen_tabelle.head())

# gibt es ungültige Kundennummern (größer als der maximale gültige Wert in kunden_tabelle)?
max_knr = kunden_tabelle["KNR"].max()
# eine neue Tabelle mit den ungültigen Nummern erzeugen
check = bestellungen_tabelle[bestellungen_tabelle["KNR"] > max_knr]
# ist die Tabelle nicht leer?
if not check.empty:
    print("Es gibt ungültige Kundennummern, die größer als der maximale gültige Wert sind.")
    # die Einträge löschen
    bestellungen_tabelle.drop(check.index, inplace=True)

# gibt es ungültige Datumsangaben?
# die Spalte in ein Datum umwandeln
bestellungen_tabelle["DATUM"] = pd.to_datetime(bestellungen_tabelle["DATUM"])
# eine neue Tabelle mit den ungültigen Einträgen erzeugen
check = bestellungen_tabelle[(bestellungen_tabelle["DATUM"] > "31.12.2021") | (bestellungen_tabelle["DATUM"] < "1.1.2021")]
print(check)
# ist die Tabelle nicht leer?
if not check.empty:
    print("Es gibt ungültige Datumsangaben.")
    # die Einträge löschen
    bestellungen_tabelle.drop(check.index, inplace=True)

#-----------------------------
import numpy as np
import pandas as pd

# === Textanalyse – Vorbereitung ===

# Den Text aus der Datei einlesen
with open("demo.txt", "r") as datei:
    text_lesen = datei.readlines()

# In ein NumPy-Array umwandeln und in Kleinbuchstaben konvertieren,
# damit die Groß-/Kleinschreibung keine Rolle spielt.
text = np.array(text_lesen)
text = np.char.lower(text)
text = np.char.strip(text)
print("Text nach Lower-Case und Strip:")
print(text)

# Sonderzeichen einlesen und aus dem Text entfernen
sonderzeichen = np.loadtxt("sonderzeichen.txt", np.str)
print("Sonderzeichen:", sonderzeichen)
for entfernen in sonderzeichen:
    text = np.char.replace(text, entfernen, "")

# Text an Leerzeichen (oder Komma, je nach Trennzeichen) aufteilen
text = np.char.split(text)
text = np.concatenate(text, axis=0)

# Stoppwörter einlesen und in Kleinbuchstaben umwandeln
stoppwoerter = np.loadtxt("stoppwoerter.txt", np.str)
stoppwoerter = np.char.lower(stoppwoerter)
print("Stoppwörter:", stoppwoerter)

# Stoppwörter aus dem Text entfernen
for entfernen in stoppwoerter:
    text = np.delete(text, np.argwhere(text == entfernen))

# Den aufbereiteten Text ausgeben und speichern
print("Aufbereiteter Text:")
print(text)
np.savetxt("demo_bearbeitet.txt", text, fmt="%s")


# === Textanalyse – Auswertung ===

# Den aufbereiteten Text einlesen
text = np.loadtxt("demo_bearbeitet.txt", np.str)
# (Optional) Erneut in Kleinbuchstaben konvertieren, falls erforderlich.
text = np.char.lower(text)
print("Text zur Auswertung:")
print(text)

# Vorkommen jedes Wortes zählen
unique, anzahl = np.unique(text, return_counts=True)

# Ergebnisse in einem DataFrame speichern
tabelle = pd.DataFrame(anzahl, index=unique)
# Nach Häufigkeit absteigend sortieren
tabelle = tabelle.sort_values(by=0, ascending=False)

# Die 10 häufigsten Wörter anzeigen und in einem Balkendiagramm darstellen
ausgabe = tabelle.head(10)
print("Die 10 häufigsten Wörter:")
print(ausgabe)
ausgabe.plot(kind="bar")



#-----------
""""
eine kleine Wetteranalyse
die Wetterdaten stammen von der Seite https://www.bgcjena.mpg.de/wetter/
"""
# pandas als pd importieren
import pandas as pd
import matplotlib.pyplot as plt

# die Daten in eine Tabelle lesen
tabelle_1 = pd.read_csv("mpi_roof_2020a.csv", encoding="ANSI")
# die ersten fünf Einträge ausgeben
print(tabelle_1.head())

# die Daten in eine Tabelle lesimport pandas as pd
import matplotlib.pyplot as plt

# 1. Read CSV files correctly with semicolon as a delimiter
df1 = pd.read_csv("/Users/mcartur/Documents/pth10_aufgabe13a.csv", sep=";")
df2 = pd.read_csv("/Users/mcartur/Documents/pth10_aufgabe13b.csv", sep=";")

# Check if any of the files are empty
if df1.empty or df2.empty:
    raise ValueError("Fehler: Mindestens eine der CSV-Dateien ist leer!")

# Check if the data is read correctly
print("Spalten in df1:", df1.columns)
print("Spalten in df2:", df2.columns)

# 2. Merge data
df = pd.concat([df1, df2], ignore_index=True)

# Check if the table has enough columns
if len(df.columns) < 2:
    raise ValueError("Fehler: Die Tabelle hat weniger als zwei Spalten! Prüfe das Trennzeichen der CSV-Datei.")

# 3. Check for missing values and remove them
df.dropna(inplace=True)

# 4. Identify and split the second column
column2 = df.columns[1]  # Get the second column
print(f"Verwende '{column2}' als zweite Spalte für die Trennung.")

# Check if values in this column are available and if there are commas
if df[column2].dtype != object:
    raise ValueError(f"Die Spalte '{column2}' enthält keine Textwerte zum Trennen.")
if df[column2].str.contains(",").sum() == 0:
    raise ValueError(f"Fehler: Die Spalte '{column2}' enthält keine Trennzeichen ','!")

# Split values into five columns (separated by commas)
new_columns = df[column2].str.split(",", expand=True)

# If fewer than five columns are created, fill with "None"
for i in range(5 - new_columns.shape[1]):
    new_columns[i + new_columns.shape[1]] = "None"

# If more than five parts are created, keep only the first five
new_columns = new_columns.iloc[:, :5]

# Rename new columns
new_columns.columns = [f"{column2}_{i+1}" for i in range(new_columns.shape[1])]

# Add new columns to the DataFrame
df = pd.concat([df, new_columns], axis=1)

# Remove the original second column
df.drop(columns=[column2], inplace=True)

# 5. Grouping by the first column
group_column = df.columns[0]

# Convert values to numeric types
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Group and calculate mean values
group_means = df.groupby(group_column).mean()
print(group_means)

# 6. Create bar chart
group_means.plot(kind="bar", title="Mittelwerte pro Gruppe")
plt.xlabel("Gruppe")
plt.ylabel("Mittelwert")
plt.tight_layout()
plt.show()

#-----
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read CSV files correctly with semicolon as a delimiter
df1 = pd.read_csv("/Users/mcartur/Documents/pth10_aufgabe13a.csv", sep=";")
df2 = pd.read_csv("/Users/mcartur/Documents/pth10_aufgabe13b.csv", sep=";")

# Check if any of the files are empty
if df1.empty or df2.empty:
    raise ValueError("Fehler: Mindestens eine der CSV-Dateien ist leer!")

# Check if the data is read correctly
print("Spalten in df1:", df1.columns)
print("Spalten in df2:", df2.columns)

# 2. Merge data
df = pd.concat([df1, df2], ignore_index=True)

# Check if the table has enough columns
if len(df.columns) < 2:
    raise ValueError("Fehler: Die Tabelle hat weniger als zwei Spalten! Prüfe das Trennzeichen der CSV-Datei.")

# 3. Check for missing values and remove them
df.dropna(inplace=True)

# 4. Identify and split the second column
column2 = df.columns[1]  # Get the second column
print(f"Verwende '{column2}' als zweite Spalte für die Trennung.")

# Check if values in this column are available and if there are commas
if df[column2].dtype != object:
    raise ValueError(f"Die Spalte '{column2}' enthält keine Textwerte zum Trennen.")
if df[column2].str.contains(",").sum() == 0:
    raise ValueError(f"Fehler: Die Spalte '{column2}' enthält keine Trennzeichen ','!")

# Split values into five columns (separated by commas)
new_columns = df[column2].str.split(",", expand=True)

# If fewer than five columns are created, fill with "None"
for i in range(5 - new_columns.shape[1]):
    new_columns[i + new_columns.shape[1]] = "None"

# If more than five parts are created, keep only the first five
new_columns = new_columns.iloc[:, :5]

# Rename new columns
new_columns.columns = [f"{column2}_{i+1}" for i in range(new_columns.shape[1])]

# Add new columns to the DataFrame
df = pd.concat([df, new_columns], axis=1)

# Remove the original second column
df.drop(columns=[column2], inplace=True)

# 5. Grouping by the first column
group_column = df.columns[0]

# Convert values to numeric types
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Group and calculate mean values
group_means = df.groupby(group_column).mean()
print(group_means)

# 6. Create bar chart
group_means.plot(kind="bar", title="Mittelwerte pro Gruppe")
plt.xlabel("Gruppe")
plt.ylabel("Mittelwert")
plt.tight_layout()
plt.show()


# Eine einfache lineare Suche
liste = range(1, 11)

for wert in liste:
    if wert == 5:
        print("Der Wert 5 wurde gefunden.")
        break  # Schleife abbrechen

    
# Eine lineare Suche mit Positionsangabe
liste = range(1, 11)
position = 1

for wert in liste:
    if wert == 5:
        print(f"Der Wert 5 wurde gefunden an Position {position}")
        break
    position += 1

import tensorflow as tf
from tensorflow import keras

# Einfaches neuronales Netz mit einer Schicht
modell = keras.Sequential([
    keras.layers.Dense(10, activation='relu', input_shape=(5,))
])

modell.compile(optimizer='adam', loss='mse')
print(modell.summary())



from nltk.chat.util import Chat, reflections

paare = [
    (r"Hallo", ["Hallo!", "Hi!", "Guten Tag!"]),
    (r"Wie geht es dir?", ["Mir geht es gut, danke!", "Ich bin eine KI, mir geht es immer gut."])
]

chatbot = Chat(paire, reflections)
print("Starte den Chatbot (tippe 'bye' zum Beenden)")
chatbot.converse()


# Binäre Suche mit Positionsrückgabe
def binaere_suche(liste, suchwert):
    start = 0
    ende = len(liste) - 1

    while start <= ende:
        mitte = (start + ende) // 2
        if liste[mitte] == suchwert:
            return mitte  # Index des gefundenen Elements
        elif liste[mitte] < suchwert:
            start = mitte + 1
        else:
            ende = mitte - 1
    return -1  # Element nicht gefunden

# Beispiel: Sortierte Liste
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binaere_suche(liste, 5))  # Gibt den Index von 5 zurück


from queue import Queue

def breitensuche(baum, start, ziel):
    besucht = set()
    besucht.add(start)
    warteschlange = Queue()
    warteschlange.put(start)

    while not warteschlange.empty():
        knoten = warteschlange.get()
        if knoten == ziel:
            return True
        for nachbar in baum[knoten]:
            if nachbar not in besucht:
                besucht.add(nachbar)
                warteschlange.put(nachbar)
    return False

# Beispiel-Baum als Dictionary
baum = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G"],
    "D": ["H", "I"],
    "E": [], "F": [], "G": [], "H": [], "I": []
}

print(breitensuche(baum, "A", "F"))  # Ausgabe: True


def tiefensuche(besucht, baum, knoten, ziel):
    if knoten == ziel:
        return True
    if knoten not in besucht:
        besucht.add(knoten)
        for nachbar in baum[knoten]:
            if tiefensuche(besucht, baum, nachbar, ziel):
                return True
    return False

# Beispiel-Baum
besucht = set()
baum = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G"],
    "D": ["H", "I"],
    "E": [], "F": [], "G": [], "H": [], "I": []
}

print(tiefensuche(besucht, baum, "A", "F"))  # Ausgabe: True

import heapq

def dijkstra(graph, start):
    distanzen = {knoten: float('inf') for knoten in graph}
    distanzen[start] = 0
    prioritaetswarteschlange = [(0, start)]

    while prioritaetswarteschlange:
        aktuelle_distanz, aktueller_knoten = heapq.heappop(prioritaetswarteschlange)
        for nachbar, kosten in graph[aktueller_knoten].items():
            distanz = aktuelle_distanz + kosten
            if distanz < distanzen[nachbar]:
                distanzen[nachbar] = distanz
                heapq.heappush(prioritaetswarteschlange, (distanz, nachbar))
    return distanzen

# Beispiel-Graph mit Distanzen
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1}
}

print(dijkstra(graph, "A"))

#----------------

import heapq

def a_star(baum, start, ziel, heuristik):
    offene_liste = []
    heapq.heappush(offene_liste, (0, start))
    g_wert = {start: 0}  # Bereits zurückgelegte Kosten
    eltern = {start: None}  # Um den Pfad rekonstruieren zu können

    while offene_liste:
        _, aktueller_knoten = heapq.heappop(offene_liste)
        if aktueller_knoten == ziel:
            # Pfad rekonstruieren
            pfad = []
            while aktueller_knoten:
                pfad.append(aktueller_knoten)
                aktueller_knoten = eltern[aktueller_knoten]
            return list(reversed(pfad))
        
        for nachbar, kosten in baum[aktueller_knoten].items():
            neue_kosten = g_wert[aktueller_knoten] + kosten
            if nachbar not in g_wert or neue_kosten < g_wert[nachbar]:
                g_wert[nachbar] = neue_kosten
                f_wert = neue_kosten + heuristik[nachbar]
                heapq.heappush(offene_liste, (f_wert, nachbar))
                eltern[nachbar] = aktueller_knoten
    return None

# Beispiel: Graph (Baum) und Heuristikwerte
baum = {
    "A": {"B": 1, "C": 4},
    "B": {"D": 2},
    "C": {"D": 1},
    "D": {}
}
# Heuristik (geschätzte Entfernung zum Ziel "D")
heuristik = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 0
}

print(a_star(baum, "A", "D", heuristik))

#------
def lineare_suche(liste, wert):
    for i in range(len(liste)):
        if liste[i] == wert:
            return i  # Index des gefundenen Werts
    return -1  # Wert nicht gefunden

liste = [10, 20, 30, 40, 50]
print(lineare_suche(liste, 30))  # Ausgabe: 2

liste = [3, 7, 1, 4, 7]
print(liste.index(7))  # Ausgabe: 1 (erstes Auftreten von 7)

liste = [1, 2, 3]
print(liste.index(5))  # ValueError: 5 is not in list

liste = [3, 7, 1, 4, 7]
print(liste.index(7, 2))  # Suche nach 7 ab Index 2 → Ausgabe: 4

import numpy as np
arr = np.array([10, 20, 30, 40])
print(np.where(arr == 30))  # Ausgabe: (array([2]),)

def binaere_suche(liste, wert):
    links, rechts = 0, len(liste) - 1
    while links <= rechts:
        mitte = (links + rechts) // 2
        if liste[mitte] == wert:
            return mitte
        elif liste[mitte] < wert:
            links = mitte + 1
        else:
            rechts = mitte - 1
    return -1

liste = [10, 20, 30, 40, 50]
print(binaere_suche(liste, 30))  # Ausgabe: 2

import numpy as np
arr = np.array([10, 20, 20, 20, 30])
indices = np.where(arr == 20)  # Alle Indizes von 20
print(indices)  # Ausgabe: (array([1, 2, 3]),)


arr = np.array([10, 20, 30, 40])
print(np.searchsorted(arr, 25))  # Ausgabe: 2 (zwischen 20 und 30)


from collections import deque
queue = deque()
queue.append("A")  # Hinten hinzufügen
queue.appendleft("B")  # Vorne hinzufügen
print(queue)  # Ausgabe: deque(['B', 'A'])


from itertools import permutations

def berechne_distanz(route, distanzmatrix):
    return sum(distanzmatrix[route[i]][route[i+1]] for i in range(len(route)-1)) + distanzmatrix[route[-1]][route[0]]

def brute_force_tsp(distanzmatrix):
    n = len(distanzmatrix)
    min_distanz = float("inf")
    beste_route = None
    
    for perm in permutations(range(n)):
        distanz = berechne_distanz(perm, distanzmatrix)
        if distanz < min_distanz:
            min_distanz = distanz
            beste_route = perm
    
    return beste_route, min_distanz
# Beispiel-Distanzmatrix
distanzmatrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
route, dist = brute_force_tsp(distanzmatrix)
print(f"Beste Route: {route} mit Distanz {dist}")

import numpy as np
# Beispiel-Distanzmatrix für 5 Städte
dist_matrix = np.array([
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
])

def nearest_neighbor(dist_matrix, start=0):
    n = len(dist_matrix)
    visited = [False] * n
    path = [start]
    visited[start] = True
    total_distance = 0

    for _ in range(n - 1):
        last = path[-1]
        # Wähle die nächstgelegene unbesuchte Stadt
        nearest = np.argmin([dist_matrix[last, j] if not visited[j] else np.inf for j in range(n)])
        path.append(nearest)
        visited[nearest] = True
        total_distance += dist_matrix[last, nearest]

    # Rückkehr zum Startpunkt
    total_distance += dist_matrix[path[-1], start]
    path.append(start)
    
    return path, total_distance

route, distance = nearest_neighbor(dist_matrix)
print("Beste gefundene Route:", route)
print("Gesamtdistanz:", distance)


import queue
# Create and fill the queue with values 1 to 10
queue_instance = queue.Queue()
for value in range(1, 11):
    queue_instance.put(value)
# Dequeue and print values until the queue is empty
while not queue_instance.empty():
    current_value = queue_instance.get()
    print(current_value)

#-------
# Read five values (as strings; use int(input(...)) for integers)
values = []
for i in range(5):
    value = input(f"Geben Sie Wert {i+1} ein: ")
    values.append(value)
# Read search value
search_value = input("Welchen Wert möchten Sie suchen? ")
# Find all occurrences using index()
matches = []  # List of found indices
start_index = 0  # Start index for searching
while True:
    try:
        # Find the index of search_value starting from start_index
        index = values.index(search_value, start_index)
        matches.append(index)
        # Update start index to find further occurrences
        start_index = index + 1
    except ValueError:
        # index() raises ValueError if search_value is not found
        break
# Output results
if matches:
    print("Der Wert", search_value, "wurde an den folgenden Positionen gefunden:", matches)
else:
    print("Der Wert", search_value, "wurde nicht gefunden.")

#------
from itertools import permutations

def traveling_salesman(distances, cities):
    optimal_distance = float("inf")
    best_route = ()  # Stores the optimal path
    for permutation in permutations(cities):
        current_distance = 0
        x = 0  # Set starting point (Index 0)
        valid = True  # Flag to check if this permutation is still valid
        for y in permutation:
            current_distance += distances[x][y]
            # If the partial sum already exceeds the optimal path, stop early
            if current_distance >= optimal_distance:
                valid = False
                break
            x = y  # Move to the next node
        if not valid:
            continue  # Skip to the next permutation

        # Add return distance from the last node to the starting point
        current_distance += distances[x][0]
        
        # Update if a new optimal path is found
        if current_distance < optimal_distance:
            optimal_distance = current_distance
            best_route = permutation  # Store the path

    return optimal_distance, best_route

# List of cities (Index corresponds to position in the distance matrix)
cities = [0, 1, 2, 3]

# Distance matrix (symmetric)
distances = [
    [0, 40, 10, 50],
    [40, 0, 60, 30],
    [10, 60, 0, 20],
    [50, 30, 20, 0]
]

# Compute and print solution
solution, route = traveling_salesman(distances, cities)
print("Die beste Lösung liefert die Distanz", solution)
print("Die Route ist", route)


#---------
# Global list storing tuples (total_cost, route)
results = []
def traveling_salesman(distances, visited, current_node, num_cities, step, cost, route):
    # Base case: All cities have been visited
    if step == num_cities:
        # Add return path to the starting node (0)
        total_cost = cost + distances[current_node][0]
        # Store the complete route (route + return to start)
        results.append((total_cost, route + [0]))
        return
    # Check each node to see if it has not been visited
    for node in range(num_cities):
        if node not in visited:
            visited.add(node)
            # Recursive call: Append node to the current route
            traveling_salesman(distances, visited, node, num_cities, step + 1,
                               cost + distances[current_node][node], route + [node])
            visited.remove(node)
# List of cities (Index corresponds to position in the distance matrix)
cities = [0, 1, 2, 3]
# Distance matrix (symmetric)
distances = [
    [0, 40, 10, 50],
    [40, 0, 60, 30],
    [10, 60, 0, 20],
    [50, 30, 20, 0]
]
num_cities = len(cities)
visited = set()
# Mark starting node 0 as visited, and route begins with 0
visited.add(0)
results = []  # Reset list
# Call the recursive function
traveling_salesman(distances, visited, 0, num_cities, 1, 0, [0])
# Find the result with the minimum cost
best_solution = min(results, key=lambda x: x[0])
print("Die beste Lösung liefert die Distanz", best_solution[0])
print("Die Route ist", best_solution[1])


from sklearn.datasets import load_iris
iris_dataset = load_iris(as_frame=True)
x = iris_dataset.data  # Merkmale
y = iris_dataset.target  # Zielwerte
print(x.head())  # Anzeige der ersten 5 Einträge
print(y.head())  # Anzeige der zugehörigen Spezies
print(iris_dataset.target_names)  # Namen der Spezies

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=50, random_state=5)



from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# Daten aufteilen
x_train, x_test, y_train, y_test = train_test_split(iris_dataset.data, iris_dataset.target, test_size=50, random_state=5)
# Modell erstellen und trainieren
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
# Genauigkeit berechnen
vorhersage = knn.predict(x_test)
print(accuracy_score(y_test, vorhersage))

from tensorflow import keras
import matplotlib.pyplot as plt
(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
# Zeigt ein Beispielbild
plt.imshow(x_train[0], cmap="binary")
plt.show()


modell = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),  # Eingabeschicht
    keras.layers.Dense(100, activation="relu"),  # Versteckte Schicht mit 100 Neuronen
    keras.layers.Dense(10, activation="softmax")  # Ausgabeschicht für 10 Klassen
])

modell.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
modell.fit(x_train, y_train, epochs=10)  # Training mit 10 Epochen
modell.evaluate(x_test, y_test)  # Modell testen

test = x_test[:10]
vorhersage = modell.predict(test)
print(vorhersage.argmax(axis=-1))  # Gibt vorhergesagte Klassen aus

for i in range(10):
    plt.subplot(1, 10, i + 1)
    plt.imshow(test[i], cmap="binary")
    plt.axis("off")
    print("Vorhersage:", namen[vorhersage.argmax(axis=-1)[i]], "Real:", namen[y_test[i]])
plt.show()

from tensorflow import keras
# Create model
model = keras.models.Sequential([
    keras.layers.Dense(50, activation="relu"),  # Hidden layer with 50 neurons and ReLU activation
    keras.layers.Dense(5, activation="softmax")  # Output layer with 5 neurons and Softmax activation
])
# Display model summary
model.summary()

#------
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
# Create model with explicit input layer
model = Sequential([
    Input(shape=(10,)),                 # Corrected input layer
    Dense(50, activation="relu"),        # Hidden layer with 50 neurons
    Dense(5, activation="softmax")       # Output layer with 5 neurons
])
# Display model summary
model.summary()

#--------
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import numpy as np
# Input data for OR gate (truth table)
x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input values
y_train = np.array([[0], [1], [1], [1]])  # Expected outputs
# Create optimized model
model = Sequential([
    Input(shape=(2,)),                # Explicit input layer (no more input_dim)
    Dense(2, activation="sigmoid"),    # Hidden layer with 2 neurons
    Dense(1, activation="sigmoid")     # Output layer with 1 neuron
])
# Compile model
model.compile(optimizer="adam", loss="mean_squared_error")
# Train model
model.fit(x_train, y_train, epochs=500, verbose=0)  # Train for 500 epochs
# Test model
print("Testausgabe für OR-Gatter:")
print(model.predict(x_train).round())  # Expected outputs: [[0], [1], [1], [1]]

#----------
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
# Das Dataset laden
(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
# Normalisieren der Daten
x_train = x_train / 255.0
x_test = x_test / 255.0
# Umwandlung der Daten in das passende Format für CNNs (Hinzufügen einer Kanal-Dimension)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)
# Namenszuordnung für die Klassen
namen = ["T-Shirt", "Hose", "Pullover", "Kleid", "Mantel",
         "Sandale", "Hemd", "Turnschuh", "Tasche", "Stiefel"]

# CNN-Modell erstellen
modell = keras.models.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),  # Faltungs-Schicht
    keras.layers.MaxPooling2D((2, 2)),  # Pooling-Schicht
    keras.layers.Conv2D(64, (3, 3), activation="relu"),  # Weitere Faltungs-Schicht
    keras.layers.MaxPooling2D((2, 2)),  # Pooling-Schicht
    keras.layers.Flatten(),  # Umwandlung in eindimensionalen Vektor
    keras.layers.Dense(128, activation="relu"),  # Vollständig verbundene Schicht
    keras.layers.Dense(10, activation="softmax")  # Ausgabe-Schicht für 10 Klassen
])
# Modell kompilieren
modell.compile(optimizer="adam",
               loss="sparse_categorical_crossentropy",
               metrics=["accuracy"])
# Modell trainieren
modell.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
# Modell evaluieren
modell.evaluate(x_test, y_test)
# Vorhersage für einige Testbilder
test = x_test[:10]
vorhersage = modell.predict(test)
ausgabe_index = np.argmax(vorhersage, axis=-1)
# Ergebnisse anzeigen
for i in range(len(test)):
    plt.subplot(1, len(test), i + 1)
    plt.imshow(test[i].reshape(28, 28), cmap="binary")
    plt.axis("off")
    print(f"Vorhersage: {namen[ausgabe_index[i]]}, Korrekt: {namen[y_test[i]]}")
plt.show()

#------

# POSITION:
print("FULL-STACK SOFTWAREENTWICKLER")
print("DATA SCIENCE & MACHINE LEARNING")
print("MEDIENTECHNIKER")
