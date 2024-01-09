import unittest

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
        super().__init__(max_speed, condition, price)

    def boost(self):
        # Method to double the max_speed of Anakin's Podracer.
        self.max_speed *= 2

# Subclass of Podracer representing Sebulba's Podracer with unique capabilities.
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other_pod):
        # Method for Sebulba's Podracer to damage another podracer, setting its condition to 'trashed'.
        other_pod.condition = "trashed"

# Test class for the Podracer system
class TestPodracerSystem(unittest.TestCase):

    def test_podracer_repair(self):
        podracer = Podracer(100, 'trashed', 500)
        podracer.repair()
        self.assertEqual(podracer.condition, 'repaired')

    def test_anakinspod_boost(self):
        anakinspod = AnakinsPod(100, 'perfect', 1000)
        anakinspod.boost()
        self.assertEqual(anakinspod.max_speed, 200)

    def test_sebulbaspod_flame_jet(self):
        sebulbaspod = SebulbasPod(150, 'perfect', 1500)
        target_pod = Podracer(100, 'perfect', 500)
        sebulbaspod.flame_jet(target_pod)
        self.assertEqual(target_pod.condition, 'trashed')

# This block ensures that the tests only run when the script is executed directly
if __name__ == '__main__':
    unittest.main()
