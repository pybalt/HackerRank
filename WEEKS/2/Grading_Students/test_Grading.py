import unittest
from Grading_Students import gradingStudents


class Solution(unittest.TestCase):
    
    def test_fourP_returned_values(self):
        self.assertEqual(gradingStudents([75, 67,
                                          40, 33]), [75, 67,
                                                    40, 33])
    
    def test_twoP_returned_values(self):
        self.assertEqual(gradingStudents([37, 38]), [37, 40])
    
    def test_sevenP_returned_values(self):
        self.assertEqual(gradingStudents([27, 23, 65, 
                                          43, 
                                          0, 82, 0]),
                                        
                                        [27, 23, 65, 
                                         45, 
                                         0, 82, 0])
    def test_rare_input(self):
        self.assertEqual(gradingStudents([80, 96, 18, 
                                         73, 78, 60, 
                                         60, 15, 45, 
                                         15, 10, 5, 
                                         46, 87, 33, 
                                         60, 14, 71, 
                                         65, 2, 5, 
                                         97, 0]), [80, 96, 18, 
                                                  75, 80, 60, 
                                                  60, 15, 45, 
                                                  15, 10, 5, 
                                                  46, 87, 33, 
                                                  60, 14, 71, 
                                                  65, 2, 5, 
                                                  97, 0])