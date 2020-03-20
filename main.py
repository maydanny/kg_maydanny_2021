def mapping_exists(s1, s2):          
    dict_s1 = {}
    dict_s2 = {}
    
    for i,value in enumerate(s1):
        dict_s1[value] = dict_s1.get(value,[])+[i]
            
    for j,value in enumerate(s2):
        dict_s2[value] = dict_s2.get(value,[])+[j]
    
    if sorted(dict_s1.values()) <= sorted(dict_s2.values()): return True
    else: return False
    

