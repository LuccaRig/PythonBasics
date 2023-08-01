def reps(Numlist = [], *args):
    ListaReturn = []
    
    for i in Numlist:
        if i not in ListaReturn and (Numlist.count(i) >= 2):
            ListaReturn.append(i)
                

    ListaReturn.sort()
    return ListaReturn
            

print(reps([1, 4, 2,  3, 4, 2, 3, 4]))
print(reps([1, 2, 3, 4, 5]))

