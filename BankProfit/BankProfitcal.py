# This function finds the buy sell

def stockBuySell(price, n):
	
	# Prices must be given for at
	
	if (n == 1):
		return
	
	# Traverse through given price array
	i = 0
	while (i < (n - 1)):
		
	
		while ((i < (n - 1)) and
				(price[i + 1] <= price[i])):
			i += 1
		
	
		if (i == n - 1):
			break
		
	
		buy = i
		i += 1
		
		
		while ((i < n) and
			(price[i] >= price[i - 1])):
			i += 1
			
	
		sell = i - 1
		
		print("Buy on day: ",buy," ",
				"Sell on day: ",sell)
		
# Driver code


price = [100, 180, 260,
		310, 40, 535, 695]
n = len(price)

# Function call
stockBuySell(price, n)
# This is code contributed by Rahul gupta
