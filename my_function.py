'''def addOne(x):
    return x + 1


def addTwo(x):
    two = 2
    return x + two

print "addOne reports: ",addOne(5)
print "addTwo reports: ",addTwo(5)

"""def convertCelsiusToFahrenheit(x):
    return x * (9/5.0) + 32

result = convertCelsiusToFahrenheit(36)
print result

name1 = ["Reid"]
name2 = ["zavala"]

def swap(name1, name2):
  nun = name1[0]
  name1[0] = name2[0]
  name2[0] = nun

swap(name1,name2)
print(name1)
print(name2)'''

'''def convertCelsiusToFahrenheit(celsius):
    return celsius * (9/5.0)+32

Ci = float(raw_input("Enter temperature in Celsius"))
F=convertCelsiusToFahrenheit(Ci)
print 'temperature in Fahrenheit is', F

def convertFahrenheitToKelvin(fahrenheit):
    k = (5*F + 2297.15)/9
    return fahrenheit

def convertCelsiusToKelvin(celsius):
    k = (5*F + 2297.15)/9
    return celsius

def convertKelvinToCelsius(kelvin):'''

'''def isEvenVerbose(x, verbose = False):
    i = x % 2 == 0

    if verbose == True:
        if i:
            print "number",x, "is even"
        else:
            print "number",x, "is odd"
    return i

isEvenVerbose(6)
isEvenVerbose(6, True)
isEvenVerbose(5, True)'''

'''def countup(n):
    while n > 11:
        print n
        n = n - 1
    print "launch"
countup(0)'''

'''i = inter([1,2,3])
next(1)
next(2)
next(3)'''

'''for I in ([1,2,3,4]):
    print I'''

'''def alternate(a):
    s = ""
    i = True
    for str in a:
        if i:
            s += str.upper()
        else:
            s += str.lower()
        if str != ' ':
            i = not i
    return s
print alternate("capitalize")'''

students = {"10001578":"Jonathan",
            "10005776":"Elvis",
            "10007543":"Abigail",
            "10008712":"Nusrath",
            "10005151":"Olawale",
            "10006570":"Olivia",
            "10003570":"Rayona",
            "10002576":"Egide",
            "10005789":"Zanif",
            "10002213":"Rahid",
            "10003207":"Imran"}

'''def studentlookup(students,name):
    for x in students:
        if students[x] == name:
            return x
    return "Invalid student name"
print studentlookup(students,"Abigail")'''

'''v = []
i = int(raw_input())
while (i != 0):
    v.append(i%2)
    i=i/2
print v'''

'''def fact(n):
    if n==1:
        return n
    else:

        return n+fact(n-1)
print fact(10)'''

''''height=int(raw_input("Enter Height: "))
width=int(raw_input("Enter Width: "))
def customBox(height,width):
    for i in range(height):
        if(i >=2 and i<=(height-3)):
            print "##"+ " "* (width-4) + "##"
        else:
            print "#" * width
customBox(height,width)'''

'''def countBox():
    tbborder = " ######################"
    lrborder = "#                     #"
    letters = ("A1 A2 A3 A4 A5 A6 A7 A8")
    print (tbborder)
    for i in range(9):
        print lrborder
        print letters
    print (tbborder)

countBox()
letters = ("A1 A2 A3 A4 A5 A6 A7 A8")
print letters
letters = ("B1 B2 B3 B4 B5 B6 B7 B8")
print letters
letters = ("C1 C2 C3 C4 C5 C6 C7 C8")
print letters
letters = ("D1 D2 D3 D4 D5 D6 D7 D8")
print letters
letters = ("E1 E2 E3 E4 E5 E6 E7 E8")
print letters
letters = ("F1 F2 F3 F4 F5 F6 F7 F8")
print letters
letters = ("G1 G2 G3 G4 G5 G6 G7 G8")
print letters
letters = ("H1 H2 H3 H4 H5 H6 H7 H8")
print letters'''
'''print "%s and %s %s up the %s" %("Jack","Jill","ran","hill")'''

'''base = ""
base = ("#" * 27) + '\n'
for j in range(8):
    base = base + "# "
    for i in range(1,9):
        base = base + chr(65+j) + str(i)
        if i != 8:
            base = base + " "
    if j != 7:
    base = base + ' #\n'
base = base + ("#" * 27) + '\n'
print(base)'''

'''class MyClass:
    def __init__(self, my_name):
        self.name = my_name

    def getName(self):
        return 'Hello ' + self.name

M1 = MyClass('foo')
M2 = MyClass('bar')
print M1.getName()
print M2.getName()'''

'''''class Musician:
    def __init__(self, musician_name, musician_genre):
        self.name = musician_name
        self.genre = musician_genre

beyonce = Musician('Beyonce', 'R&B')
nickiminaj = Musician('Nicki Minaj', 'Rapper')

print beyonce.name + ':' + beyonce.genre
print nickiminaj.name + ':' + nickiminaj.genre'''

'''class SpaceShips:
    def __init__(self, spaceships_house, spaceships_name, spaceships_pilot):
        self.name = spaceships_name
        self.house = spaceships_house
        self.pilot = spaceships_pilot
    def decription(self):
        print "Look at my SpaceShips, the %s , %s and the %s in the spaceship." %(self.name, self.house, self.pilot)

planet = SpaceShips('Planet','space', 365)
orbit = SpaceShips('Orbit','mars', 667)

print planet.name + ":" + planet.name
print orbit.name + ":" + str(orbit.pilot)'''

class Box:
    def __init__(self, box_width, box_height, box_border):
        self.name = box_width
        self.name = box_height
        self.name = box_border

    def getWidth(self):
        return width
    def getHeight(self):
        return height
    def getBorder(self):
        return border
    def FillBox():
        return (activity1)
    def Border():
        return (activity2)

for i in range()

''''
height=int(raw_input("Enter Height: "))
width=int(raw_input("Enter Width: "))
border=int(raw_input("Enter Border: "))
def Box(height,width, border):
    for i in range(height):
        if(i >=2 and i<=(height-3)):
            print "##"+ " "* (width-4) + "##"
        else:
            print "#" * border
Box(height,width,border)
