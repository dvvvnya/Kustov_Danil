s=input('vvedite stroku: ')
s2=''
k=0
for i in range (len(s)) :
    if s[i]!='.' :
        s2+=s[i]    
    else : k=k+1
print(s2)
print('kolichestvo zamen: ',k)