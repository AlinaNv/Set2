N=int(input())
s1=[]
s2=[]
for i in range(N):
     a=input()
     s1.append(a)
     w=set(s1)
for i in range(N):
     b=input()
     s2.append(b)
     q=set(s2)


print(w)
print(q)
print(set(q.intersection(w)))
