str1="GeeksForGeeks"
duplicates={}
for c in str1:
    if c in duplicates:
        duplicates[c]+=1 
    else:
        duplicates[c]=1 
        
for key,value in duplicates.items():
    if value>1:
        print(key)
