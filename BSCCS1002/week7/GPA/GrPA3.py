def merge(D1, D2, priority):
    dict = {}
    for elem in D1:
        dict.update({elem: D1[elem]})
    for elem in D2:
        if (elem in dict) and (priority == "first"):
            continue
        else:
            dict.update({elem: D2[elem]})
            
    return dict