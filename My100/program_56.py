# 56. Define a custom exception class which takes a string message as attribute.

class MyError(Exception):

    def __init__(self,msg):
        self.msg = msg

raise MyError("Error message")