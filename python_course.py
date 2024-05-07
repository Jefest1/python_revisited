# A for loop for multiplications
def calc_multiple(nums):
    for i in range(len(nums)):
        for j in range(1, 13):
            prod = nums[i] * j
            print(f"{nums[i]} x {j} = {prod}")

        print("=======================")


calc_multiple([2, 3, 4, 5])
