# 55. Write a function to compute 5/0 and use try/except to catch the exceptions.

def func():

    try:
        print(5/0)
    except Exception:
        print("Error")
    finally:
        print("Final Error")
func()
