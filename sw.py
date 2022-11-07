import random
import sys
import re

print("Welcome to BeeFit!!!")
userexist = input("Do you already have an account ? Enter Yes or No: ")


def firstentrance():
    global username, password, age, height,gender, weight, aim,  dailymovement
    global desiredweight
    if userexist == "No" or userexist == "no":
        print("Welcome to BeeFit new bee! Let's create you an account.")
        username = input("Please enter username to create your account:")

        while True:
            password = input("Please enter password to create your account. Remember that your password should have at least 8 characters and contain capital letters and symbols")
            if (len(password) < 8):
                print("Your password should be longer.")
                continue
            elif not re.search("[A-Z]", password):
                print("Your password should consist of at least one capital letter.")
                continue
            elif not re.search("[0-9]", password):
                print("Your password should consist of at least one number.")
                continue
            else:
                print("Password satisfied the requirements.")
                break

        print("Let's continue! Please give us information about you.")
        while True:
            gender = input("Enter gender. W / M : ")
            if gender == "M" or gender == "m" or gender =="W" or gender == "w":
                print("Wonderful! Few steps left. Hang on.")
                break
            else:
                print("Ops! Please write again.")
                continue

        while True:
            weight = int(input("Please enter your weight in kilograms and not decimals:"))
            if weight is float:
                print("Ops! No decimals please! Try again.")
                continue
            else:
                break

        while True:
            height = int(input("Please enter your height in cm and not decimals:"))
            if height is float:
                print("Ops! No decimals please! Try again.")
                continue
            else:
                break

        while True:
            age = int(input("Please enter your age:"))
            if age != int(age):
                print("Please enter a valid age.")
                continue
            elif age < 18:
                print("You are not old enough to use this program. You can only use this program with the supervision of a parent / family member. ")
                sys.exit(0)
            else:
                break

        while True:
            dailymovement = int(input("Please enter daily movement from 0 to 2: (if you would like more information about daily info please enter '-1'."))
            if dailymovement == -1:
                print("Hello there! Daily movement is an important piece of our lives to stay healthy!")
                print("If you have walked more than 10.000 steps or worked out/ran/heaviy physical activites, then you can enter 2.")
                print("If you have walked between 5.000 and 10.000 steps or slightly worked out/kinda run, then you can enter 1.")
                print("If you have walked less than 5.000 steps or didn't do any activites, then you can enter 0.")
                print("Hope this helped! ")
                continue
            else:
                break

        print("Okay, we are getting closer to the last question! What is your aim goal using BeeFit? Gain weight, lose weight or just eating healthy?")
        aim = int(input("Enter 1 for gain weight, 2 for lose weight and 3 for keep your shape."))

        while True:
            desiredweight = int(input("Please enter your desired weight:"))
            if weight is float:
                print("Ops! No decimals please! Try again.")
                continue
            else:
                break
        print("Great! Let's get started!")

        with open("yenikullaıcı.txt", "a") as file:
            file.write(f"{username} {password},{age},{weight},{height},{gender},{dailymovement},{desiredweight}\n")

    elif userexist == "Yes" or userexist == "yes":
        print("Welcome back old bee!")
    else:
        print("Invalid.")

firstentrance()

def bmicalc(weight, height):
    bmi = weight / (height * height)
    print("Would you like to know your BMI according to your weight and height?")
    print("Note that BMI calculations can help you to choose best aim. But of course, the diet plan would be created according to your wishes.")
    bmiuser = input("Please enter Yes / No")
    while True:
        if bmiuser == "Yes" or "yes":
            if bmi <= 18.5:
                print('Your BMI is:', bmi, 'You are underweight. You should consider to gain weight.')
                break
            elif 18.5 < bmi < 25:
                print('Your BMI is:', bmi, 'You are normal. You should consider to keep your shape.')
                break
            elif 25 < bmi < 30:
                print('Your BMI is:', bmi, 'You are overweight. You should consider to lose weight.')
                break
            elif bmi > 30:
                print('Your BMI is:', bmi, 'You are obese. You should consider to lose weight.')
                break

        elif bmiuser == "No" or "no":
            print("It's your choice!")
            break
        else:
            print("Invalid input. Please try again!")
            continue

def caloriecalcformen(weight,height,age):

        BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        RMR = BMR * 1.1
        AB = RMR * 0.1
        EB = 600
        calorie = RMR + AB + EB
        print("Calorie calculation for you is:",calorie)
        return calorie

def caloriecalcforwoman(weight, height, age):
        BMR = 665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        RMR = BMR * 1.1
        AB = RMR * 0.1
        EB = 600
        calorie = RMR + AB + EB
        print("Calorie calculation for you is:",calorie)
        return calorie


