from mockito import mock, verify
import unittest
#import sys

# Using double backslashes
#sys.path.append("C:\\Users\\vanid\\Documents\\lab-devops\\pyb\\src\\main\\python")

# Or using raw string literal
# sys.path.append(r"C:\Users\vanid\Documents\lab-devops\pyb\src\main\python")
#
from helloworld import helloworldd

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        # Create a mock object for 'out'
        out = mock()
        
        # Call the function to be tested
        helloworldd(out)
        
        # Verify that the 'write' method of the 'out' object was called with the expected message
        verify(out).write("Hello world of Python\n")

if __name__ == "__main__":
    unittest.main()
