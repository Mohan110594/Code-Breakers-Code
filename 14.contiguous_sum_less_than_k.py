nums = [1,2,3,2,1]
k=3
rsum=0
index=-1
out=0
for i in range(len(nums)):
    rsum=rsum+nums[i]
    while rsum>k:
        index=index+1
        rsum=rsum-nums[index]
    out=out+i-index
print(out)


