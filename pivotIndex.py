
def pivotIndex(nums):
    
    for num in range(len(nums)):

        leftsum = 0 
        rightsum = 0

        print()
        print("The index for nums")
        print(num)
        print()

        # check the left of the array
        #if (num != 0):
        print("Left of the index sum")
        for leftNum in nums[0:num]:
            leftsum += leftNum
            print(leftsum)

        # check the right of the array
        #if (num != len(nums)):
        print("Right of the index sum")
        for rightNum in nums[num+1:len(nums)]:
            rightsum += rightNum
            print(rightsum)

        # compare sums
        if (leftsum == rightsum):
            return num

    return -1

nums = [-1,-1,-1,0,1,1]

print(pivotIndex(nums))