import unittest
import landscape
import math
from Lab9 import Sled
import Lab9

class TestSled(unittest.TestCase):
    def setUp(self):
        self.sled = Sled('TestSled', 0.1)
    
    def test_initialization(self):
        self.assertEqual(self.sled.name, 'TestSled')
        self.assertEqual(self.sled.speed, 0.1)
        self.assertTrue(-10 <= self.sled.position <= 10)

    def test_found_treasure(self):
        # If the sled is at the treasure's position, it should have found the treasure
        self.sled.position = -1.3
        self.assertTrue(self.sled.found_treasure(-1.3, 0.05))
        
        # If the sled is too far from the treasure's position, it should not have found the treasure
        self.sled.position = 0
        self.assertFalse(self.sled.found_treasure(-1.3, 0.05))

class TestLandscape(unittest.TestCase):
    def test_elevation(self):
        # The elevation at position 0 should be 0
        self.assertEqual(landscape.elevation(0), 0)
        
        # The elevation at position 1 should be 1 + 10*sin(1)
        self.assertEqual(landscape.elevation(1), 1 + 10*math.sin(1))

    def test_slope(self):
        # The slope at position 0 should be 0
        self.assertEqual(landscape.slope(0), 10)
        
        # The slope at position 1 should be 2*1 + 10*cos(1)
        self.assertEqual(landscape.slope(1), 2*1 + 10*math.cos(1))

if __name__ == '__main__':
    unittest.main()
