nums=[23,45,1,2,8,19,-3,16,-11,28]
len_of_arr=len(nums)
target=int(input("Number to be search"))

def linear_search(nums, target):
    if len_of_arr ==0:
        return -1
    for i in range (len_of_arr):
        if nums[i]==target:
            return i
        
    return ("number does not found in arry")


print(linear_search(nums,target))