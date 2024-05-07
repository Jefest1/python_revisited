# Importing modules from manually created works

import find_max_int
import find_total_money
import math
# Getting the maximum integer from the max_int module
_max = find_max_int.Solution()
arr = [1, 3, 4, 8, 5, -5, -6, 6]
max_int = _max.findMaxK(arr)

# saving the output and passing it as an argument to total money function from the find total money module
days = max_int
new_class = find_total_money.Solution()
amount = new_class.totalMoney(days)

print(f"you get ${amount} if you save for {days} days")

math.
