hash_table = {

}

nums = [2,2,2,1,1,1,2,2]

def majority_element(nums):
    for num in nums:
        if num not in hash_table.keys():
            hash_table[num] = 1
        else:
            hash_table[num] += 1
            if hash_table[num] >= len(nums)//2:
                return num
print(majority_element(nums))