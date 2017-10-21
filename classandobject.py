#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      16ece026
#
# Created:     21/10/2017
# Copyright:   (c) 16ece026 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
   class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')
ob = MyClass()
print(MyClass.func)
print(ob.func)
ob.func()

if __name__ == '__main__':
    main()
