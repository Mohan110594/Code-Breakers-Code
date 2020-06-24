#Time comp --> o(n logn)
#space comp --> o(1)

jobs=[(3,3), (1,6), (6,7), (0,2)]
jobs=sorted(jobs,key=lambda x:x[1])
start=jobs[0][0]
end=jobs[0][1]
count=1
for i in range(1,len(jobs)):
    if end<=jobs[i][0]:
        start=jobs[i][0]
        end=jobs[i][1]
        count+=1
print(count)
