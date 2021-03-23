import fictionary
import random

PRESENT, PRETERITE, IMPERFECT, PLUPERFECT, FUTURE, CONDITIONAL, PRESENTSUBJECTIVE, IMPERFECTSUBJECTIVE, FUTURESUBJECTIVE = range(9)
EU, ELAE, NOS, ELESAS = range(4)
TU = ELAE

conjList = [PRESENT, PRETERITE, IMPERFECT, PLUPERFECT, FUTURE, CONDITIONAL, PRESENTSUBJECTIVE, IMPERFECTSUBJECTIVE, FUTURESUBJECTIVE]

AR, ER, IR = range(3)

conjCodes = {
    0: 'present',
    1: 'preterite',
    2: 'imperfect',
    3: 'pluperfect',
    4: 'future',
    5: 'conditional',
    6: 'present subjective',
    7: 'imperfect subjective',
    8: 'future subjective'
}
persCodes = {
    0: 'eu',
    1: 'tu',
    1: 'ele',
    1: 'ela',
    2: 'nos',
    3: 'eles',
    3: 'elas',
}



def conjugate(verb, pers, tense):
    
    if tense in [PRESENT, PRETERITE, IMPERFECT, PRESENTSUBJECTIVE]:
        newVerb = verb[:-2]
    elif tense in [PLUPERFECT, IMPERFECTSUBJECTIVE]:
        newVerb = verb[:-1]    
    else:
        newVerb = verb
    
##    if tense == "(present)":
##        tensePosition = 0
##    elif tense == "(preterite)":
##        tensePosition = 1
##    elif tense == "(imperfect)":
##        tensePosition = 2
##    elif tense == "(pluperfect)":
##        tensePosition = 3       
##    elif tense == "(future)":
##        tensePosition = 4
##    elif tense == "(conditional)":
##        tensePosition = 5
##    elif tense == "(presentsubj)":
##        tensePosition = 6
##    elif tense == "(imperfectsubj)":
##        tensePosition = 7
##    elif tense == "(futuresubj)":
##        tensePosition = 8

    tensePosition = tense
        
##    if pers == "(Eu)":
##        persPosition = 0
##    elif pers == "(Tu)":
##        persPosition = 1
##    elif pers == "(Ele/a)":
##        persPosition = 1
##    elif pers == "(Nos)":
##        persPosition = 2
##    elif pers == "(Eles/as)":
##        persPosition = 3   

    persPosition = pers
        
    if verb.endswith("ar"):
        ConjList = [['o', 'a', 'a', 'a'],['ei','ou','a', 'ara'],['ava','ava','ava','ava'],['ra','ra','ra','ra',],['ei','a','e','ao'],['ia','ia','ia','ia'],['e','e','e','e'],['sse','sse','sse','sse'],['','','','e']]
        newVerb += ConjList[tensePosition][persPosition]        
    elif verb.endswith("er"):
        ConjList = [['o','e','e','e'],['i','eu','e','era'],['ia','ia','ia','ia'],['ra','ra','ra','ra',],['ei','a','e','ao'],['ia','ia','ia','ia'],['e','e','e','e'],['sse','sse','sse','sse'],['','','','e']]
        newVerb += ConjList[tensePosition][persPosition]
    elif verb.endswith("ir"):
        ConjList = [['o','e','i','e'],['i','iu','i','ira'],['ia','ia','ia','ia'],['ra','ra','ra','ra',],['ei','a','e','ao'],['ia','ia','ia','ia'],['e','e','e','e'],['sse','sse','sse','sse'],['','','','e']]
        newVerb += ConjList[tensePosition][persPosition]
    else:
        raise NameError(f'{verb} does not end in Ar, Er, or Ir')
    
    if pers == TU:
        newVerb += 's'
    elif pers == NOS:
        newVerb += 'mos'    
    elif pers == ELESAS:
        newVerb += 'm'
        
    return newVerb

def rand_verb(verb = ['ar', 'er', 'ir']): # take in list of possible verbs
    
    tryAgain = 1
    while tryAgain == 1:
        word = fictionary.word(min_length = 4, max_length = 7)
        if len(word) < 8:
            tryAgain = 0
    
    # trim word of any a,e,i or ar, er, ir
    if word.endswith("e") or word.endswith("a") or word.endswith("i"):
        word = word[:-1]
    elif word.endswith("er") or word.endswith("ar") or word.endswith("ir"):
        word = word[:-2]

    word += random.choice(verb)

    return word
