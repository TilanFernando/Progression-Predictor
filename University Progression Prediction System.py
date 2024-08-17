
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

#Function to add multiple outcomes or exit to view histogram ---------------------------------------------------
        
def multiple_outcomes_or_exit_to_histogram():
    global multiple_outcomes

    while True:
        try:
            print("\n")
            print("Would You Like to enter another set of values?")
            
            multiple_outcomes = str(input("Enter 'q' to Quit or 'y' to add another student : "))

           
            if multiple_outcomes == "y":
                    print("\n")
                    staff_version()
            else:
                if multiple_outcomes == "q":
                        print("\n")
                        histogram()
                        input_progression_data_list()
                        textfile()
                        break
                        print("\n")
                 
        except ValueError:
              print("----------------------------------------------------------")
              print("--->> Invalid Input !!!")
              print("\n")
              multiple_outcomes_or_exit_to_histogram()
              break

#Function to print the histogram

def histogram():
    global progress_count,module_trailer_count,module_retriever_count,exclude_count,count
    while True:
            print("----------------------------------------------------------")
            print("                        HISTOGRAM                         ")
            
            print()
          
            print("Progress                           (",(progress_count),"):",progress_count * '*')
            
            print("Progress(Module-Trailer)           (",(module_trailer_count),"):",module_trailer_count * '*')

            print("Do not Progress - Module Retriever (",(module_retriever_count),"):",module_retriever_count * '*')
         
            print("Exclude                            (",(exclude_count),"):",exclude_count * '*')
            
            print()
            
            print(count,"Student Outcomes in Total.") # Displaying total outcomes

            print("----------------------------------------------------------")

            print("\n")
            break     

#function to display input progression data----------------------------------- 

def input_progression_data_list():

    print("(PART 2)")
    print()
    print("Progress :",(input_progression_data["Progress"]))
    print("Progress (Module-Trailer) : ",(input_progression_data["Progress (module trailer)"]))
    print("Do not Progress – Module Retriever : ",(input_progression_data["Do not Progress – module retriever"]))
    print("Exclude : ",(input_progression_data["Exclude"]))
