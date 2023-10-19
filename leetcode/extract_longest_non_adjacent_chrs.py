a=input("enter a string:")
l=[]
s={}

start=[]
end=[]
gl=[]
if len(a)==1:
    gl.append(1)
elif len(a)==2:
    if all(x==a[0] for x in a):
        gl.append(1)
    else:
        gl.append(2)
else:
    if all(x==a[0] for x in a):
        gl.append(1)
    else:
        # add 0 if first two are the same
        if a[0]==a[1]:
            start.insert(0,0)
        for i in range(1,len(a)-1):
            if not a[i-1]==a[i] and a[i]==a[i+1]:
                start.append(i)

        for i in range(2,len(a)):
            if a[i-2]==a[i-1] and not a[i-1]==a[i]:
                end.append(i-1)
        if a[len(a)-1]==a[len(a)-2]:
            end.append(len(a)-1)

        if len(start)>1:
            for i in range(len(start)-1):
                gl.append(start[i+1]-end[i]+1)
        else:
            gl.append(start[0])
            gl.append(end[0])
        for i in range(len(start)):
            s[i]=[start[i],end[i]]
print(start)
print(end)
print(gl)

print(f"dict for index of adjacent chrs: {s}")
for i in range(len(start)):
    print(f"the {int(i+1)} adjacent: {a[s[i][0]:s[i][1]+1]}")


cl=[]
if len(start)>1:
    for i in range(len(start)-1):
        print(f"the {int(i+1)} non-adjacent: {a[end[i]:start[i+1]+1]}")
        cl.append(len(a[end[i]:start[i+1]+1]))
    print(f"length of the longest non-adjacent chrs: {max(cl)}")
else:
    print(f"the 1 non-adjacent: {a[:min(gl)+1]}, the 2 non-adjacent: {a[max(gl):]}")
    cl.append(len(a[:min(gl)+1]))
    cl.append(len(a[max(gl):]))
    print(f"length of the longest non-adjacent chrs: {max(cl)}")
