def sortRoman(names):
    out1=[]
    for name in names:
        n,num = name.split()
        num = convertRoman(num)
        out1.append((n,num,name))
        out1.sort(key = lambda x: [x[1],x[0]],reverse=False)
        out2 = list(map(lambda x:x[2],out1))
    return out2

def convertRoman(s):
    temp = 0
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    for i in range(0,len(s)-1):
        if roman[s[i]] < roman[s[i+1]] :
            temp -= roman[s[i]]
        else:
            temp += roman[s[i]]
    return temp+roman[s[-1]]
    
arr=  ['William V','Willam I','Willam III','Adam II','Brain IV','Adam IV']
print(sortRoman(arr))