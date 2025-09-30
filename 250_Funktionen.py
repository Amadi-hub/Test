
# Funktionen

# Eigene Funktionen definieren.

# Python stellt auch Funktionen zur Verfügung:
# z.B. print(), type(), round(), randint()

# Wir betreten jetzt das Zeitalter der Prozeduralen Programmierung.
# Eine Prozedur ist verwandt mit einer Funktion.

# Funktionsdefinition
# Schlüsselwort def (von define - definieren)
def meine_erste_funktion():
    print('Hello World')
    # print('Hallo Welt')

# Funktionsaufruf
meine_erste_funktion()  # Hello World

# Funktionsbezeichner.
# Erlaubte Zeichen wie beim Variablenbezeichner:
# Buchstaben, Ziffern, Unterstrich, aber Ziffern nicht am Anfang.
# Sprechende Bezeichner:
# Der Bezeichner sollte eine Handlungsaufforderung (Imperativ) sein
# oder den Rückgabewert beschreiben.

# Vorteil: Man kann Funktionen mehrmals ausführen
meine_erste_funktion()  # Hello World
meine_erste_funktion()  # Hello World
meine_erste_funktion()  # Hello World

# Parameter steht in den runden Klammern bei der Funktionsdefinition.
# Ein Parameter ist quasi eine lokale Variable innerhalb der Funktion.
def gib_aus(text):
    print(text)

# Argumente stehen in den Klammern beim Funktionsaufruf.
gib_aus('Hallo')  # Hallo
gib_aus(777)      # 777

# Mehrere Parameter per kommaseparierter Liste.
def addiere(zahl1, zahl2):
    ergebnis = zahl1 + zahl2
    print(ergebnis)

# Mehrere Argumente dementsprechend per kommaseparierter Liste.
# Selber schreiben nur: 3, 4
# Den Rest (zahl1: zahl2:) macht PyCharm automatisch.
addiere(3, 4)    # 7
addiere(23, 42)  # 65

# Die Anzahl von Parameter und Argumenten muss zueinander passen:
# addiere(9)        # TypeError: addiere() missing 1 required positional argument: 'zahl2'
# addiere(1, 2, 3)  # TypeError: addiere() takes 2 positional arguments but 3 were given

# Rückgabewert.
# Per Schlüsselwort return.
# Standardmäßig hat jede Funktion ein return
# und der Wert an die Stelle des Funktionsaufrufs zurückgegeben.
# Dadurch kann man flexibler im nächsten Schritt entscheiden,
# was im nächsten Schritt mit dem Wert passieren soll. Z.B. printen, in die DB oder eine Datei, ...
def addiere2(zahl1, zahl2):
    ergebnis = zahl1 + zahl2
    return ergebnis

print(addiere2(7, 9))  # 16
zahl3 = addiere2(8, 4)
zahl3 += 1
print(zahl3)

# Die Funktion wird abgearbeitet und am Ende steht der Rückgabe-Wert an der Stelle der Funktion.
print(addiere2(7, 9))
print(16)

# Anderes Beispiel
def name(vorname, nachname):
    return vorname + ' ' + nachname

print(name('Cord', 'Mählmann'))  # Cord Mählmann

def urlaubsanspruch(alter, gdb, jahre_im_betrieb):
    urlaub = 26

    # Minderjährige
    if alter <= 17:
        urlaub = 30
    # Älter als 55
    elif alter > 55:
        urlaub = 28

    # Behinderung
    if gdb >= 50:
        urlaub += 5

    # Zugehörigkeit
    if jahre_im_betrieb > 10:
        urlaub += 2

    return urlaub

print(urlaubsanspruch(40, 0, 2))   # 26
print(urlaubsanspruch(57, 0, 20))  # 30
print(urlaubsanspruch(17, 0, 1))   # 30
print(urlaubsanspruch(17, 5, 1))   # 35





def urlaubsanspruch26(alter, gdb, jahre_im_betrieb):
    urlaub = 26

    # Minderjährige
    if alter <= 17:
        urlaub = 30
    # Älter als 55
    elif alter > 55:
        urlaub = 28

    # Behinderung
    if gdb >= 50:
        urlaub += 5

    # Zugehörigkeit
    if jahre_im_betrieb > 10:
        urlaub += 2

    return urlaub




def urlaubsanspruch27(alter, gdb, jahre_im_betrieb):
    urlaub = 27

    # Minderjährige
    if alter <= 17:
        urlaub = 30
    # Älter als 55
    elif alter > 55:
        urlaub = 28

    # Behinderung
    if gdb >= 50:
        urlaub += 5

    # Zugehörigkeit
    if jahre_im_betrieb > 10:
        urlaub += 2

    return urlaub




def urlaubsanspruch_offen(urlaub, alter, gdb, jahre_im_betrieb):

    # Minderjährige
    if alter <= 17:
        urlaub = 30
    # Älter als 55
    elif alter > 55:
        urlaub = 28

    # Behinderung
    if gdb >= 50:
        urlaub += 5

    # Zugehörigkeit
    if jahre_im_betrieb > 10:
        urlaub += 2

    return urlaub

print(urlaubsanspruch_offen(27, 17, 5, 1))   # 35























