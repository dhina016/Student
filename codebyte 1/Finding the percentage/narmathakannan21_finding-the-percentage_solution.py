n=int(input())
marks={}
for i in range(n):
    name,*line=input().split()
    scores=list(map(float,line))
    scores=sum(scores)/3
    marks[name]=scores
    
    