import random
import pprint
import logging
import re
def generate_test(binput,output):
    logging.basicConfig(filename=output+'.log', level=logging.INFO)
    converter = {"\\d": "[0-9]", "\\D": "[^0-9]", "\\w": "[a-zA-Z0-9_]", "\\W": "[^a-zA-Z0-9_]","*": "{1,9}"}
    lastpattern = ""
    result = ""
    uinput=binput
    # Convert backslash shortcuts
    while "\\" in uinput or "*" in uinput:
        ind = uinput.find("\\")
        if(ind!=-1):
            reg = uinput[ind:ind + 2]
            uinput = uinput[:ind] + converter.get(reg) + uinput[ind + 2:]
        else:
            ind = uinput.find("*")
            reg = "*"
            uinput = uinput[:ind] + converter.get(reg) + uinput[ind + 1:]

    # Process regex expression
    while uinput != "":
        if uinput[0] == "[":
            lastpattern = uinput[1:uinput.find("]")]
            uinput = uinput[uinput.find("]") + 1:]
            result += squared(lastpattern)
        elif uinput[0] == "{":
            t = uinput.find("}")
            times_to_repeat = times(uinput[1:t])
            for i in range(times_to_repeat-1):
                result += squared(lastpattern)
            uinput = uinput[t + 1:]  # Move past the closing curly brace
        else:
            lastpattern = uinput[0]
            result += uinput[0]
            uinput = uinput[1:]
    match = re.search(binput, result)
    if match==None:
        logging.critical("REGEX DOES NOT MATCH!!!!")
    return result
def times(expression):
    comma = expression.find(",")
    if comma != -1:
        try:
            first = int(expression[0:comma])
            second = int(expression[comma + 1:])
            try:
                return random.randrange(first, second+1)
            except:
                logging.error("In { }, the first value is supposed to be less than the second value. ")
                return 1
        except:
            logging.error("{"+"} expression is only integers")
            return 1
    try:
        return int(expression)
    except:
        logging.error("{"+"} expression is only integers OR { } expression is not seperated by comma.")
        return 1

def squared(expression):
    dash = expression.find("-")
    while dash != -1 and dash>0 and dash<len(expression)-1:
        first = ord(expression[dash - 1])
        second = ord(expression[dash + 1])
        save1=expression[:dash - 1]
        save2=expression[dash + 2:]
        expression=""
        for i in range(first, second + 1):  # Include second value
            expression += chr(i)
        expression = save1+expression+save2
        dash = expression.find("-")
    return expression[random.randrange(0, len(expression))]


if __name__ == "__main__":

    # Check for empty strings or string with only spaces
    # This step is not required here
    # if not bool(city.strip()):
    #     city = "Kansas City"
    print("How many test cases?")
    testcases = int(input())
    print("Type a regex expression:")
    binput = input()
    result = []
    for i in range(testcases):
        result.append(generate_test(binput))
    match = re.search(binput, result)
    if match==None:
        logging.critical("REGEX DOES NOT MATCH!!!!")
    print("\n")
    pprint.pprint(result)
