import mysql
import mysql.connector as ms
from random import randint
import math
from math import *



connection = ms.connect(host='localhost',user='<username>',passwd='<password>',database='accounts')
if connection.is_connected():
    print("READY TO GO!!!")
Login_status = 'N'

    
mycursor = connection.cursor(buffered=True)

list_real = []
list1_real = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []

def pokechoose():
    list = []
    count = 1
    query = 'SELECT NAME, TYPE FROM poke ORDER BY RAND() LIMIT 1 ;'
    if count == 1:
        mycursor.execute(query)
        user = mycursor.fetchmany()
        pokemon = user[0]
        listel = pokemon[0]
        list.append(listel)
        count = count + 1
    list_real.extend(list)
    query1 = "INSERT INTO pokenew VALUES(%s,%s)"
    credentials1 = (pokemon[0],1)
    mycursor.execute(query1,credentials1)  
    
def pokechoose1():
    listq = []
    count = 1
    query = 'SELECT NAME, TYPE FROM poke ORDER BY RAND() LIMIT 1 ;'
    if count == 1:
        mycursor.execute(query)
        user = mycursor.fetchmany()
        pokemon = user[0]
        listel = pokemon[0]
        listq.append(listel)

        count = count + 1
    list1_real.extend(listq)
    query1 = "INSERT INTO pokenew VALUES(%s,%s)"
    credentials1 = (pokemon[0],2)
    mycursor.execute(query1,credentials1)

def selection():
    pokechoose()
    pokechoose1()
    query = "SELECT NAME FROM pokenew WHERE TYPE = 1"
    mycursor.execute(query)
    namea = mycursor.fetchone()
    namea = namea[0]
    query2 = "SELECT NAME FROM pokenew WHERE TYPE = 2"
    mycursor.execute(query2)
    nameb = mycursor.fetchone()
    nameb = nameb[0]
    print("")
    print("You choose",namea,".")
    var = namea
    list2.append(var)
    print("")
    print("BOT sent out",nameb,".")
    var2 = nameb
    list3.append(var2)
    print("")
    print(namea,"moves are - ")
    moves()
    print("")
    print(nameb,"moves are - ")
    moves2()
    print()
    selection_move_a()

def moves():
    query = "SELECT NAME FROM pokenew WHERE TYPE = 1"
    mycursor.execute(query)
    namec = mycursor.fetchone()
    namec = namec[0]
    query2 = "SELECT NAME FROM pokenew WHERE TYPE = 2"
    mycursor.execute(query2)
    nameb = mycursor.fetchone()
    nameb = nameb[0]
    query = "SELECT TYPE FROM poke WHERE NAME = %s" 
    credentials = (namec,)
    mycursor.execute(query,credentials)
    type = mycursor.fetchone()
    type_var = type[0]
    type_var2 = type_var.split(',')
    try:
        count = 0
        index = 1
        query2 = "SELECT NAME FROM moves WHERE TYPE = %s OR TYPE = %s"
        credentials2 = (type_var2[0],type_var2[1])
        mycursor.execute(query2,credentials2)
        poke_moves = mycursor.fetchall()
        poke_move_result = [lis[0] for lis in poke_moves]
        noi = len(poke_move_result)
        noi = noi - 1
        while count < 4:
            noi_var = randint(0,noi)
            print(index,')',poke_move_result[noi_var])
            list4.append(poke_move_result[noi_var])
            index = index + 1
            count = count + 1
    except IndexError:
        count = 0
        index = 1
        query2 = "SELECT NAME FROM moves WHERE TYPE = %s "
        credentials2 = (type_var2[0],)
        mycursor.execute(query2,credentials2)
        poke_moves = mycursor.fetchall()
        poke_move_result = [lis[0] for lis in poke_moves]
        noi = len(poke_move_result)
        noi = noi - 1
        while count < 4:
            noi_var = randint(0,noi)
            print(index,')',poke_move_result[noi_var])
            list4.append(poke_move_result[noi_var])
            index = index + 1
            count = count + 1
        
def moves2():
    query = "SELECT NAME FROM pokenew WHERE TYPE = 1"
    mycursor.execute(query)
    namea = mycursor.fetchone()
    namea = namea[0]
    query2 = "SELECT NAME FROM pokenew WHERE TYPE = 2"
    mycursor.execute(query2)
    nameb = mycursor.fetchone()
    nameb = nameb[0]
    query = "SELECT TYPE FROM poke WHERE NAME = %s" 
    credentials = (nameb,)
    mycursor.execute(query,credentials)
    type = mycursor.fetchone()
    type_var = type[0]
    type_var2 = type_var.split(',')
    try:
        count = 0
        index = 1
        query2 = "SELECT NAME FROM moves WHERE TYPE = %s OR TYPE = %s"
        credentials2 = (type_var2[0],type_var2[1])
        mycursor.execute(query2,credentials2)
        poke_moves = mycursor.fetchall()
        poke_move_result = [lis[0] for lis in poke_moves]
        noi = len(poke_move_result)
        noi = noi - 1
        while count < 4:
            noi_var = randint(0,noi)
            a = poke_move_result[noi_var]
            print(index,')',a)
            list5.append(a)
            index = index + 1
            count = count + 1
    except IndexError:
        count = 0
        index = 1
        query2 = "SELECT NAME FROM moves WHERE TYPE = %s "
        credentials2 = (type_var2[0],)
        mycursor.execute(query2,credentials2)
        poke_moves = mycursor.fetchall()
        poke_move_result = [lis[0] for lis in poke_moves]
        noi = len(poke_move_result)
        noi = noi - 1
        while count < 4:
            noi_var = randint(0,noi)
            a = poke_move_result[noi_var]
            print(index,')',a)
            list5.append(a)
            index = index + 1
            count = count + 1

