import random  # lets us create random numbers and letters


print("Welcome to the EC2 Instance Name Generator!\n")



department = input("Enter your department name: ")



number = input("How many EC2 instance names would you like to create? ")



if not number.isdigit():
    print("Oops! Please enter a number next time.")
else:
    number = int(number)


    print("\nHere are your EC2 instance names:\n")

  
    names = []

    
    for i in range(number):


        letters = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + \
                  random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + \
                  random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

      
        numbers = random.choice("0123456789") + \
                  random.choice("0123456789") + \
                  random.choice("0123456789")


        name = department.upper() + "-EC2-" + letters + numbers

      
        while name in names:
            letters = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + \
                      random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + \
                      random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            numbers = random.choice("0123456789") + \
                      random.choice("0123456789") + \
                      random.choice("0123456789")
            name = department.upper() + "-EC2-" + letters + numbers

      
        names.append(name)

        
        print(f"{i + 1}. {name}")

    print("\nDone! All EC2 instance names were created.")
