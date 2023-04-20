#!/usr/bin/env python3

def test(a,b):
    return a + ': ' + b

def gen_quiz(qpool: list, *indexes, altcodes = 'ABCDEF', quiz = None):
    
    if not quiz:
        quiz = []

    for i in indexes:
        if abs(i) >= len(qpool) :
            print ('Ignoring index ' + str(i) + ' - list index out of range')
            continue

        pool_on_index = qpool[i]
        q_name = pool_on_index[0]
        q_answers = pool_on_index[1]

        new_answers = []
        for a in range(len(altcodes)):
            if a < len(q_answers):
                new_answers.append(test(altcodes[a], q_answers[a]))
        
        quiz.append((q_name, new_answers))

    return quiz

if __name__ == "__main__":
    import doctest
    doctest.testmod()
