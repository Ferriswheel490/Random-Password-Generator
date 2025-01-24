#Fairus De La Cruz Random Password Generator


'''''
A function for password
like how long it should be
letters in lower and uppercase
numbers and special charaters
'''''
def first_step(how_long):
    how_long = input('how long is your password:')


def letters(y,n, upper_letters, lower_letters, lower_upper):
    does_it_need_letters = input("does it need letters:")
    y = input("yes")
    if does_it_need_letters == True:
        do_you_want_upper__lower_or_both = input("do you want uppercase, lowercase, or both:")
        if upper_letters == upper_letters:
            print("ok")
        
        elif lower_letters == lower_letters:
            print("ok")
        
        elif lower_upper == lower_upper:
            print("it'll have both upper and lower case")
        
        elif n == n:
            print("it might not be strong")
        
        else:
            print("it might not be stong but do what you want")
            

def special_chataters(special_charaters, yes, no):
    special_charaters = input("do you want special charaters:")
    if special_charaters == yes:
        print("It'll have special charaters")
    else:
        print("that is not an option")
