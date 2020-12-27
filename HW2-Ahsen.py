First_Name=input("Please,enter your first name:")
Last_Name=input("Please,enter your last name:")
Age=int(input("Please,enter your age:"))
Date_of_Birth=input("Please,enter your date of birth:")
Information_list=[First_Name,Last_Name,Age,Date_of_Birth]
for i in Information_list:
    print(i)
if Age<18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to street.")