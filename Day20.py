with open("Day20Input.txt", 'r') as f:
    nums = [(idx,int(num)*811589153) for idx, num in enumerate(f)]

def move_number(nums:list, index:int):
    value = nums[index]
    new_index =(index + value[1] + (len(nums)-1)) % (len(nums)-1)
    nums.remove(value)
    nums.insert(new_index,(value[0],value[1]))
    return nums

working_list = nums.copy()
for i in range(10):
    for num in nums:
        working_list = move_number(working_list, working_list.index(num))

zero_index = [idx for idx, item in enumerate(working_list) if item[1] == 0][0]
print(working_list[(zero_index+1000)%len(working_list)][1] + working_list[(zero_index+2000)%len(working_list)][1] + working_list[(zero_index+3000)%len(working_list)][1])
print()