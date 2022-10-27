import mysql
import mysql.connector as ms




connection = ms.connect(host='localhost',user='<username>',passwd='<password>',database='database_name')
if connection.is_connected():
    print("READY TO GO!!!")
Login_status = 'N'

    
mycursor = connection.cursor()

def pokechoose():
    query = 'SELECT NAME FROM poke ORDER BY RAND() LIMIT 1 ;'
    mycursor.execute(query)
    user = mycursor.fetchmany()
    pokemon = user[0]
    print(pokemon[0])
    
        
def pokemon_choosing_1():
    total = 4
    while total > 0:
        pokechoose() 
        total = total - 1

def pokemon_choosing_2():
    total = 4
    while total > 0:
        pokechoose() 
        total = total - 1

def instruct():
    print("COMING SOON!!")

def random_mode(login_username,login_password):
    query = 'SELECT USERNAME FROM login WHERE USERNAME = %s AND PASSWORDA = %s ; '
    credentials = (login_username,login_password)
    mycursor.execute(query,credentials)
    username1 = mycursor.fetchone()
    print("WELCOME TO RANDOM MODE")
    print("TYPE 1 FOR THE INSTRUCTIONS , IF YOU ALREADY KNOW THEM .... TYPE 2 ")
    instructions = int(input(""))
    if instructions == 1:
        instruct()
        print("")
        print("")
        print("HOPE THEY ARE CLEAR TO YOU.")
        print("LETS START THE GAME NOW.")
    elif instructions == 2:
        print("VERY WELL , LETS START THE GAME NOW.")
    print(username1[0])

def account_creation():
    global Login_status
    user_username = input("Enter your username - ")
    user_password = input("Enter your password - ")
    gender = input("Enter your gender - ")
    age = int(input("ENTER YOUR AGE - "))
    try:
        query = "INSERT INTO login(USERNAME,PASSWORDA,GENDER,AGE) VALUES(%s,%s,%s,%s)"
        credentials = [(user_username,user_password,gender,age)]
        mycursor.executemany(query,credentials)
        connection.commit()
        print("Account Successfully Registered.")
        Login_status = 'Y'
    except mysql.connector.errors.IntegrityError:
        print("This Username Already Exists.")
    if Login_status == 'Y':
        query1 = "SELECT AGE,USERNAME,GENDER FROM login WHERE USERNAME = %s AND PASSWORDA = %s"
        credentials1 = (user_username,user_password)
        mycursor.execute(query1,credentials1)
        user1 = mycursor.fetchone()
        print("USERNAME-",user1[1])
        print("AGE-",user1[0])
        print("GENDER-",user1[2])
        print("WELCOME USER")
        random_mode(user_username,user_password)
    
    
    
def user_login():
    global Login_status
    login_username = input("Enter your username - ")
    login_password = input("Enter your password - ")
    query = "SELECT * FROM login WHERE USERNAME = %s AND PASSWORDA = %s"
    credentials = (login_username,login_password)
    mycursor.execute(query,credentials)
    user = mycursor.fetchone()
    if user is not None:
        print("Login Successfull")
        Login_status = 'Y'
    else:
        print("Wrong Username Or Password")
        print("TRY AGAIN!!")
    if Login_status == 'Y':
        query1 = "SELECT AGE,USERNAME,GENDER FROM login WHERE USERNAME = %s AND PASSWORDA = %s"
        credentials1 = (login_username,login_password)
        mycursor.execute(query1,credentials1)
        user1 = mycursor.fetchone()
        print("USERNAME-",user1[1])
        print("AGE-",user1[0])
        print("GENDER-",user1[2])
        print("WELCOME USER")
        random_mode(login_username,login_password)
def First_Starting():
    print("                    THE POKEMON GAME")
    print("                    By <Name>")
    print("                         <Class>")
    print("                       <Roll no >")
    print("")
    print("")
    print("")
    print("")
    print("")
    start = int(input("Enter 1 to start the game - "))
    if start == 1:
        choice = int(input("If u already have an account enter 1 else enter 2 - "))
        if choice == 1:
            user_login()
        elif choice == 2:
            account_creation()
        else:
            print("Choose between 1 and 2")
    else:
        print("INVALID INPUT")


First_Starting()
        
        
        
