
def check(char, pat,lenpat,textindex):
    j = lenpat - 1
    a = -1
    while j >= 0:
        if pat[j] == char or pat[j] == "\\" or pat[j] == "?" or pat[j] == "*":
            a = textindex - j
            break
        j -=1
    return a
     
def sundayAlg(text,pat):
    t ,p= len(text),len(pat)
    i = 0
    j = p - 1
    while i < t-p :
        b = 0
        z = p - 1
        while b < p:
            if pat[z] == "\\" or pat[z] == "?" or pat[z] == "*":
                z-=1
                b+=1
                if z < 0:
                    t = -1
                    break            
            if pat[z] != text[i+z]:
                a = check(text[i+j+1],pat,p,i+j+1)
                if a < 0:
                    i = i + j + 2 
                else: 
                    i = a
                break
            if z < 0:
                t = -1
                break        
            z-=1
            b+=1  
              
        else:
            break    
    return i                  

print(sundayAlg('ab\tdabadccdbabd', 'c?d')) 
