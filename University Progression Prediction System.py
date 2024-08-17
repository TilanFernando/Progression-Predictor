
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

        #Defining function to get the progression outcome-----------------------------------------------------------

def progression_outcome():

    #global variables
    global credit_pass,credit_defer,credit_fail,progress_count,module_trailer_count,module_retriever_count,exclude_count,count

    count += 1 #total inputs count

    # using loop to select progression outcome when the if conditions are satisfied
    while True:

        if credit_pass ==120 and credit_defer == 0 and credit_fail == 0:

                print("----------------------------------------------------------")
                print("PROGRESS")
                print("\n")
                progress_count += 1 #count for the histogram
                input_progression_data["Progress"].append(str(credit_pass) + ", " + str(credit_defer) + ", " + str(credit_fail))#according to progression outcome obtaining input progression data 
                break
            
        elif credit_pass == 100 and (credit_defer ==20 or credit_fail == 20):
                
                print("----------------------------------------------------------")
                print("PROGRESS-MODULE TRAILER")
                print("\n")
                module_trailer_count += 1
                input_progression_data["Progress (module trailer)"].append(str(credit_pass) + ", " + str(credit_defer) + ", " + str(credit_fail))#according to progression outcome obtaining input progression data 
                break
            
        elif credit_pass <= 80 and (credit_defer >= 40 or credit_fail < 80) or (credit_defer <= 40 or credit_fail <= 80):
                
                print("----------------------------------------------------------")
                print("DO NOT PROGRESS-MODULE RETRIEVER")
                print("\n")
                module_retriever_count += 1
                input_progression_data["Do not Progress – module retriever"].append(str(credit_pass) + ", " + str(credit_defer) + ", " + str(credit_fail))#according to progression outcome obtaining input progression data 
                break
            
        elif credit_pass in range(0,41,20) and (credit_defer < 40 or credit_fail >= 80):
                
                print("----------------------------------------------------------")
                print("EXCLUDE")
                print("\n")
                exclude_count += 1
                input_progression_data["Exclude"].append(str(credit_pass) + ", " + str(credit_defer) + ", " + str(credit_fail))#according to progression outcome obtaining input progression data 
                break
