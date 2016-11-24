from json import dumps, load
from numpy import exp, array, random, dot
import re
import json

'''
funzione: calcola la prob. che el sia legato al succ.
   k=spazio degli eventi,
   p_0=prob già nel db,
   check=se è la prima volta che si calcola la prob.
'''
def prob(p_0,k,check): #funzione
    if check == 1:
        prob = round(int((round(k*p_0)) + 1)/(k+1),4)
    else:
        prob = 0
    return prob

print ("Sto elaborando...")

with open('input.txt', 'r') as inp:
    data=inp.read().replace('\n', '')

with open("output.json") as out:
        result = load(out)
    
words = re.sub("[^\w]", " ",  data).split() #so we match any non alphanumeric character and replace it with a space

print (words,len(words))
#user_input = input("Scrivi qualcosa: ") #può servire...
x = 0

while (x < len(words)-1):
    el = words[x].lower()
    print (el)
    if el != ',' or el != ';': #escludi , e ;
        p_w_s = 0 #probailità iniziale
        k = 0 #spazio degli eventi iniziale
        
        el_array = {}
        check = 0

        if el in result: #se c'è la parola nel DB
            el_array = result[el]
            k = result[el]['k']

        s_id = x + 1
        s_el = words[s_id].lower()
        #print (x,s_id,s_el) #debug...
        if s_el in el_array: #se c'è el. succ. nel ramo di el. nel DB
            p_w_s = result[el][s_el] #prob. che el corrente sia legato al succ. dal DB
            check = 1
        p_w_s_def = prob(p_w_s,k,check) #probabilità
        print (s_el,p_w_s_def)
        if el in result:
            for p_el in result[el]:
                if p_el != 'k': #ovviamente non deve modificare la chiave k...
                    result[el][p_el] = prob(result[el][p_el],k+1,1) #modifica anche le prob. degli altri el. dentro el
            result[el][s_el] = p_w_s_def #scrivi nel DB
            result[el]['k'] = k+1 #idem
        else:
            result[el] = {s_el:p_w_s_def,'k':k+1}
        print (result)
        with open("output.json", 'w') as file:
            json.dump(result, file)

    x = x+1        

out.close()
print ("Fatto!")
