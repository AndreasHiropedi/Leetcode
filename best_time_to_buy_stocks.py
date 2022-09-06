if len(prices) <= 1:
            return 0
        max_profit = prices[1] - prices[0]
        min_element = prices[0]
        for i in range(1, len(prices)):
            if (prices[i] - min_element > max_profit):
                max_profit = prices[i] - min_element
            if (prices[i] < min_element):
                min_element = prices[i]
        if max_profit < 0:
            return 0
        return max_profit
