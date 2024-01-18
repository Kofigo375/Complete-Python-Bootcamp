import unittest
import cap
 
## create a class for our testing and 
## inherit from the unittes.TestCase class
class TestCap(unittest.TestCase):

    ## defining test methods
    ## they must start with the word 'text'
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multi_words(self):
        text = 'multi python'
        result = cap.cap_text
        self.assertEqual(result, 'Multi Python')
## the unittest.main() function will look through
## our testcap script and run every method 
## that start with test 
if __name__ == '__main__':
    unittest.main()



