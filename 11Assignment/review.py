from random import randint

Nouns = ['1','2','3']

def get_rand() : 
    random_list = []
    for i in range(11) : 
        random_list.append(Nouns[randint(0,2)])
    return random_list

def get_rank(random_list) : 
    result = {}
    for n in random_list :
        if not ("insert") : 
            result[n] = 0
    result[n] += 1
    return result

if __name__ == "__main__" : 
    result = get_rank(get_rand())
    for k, v in result : 
        print("pull about this")

