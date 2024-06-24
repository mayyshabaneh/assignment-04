# this code convert from decimal to binary system by using while loop and create an array to insert a modulas number in it then create a value when the temp be 0
import string

def DectoBin (value):
    result = []
    temp = value #initial a temp value to print a value in consoule
    while temp != 0 :
            result.insert(0,temp % 2)
            temp //= 2
    listtostr = ' '.join(map(str,result))
    print(f"decimal value : {value} = in binary ",listtostr)

DectoBin(25)
DectoBin(47)
DectoBin(123)
DectoBin(47)


# the code create an temp array to store a vlaue in it by % number to 10 , to find the last value a digit in araay mulitply with 2 power its position in array , or initialize a position variable as a counter
def BintoDec(value):
    V= value
    result = 0
    temp = []
    position = 0
    while value != 0:
        digit = value % 10
        result += digit * (2 ** position) #multiply the digit with 2 power its position
        temp.append(digit)
        value //= 10
        position += 1
    # print(temp) #print an a temp array to sure that the number is correct
    print(f"the binary value {V} in decimal = ",result)
    return result
    
BintoDec(10000000000111111)
BintoDec(1011)
BintoDec(11001)

def OcttoDec(value):
    result = 0
    temp = []
    position = 0
    while value != 0:
        digit = value % 10
        result += digit * (8 ** position)
        temp.append(digit)
        value //= 10
        position += 1
    # print(temp) #print an a temp array to sure that the number is correct
    # print(result)
    return result

OcttoDec(10)


def DectoOCT (value):
    result = []
    temp = value #initial a temp value to print a value in consoule
    while temp != 0 :
            result.insert(0,temp % 8)
            temp //= 8
    listtostr = ' '.join(map(str,result))
    print(f"decimal value : {value} = in Octal ",listtostr)
    return result

DectoOCT(197)

def OcttoBin(value):
    DectoBin(OcttoDec(value))

OcttoBin(10)

def BintoOct(value):   
    DectoOCT(BintoDec(value))
    
BintoOct(1010101)

def HexaToDec(value : string):
    stack = list(value)
    result = 0
    temp = []
    position = 0
    hex_map = {'A' : 10 , 'B' : 11 , 'C' : 12 , 'D' : 13 , 'E' : 14 , 'F' : 15}
    while stack:
        top = stack.pop()
        if top in hex_map:
            tempp = hex_map[top]
        else :
            tempp = int(top)
        result += tempp * (16 ** position)
        temp.append(tempp)
        position += 1
    # print("temp value is " , temp)
    print("result is : " , result)
    return result

HexaToDec("1A3")
HexaToDec("4F2")
HexaToDec("B72")

def HexatoBin(value):
    return DectoBin(HexaToDec(value))

HexatoBin("A2B")

def DectoHexa(value):
    result = []
    temp = value #initial a temp value to print a value in consoule
    hex_map = {10:'A' , 11 :'B' , 12:'C' , 13:'D' , 14:'E' , 15:'F'}
    while temp != 0 :
            rem = temp % 16
            if rem in hex_map :
                result.insert(0,hex_map[rem])
            else :
                result.insert(0,rem)
            temp //= 16
    listtostr = ' '.join(map(str,result))
    print(f"decimal value : {value} = in hex ",listtostr)
    return result

DectoHexa(1557)

def BintoHexa(value):
    DectoHexa(BintoDec(value))

BintoHexa(11100101)

def BintoBCD(value):    
    pass


def BCDtoBin(value : string):
    hex_map = {0:'0000' , 1:'0001' , 2:'0010' , 3:'0011' , 4:'0100' , 5:'0101' , 6:'0110' , 7:'0111' , 8:'1000' , 9:'1001'}
    temp = value
    stack = list(value)
    result = []
    while stack :
        top = int(stack.pop())
        result.insert(0,hex_map[top])
    # listtostr = ' '.join(map(str,listtostr))
    print (f"result in BCD {temp} = ",result)
    return result

BCDtoBin("123")

def BW_AND(a,b):
    return a&b

print(f"bitwise and : {BW_AND(10,12)}")

def BW_OR(a,b):
    return a|b

print(f"bitwise or : {BW_OR(10,12)}")

def BW_XOR(a,b):
    return a^b

print(f"bitwise xor : {BW_XOR(10,12)}")

def BW_NOT(a):
    return ~a

print(f"bitwise not : {BW_NOT(100011)}")

def BW_LSHIFT(a,value):
    return a<<value

print(f"bitwise left shift : {BW_LSHIFT(12,2)}")

def BW_RSHIFT(a,value):
    return a>>value

print(f"bitwise right shift : {BW_RSHIFT(12,2)}")
