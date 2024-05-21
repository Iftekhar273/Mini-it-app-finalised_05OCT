from tkinter import*
from tkinter import ttk
import webbrowser
import os
import time

#------------------- main screen ---------------------
master = Tk()
master.title("Fitness app 2.0")

options = [
        "Male",
        "Female"
    ]
#------------------- Registration ---------------------
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    height = temp_height.get()
    weight = temp_weight.get()
    password = temp_password.get()

    # ------------------- avoiding overwrite ---------------------
    all_accounts = os.listdir()
    if name == "" or age == "" or gender == "" or height == "" or weight == "" or password == "":
        notif.config(fg="red",text="All fields required * ")
        return

    # ------------------- checking ---------------------
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red",text="Account already exist")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name +'\n')
            new_file.write(password +'\n')
            new_file.write(gender + '\n')
            new_file.write(weight + '\n')
            new_file.write(height + '\n')
            new_file.write(age + '\n')
            new_file.close()
            notif.config(fg="green", text="Account has been created")
def quitprogram():
    master.destroy()

def register():
    # ------------------- global ---------------------
    global temp_name
    global temp_gender
    global temp_height
    global temp_weight
    global temp_password
    global temp_age
    global notif
    global register_screen

    # ------------------- variables ---------------------
    temp_name = StringVar()
    temp_age = StringVar()
    temp_height = StringVar()
    temp_weight = StringVar()
    temp_password = StringVar()

    #------------------- screen ---------------------
    register_screen = Toplevel(master)
    register_screen.title("Register")

    # ------------------- dropdown for gender ---------------------
    temp_gender = StringVar()
    temp_gender.set(options[0])

    drop = OptionMenu(register_screen, temp_gender, *options)
    drop.grid(row=2, column=0)

    # ------------------- labels ---------------------
    Label(register_screen, text="Please enter your details below to register",bg="grey", font=("Calibri", 12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Username", font=("Calibri", 12)).grid(row=1,sticky=W)
    Label(register_screen, text="Gender", font=("Calibri", 12)).grid(row=2,sticky=W)
    Label(register_screen, text="Height/cm", font=("Calibri", 12)).grid(row=3,sticky=W)
    Label(register_screen, text="Weight/kg", font=("Calibri", 12)).grid(row=4,sticky=W)
    Label(register_screen, text="Password", font=("Calibri", 12)).grid(row=5,sticky=W)
    Label(register_screen, text="Age", font=("Calibri", 12)).grid(row=6, sticky=W)

    notif = Label(register_screen, font=("Calibri", 12))
    notif.grid(row=9,sticky=W,pady=10)

    # ------------------- entries ---------------------
    Entry(register_screen, textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen, textvariable=temp_height).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_weight).grid(row=4, column=0)
    Entry(register_screen, textvariable=temp_password,show="*").grid(row=5, column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=6, column=0)

    # ------------------- buttons ---------------------
    Button(register_screen, text="Register", command = finish_reg,width = 10, font=("Calibri",12)).grid(row=7,sticky=N)
    Button(register_screen, text = "Login", font = ("Calibri",12),width = 10, command =lambda:[register_screen.destroy(),login()]).grid(row = 8,sticky=N)
# ---------------------- Login -------------------------
def login_session():
    
    # ------------------- global ---------------------
    global login_name

    # ------------------- reading existing accounts ---------------------
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split("\n")
            password = file_data[1]
            # ------------------- login success ---------------------
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title("Main menu")
                # ------------------- labels ---------------------
                Label(account_dashboard, text="Account dashboard", bg = "grey", font=("Calibri",12)).grid(row=0, sticky=N, pady=10)
                Label(account_dashboard, text="Welcome "+name, font=("Calibri", 12)).grid(row=1, sticky=N, pady=5)

                # ------------------- Buttons ---------------------
                Button(account_dashboard, text="User Profile", font=("Calibri",12),width=30,command=lambda:[account_dashboard.destroy(),user_profile()]).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard, text="BMI calculator", font=("Calibri", 12), width=30,command=lambda:[account_dashboard.destroy(),bmi_calculator()]).grid(row=3, sticky=N,padx=10)
                Button(account_dashboard, text="Food tracker", font=("Calibri", 12), width=30,command=lambda:[account_dashboard.destroy(),food_tracker()]).grid(row=4, sticky=N,padx=10)
                Button(account_dashboard, text="Statistics on exercise", font=("Calibri", 12), width=30,command=lambda:[account_dashboard.destroy(),statistics_on_exercise()]).grid(row=5, sticky=N,padx=10)
                Button(account_dashboard, text="Advices and Videos", font=("Calibri", 12), width=30,command=lambda:[account_dashboard.destroy(),exercise_tips()]).grid(row=6, sticky=N,padx=10)
                Button(account_dashboard, text="Quit", font=("Calibri",12), width=30, bg="grey",command=quitprogram).grid(row=7, sticky=N,padx=10)
                Label(account_dashboard).grid(row=8, sticky=N, pady=10)
                return
        # ------------------- login fail ---------------------
            else:
                login_notif.config(fg="red", text="Password Incorrect !")
            return

    login_notif.config(fg="red", text="No account found !")

