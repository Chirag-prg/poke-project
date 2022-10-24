import mysql
import mysql.connector as ms



connection = ms.connect(host='localhost',user='<username>',passwd='<password>',database='<database_name>')
if connection.is_connected():
    print("READY TO GO!!!")


mycursor = connection.cursor()


def adding_values():
    ans = 'y'
    while ans == 'y':
       name = str(input("Input pokemon name name - "))
       type = input("Input type - ")
       type2 = input("Input type2 - ")
       hp = input("Input hp - ")
       attk = input("Input attk - ")
       defe = input("Input def - ")
       spa = input("Input spa - ")
       spd = input("Input spd - ")
       spe = input("Input speed - ")

       try:
            query = "INSERT INTO poke(NAME,TYPE,HP,ATTK,DEF,SPA,SPD,SPE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            credentials = [(name,type,hp,attk,defe,spa,spd,spe)]
            mycursor.executemany(query,credentials)
            connection.commit()
            print("Pokemon Successfully Registered.")
       except mysql.connector.errors.IntegrityError:
            print("This Username Already Exists.")
       ans = input("y/n - ")
adding_values()
