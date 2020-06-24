#Time comp --> o(n)
#space comp --> o(1)

same as contiguous_product_less_than_k problem

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


