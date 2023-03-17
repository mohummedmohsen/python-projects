import datetime

user_input = input("enter your goal with a deadline seperate by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_data = datetime.datetime.strptime(deadline, "%d-%m-%Y ")
todat_date = datetime.datetime.today()
time_till = deadline_data - todat_date

print(f"dear user! time remaining for your goal: {goal} is {time_till}")