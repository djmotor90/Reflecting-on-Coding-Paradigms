# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.
# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.



# Base class representing a generic podracer with basic attributes and functionality.
class Podracer:
    def __init__(self, max_speed, condition, price):
        # Constructor for initializing a podracer with speed, condition, and price.
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        # Method to repair the podracer, setting its condition to 'repaired'.
        self.condition = "repaired"

# Subclass of Podracer representing Anakin's Podracer with enhanced features.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)
    def boost(self):
        # Method to double the max_speed of Anakin's Podracer.
        self.max_speed *= 2

# Subclass of Podracer representing Sebulba's Podracer with unique capabilities.
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)
    def flame_jet(self, other_pod):
        # Method for Sebulba's Podracer to damage another podracer, setting its condition to 'trashed'.
        other_pod.condition = "trashed"


# Once a functional solution to this problem has been implemented, answer the following questions.
# How does this solution ensure data immutability?
        #Answer: The solution does not ensure data immutability. In OOP, especially in Python, object attributes can be changed after an object is created. 
        #This solution allows modification of attributes like max_speed, condition, and price.
# Is this solution a pure function? Why or why not?
        #Answer: The methods in this solution are not pure functions. In OOP, methods often change the state of the object (have side effects), which is contrary to the definition of pure functions. 
        #For example, repair() modifies the condition attribute.
# Is this solution a higher order function? Why or why not?
        #Answer: The solution does not include higher-order functions. Higher-order functions are those that take functions as arguments or return functions. 
        #The methods here operate on the object's state and do not handle functions as inputs or outputs.
# Would it have been easier to solve this problem using a different programming style?
        #Answer: The choice of programming style depends on the requirements and the problem domain. OOP is well-suited for representing entities with attributes and behaviors, 
        #like the Podracer classes. In this case, OOP provides a clear and intuitive structure for the problem.
# Why in particular is functional programming a helpful paradigm when solving this problem?
        #If implemented in a functional programming style, the emphasis would be on immutable data and pure functions, which might offer benefits in terms of predictability and ease of testing, but at the cost of a more natural mapping to real-world entities like podracers.



        