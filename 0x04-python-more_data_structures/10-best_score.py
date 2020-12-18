#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    kList = list(a_dictionary.keys())
    vList = list(a_dictionary.values())
    score = 0
    for i in range(0, len(vList)):
        if (int(vList[i]) > score):
            score = vList[i]
    pos = vList.index(score)
    return(kList[pos])
