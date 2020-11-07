def maxdist(s):
    n=len(s)
    if n==0 or n==1:
        print(n)
    maxchar=count(s)
    minimum=n+1
    p={}
    start=0
    p[s[start]]=1
    for i in range(1,n):
        if s[i] in p:
            p[s[i]]+=1
        else:
            p[s[i]]=1
        if len(p)==maxchar:
            while start<i and p[s[start]]>1:
                p[s[start]]-=1
                start+=1
            if minimum>i+1-start:
                minimum=i+1-start
    print(minimum)
 
    
def count(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return len(d)
    
s=str(input())
maxdist(s)