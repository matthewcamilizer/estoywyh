a=input("enter a string:")
l=[]
s={}

def non_duplicated(a,l):
    for i in range(len(a)):
        for j in range(i):
            if a[j]==a[i]:
                if [i,j] not in l:
                    l.append(i)

    # get the start index of the next duplicate element
    l=list(sorted(set(l)))
    if len(a) not in l:
        l.append(len(a))


    difs=[]
    if len(l)==1:
        difs.append(l[0])
    elif len(l)==2:
        difs.append(l[1]-len[0])
    else:
        for i in range(2,len(l)):
            dif=l[i]-l[i-2]
            if dif not in difs:
                difs.append(dif)

    return max(difs), a[l[i-2]:l[i]]

o=non_duplicated(a,l)
print(f"the longest chrs without duplication is {o[1]}, length: {o[0]}")
