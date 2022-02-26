print('Введите ваш логин:')
log=input();
print('Введите пароль:')
pas=input();

def call(a,b):
    import mysql.connector
    mydb = mysql.connector.connect(host='127.0.0.1', database='new', user='root', password='')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM user')
    l = mycursor.fetchall()
    k = 0
    for l1 in l:
        if l1[1] == a and l1[2] == b:
            k += 1
    # print(k)
    if k != 0:
        print('Добро пожаловать')
    else:
        print('Ваш пароль или логин неверен ')
call(log,pas)


