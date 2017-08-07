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

def fact(n):
    if n==1:
        print n
        return n
    else:
        print n
        return n+fact(n-1)
print fact(10)
