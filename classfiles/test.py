

nums = [100,99,4,200,1,22,3,2]
nums.sort()
numdealtwith = len(nums)
currentindex = 0
seriescollection = [[]]
tempseries = []

for x in nums:
    while numdealtwith > 0:
        tempseries = [x]
        if (x == nums[currentindex + 1]):
                tempseries.append(nums[x + 1])
                nums.remove(nums[x + 1])
        elif (x == nums[currentindex - 1]):
                tempseries.append(nums[x + 1])               
                nums.remove(nums[x + 1])
