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
        gl.append(2)
    else:
        gl.append(1)
else:
    if all(x==a[0] for x in a):
        gl.append(len(a))
    else:
        for i in range(len(a)):
            if not a[i-2]==a[i-1] and a[i-1]==a[i]:
                start.append(i-1)

        for i in range(2,len(a)):
            if a[i-2]==a[i-1] and not a[i-1]==a[i]:
                end.append(i-1)
        if a[len(a)-1]==a[len(a)-2]:
            end.append(len(a)-1)

        for i in range(len(start)):
            gl.append(end[i]-start[i]+1)
            s[str(i+1)]=[start[i],end[i]]

print(max(gl))
