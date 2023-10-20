#find the index of duplicated elements in a list, which are 'i' and 'j'.
#enter a integer "k", if abs(i-j)<=k can be done, return True, else False

k=int(input('Entet integer k: '))
l=input("enter numbers divided by a comma: ").split(',')

def exists(l:list,k:int):
    for i in range(len(l)):
        for j in range(i):
            if l[i]==l[j]:
                return True
    return False

if __name__=='__main__':
    print(exists(l,k))

