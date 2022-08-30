# It's a function that generates reports and displays statistics about the reports.
# imported modules 
from dateutil.parser import parse
import datetime

'''
It's a function that generates reports and displays statistics about the reports.
'''

# Its a function that registers a user
def reg_user():
 # Used a while True loop to ask input multiple times
 while True:
  username_one = input("Enter username you want to register: ")
  password_one = input("Enter password you want to register: ")
  # used with open to open the "user.txt"
  with open("user.txt","r") as f:
   # created a variable called "f" and assigned it to f.readlines() to read all the lines in the file
   var_1 = f.readlines()
   # created a variable called "var_2" and assigned it to read all the lines in the file var_2 joined
   var_2 = " ".join(var_1).replace("\n","")
   # created a variable called "var_3" and assigned it to var_2 and used the replace function to to replace the comma to an empty string
   var_3 = var_2.replace(",","")
   # created a variable called var_4 and used the split function to created a list with splited in a string
   var_4 = var_3.split()
   # created empty lists
   list_one = []
   list_two = []
   for i in range(len(var_4)):
    if i % 2 == 0:
     list_one.append(var_4[i])
    else:
     list_two.append(var_4[i]) 


  if username_one in list_one:
   print("sorry username already taken") 
  elif username_one not in list_one:
   with open("user.txt","a") as x:
    x.write("\n" + f"{username_one}, {password_one}")
   break


def add_task():
  # created a variable called add_info and assigned it to user input requesting input
  add_info = input("Enter your another username: ")
  # created a variable called title_task and assigned it to user input requesting input
  title_task = input("Enter new title task: ")
  # created a variable called describe_task and assigned it to user input requesting input
  describe_task = input("Enter new description: ")
  # created a variable called due_date and assigned it to user input requesting input
  due_date = input("Enter the due date: ")
  # created a variable called current_date and assigned it to user input requesting input
  current_date = input("Enter current date: ")
  with open("tasks.txt","a") as g:
   # used the write funtion to write on to the file
   g.write("\n" + f"{add_info}, {title_task}, {describe_task}, {due_date}, {current_date}, No")

# the view_all() function will display all the info in a readable manner
def view_all():
 with open("tasks.txt","r") as f:
     var_1 = f.readlines()
     for i in var_1:    
      var_1 = i.replace("\n","")
      var_2 = var_1.split(",")
      print(" " + "Task:" + "\t\t\t\t\t\t" + var_2[1] + "\n", "Assigned to:"+ "\t\t\t\t " + var_2[0] + "\n", "Date assigned:" + "\t\t\t" + var_2[3] + "\n", "Due date:" + "\t\t\t\t\t" + var_2[4] + "\n", "Task Complete?" + "\t\t\t" + var_2[5] + "\n", "Task description:" + "\t\t" + var_2[2] + "\n") 

def view_mine():
 with open("tasks.txt","r") as f:
  viewm_1 = f.readlines()
  for i in viewm_1:
   viewm_1 = i.replace("\n","").split(",")
   # if the following is in viewm_1, the following will be ran
   if username in viewm_1:
    print(f"User Assigned:     {viewm_1[0]}")
    print(f"Task Title:       {viewm_1[1]}")
    print(f"Task Description: {viewm_1[2]}")
    print(f"Date Assigned:    {viewm_1[3]}")
    print(f"Due Date:         {viewm_1[4]}")
    print(f"Completion:       {viewm_1[5]}\n")
    
 with open("tasks.txt","r") as f:
   viewm_1 = f.readlines()
   count = 0
   count_list1 = []
   count_list2 = []
   for i in viewm_1:
      count+=1
      viewm_2 = i.replace("\n","").split(",") 
      count_list1.append(str(count))
      count_list2.append(viewm_2)
      

 for x,y in zip(count_list1,count_list2): 
  print(x,y)
  
 # created an empty list 
 contents_list = []
 task_one = str(input("Enter the number of the task you would like to mark the task as complete or edit the task: ")) 
 for x1,y1 in zip(count_list1,count_list2): 
  # if the following is true than the statement will be executed
  if task_one == x1:
   mark_one = input("Choose whether to (mark the task as complete) or (edit the task): ")
   if mark_one == "edit the task":
    edit_opt = input("Pick whether to edit (username1) or (due date1): ")
    if edit_opt == "username1":
     edit_username = input(" Enter the new username you would like to change to: ")
     
     y1[0] = edit_username 
     contents_list.append(",".join(y1))
   
    elif edit_opt == "due date1":
     edit_date = input(" Enter the new date you would like to change to: ")
     y1[4] = edit_date
     contents_list.append(",".join(y1))
  
   elif mark_one == "mark the task as complete":
    y1[5] = " Yes"
    contents_list.append(",".join(y1))
 
  else:
   contents_list.append(",".join(y1))

 with open("tasks.txt","w+") as output_1:
  for j2 in contents_list:
   output_1.write(j2+"\n")


 menu_info = input("Enter -1 to go back to menu or 1 to end: ")
 if menu_info == "-1":
  menu_func()
 elif menu_info == "1":
  pass
  

