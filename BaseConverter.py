"""
The purpose of this program is to take in a number, in any base, and convert it
into the same number but in another base.
PRECONDITION: original base >= 1, new base >= 1, number is a valid number
POSTCONDITION: original number converted to new base
"""
print("====================\n\nWelcome to my base-changing program!\nThis program supports any base with digits [0-9A-Z].\nCase will be ignored (i.e., 'a' == 'A').\nThe program has error catches set up.\n\n====================")

# Initializing program variables
SENTINEL1 = "/END"
SENTINEL2 = "/CHANGE1"
SENTINEL3 = "/CHANGE2"
SENTINEL4 = "/CHANGEB"

ORIGINBASE = 0
BASE = 0

# The purpose of this function is to obtain user input on what the bases are to be
def baseChange(check):
    if (check == 0 or check == 2):
        while (True):
            try:
                global ORIGINBASE
                ORIGINBASE = int(input("\nWhat base is your number in?\nThis number has to be greater than 1\nINPUT: "))
                while (ORIGINBASE <= 1):
                    ORIGINBASE = int(input("\nPlease input another number.\nThis number has to be greater than 1\nINPUT: "))
                break
            except:
                print("\nThe bases have to be numbers.")
    if (check == 1 or check == 2):
        while(True):
            try:
                global BASE
                BASE = int(input("\nWhat base do you want to convert to? \nThis number has to be greater than 1\nINPUT: "))
                while (BASE <= 1):
                    BASE = int(input("\nPlease input another number.\nThis number has to be greater than 1\nINPUT: "))
                break
            except:
                print("\nThe bases have to be numbers.")

# The purpose of this function is to use recursive long division to convert
# an input into the new base, returning it as a string
def convertToBASE(current, output):
    if current == 0 and output == "":   # Case: 0
        return "0"                       
    if current == 0:                    # Terminating condition
        return output
    div = int(current/BASE)             # Dividing
    rem = current % BASE                # Getting remainder
    part = ""                           # Initializing new part
    if (rem < 10):                      # If rem is less than 10
        part = str(rem)         
    else:                               # If rem is greater than 10, needs letter
        part = chr(ord('a') + rem - 10)
    output = part + output              # Writing rem backwards
    return convertToBASE(div, output)   # Recursive call

# The purpose of this function is to use place value to convert
# an input into decimal, to easily facilitate conversion to other bases
def convertToDEC(current):
    out = 0                             # Initializes sum variable
    i = len(current) - 1                # Initializes index variable for exponentiation
    for char in current:                # For each 'digit'
        if (ord(char) >= ord('a')):     # If digit is a letter
            if (ord(char) - ord('a') + 10 >= ORIGINBASE):
                return -1               # If the number is not possible in ORIGINBASE
            out += pow(ORIGINBASE, i) * (ord(char) - ord('a') + 10)
        else:                           # If digit is a decimal
            out += pow(ORIGINBASE, i) * int(char)
        i -= 1                          # De-incrementing the index
    return out                          

#TODO CODE GOES HERE
baseChange(2)
while(True):
                                        # Input of number
    number = input("\n====================\n\nWhat is your number?\nInput '" + SENTINEL1 + "' without the quotes to terminate program\nInput '" + SENTINEL2 + "' without the quotes to change your input base\nInput '" + SENTINEL3 + "' without the quotes to change the output base\nInput '" + SENTINEL4 + "' without the quotes to change both bases\nINPUT: ").lower().strip()
    
    if (number.upper() == SENTINEL1):   # Program termination
        print("\n====================\n\nProgram terminated.")
        break
    
    elif (number.upper() == SENTINEL2): # Base input changing
        baseChange(0)
        continue
    
    elif (number.upper() == SENTINEL3): # Base output changing
        baseChange(1)
        continue
    
    elif (number.upper() == SENTINEL4): # Both changing
        baseChange(2)
        continue
    
    negative = number[0] == '-'         # Checking if number is negative
    
    if (negative):                      
        number = number[1:]             # Cutting out negative symbol
    try:
        number = convertToDEC(number)   # Converting to decimal to make it easier to change bases
        if (number == -1):              # If the number is impossible (i.e 'A' in base-10)
            print("\nYour number is not written in base-" + str(ORIGINBASE))
            continue
                                        # Converting to new base
        number = convertToBASE(number, "")  
        
        if (negative):                  # Printing with negative
            print("\nYour number in base-" + str(BASE) + " is: \n-" + str(number).upper())
        else:                           # Printing without negative
            print("\nYour number in base-" + str(BASE) + " is: \n" + str(number).upper())
    except:                             # If the number is invalid, print this
        print("\nSomething went wrong.\nMake sure your number is a valid number")


#BASE = 16
#for i in range (10000):
#    print("0x" + str(convertToBASE(i, "")) == str(hex(i)))
#^^ testing if the program works for base-16, it's original purpose, should all say "True"