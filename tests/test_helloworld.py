from helloworld import hello_world
from helloworld import another_function

def test_check_default():
    assert hello_world() == "Hello, World!"

def test_check_given_name():
    assert hello_world("jimbo") == "Hello, jimbo"

def test_another_function():
    assert another_function() == "This is another function!"