def gen_rep(): 
 completed_list = []
 incomplte_list = []
 overdue_list = []
 overdue_list2 = []
 task_list = []
 with open("tasks.txt", "r") as f:
  view_lines = f.readlines()
  j = 0
  for i in view_lines:
   view_each = i.replace("\n","").split(",")
   j += 1
   completed_list.append(view_each.count(" Yes"))
   incomplte_list.append(view_each.count(" No"))
   task_list.append(view_each[1])
   object_date = parse(view_each[4])
   # used the parse and the datetime module to compare dates
   if " No" in view_each and object_date < datetime.datetime.today():
    overdue_list.append(view_each)
   elif object_date < datetime.datetime.today():
    overdue_list2.append(object_date)

 with open("task_overview.txt","w") as task_view:  
  task_view.write("INFO FOR ALL TASKS\n")  
  task_view.write(f"The total number of tasks that have been generated and tracked: {j}\n")
  task_view.write(f"The total number of completed tasks: {sum(completed_list)}\n")
  task_view.write(f"The total number of uncompleted tasks: {sum(incomplte_list)}\n")
  task_view.write(f"The total number of tasks that haven't been completed and that are overdue:  {len(overdue_list)}\n")
  task_view.write(f"The percentage of tasks that are incompleted: {round((sum(incomplte_list)/j * 100),2)}%\n")
  task_view.write(f"The percentage of the tasks that are overdue: {round((len(overdue_list2) / j * 100),2)}%\n")

 with open("user_overview.txt","w") as over_view: 
  user_list = []
  with open("user.txt", "r") as f2:
   task_generater = f2.readlines()
   for i2 in task_generater:
    user_1 = i2.replace("\n","")
    user_list.append(user_1)
   over_view.write(f"The total number of users registered: {len(user_list)}\n")
   over_view.write(f"The total number of tasks that have been generated and tracked: {len(task_list)}\n")
 
  over_view.write("INFO FOR EACH USER\n")
  with open("tasks.txt","r") as f3:
   taskper_user = f3.readlines()
   for i3 in taskper_user:
    view_task = i3.replace("\n","").split(",")
    object_date2 = parse(view_task[4])
    over_view.write(f"The total number of tasks assined to {view_task[0]} is {len([view_task[1]])}\n")
    over_view.write(f"The percentage of the total number of tasks have been assigned to {view_task[0]} is {len([view_task[1]])/len([view_task[1]]) * 100}%\n")
    if " No" in view_task and object_date2 < datetime.datetime.today():
     over_view.write(f"The percentage of the tasks assigned to {view_task[0]} that have not been completed and are overdue is {len([view_task[1]])/len([view_task[1]]) * 100}%\n")
    elif " No" in view_task:
     over_view.write(f"The percentage of tasks that have been completed by {view_task[0]} is {0}%\n")
     over_view.write(f"The percentage of tasks that must be completed by {view_task[0]} is {len([[1]]) / len([view_task[1]]) * 100}%\n")
    elif " Yes" in view_task:
     over_view.write(f"The percentage of tasks that have been completed by {view_task[0]} is {len([view_task[1]]) / len([view_task[1]]) * 100}%\n")
     over_view.write(f"The percentage of tasks that must be completed by {view_task[0]} is {0}%\n")
     over_view.write(f"The percentage of tasks that have not been completed and have been overdue by {view_task[0]} is {0}%\n")
     over_view.write(f"The percentage of the tasks assigned to {view_task[0]} that have not been completed and are overdue is {0}%\n")
     
# this funtion will display the stats_view 
def stats_view():
 "It opens the two files, reads the lines, and prints them"
 print(" The statictics about task_overview file \n")
 with open("task_overview.txt","r") as stats_1:
  stats_v1 = stats_1.readlines()
  for stats_fl1 in stats_v1:
   print(stats_fl1.replace("\n",""))
  
 print("\n The statictics about user_overview file \n")
 with open("user_overview.txt","r") as stats_2:
  stats_v2 = stats_2.readlines()
  for stats_fl2 in  stats_v2:
   print(stats_fl2.replace("\n",""))
  


with open("user.txt","r+") as f:
 y = f.readlines()
 var_2 = " ".join(y)
 var_3 = var_2.replace(",","")
 var_4 = var_3.split()

#created empty lists
x_list1 = []
x_list2 = []
for i in range(0,len(var_4)):
 if i % 2 == 0:
  x_list1.append(var_4[i])
 else:
  x_list2.append(var_4[i])
  
# created a dictionary
manage_task = dict(zip(x_list1,x_list2))


'''
The function above is a menu function that allows the user to select from a list of options.
'''
def menu_func():
   while True:
   # presenting the menu to the user and
   # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
          r - Registering a user
          a - Adding a task
          va - View all tasks
          vm - View my task
          gr - Generate reports
          ds - Display statistics
          e - Exit
          : ''').lower()
          
    if menu == "r" and username == "admin":
      reg_user()
      
      
    elif menu == "a":
      add_task() 
      
      
    elif menu == "va":
      view_all()
      
      
    elif menu == "vm":
      view_mine()
      
    
    elif menu == "gr":
     gen_rep()
     break
     
    elif menu == "ds":
     gen_rep()
     stats_view()
     break
    
    elif menu == "e":
     # the string will be displayed
     print('Goodbye!!!')
     break


# This is a while loop that is asking the user to enter their username and password. If the username
# and password is correct, it will call the menu_func() function.

while True:
 username = input("Enter your username: ")
 userpassword = input("Enter your password: ")
 if username in manage_task.keys() and userpassword == manage_task[username]:
  menu_func()
  break

   
 