def makingthelist(pro_list, carb_list, fat_list, calorie):
    cntr = 0
    dietlist = []
    while cntr < calorie:
        if len(dietlist) < 4 :
            pro = random.choice(pro_list)
            if pro not in dietlist:
               pro_kalori = int(pro[1])
               cntr += pro_kalori
               dietlist.append(pro)
            if cntr >= calorie:
                break
            carb = random.choice(carb_list)
            if carb not in dietlist:
                karbo_kalori = int(carb[1])
                cntr += karbo_kalori
                dietlist.append(carb)
            if cntr >= calorie:
                break
            fat = random.choice(fat_list)
            if fat not in dietlist:
                yag_kalori = int(fat[1])
                cntr += yag_kalori
                dietlist.append(fat)
            if cntr >= calorie:
                break
        return dietlist


def dietlist(calorie):
    calorie = calorie / 3
    breakfastcarblist=[]
    breakfastprolist=[]
    breakfastfatlist=[]
    with open("Kahvaltı.txt","r") as file:
        for i in file:
            i=i.split(",")
            if i[-1].strip()=="karbonhidrat":
                  breakfastcarblist.append(i)
            elif i[-1].strip()=="protein":
                 breakfastprolist.append(i)
            else:
                 breakfastfatlist.append(i)
    print("Breakfast list is: ")
    breakfastlist= makingthelist(breakfastprolist, breakfastcarblist, breakfastfatlist, calorie)


    for i in breakfastlist:
        print(i[0])
    dinnercarblist = []
    dinnertprolist = []
    dinnerfatlist = []

    with open("Öğle-Akşam.txt", "r") as file:
        for i in file:
            i = i.split(",")
            if i[-1].strip() == "karbonhidrat":
                  dinnercarblist.append(i)
            elif i[-1].strip() == "protein":
                dinnertprolist.append(i)
            else:
                 dinnerfatlist.append(i)

    print("\nLunch list is: ")
    lunchlist = makingthelist(dinnertprolist, dinnercarblist, dinnerfatlist, calorie)
    for i in lunchlist:
        print(i[0])

    print("\nDinner list is: ")
    dinnerlist = makingthelist(dinnertprolist, dinnercarblist, dinnerfatlist, calorie)
    for i in dinnerlist:
        print(i[0])

with open("yenikullaıcı.txt","r") as file:
    list1=[]
    for i in file:
        i=i.split(",")[0]
        list1.append(i)


if userexist =="Yes" or "yes":
    print("Please confirm you are a user.")
    # password or username check
    while True:
        usernamecheck = input("Enter username please:")
        passwordcheck = input("Enter password please:")

        if (usernamecheck + " " + passwordcheck) not in list1:
            print("Your password or username is incorrect. Please try again.")
            continue
        else:
            print("Logging in your account ...")
            break

    print("We hope you had a great day. So, what was your daily movement was like?")

    dailymovement = int(input("Please enter daily movement from 0 to 2: "))

    while True:
        newweight = int(input("What is your weight today? Please enter without decimals: "))
        if newweight is float:
            print("Ops! No decimals please! Try again.")
            break
        else:
            break

    with open("yenikullaıcı.txt") as file:
        for i in file:
            desiredweight = i[6]
        if newweight == desiredweight:
            print("You have reached your dream weight !!!!!!!!")
            print("We are so proud of you!")
            print("Sadly, this program has reached it's purpose and now will be exiting...")
            print("If you would like to use this program again you can always restart it! Take care.")
            sys.exit(0)

        else:
            i=i.split(",")
            name=i[0]
            age=int(i[1])
            weight=int(i[2])
            height=int(i[3])
            gender=i[4]
            dailymovement=int(i[5].strip())

            if gender == "m" or "M":
                calorie = caloriecalcformen(weight, height, age)
                if dailymovement == 0:
                    calorie = calorie - 500
                    dietlist(calorie)
                elif dailymovement == 1:
                    calorie = calorie - 250
                    dietlist(calorie)
                elif dailymovement == 2:
                    calorie = calorie - 100
                    dietlist(calorie)
            elif gender == "w" or "W":
                calorie = caloriecalcforwoman(weight, height, age)
                if dailymovement == 0:
                    calorie = calorie - 500
                    dietlist(calorie)
                elif dailymovement == 1:
                    calorie = calorie - 250
                    dietlist(calorie)
                elif dailymovement == 2:
                    calorie = calorie - 100
                    dietlist(calorie)
else:
    firstentrance()


def esmatris(list):
    for i in list:
        if len(list)==len(i):