# ------------------- user profile ---------------------
def user_profile():
    # ------------------- variables ---------------------
    global personal_details_screen

    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_name = user_details[0]
    details_gender = user_details[2]
    details_height = user_details[4]
    details_weight = user_details[3]
    details_age = user_details[5]

    personal_details_screen = Toplevel(master)
    personal_details_screen.title("User profile")

    # ------------------- labels ---------------------
    Label(personal_details_screen, text="User Profile",bg = "grey", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Username : "+details_name, font=("Calibri", 12)).grid(row=1, sticky=W)
    Label(personal_details_screen, text="Age : " +details_age, font=("Calibri", 12)).grid(row=2, sticky=W)
    Label(personal_details_screen, text="Gender : "+details_gender, font=("Calibri", 12)).grid(row=3, sticky=W)
    Label(personal_details_screen, text="Height : "+details_height, font=("Calibri", 12)).grid(row=4, sticky=W)
    Label(personal_details_screen, text="Weight : "+details_weight, font=("Calibri", 12)).grid(row=5, sticky=W)

    # ------------------- buttons ---------------------
    Button(personal_details_screen, text="Edit", command=profile_edit, font=("Calibri", 12)).grid(row=6, sticky=N, pady=10)
    Button(personal_details_screen, text="Back", font=("Calibri",12),width=30,command=lambda:[personal_details_screen.destroy(),login_session()]).grid(row=7,sticky=N,padx=10)
def profile_edit():
    # ------------------- variables ---------------------
    global new_height
    global new_weight
    global new_age
    global profile_notif

    new_height = StringVar()
    new_weight = StringVar()
    new_age = StringVar()

    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_height = user_details[4]
    details_weight = user_details[3]
    details_age = user_details[5]

    profile_edit_screen = Toplevel(master)
    profile_edit_screen.title("Edit profile")

    profile_notif = Label(profile_edit_screen, font=("Calibri", 12))
    profile_notif.grid(row=5, sticky=N)

    # ------------------- labels ---------------------
    Label(profile_edit_screen, text="Edit profile",bg = "grey", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
    Label(profile_edit_screen, text="User past height : "+details_height, font=("Calibri", 12)).grid(row=1, sticky=W)
    Label(profile_edit_screen, text="User past weight : "+details_weight, font=("Calibri", 12)).grid(row=2, sticky=W)
    Label(profile_edit_screen, text="User past age : " + details_age, font=("Calibri", 12)).grid(row=3, sticky=W)

    # ------------------- entry ---------------------
    Entry(profile_edit_screen, textvariable=new_height).grid(row=1, column=1, padx=5)
    Entry(profile_edit_screen, textvariable=new_weight).grid(row=2, column=1, padx=5)
    Entry(profile_edit_screen, textvariable=new_age).grid(row=3, column=1, padx=5)

    # ------------------- buttons ---------------------
    Button(profile_edit_screen, text="Done", command=profile_edit_finish, font=("Calibri", 12)).grid(row=4, sticky=N, pady=10)

def profile_edit_finish():
    height = new_height.get()
    weight = new_weight.get()
    age = new_age.get()

    if height == "" or weight == "" or age =="":
        profile_notif.config(fg="red",text="All fields required * ")
        return
    # ------------------- variables ---------------------
    file = open(login_name, "r+")
    file_data = file.read()
    user_details = file_data.split("\n")

    details_height = user_details[4]
    updated_height = details_height
    updated_height = height

    details_weight = user_details[3]
    updated_weight = details_weight
    updated_weight = weight

    details_age = user_details[5]
    updated_age = details_age
    updated_age = age

    file_data = file_data.replace(details_height, height)
    file_data = file_data.replace(details_weight, weight)
    file_data = file_data.replace(details_age, age)
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    profile_notif.config(text="Profile edited!",fg="green")

# ------------------- bmi calculator ---------------------
def bmi_calculator():
    # ------------------- variables ---------------------
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split("\n")
    details_height = user_details[4]
    details_weight = user_details[3]

    inte_height = (int(details_height))
    inte_weight = (int(details_weight))

    calculator_screen = Toplevel(master)
    calculator_screen.title("Bmi Calculator")

    bmi_notif = Label(calculator_screen, font=("Calibri", 12))
    bmi_notif.grid(row=4, sticky=N)

    #----------------- bmi calculator ----------------
    details_bmi = inte_weight / ((inte_height / 100) ** 2)
    if details_bmi < 20:
        bmi_notif.config(fg="red", text="User is Underweight")
    elif details_bmi < 25:
        bmi_notif.config(fg="green", text="User is Normal!")
    elif details_bmi > 25:
        bmi_notif.config(fg="red", text="User is Overweight")
    elif details_bmi > 30:
        bmi_notif.config(fg="red", text="User is Obese")
        return

    # ------------------- labels ---------------------
    Label(calculator_screen, text="Bmi Calculator",bg = "grey", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
    Label(calculator_screen, text="Current User height : "+details_height, font=("Calibri", 12)).grid(row=1, sticky=W)
    Label(calculator_screen, text="Current User weight : "+details_weight, font=("Calibri", 12)).grid(row=2, sticky=W)
    Label(calculator_screen, text="User bmi is : "+str(details_bmi), font=("Calibri", 12)).grid(row=3, sticky=W)

    Button(calculator_screen, text="Edit", command=profile_edit, font=("Calibri", 12)).grid(row=5, sticky=N,pady=10)
    Button(calculator_screen, text="Back", font=("Calibri",12),width=30,command=lambda:[calculator_screen.destroy(),login_session()]).grid(row=5,column=1,sticky=N,padx=10)
# -------------------------------------------- Hariz part -----------------------------------------------------------
def food_tracker():
    # ------------------- global ---------------------
    global temp_food
    global temp_amount
    global food_notif
    global my_progress
    global counter_total
    counter_total = int()
    # ------------------- variables ---------------------
    
    temp_food = StringVar()
    temp_amount = StringVar()
    temp_total = StringVar()
 
    #------------------- screen ---------------------
    
    ftrack = Toplevel(master)
    ftrack.title("Food tracker")
    ftrack.config(bg="gray20")
    # ------------------- labels ---------------------
    
    Label(ftrack, text="Welcome to Food tracker!", font=("Calibri",18),bg="gray",fg="white").grid(row=0, sticky=N, pady=10)
    Label(ftrack, text="What did you eat?", font=("Calibri",12),bg="gray",fg="white").grid(row=1,sticky=N,pady=10)
    Label(ftrack, text="How much did you eat? \n(pieces/slices/servings)", font=("Calibri",12),bg="gray",fg="white").grid(row=2,sticky=N,pady=10)
    
    # ------------------- entry ---------------------
    
    Entry(ftrack, textvariable = temp_food,bg="gray").grid(row=1, column =1, padx=5)
    Entry(ftrack, textvariable=temp_amount,bg="gray").grid(row=2, column=1, padx=5)
    
     # ------------------- Buttons ---------------------
     
    Button(ftrack, text="Submit", command = tracking, font=("Calibri",12)).grid(row=4,sticky=N,pady=10)
    Button(ftrack, text="Add food", font=("Calibri", 12), width=30,command=writeFile).grid(row=5, sticky=N,padx=10)
    Button(ftrack, text="Reset progress", command = reset, font=("Calibri",12)).grid(row=4,column=1,sticky=N,pady=10)
    Button(ftrack, text="Main Menu", font=("Calibri",12),bg="light grey",width=30,command=lambda:[ftrack.destroy(),login_session()]).grid(row=6,sticky=N,padx=10)
    Button(ftrack, text="Statistics on exercise",bg="light grey", font=("Calibri", 12),width=20,command=lambda:[ftrack.destroy(),statistics_on_exercise()]).grid(row=6,column=1, sticky=N,padx=10)
    Button(ftrack, text="Advices and Videos",bg="light grey", font=("Calibri", 12),width=20,command=lambda:[ftrack.destroy(),exercise_tips()]).grid(row=7,column=1, sticky=N,padx=10)
    Button(ftrack, text="Quit", font=("Calibri",12),width=20,bg="grey",command=exit).grid(row=8,column=1, sticky=N,padx=10)
    food_notif = Text(ftrack, font= ("Calibri",12), width=40,height=7)
    food_notif.grid(row=3)
    
    #progessbar
    my_progress = ttk.Progressbar(ftrack, orient=VERTICAL, length=250, mode='determinate')    
    my_progress.grid(row=3,column=1)
    
    Label(ftrack, text="<-------------", font=("Calibri",12),bg="gray").grid(row=3,column=1,sticky=NE)
    Label(ftrack, text="2500calories", font=("Calibri",12),bg="gray").grid(row=3,column=2,sticky=NW)
    Label(ftrack, text="<-------------", font=("Calibri",12),bg="gray").grid(row=3,column=1,sticky=E,pady=120)
    Label(ftrack, text="1250calories", font=("Calibri",12),bg="gray").grid(row=3,column=2,sticky=W,pady=120)
    
    
def reset():
    global counter_total
    food_notif.delete("1.0",END)
    my_progress['value'] = 0
    counter_total = 0
    counter = 0
    
    sentence = "The amount of calories is: " + str(counter)
    sentence2 = "The total amount of calories is: " + str(counter_total)
    
    food_notif.insert(END,sentence + "\n")
    food_notif.insert(END,sentence2)
    
def tracking():
    # ------------------- code ---------------------
    global sentence
    global counter_total
    global counter
    temp_prog = my_progress['value']
    food = temp_food.get().lower()
    amount = temp_amount.get()
    sentence = StringVar()
    
    """Opens the file, adds data into dict"""
    food_list = {}  #food in list.txt file is put in here
    counter = int()
    food_notif.delete("1.0",END) #deletes the text in text box so it will not repeat
    
    with open("food.txt") as file:
        for row in file:
            if not row:
                continue
            #split the words and add them to dictionary productList
            else:
                product, values = row.split(',') 
                food_list[product] = values
         
        for char in amount:
            if char.isalpha() == True:
                sentence = "Please re-enter correct amount"
                food_notif.insert(END,sentence + '\n')
                  
        if food in food_list:
            if amount.isdigit() == True:
                x = food_list.get(food) # to get the calorie only
                counter += int(x) * int(amount)     
                counter_total += int(x) * int(amount)
                sentence = "The amount of calories is: " + str(counter)
                sentence2 = "The total amount of calories is: " + str(counter_total)
                food_notif.insert(END,sentence + "\n")
                food_notif.insert(END,sentence2)
                
                counter_progress = counter/2500 * 100
                my_progress['value'] += counter_progress     #adds to progress bar on every meal
                
                if counter_total > 2500:
                    result = Toplevel(master)
                    result.title("Uh OH!!!!!!")
                    Label(result, text="You have exceeded the daily calorie intake!", font=("Helvetica 18 bold"),fg="white",bg="gray20").grid(row=0, sticky=N, pady=10)
                               
        else:
            sentence = "SORRY! Food is not in database"
            food_notif.insert(END,sentence)
           
          
def WriteFile():
    
    name = food_add.get()
    name2 = calorie_add.get()
    productvalue = name +","+name2
    file = open('food.txt','a+')
    file.write("\n" + productvalue)
    file.close()


def writeFile():
    global food_add 
    global calorie_add
    f_add = Toplevel(master)
    f_add.title("Add food")
    
    food_add = StringVar()
    calorie_add = StringVar()
    
    Label(f_add, text="NEW FOOD?!?!", font=("Calibri",12)).grid(row=0, sticky=N, pady=10)
    Label(f_add, text="Calorie!!!!", font=("Calibri",12)).grid(row=1,sticky=N,pady=10)
    
    Entry(f_add, textvariable = food_add).grid(row=0, column =1, padx=5)
    Entry(f_add, textvariable = calorie_add).grid(row=1, column =1, padx=5)
  
    Button(f_add, text="Submit", command =lambda:[f_add.destroy(),WriteFile()], font=("Calibri",12)).grid(row=7,sticky=N,pady=10)
    
# ------------------------------------------- End of hariz part -----------------------------------------------------
# ------------------------------------------- Aiman part -----------------------------------------------------
def statistics_on_exercise():
  def startExercise():
    def first_button():
      def second_button():
        #------------destroy the screen before----------
        first_button.destroy()
        #--------------time calculations---------------
        end_time=time.time()
        duration=(int(end_time - start_time))+0.1
        avg="{:.2f}".format(reps/duration)
        avg= str(avg)
        duration = str(duration)
        #-------------------writing inside the text file------
        fh = open(login_name +'exer.txt', 'a')
        fh.write(n +','+str(duration)+','+str(avg) +',' +str(reps) +'\n')
        fh.close()
        #---------------starting new screen-----------------
        second_button = Toplevel(master)
        second_button.title("Statistics on Exercise")
        #-------------labels---------------------------
        Label(second_button, text="Congrats! You are done doing "+str(reps) +" " +n, font=("Calibri",12)).grid(row=0, sticky=N, pady=10)
        Label(second_button, text="TIME taken is: "+duration +" second(s)", font=("Calibri",12)).grid(row=1, sticky=N, pady=10)
        Label(second_button, text="Thats an average of "+avg +" "+n +" per second!", font=("Calibri",12)).grid(row=2, sticky=N, pady=10)
        Button(second_button, text="Back", font=("Calibri",12),command=lambda:[second_button.destroy(),statistics_on_exercise()]).grid(row=3,sticky=W,pady=20)
        return

      n = temp_exer.get()
      reps = temp_reps.get()
      start_exercise.destroy()
      start_time=time.time()
      first_button = Toplevel(master)
      first_button.title("Statistics on Exercise")
      
      #------------------labels-----------------------
      Label(first_button, text="Currently doing: " +n, font=("Calibri",12)).grid(row=0, sticky=N, pady=10)
      #----------------button---------------------------
      Button(first_button, text="Press when Done!", font=("Calibri",12),command=second_button).grid(row=7,sticky=N,pady=10)

    #----------------variables------------------
    temp_exer = StringVar()
    temp_reps = IntVar()
    #----------------starting the page-----------------
    start_exercise = Toplevel(master)
    start_exercise.title("Statistics on Exercise")
    start_exercise.config(bg="gray20")
    # ------------------- labels ---------------------
    Label(start_exercise, text="Lets start our Exercise. Enter the information below to start!", font=("Calibri",12)).grid(row=0, sticky=N, pady=10)
    Label(start_exercise, text="Current Exercise is?: ", font=("Calibri", 12)).grid(row=1, sticky=W)
    Label(start_exercise, text= "Reps?:" , font=("Calibri", 12)).grid(row=2, sticky=W)
    # ------------------- entries ---------------------
    Entry(start_exercise, textvariable=temp_exer).grid(row=1,column=0, sticky=E)
    Entry(start_exercise, textvariable=temp_reps).grid(row=2,column=0, sticky=E)
    # ------------------- buttons ---------------------
    Button(start_exercise, text="Lets Begin!", font=("Calibri",12),command=first_button).grid(row=7,sticky=N,pady=10)
    Button(start_exercise, text="Back", font=("Calibri",12),command=lambda:[start_exercise.destroy(),statistics_on_exercise()]).grid(row=8,sticky=W,pady=20)

  def checkLogs():
    #------------making sure a text file exists---------
    fh = open (login_name +'exer.txt', 'a')
    fh.close()
    #-----------reading the text file---------------
    fh = open(login_name +'exer.txt','r')
    data = fh.readlines()
    fh.close()

    if len(data) == 0:
      #print("Sorry, no Data!")
      checkLogs = Toplevel(master)
      checkLogs.title("Statistics on Exercise")
      checkLogs.config(bg="gray20")
      
      Label(checkLogs, text="Logs of Previous Exercises: ", font=("Calibri",12)).grid(row=0, sticky=N, pady=10)
      Label(checkLogs, text="There are none :(", font=("Calibri",12)).grid(row=1, sticky=N, pady=10)
      Button(checkLogs, text="Back", font=("Calibri",12),command=lambda:[checkLogs.destroy(),statistics_on_exercise()]).grid(row=8,sticky=W,pady=10)
      return
    else:
      exerData = []
      for count in range(0,len(data)):
        nextWork = data[count].split(',')
        nextWork[1] = float(nextWork[1])
        nextWork[2] = float(nextWork[2])
        exerData.append(nextWork)
        #print(exerData)

      checkLogs = Toplevel(master)
      checkLogs.title("Statistics on Exercise")
      checkLogs.config(bg="gray20")

      Label(checkLogs, text="Logs of Previous Exercises: ", font=("Calibri",12)).grid(row=0, sticky=N, pady=10)

      for item in range(0,len(exerData)):
        Label(checkLogs, text="Exercise: "+exerData[item][0] +"; Time Taken: " +str(exerData[item][1]) +"secs ; Reps per second: " +str(exerData[item][2]) +"; Reps Done: "+str(exerData[item][3]) , font=("Calibri",12)).grid(row=item+1, sticky=N, pady=10,padx=10)
      Button(checkLogs, text="Back", font=("Calibri",12),command=lambda:[checkLogs.destroy(),statistics_on_exercise()]).grid(row=item+2,sticky=W,pady=10)
      return

  #def setExercise():
    def change():
      n = temp_exercise.get()
      #name = temp_name.get()
      setExercise.destroy()
      return n
    temp_exercise = StringVar()

    setExercise = Toplevel(master)
    setExercise.title("Statistics on Exercise")
    # ------------------- labels ---------------------
    Label(setExercise, text="Enter your preferred Exercise!", font=("Calibri",12)).grid(row=0, sticky=N, pady=10)
    Label(setExercise, text="Current Exercise is: ", font=("Calibri", 12)).grid(row=1, sticky=W, pady=5)
    Label(setExercise, text= n , font=("Calibri", 12)).grid(row=1, sticky=E, pady=5)

    Label(setExercise, text= "Exercise:" , font=("Calibri", 12)).grid(row=2, sticky=W)

    # ------------------- entries ---------------------
    Entry(setExercise, textvariable=temp_exercise).grid(row=2,column=0, sticky=E)

    # ------------------- buttons ---------------------
    Button(setExercise, text="Lets Begin!", font=("Calibri",12),command=change).grid(row=7,sticky=N,pady=10)

    return n

  exercise_dashboard = Toplevel(master)
  exercise_dashboard.title("Statistics on Exercise")
  exercise_dashboard.config(bg="gray20")
  # ------------------- labels ---------------------
  Label(exercise_dashboard, text="Welcome to Exercise and Statistics!", font=("Calibri",12)).grid(row=0,column=1, sticky=N, pady=10)

  # ------------------- Buttons ---------------------
  Button(exercise_dashboard, text="Start Your Exercise", font=("Calibri",12),bg="white",width=30,command=lambda:[exercise_dashboard.destroy(),startExercise()]).grid(row=3,column=1,sticky=N,padx=10)
  Button(exercise_dashboard, text="Your Previous Logs", font=("Calibri", 12),bg="white",width=30,command=lambda:[exercise_dashboard.destroy(),checkLogs()]).grid(row=4,column=1,sticky=N,padx=10)
  Button(exercise_dashboard, text="Main Menu", font=("Calibri",12),bg="light grey",width=30,command=lambda:[exercise_dashboard.destroy(),login_session()]).grid(row=5,column=1,sticky=N,padx=10)
  Button(exercise_dashboard, text="Food tracker", font=("Calibri", 12),bg="light grey", width=30,command=lambda:[exercise_dashboard.destroy(),food_tracker()]).grid(row=6, column=1)
  Button(exercise_dashboard, text="Advices and Videos", font=("Calibri", 12),bg="light grey", width=30,command=lambda:[exercise_dashboard.destroy(),exercise_tips()]).grid(row=7,column=1)
  Button(exercise_dashboard, text="Quit",bg="grey", font=("Calibri", 12), width=30,command=exit).grid(row=8, column=1)
  master.mainloop()

# ------------------------------------------- End of Aiman part -----------------------------------------------------
# ------------------------------------------- Iftekhar part -----------------------------------------------------
def exercise_tips():
    


    master = Tk()
    master.title("Advices and Videos")
    master.config(bg="gray20")
       
    def tips():
        master.withdraw() #.destroy() will destroy a window
        #--------------------screen---------------------
        
           
        root = Toplevel()
        root.title("Tips")
        root.geometry("300x300")

        def newWin ():
            if tips1.get() == "Eating":
                root.withdraw()
                new = Toplevel()
                new.title("Eating")
                
                openFile = open("tips.txt", "r")
                data = openFile.read()
                openFile.close()
                
                Label(new, text=data).pack()
                
                
                def button_3():
                    new.destroy() #.destroy() will destroy a window
                    root.deiconify()
            
            
            #---------------------buttons---------------------
            
                my_button2 = Button(new, text="Back", font=("Calibri", 12), width=30,command=button_3, bg='grey')
                my_button2.pack(side="bottom")
                new.mainloop()
            if tips1.get() == "Exercising":
                root.withdraw()
                new = Toplevel()
                new.title("Exercising")
                
                openFile = open("tips_2.txt", "r")
                data = openFile.read()
                openFile.close()
                    
                Label(new, text=data).pack()
                
                
                def button_3():
                    new.destroy() #.destroy() will destroy a window
                    root.deiconify()
            
            
            #---------------------buttons---------------------
            
                my_button2 = Button(new, text="Back", font=("Calibri", 12), width=30,command=button_3, bg='grey')
                my_button2.pack(side="bottom")
                
                new.mainloop()
            if tips1.get() == "Sleep":
                root.withdraw()
                new = Toplevel()
                new.title("Sleep")
                
                openFile = open("tips_3.txt", "r")
                data = openFile.read()
                openFile.close()
                    
                Label(new, text=data).pack()
                
                
                def button_3():
                    new.destroy() #.destroy() will destroy a window
                    root.deiconify()
            
            #---------------------buttons---------------------
            
                my_button2 = Button(new, text="Back", font=("Calibri", 12), width=30,command=button_3, bg='grey')
                my_button2.pack(side="bottom")
                
                new.mainloop()    
        tips1 = StringVar()

                        #window, variable, options all seperated by ","
        dropdown_main = OptionMenu(root, tips1, "Eating", "Exercising", "Sleep")
        dropdown_main.pack()

        button_main = Button(root, text="Open", command=newWin).pack() 
        
            
        def button_2():
            root.destroy() #.destroy() will destroy a window
            master.deiconify()
        
        
        #---------------------buttons---------------------
        
        my_button2 = Button(root, text="Back", font=("Calibri", 12), width=30,command=button_2, bg='grey')
        my_button2.pack(side="bottom")


    def heatlth_benifits_of_different_fruits():
        master.withdraw()
        #--------------------screen---------------------
        fruits_screen=Toplevel(master)
        fruits_screen.title("Heatlth benifits of different fruits")
        #-------------------Label-----------------------
        Label(fruits_screen,text="Select One Fruit\n",font=("Calibri", 12)).grid(row=0, sticky=N,pady=10)
        def button_4():
            fruits_screen.destroy()
            master.deiconify()
            
        
            
        def Orange ():
            def button_3():
                orange_screen.destroy()
                fruits_screen.deiconify()
            fruits_screen.withdraw()
            #--------------------screen---------------------
            orange_screen=Toplevel(master)
            orange_screen.title("Orange")
            Label(orange_screen,text="\ni)Oranges are water-rich.",font=("Calibri", 12)).grid(row=0, sticky=N,pady=10)
            Label(orange_screen,text="\nii)High in Vitamin C,Oranges are an excellent source of vitamin C. ",font=("Calibri", 12)).grid(row=1, sticky=N,pady=10)
            Label(orange_screen,text="\niii)Prevents skin damage.",font=("Calibri", 12)).grid(row=2, sticky=N,pady=10)
            my_button2 = Button(orange_screen, text="Back", font=("Calibri", 12), width=30,command=button_3, bg='grey')
            my_button2.grid(row=3, sticky=N,padx=10)
        def Apple ():
            def button_3():
                apple_screen.destroy()
                fruits_screen.deiconify()
            fruits_screen.withdraw()
            #--------------------screen---------------------
            apple_screen=Toplevel(master)
            apple_screen.title("Apple")
            Label(apple_screen,text="\ni)Apples May Be Good for Weight Loss.",font=("Calibri", 12)).grid(row=0, sticky=N,pady=10)
            Label(apple_screen,text="\nii)Apples May Be Good for Your Heart.",font=("Calibri", 12)).grid(row=1, sticky=N,pady=10)
            Label(apple_screen,text="\niii)Apples are Linked to a Lower Risk of Diabetes. ",font=("Calibri", 12)).grid(row=2, sticky=N,pady=10)
            my_button2 = Button(apple_screen, text="Back", font=("Calibri", 12), width=30,command=button_3, bg='grey')
            my_button2.grid(row=3, sticky=N,padx=10)
        def Jackfruit():
            def button_3():
                jackfruit_screen.destroy()
                fruits_screen.deiconify()
            fruits_screen.withdraw()
            #--------------------screen---------------------
            jackfruit_screen=Toplevel(master)
            jackfruit_screen.title("Jackfruit")
            Label(jackfruit_screen,text="\ni)Helps in Curing Mental Stress and Skin Diseases.",font=("Calibri", 12)).grid(row=0, sticky=N,pady=10)
            Label(jackfruit_screen,text="\nii)It Prevents Anaemia.",font=("Calibri", 12)).grid(row=1, sticky=N,pady=10)
            Label(jackfruit_screen,text="\niii)Healthy Hair and Good Eyesight.",font=("Calibri", 12)).grid(row=2, sticky=N,pady=10)
            my_button2 = Button(jackfruit_screen, text="Back", font=("Calibri", 12), width=30,command=button_3, bg='grey')
            my_button2.grid(row=3, sticky=N,padx=10)        
        def Durian () :
            def button_3():
                durian_screen.destroy()
                fruits_screen.deiconify()
            fruits_screen.withdraw()
            #--------------------screen---------------------
            durian_screen=Toplevel(master)
            durian_screen.title("Durian")
            Label(durian_screen,text="\ni)Reduces cancer risk. Its antioxidants may neutralize cancer-promoting free radicals.",font=("Calibri", 12)).grid(row=0, sticky=N,pady=10)
            
            Label(durian_screen,text="\nii)Prevents heart disease. Several compounds in durian may help reduce cholesterol levels and your risk of atherosclerosis, or the hardening of your arteries.",font=("Calibri", 12)).grid(row=1, sticky=N,pady=10)
            Label(durian_screen,text="\niii)Lowers blood sugar.",font=("Calibri", 12)).grid(row=2, sticky=N,pady=10)
            my_button2 = Button(durian_screen, text="Back", font=("Calibri", 12), width=30,command=button_3, bg='grey')
            my_button2.grid(row=3, sticky=N,padx=10)
        def Banana ():
            def button_3():
                banana_screen.destroy()
                fruits_screen.deiconify()
            fruits_screen.withdraw()
            #--------------------screen---------------------
            banana_screen=Toplevel(master)
            banana_screen.title("Banana")
            Label(banana_screen,text="\ni)Bananas are respectable sources of vitamin C.",font=("Calibri", 12)).grid(row=0, sticky=N,pady=10)
            Label(banana_screen,text="\nii)Manganese in bananas is good for your skin.",font=("Calibri", 12)).grid(row=1, sticky=N,pady=10) 
            Label(banana_screen,text="\niii)Potassium in bananas is good for your heart health and blood pressure.",font=("Calibri", 12)).grid(row=2, sticky=N,pady=10)
            my_button2 = Button(banana_screen, text="Back", font=("Calibri", 12), width=30,command=button_3, bg='grey')
            my_button2.grid(row=3, sticky=N,padx=10)
        #---------------------Buttons------------------------
        my_button3 = Button(fruits_screen, text="Oranges", font=("Calibri",12),width=30,command=Orange)
        my_button3.grid(row=1, sticky=N,padx=10)
        my_button4 = Button(fruits_screen, text="Apple", font=("Calibri",12),width=30,command=Apple)
        my_button4.grid(row=2, sticky=N,padx=10)
        my_button5 = Button(fruits_screen, text="Jackfruit", font=("Calibri",12),width=30,command=Jackfruit)
        my_button5.grid(row=3, sticky=N,padx=10)
        my_button6 = Button(fruits_screen, text="Durian", font=("Calibri",12),width=30,command=Durian)
        my_button6.grid(row=4, sticky=N,padx=10)
        my_button7 = Button(fruits_screen, text="Banana", font=("Calibri",12),width=30,command=Banana)
        my_button7.grid(row=5, sticky=N,padx=10)
        my_button8 = Button(fruits_screen, text="Back", font=("Calibri", 12), width=30,command=button_4, bg='grey')
        my_button8.grid(row=6, sticky=N,padx=10)

    def Video():
        master.withdraw() #.destroy() will destroy a window
        #--------------------screen---------------------
        video_screen=Toplevel(master)
        video_screen.title("Video")
        def button_2():
            video_screen.destroy() #.destroy() will destroy a window
            master.deiconify()
        def onClick(x):
            webbrowser.open(x,new=1)


        label = Label(video_screen,text="Videos")
        label.grid(row=0, sticky=N,padx=10)

        def firstVideo() :
            
            labelOne = Label(video_screen,text="Click Here to Watch 10 Simple Exercises To Lose Weight At Home")
            labelOne.grid(row=1, sticky=N,padx=10)


            url = "https://www.youtube.com/watch?v=YjmQVMLhNT4"

            click = Button(video_screen,text="Click", command=lambda: onClick(url))
            click.grid(row=2, sticky=N,padx=10)
        firstVideo()

        def secondVideo():
            labelOne = Label(video_screen,text="Click Here to Watch 5 Healthy Low Calorie Recipes For Weight Loss")
            labelOne.grid(row=3, sticky=N,padx=10)


            url = "https://www.youtube.com/watch?v=QYcw8QbYj8o"

            click = Button(video_screen,text="Click", command=lambda: onClick(url))
            click.grid(row=4, sticky=N,padx=10)

        secondVideo()

        def thirdVideo():
            labelOne = Label(video_screen,text="Click Here to Watch 10 minute Morning Yoga for Beginners")
            labelOne.grid(row=5, sticky=N,padx=10)


            url = "https://www.youtube.com/watch?v=VaoV1PrYft4"

            click = Button(video_screen,text="Click", command=lambda: onClick(url))
            click.grid(row=6, sticky=N,padx=10)

        thirdVideo()

        my_button2 = Button(video_screen, text="Back", font=("Calibri", 12), width=30,command=button_2, bg='grey')
        my_button2.grid(row=7, sticky=N,padx=10)
    def main(): 
        
        #--------------------screen---------------------
        main_screen=master
        main_screen.title("Advices and Videos")

        #-------------------- labels ---------------------
        Label(main_screen, text="Choose One", font=("Calibri", 12)).grid(row=0,column=1,sticky=N,pady=10)
        #---------------------buttons---------------------
        Button(main_screen, text="Tips", font=("Calibri",12),width=30,command=tips).grid(row=2,column=1,sticky=N,padx=10)
        Button(main_screen, text="Heatlth benifits of different Fruits", font=("Calibri", 12), width=30,command=heatlth_benifits_of_different_fruits).grid(row=3,column=1, sticky=N,padx=10)
        Button(main_screen, text="Videos", font=("Calibri", 12), width=30,command=Video).grid(row=4,column=1, sticky=N,padx=10)
        Button(main_screen, text="Main Menu", font=("Calibri",12),bg="light grey",width=30,command=lambda:[main_screen.destroy(),login_session()]).grid(row=5,column=1,sticky=N,padx=10)
        Button(main_screen, text="Food tracker", font=("Calibri", 12),bg="light grey", width=30,command=lambda:[main_screen.destroy(),food_tracker()]).grid(row=6, column=0)
        Button(main_screen, text="Statistics on exercise", font=("Calibri", 12),bg="light grey", width=30,command=lambda:[main_screen.destroy(),statistics_on_exercise()]).grid(row=6, column=1)
        Button(main_screen, text="Quit", font=("Calibri", 12),bg="grey", width=30,command=exit).grid(row=6, column=3)
        
    main()




# ------------------------------------------- End of Iftekhar's part -----------------------------------------------------
def backbutton_master():
    login_screen.destroy()
    master.deiconify()

# ---------------------- Login -------------------------
def login():
    # ------------------- global variables ---------------------
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    master.withdraw()
    # ------------------- Variables ---------------------
    temp_login_name = StringVar()
    temp_login_password = StringVar()

    # ------------------- login screen ---------------------
    login_screen = Toplevel(master)
    login_screen.title("Login")

    # ------------------- Labels ---------------------
    Label(login_screen, text="Login to your account",bg="grey", font=("Calibri",12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text="Username", font=("Calibri",12)).grid(row=1,sticky=W)
    Label(login_screen, text="Password", font=("Calibri",12)).grid(row=2,sticky=W)

    # ------------------- notification ---------------------
    login_notif = Label(login_screen, font= ("Calibri",12))
    login_notif.grid(row=5,sticky=N)

    # ------------------- entry ---------------------
    Entry(login_screen, textvariable = temp_login_name).grid(row = 1, column = 1, padx = 5)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=2, column=1, padx=5)

    # ------------------- buttons ---------------------
    Button(login_screen, text = "Login", command = login_session, width = 15, font = ("Calibri",12)).grid(row=3,sticky=W,pady=5,padx=5)
    Button(login_screen, text="Back", command=backbutton_master, width=15, font=("Calibri", 12)).grid(row=4, sticky=W,pady=5, padx=5)

#------------------- labels ---------------------
Label(master, text = "Fitness app Beta", bg = "grey", font = ("Calibri",14)).grid(row = 0,sticky = N,pady = 10)
Label(master, text = "welcome to our fitness app", font = ("Calibri",12)).grid(row = 1,sticky = N)

#------------------- buttons ---------------------
Button(master, text = "Register", font = ("Calibri",12),width = 20, command = register).grid(row = 3,sticky = N)
Button(master, text = "Login", font = ("Calibri",12),width = 20, command = login).grid(row = 4,sticky = N,pady = 10)

master.mainloop()