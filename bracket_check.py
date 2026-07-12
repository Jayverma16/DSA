def bracheck(str_brac):
    pair = {"{":"}","[":"]","(":")"}
    n = len(str_brac) 
    
    for i in range(n//2):
        print(str_brac[i],str_brac[n-i-1] )
        if pair[str_brac[i]] != str_brac[n-i-1]:
            return False
    return True









s = "{[()]}"     # valid
print(bracheck(s))
s = "{[(])}"
print(bracheck(s))