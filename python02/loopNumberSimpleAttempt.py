def main():
    
    #ask the user to input a number
    #number = eval(input("Please give me a number. "))
    
    current_total = 0
    value = -1
    
    #Brother may i have a loop? 
    while value != 0:
        value = eval(input("Please give me another number. "))
        current_total = current_total + value

    #Encountered a 0 and left loop
        
    #no more loop, no need for if statement here, is redundant
    print("Thank you. Loop Terminated. ")
    print("The Total is: ")
    print(current_total)

main()
