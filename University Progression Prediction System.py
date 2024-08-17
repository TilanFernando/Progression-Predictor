
#Initialising variables
credit_pass = 0
credit_defer = 0
credit_fail = 0
total_credits = 0
student_count = 0
progress_count = 0
module_trailer_count = 0
module_retriever_count = 0
exclude_count = 0
count = 0

#credit range of values
credit_range = [0,20,40,60,80,100,120]

# input progression data stored using a dictionary 
input_progression_data = {"Progress" : [],"Progress (module trailer)" : [],"Do not Progress – module retriever" : [],"Exclude" : []}


#Function to validate user inputs-------------------------------------

def valid_credits():
    
    global credit_pass,credit_defer,credit_fail
    
    while True:
        
            try:
                credit_pass = int(input("Please enter your credits at Pass : ")) # obtaining user inputs
            except :
                print("--->> Integer Required !!!") #valiting user inputs when non-integer is entered
                continue
            else:
                if credit_pass not in credit_range: #validating user inputs when value entered is out of range
                    print("--->> Out of Range !!!")
                else:
                    break


    while True:
        
            try:
                credit_defer = int(input("Please enter your credits at Defer : "))
            except:
                print("--->> Integer Required !!!")
                continue
            else:
                if credit_defer not in credit_range:
                    print("--->> Out of Range !!!")
                else:
                    break

 
    while True:
            try:
                credit_fail = int(input("Please enter your credits at Fail : "))
            except :
                print("--->> Integer Required !!!")
                continue
            else:
                if credit_fail not in credit_range:
                    print("--->> Out of Range !!!")
                else:
                    break

        
