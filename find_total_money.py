class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """

        # create a variable to hold the total money and daily deposit
        total_money = 0
        daily_deposit = 1

        # create a loop to iterate over number of days(n) and calculate amound saved
        for day in range(1, n+1):
            total_money += daily_deposit

            # increment daily deposit by one since we he deposits one more $ more than the previous day
            daily_deposit += 1
            # check if the day is 7 meaning sunday
            if day % 7 == 0:
                # now reset daily deposit to one and add $1 for the next monday
                daily_deposit = day // 7 + 1
        return total_money


savings = Solution()
savings.totalMoney(10)