def selection_move_a():
    query = "SELECT NAME FROM pokenew WHERE TYPE = 1"
    mycursor.execute(query)
    namea = mycursor.fetchone()
    namea = namea[0]
    query2 = "SELECT NAME FROM pokenew WHERE TYPE = 2"
    mycursor.execute(query2)
    nameb = mycursor.fetchone()
    nameb = nameb[0]
    move = int(input("Which move you want to choose(1-4) - "))
    move = move - 1
    print("")
    print(namea,"Used",list4[move],"on",nameb,".")
    query = "SELECT TYPE FROM moves WHERE NAME = %s"
    credentials = (list4[move],)
    mycursor.execute(query,credentials)
    type = mycursor.fetchone()
    type_a = type[0]
    list6.append(type_a)
    print("")
    move1 = randint(0,3)
    print(nameb,"Used",list5[move1],"on",namea,".")
    query1 = "SELECT TYPE FROM moves WHERE NAME = %s"
    credentials1 = (list5[move1],)
    mycursor.execute(query1,credentials1)
    type1 = mycursor.fetchone()
    type_a1 = type1[0]
    list7.append(type_a1)
    new_moveset()

def new_moveset():
    query = "SELECT NAME FROM pokenew WHERE TYPE = 1"
    mycursor.execute(query)
    namea = mycursor.fetchone()
    namea = namea[0]
    query2 = "SELECT NAME FROM pokenew WHERE TYPE = 2"
    mycursor.execute(query2)
    nameb = mycursor.fetchone()
    nameb = nameb[0]
    query = "SELECT HP FROM poke WHERE NAME = %s"
    credentials = (nameb,)
    mycursor.execute(query,credentials)
    health_a = mycursor.fetchone()
    health = health_a[0]
    query6 = "INSERT INTO battle(NAME,HP) VALUES(%s,%s)"
    credentials6 = (nameb,health)
    mycursor.execute(query6,credentials6)
    query7 = "SELECT HP FROM battle WHERE NAME = %s"
    credentials7 = (nameb,)
    mycursor.execute(query7,credentials7)
    player_healtha = mycursor.fetchone()
    player_health1 = player_healtha[0]
    level_a = 80
    query2 = "SELECT ATTK,DEF FROM poke WHERE NAME = %s;"
    credentials2 = (namea,)
    mycursor.execute(query2,credentials2)
    attack_b = mycursor.fetchone()
    b = attack_b[0]
    query3 ="SELECT POWER FROM moves WHERE NAME = %s"
    credentials3 = (list4[0],)
    mycursor.execute(query3,credentials3)
    power_c = mycursor.fetchone()
    c = power_c[0]
    d = attack_b[1]
    e = randint(217,255)
    x = 1
    final_damage = ((((((((2*level_a/5+2)*b*c)/d)/50)+2)*x)*4/10)*e)/255
    remaining_health1 = player_health1 - final_damage
    remaining_health1 = round(remaining_health1)
    if remaining_health1 < 0 :
        remaining_health1 = 0
    elif remaining_health1 > 0:
        pass
    query8 = "UPDATE battle SET HP = %s WHERE NAME = %s"
    credentials8 = (remaining_health1,nameb)
    mycursor.execute(query8,credentials8)
    query13 = "SELECT HP FROM battle WHERE NAME = %s"
    credentials13 = (nameb,)
    mycursor.execute(query13,credentials13)
    new_healtha = mycursor.fetchone()
    new_healtha = new_healtha[0]
    if new_healtha == 0 :
        quer = "DELETE FROM battle WHERE NAME = %s"
        cred = (nameb,)
        mycursor.execute(quer,cred)
    else:
        pass
    print("")
    print(nameb,"is down to",new_healtha)
    query1 = "SELECT HP FROM poke WHERE NAME = %s"
    credentials1 = (namea,)
    mycursor.execute(query1,credentials1)
    health_b = mycursor.fetchone()
    health_real = health_b[0]
    query9 = "INSERT INTO battle(NAME,HP) VALUES(%s,%s)"
    credentials9 = (namea,health_real)
    mycursor.execute(query9,credentials9)
    query10 = "SELECT HP FROM battle WHERE NAME = %s"
    credentials10 = (namea,)
    mycursor.execute(query10,credentials10)
    player_healthb = mycursor.fetchone()
    player_healthc = player_healthb[0]
    level_a1 = 80
    query4 = "SELECT ATTK,DEF FROM poke WHERE NAME = %s;"
    credentials4 = (nameb,)
    mycursor.execute(query4,credentials4)
    attack_b1 = mycursor.fetchone()
    b1 = attack_b1[0]
    query5 ="SELECT POWER FROM moves WHERE NAME = %s"
    credentials5 = (list5[0],)
    mycursor.execute(query5,credentials5)
    power_c1 = mycursor.fetchone()
    c1 = power_c1[0]
    d1 = attack_b1[1]
    e1 = randint(217,255)
    x1 = 1
    final_damage1 = ((((((((2*level_a1/5+2)*b1*c1)/d1)/50)+2)*x1)*4/10)*e1)/255
    remaining_health_b = player_healthc - final_damage1
    remaining_health_b = round(remaining_health_b)
    if remaining_health_b < 0 :
        remaining_health_b = 0
    elif remaining_health_b > 0:
        pass
    query11 = "UPDATE battle SET HP = %s WHERE NAME = %s"
    credentials11 = (remaining_health_b,namea)
    mycursor.execute(query11,credentials11)
    query12 = "SELECT HP FROM battle WHERE NAME = %s"
    credentials12 = (namea,)
    mycursor.execute(query12,credentials12)
    new_healthe = mycursor.fetchone()
    new_healthe = new_healthe[0]
    if new_healthe == 0 :
        quer1 = "DELETE FROM battle WHERE NAME = %s"
        cred1 = (namea,)
        mycursor.execute(quer1,cred1)
    else:
        pass
    print("")
    print(namea,"is down to",new_healthe)
    print("")
    if new_healtha == 0:
        print(namea,"won!!!!!")
    elif new_healthe == 0:
        print(nameb,"won!!!!!")
    elif new_healtha == 0 and new_healthe == 0:
        print("This Match Resulted in a Tie.")
    else:
        selection_move_a()
    return new_healtha,new_healthe

