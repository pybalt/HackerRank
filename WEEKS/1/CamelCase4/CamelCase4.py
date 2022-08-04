# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def splittedResult(expression: list, parameter: list):
    if parameter in 'Cc':
        result = re.findall('[A-Z][^A-Z]*', f'{expression}')
        result = ' '.join(result)
        result = result.lower()
    if parameter in 'MmVv':  # method
        upperWord = re.findall('[A-Z][^A-Z]*', f'{expression}')
        upperWord = ''.join(upperWord)
        indexsUpperWord = re.search(upperWord, f'{expression}')
        formatedExpression = []
        for x in expression:
            if expression.index(x) == indexsUpperWord.start():
                formatedExpression.append(' ')
                formatedExpression.append(x)
                continue
            if x in '()':
                continue
            formatedExpression.append(x)
        result = ''.join(formatedExpression)
        result = result.lower()
    else:
        result = re.findall('[A-Z][^A-Z]*', f'{expression}')
        result = ' '.join(result)
        result = result.lower()
    return result


def combinedResult(expression: list, parameter: list):
    arrFromString = expression.split(' ')
    if parameter in 'Cc':  # class -> Example of a name = ExampleOfAName
        result = []
        for i in arrFromString:
            result.append(i.title())
        result = ''.join(result)
    if parameter in 'MmVv':  # method -> Example of a name = exampleOfAName()
        result = []
        for i in arrFromString:
            if arrFromString.index(i) == 0:
                result.append(i)
                continue
            result.append(i.title())
        result.append('()')
        result = ''.join(result)
    if parameter in 'Vv':  # variable -> example of a name = exampleOfaName
        result = []
        for i in arrFromString:
            if arrFromString.index(i) == 0:
                result.append(i)
                continue
            result.append(i.title())
        result = ''.join(result)

    return result


def inputStr(string:str):
    arrFromString = string.split(';')
    if arrFromString[0] in 'Ss':
        # Operacion SPLIT
        result = splittedResult(arrFromString[2], arrFromString[1])
        print(result)

    elif arrFromString[0] in 'Cc':
        # Operacion COMBINE
        result = combinedResult(arrFromString[2], arrFromString[1])
        print(result)



if __name__ == '__main__':

    while True:
        try:
            inputStr(input().rstrip())
        except EOFError:
            break
                                                        
