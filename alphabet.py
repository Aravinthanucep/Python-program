#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Aravinthan
#
# Created:     29/01/2018
# Copyright:   (c) Aravinthan 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
  yr=int(input("enter the year"))
  if(yr/4):
    print(yr,"this is leap year")
  else:
    print(yr,"not leap year")

if __name__ == '__main__':
    main()
