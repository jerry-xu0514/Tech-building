class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    """names, values, calories lists of same length.
       name a list of strings
       values and calories lists of numbers
       returns list of Foods"""
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

def testGreedys(foods, maxC):
    print("use greedy by value to allocate", maxC, 'calories')

    testGreedy

def testGreedy(foods, maxC, Food.getvalue):
    items, val = greedy(foods, maxC)

# cheese burgers, fries, wine, steak, noodles, ramen, sushi, fried rice
# V:  100          72    120    99      33       43    130      76
# C:  500          440   200   1200     230      330   238      598
# 
# Cap: 1000 calories
# 
[0,0,0,0],[1,0,0,0],[0,1,0,0]
# toe-knee: 
# Efficiency: value per calorie, we find the max value per cal, and then go 
# in descending order.
#  


# brute force:
# find all possible combos, and then compare
# bad because its a lot of work
# O(2^n) time complexity 

# N = 8

# Sachi: 
# highest value, then lowest calorie, then second value, second low cal... etc.

# cheese burgers, fries, wine, steak, noodles, ramen, sushi, fried rice
# V:   999          1     998   2       997      3    996       4
# C:   800          200    201  444     444      444  444       444          
# 

# Greedy algorithm
# we want to maximize value
# We will maximize value EVERY step of the process
# We will always choose the item with the GREATEST value
# then we remove it from the list of available items
# then we repeat the process until:
#   calories remaining is not enough to fit any more items
