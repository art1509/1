# (15^2 - 20 + 5.5) / 6
var1 = ((15**2) - 20 + 5.5) / 6
print(var1)

#(63/2 + 45 - 8) / 2^5
var2 = (63/2 + 45 - 8) / 2**5
print(var2)

#7^3 + 20 * (10/3 + 6)
var3 = 7**3 + 20 * (10/3 + 6)
print(var3)

#83/8 * (43/20 + 5^7)
var4 = 83/8 * (43/20 + 5**7)
print(var4)

#72 + 36 / 7 * (72-6^5)
var5 = 72 + 36 / 7 * (72-6**5)
print(var5)

def func1(a, b, c):
    # a * b + c
    result = a + b * c
    print(result)
    return result
var1 = func1(7**3, 20, (10/3 + 6))

def func2(a, b, c):
    # a * b + c
    result = a * (b + c)
    print(result)
    return result
var2 = func2(63/2,  45 - 8, 5**7)

def func3(a, b, c):
    # a + b)/ c
    result = (a + b) / c
    print(result)
    return result
var3 = func3(63/2, (45-8), 2**5)

def func6(code, number):
    var6 =  "+38 (%s) %s" % (code, number)
    print("result", var6)
func6("099", "123 12 12")
def func7 (code,number):
    var7 = "+38 {} {}". format(code, number)
    print("result:", var7)

func7("(099)", "123 12 12")

def func8(code, number):
    var8 = f'+38 {code} {number}'
    print("result:", var8)

func8("(099)", "123 12 12")

s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus non dictum lacus. Etiam placerat, sapien tincidunt pellentesque ullamcorper, tortor tortor condimentum tellus, eget tempor mi turpis nec sapien. Nunc lectus ex, suscipit in justo quis, maximus consequat elit. Fusce mollis massa id ornare semper. Morbi cursus sollicitudin porttitor. Mauris at lobortis metus. Donec a nisl felis. Mauris eu enim mollis, dictum velit a, venenatis odio. Integer non pellentesque urna. Nam tortor lacus, elementum a diam sed, porttitor ullamcorper justo. Morbi laoreet tempor sapien non auctor. Proin imperdiet finibus pellentesque. Nulla gravida leo et libero egestas vulputate quis quis orci. Morbi felis est, dignissim sit amet malesuada sit amet, maximus id lacus."
print(s[:10])
print(s[-25:])

s = "HELLO WORLD"
s.lower()
print(s.lower())

def func1(fruit, vegetables):
    var1 = f"Ilike {fruit} and {vegetables}"
    print("result:", var1)
func1 ('fruit', 'vegetables')

def func2(one, two, three):
    var2 = "length - {} windh - {} height - {}".format(one, two, three)
    print("result:", var2)

func2('1', '2', '3')