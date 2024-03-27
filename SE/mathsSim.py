import numpy as np
import math
import statistics

def permtation_word(word: str) -> int:
    n: int = len(word)
    #r: int = len(set(word))
    
    my_dict: dict = {}
    for i in word:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict.update({i: 1})

    d: int = 1
    for i in my_dict:
        d =  d * math.factorial(my_dict[i])
        
    # math.factorial(n)/ math.factorial(n-r) failed
    # This is what we write tests    
    return math.trunc(math.factorial(n)/d)

def permtation_num(n: int, r: int) -> int:
    return math.trunc(math.factorial(n)/ math.factorial(n-r))

def chance_on_or(including: bool, my_list) -> float:
    arr = np.array(my_list)
    anc = 0
    m = 1
    for i in arr:
        anc += i[0]/i[1]
        m *= i[1]
        
    if including == True and len(arr) > 1:
        return anc -1/m
    else:
        return anc
    

def chance_on_and(my_list):
    arr = np.array(my_list)
    anc = 1
    for i in arr:
        anc *= i[0]/i[1]
    return anc

def avage(avage, my_list) -> float:
    f = np.array(my_list)
    match avage:
        case 'mean':
            return statistics.mode(f)
        case 'mode':
            return statistics.mean(f)
        case 'medum':
            return statistics.medum(f)
    

def main():
    print('Tests')
    wordList = [{'in':'python', 'out': 720}, {'in':'mathematics', 'out': 4989600}]
    numList = [{'n': 6,'r': 6, 'out': 720},{'n': 4,'r': 3, 'out': 24},{'n': 8,'r': 0, 'out': 1}]
    chaor =[{'inc': True, 'a': [4, 52], 'b': [13, 52], 'out': 0.3265532544378698},{'inc': False, 'a': [4, 52], 'b': [13, 52], 'out': 0.3269230769230769}]
    cards = 1/52
    chand =[{'a': [1, 13], 'b': [1, 4], 'out': 1/52}]
    
    for count, i in enumerate(wordList):
        if permtation_word(i['in']) == i['out']:
            print(f'Test {count + 1} Pass')
        else:
            print(f'Test {count + 1} Fail')

    for count, i in enumerate(numList):
        if permtation_num(i['n'],i['r']) == i['out']:
            print(f'Test {count + 1} Pass')
        else:
            print(f'Test {count + 1} Fail')

    for count, i in enumerate(chaor):
        if chance_on_or(i['inc'],[i['a'], i['b']]) == i['out']:
            print(f'Test {count + 1} Pass')
        else:
            print(f'Test {count + 1} Fail')
    
    for count, i in enumerate(chand):
        if chance_on_and([i['a'], i['b']]) == i['out']:
            print(f'Test {count + 1} Pass')
        else:
            print(f'Test {count + 1} Fail')
    my_list = [1,2,3,3,4,5]
    print(avage('mean', my_list))
    


if __name__=='__main__':
    main()