def instruct():
    print("                  INSTRUCTIONS")
    print("1) Choose between what is asked always.")
    print("2) After finishing one game if u want to change pokemon rather than using same one , restart the game.")
    print("3) This game offers wide variety of pokemons to play with.")
    print("4) Every Pokemon is of level 80.")
    print("HOPE YOU ENJOY :D")

def random_mode(login_username,login_password):
    bot_username = 'COMPUTER' 
    age = 100
    query = 'SELECT USERNAME FROM login WHERE USERNAME = %s AND PASSWORDA = %s ; '
    credentials = (login_username,login_password)
    mycursor.execute(query,credentials)
    username1 = mycursor.fetchone()
    query1 = 'SELECT USERNAME FROM login WHERE GENDER = %s AND AGE = %s ;'
    credentials1 = (bot_username,age)
    mycursor.execute(query1,credentials1)
    username2 = mycursor.fetchone()
    print("WELCOME TO RANDOM MODE TYPE - 1 Vs 1 ")
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
    while instructions > 2:
        print("Choose between 1 and 2 only.")
        print("TYPE 1 FOR THE INSTRUCTIONS , IF YOU ALREADY KNOW THEM .... TYPE 2 ")
        instructions = int(input(""))
    print("Your Opponent will be",username2[0])
    print("CHOOSING POKEMON....")
    print("")
    selection()
    
def account_creation():
    global Login_status
    user_username = input("Enter your username - ")
    user_password = input("Enter your password - ")
    useri = ""
    if user_password != useri:
        pass
    else:
        print("PASSWORD HAS TO BE ENTERED.")
        user_password = input("Enter your password - ")
    gender = input("Enter your gender - ")
    if gender == 'male' or gender == 'MALE' or gender == 'female' or gender == 'FEMALE' or gender == 'none' or gender =='NONE':
        pass
    else:
        print("Gender should be either  in all caps or in all lower and it should be only between male,female or None.")
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
        print("")
        answer = input("Do you want to continue(y/n) - ")
        while answer == 'y' or answer == 'Y':
            selection()
            random_mode(user_username,user_password)
            print("")
            answer = input("Do you want to continue(y/n) - ")
        else:
            pass
    
def user_login():
    global Login_status
    login_username = input("Enter your username - ")
    login_password = input("Enter your password - ")
    logini = ""
    if login_password != logini:
        pass
    else:
        print("Enter Password to login.")
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
        print("")
        answer = input("Do you want to continue(y/n) - ")
        while answer == 'y' or answer == 'Y':
            random_mode(login_username,login_password)
            print("")
            answer = input("Do you want to continue(y/n) - ")
        else:
            pass

def First_Starting():
    print("                    THE POKEMON GAME")
    print("                    By <Name>")
    print("                         <Class>")
    print("                     Roll no - <roll_no>")
    print("")
    print("")
    print("")
    print("")
    print("")
    start = int(input("Enter 1 to start the game - "))
    while start == 2:
        break
    if start == 1:
        choice = int(input("If u already have an account enter 1 else enter 2 - "))
        if choice == 1:
            user_login()
        elif choice == 2:
            account_creation()
        else:
            print("Choose between 1 and 2")
    elif start >= 2:
        pass
    else:
        print("INVALID INPUT")

First_Starting()
