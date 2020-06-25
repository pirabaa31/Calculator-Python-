d="People to bote for you in our Workplace that is the reason You are hired"
def total(math,english,science,history,art,gym,music,socialstudies):
    return math+english+science+history+art+gym+music+socialstudies
a="def add(): and a.count"
#print statement 
print("Welcome to Work Application")
print("_______________________________")
print("Personel Information")
#inputs (Personel Information)
firstname = input("First Name:")
middlename = input("Middle Name :")
lastname = input("Last Name:")
phonenumber = int(input("Phone Number:"))
dateofbirth = int(input("Date of Birth:"))
age = int(input("Age:"))
gender = input("Gender:")
position = input("Position:")
#if Statement (Personel Information)

if phonenumber != 4165551234 or 4165551212:
    print(phonenumber, "is Not A Valid Canadian Number!")
    

if phonenumber == 4165551234 or 4165551212:
    print(phonenumber, "is A Valid Canadian Number")
if phonenumber != 4165551234:
    print("please try again")
if age > 60 or age < 18:
    print("Sorry! But You are not age required for this job")
    
else:
    print(age,", allowed")

    question = input("show me how to put count all the letter a and for funcions show me how to start/define it p.s put and in between the two")
if question == a:
    print("Good job")
else:
    print("You did not do that correct")




print("__________________________")

#inputs (Grades) and fuction

print("School Grades")

math = int(input("Math:"))
english = int(input("English:"))
science = int(input("Science:"))
history = int(input("History:"))
art = int(input("Art:"))
gym = int(input("Health and Physical Education"))
music = int(input("Music:"))
socialstudies = int(input("Social Studies:"))
totall=total(math,english,science,history,art,gym,music,socialstudies)
if math > 70 and english > 70 and science > 70 and history > 70 and art > 70 and gym > 70 and music > 70 and socialstudies > 70 and totall > 560:
    print("Your Hired")
else:
    print("Sorry but due to you grades in school you can not be exepted for this job")
print("you got")
a=100
while a<=100:
        print(a)
        a=a+1
print("%s"%(d))
print("_____________________________")

#Done

signature=input("Signature:")
print("|___________________________________________|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~signed",signature,     "|")
print("|___________________________________________|")