#importing the random mod for random number generation
import random

min_value = 1 #min value
mav_value = 6 #max value as limits
 
#to loop the rolling through user input
roll_again = 'yes'

#loop
while roll_again == 'yes' or roll_again == 'y' :
    print('Rolling the dices ...')
    print('The values are :')
    first_try = random.randint(min_value, mav_value)
    sec_try = random.randint(min_value, mav_value-1) #here we restrict the sec try with max value 5

#if the user get 6, it will trigger again
    print(first_try)
    if first_try == 6 :
        print('Hurray!, you got other chance')
        print(sec_try)
    else:
        roll_again = input("Roll the dice again") #break or continue the loop

