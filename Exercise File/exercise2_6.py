# Advanced exercise
import math

# calculate for cherry
cherry = 2 + (2 * 2) - 2 - 2
# calculate for apple
apple = (math.sqrt(3 + 10 - 4) / 3) + (math.pow(5, 3) - 5) / 20 + 3
# calculate for orange
orange = apple - 9
# calculate for banana
banana = ((cherry * 2) - 10) / 3
# calculate for pear
pear = (banana * 3) - 8
# get result and print
result = apple - (banana * 2) + (orange * 2) * (pear + cherry)
print(f"Result: {result}")
