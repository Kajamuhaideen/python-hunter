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
    year_born = ("Paris Hilton", 1981)
    print year_born[0]
    print year_born[1]
    year_born[1] = 2011 # any modification will throw error
if __name__ == '__main__':
    main()
