# Database Table

#admin
#(admin_id, admin_username, admin_password)

#cab_dealers
#(cab_dealerid, cab_dealername, cab_dealerpassword, cab_dealeremail, cab_dealerphone)

#cabs
#(cab_id,cab_number,cab_name,cab_type(4 seater,7 seater),cab_model,cab_delarid(for relation cab_dealer table),cab_status)

#users
#(user_id,user_name,user_password,user_email,user_phone)
global dealerid
global userid
global adminid
import sqlite3 as sq
conn = sq.connect('cabsbooking-main.db')
c = conn.cursor()

# *****************************************Query For Creating Tables*****************************************************
# try:
#     conn.execute('''CREATE TABLE admin
#             (admin_id INTEGER PRIMARY KEY,
#             admin_username varchar(20) NOT NULL,
#             admin_password varchar(20) NOT NULL)''')
#
#     conn.execute('''CREATE TABLE cab_dealers
#                 (cab_dealerid INTEGER PRIMARY KEY,
#                 cab_dealername varchar(20) NOT NULL,
#                 cab_dealerpassword varchar(20) NOT NULL,
#                 cab_dealeremail varchar(20) NOT NULL,
#                 cab_dealerphone varchar(20) NOT NULL)''')
#
#     conn.execute('''CREATE TABLE cabs
#                 (cab_id INTEGER PRIMARY KEY,
#                 cab_name varchar(20) NOT NULL,
#                 cab_type varchar(20) NOT NULL,
#                 cab_model varchar(20) NOT NULL,
#                 cab_dealerid INT(11) NOT NULL,
#                 cab_from varchar(20) NOT NULL,
#                 cab_to varchar(20) NOT NULL)''')
#
#     conn.execute('''CREATE TABLE users
#                 (user_id INTEGER PRIMARY KEY,
#                 user_name varchar(20) NOT NULL,
#                 user_password varchar(20) NOT NULL,
#                 user_email varchar(20) NOT NULL,
#                 user_phone int(15) NOT NULL)''')
#
#     print('Table Created Succesfully')
#
# except:
#     print('Error while creating table.')
#
#
# conn.execute("Alter table cabs add cab_number varchar(20)")
# print('Added')

def dealer_reg():
    cab_dealername = input('Enter Name : ').strip().upper()
    cab_dealerpassword = input('Enter Password : ')
    cab_dealeremail = input('Enter Email : ')
    cab_dealerphone = input('Enter PhoneNumber : ')
    ins = "INSERT into cab_dealers(cab_dealername,cab_dealerpassword,cab_dealeremail,cab_dealerphone) values ('"+cab_dealername+"','"+cab_dealerpassword+"','"+cab_dealeremail+"','"+cab_dealerphone+"')"
    c.execute(ins)
    conn.commit()
    print('Dealer Register')
    print('-------------------------')
    init()

def dealerlogin():
    global dealerid
    cab_dealeremail = input('Enter Email : ')
    cab_dealerpassword = input('Enter Password : ')
    data = c.execute("SELECT * from cab_dealers where cab_dealeremail = '"+cab_dealeremail+"' and cab_dealerpassword = '"+cab_dealerpassword+"' ")
    d = data.fetchall()
    for a in d:
        dealerid = a[0]
    t = len(d)
    if t == 1:
        print('Login Successfully')
        initdealer()
    else:
        print('Invalid email or password')
        a = int(input('1.Try Again \n2.Main Menu : '))
        if a == 1:
            dealerlogin()
        elif a == 2:
            init()
        else:
            print('Choose either 1 or 2')

def initdealer():
    global dealerid
    b = int(input('''
                    1.Add Cabs
                    2.View Cabs
                    3.Delete Cabs
                    4.Update Cabs
                    5.Logout : '''))
    if b == 1:
        addcab()
    elif b == 2:
        viewcab()
    elif b == 3:
        delcab()
    elif b == 4:
        updatecab()
    elif b == 5:
        del dealerid
        init()

def addcab():
    global dealerid
    cab_name = input('Enter Cab Name: ')
    cab_type = input('Enter Cab Type: ')
    cab_model = input('Enter Cab Model: ')
    cab_dealerid = dealerid
    cab_from = input('Enter Location where cab travel: ')
    cab_to = input('Enter Final Destination of cab: ')
    cab_number = input('Enter Cab Number: ')
    ins = "insert into cabs(cab_name,cab_type,cab_model,cab_dealerid,cab_from,cab_to,cab_number) values ('"+cab_name+"','"+cab_type+"','"+cab_model+"','"+str(cab_dealerid)+"','"+cab_from+"','"+cab_to+"','"+cab_number+"') "
    c.execute(ins)
    conn.commit()
    print('Cab Inserted Successfully')
    initdealer()

def viewcab():
    global dealerid
    data = "SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealername,c.cab_from,c.cab_to,c.cab_number from cabs as c INNER JOIN cab_dealers as d on c.cab_dealerid = d.cab_dealerid where c.cab_dealerid='"+str(dealerid)+"'"
    cab_data=c.execute(data)
    cab_finaldata = cab_data.fetchall()
    print("{0:15}{1:15}{2:15}{3:15}{4:20}{5:15}{6:15}{7:15}".format("cab_id","Cab Name","Cab Type","Cab Model","Cab Dealer Name","Cab From","Cab To","Cab Number"))
    for d in cab_finaldata:
        print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<20}{5:<15}{6:<15}{7:<15}".format(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]))
    initdealer()

def delcab():
    global dealerid
    cabid = input('Enter cab ID to delete cab record : ')
    del1 = "Delete from cabs where cab_id='"+cabid+"' and cab_dealerid='"+str(dealerid)+"'"
    c.execute(del1)
    conn.commit()
    print('Delete Successfully')
    viewcab()

def updatecab():
    global dealerid
    cab_id = int(input("Enter Cab Id you Want to Update : "))
    cab_name = input('Enter Cab Name: ')
    cab_type = input('Enter Cab Type: ')
    cab_model = input('Enter Cab Model: ')
    cab_from = input('Enter Location where cab travel: ')
    cab_to = input('Enter Final Destination of cab: ')
    cab_number = input('Enter Cab Number: ')
    upd = "update cabs set cab_name='"+cab_name+"',cab_type='"+cab_type+"',cab_model='"+cab_model+"',cab_from='"+cab_from+"',cab_to='"+cab_to+"',cab_number='"+cab_number+"' where cab_id='"+str(cab_id)+"'"
    c.execute(upd)
    conn.commit()
    print('Succesfully Updated')
    initdealer()

def user_reg():
    user_name = input('Enter Name : ').strip().upper()
    user_password = input('Enter Password : ')
    user_email = input('Enter Email : ')
    user_phone = input('Enter PhoneNumber : ')
    data = c.execute("select * from users where user_email = '"+user_email+"'")
    l = len(data.fetchall())
    if l == 0:
        ins = "INSERT into users(user_name,user_password,user_email,user_phone) values ('" + user_name + "','" + user_password + "','" + user_email + "','" + user_phone + "')"
        c.execute(ins)
        conn.commit()
        print('User Register')
        print('----------------------')
        init()
    else:
        print('User Email Already Exists.')
        user_reg()

def userlogin():
    global userid
    user_email = input('Enter Email : ')
    user_password = input('Enter Password : ')
    data = c.execute(
        "SELECT * from users where user_email = '" + user_email + "' and user_password = '" + user_password + "' ")
    d = data.fetchall()
    for a in d:
        userid = a[0]
    t = len(d)
    if t == 1:
        print('Login Successfully')
        inituser()
    else:
        print('Invalid email or password')
        a = int(input('1.Try Again \n2.Main Menu : '))
        if a == 1:
            userlogin()
        elif a == 2:
            init()
        else:
            print('Choose either 1 or 2')

def inituser():
    global userid
    i = int(input('''
                1.View All Cabs
                2.Search Cabs
                3.Update Profile
                4.Change Password
                5.Logout : '''))
    if i == 1:
        viewcabs_user()
    elif i == 2:
        cab_from = input("Enter Cab From : ")
        cab_to = input("Enter Cab to : ")
        viewcabs_user(cab_from,cab_to)
    elif i == 3:
        userupdate()
    elif i == 4:
        change_password()
    elif i == 5:
        del userid
        init()
    else:
        print('Please Input Correct value.')

def viewcabs_user(cab_from='',cab_to=''):
    if cab_from!='' and cab_to!='':
        data = "SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealername,d.cab_dealerphone,c.cab_from,c.cab_to,c.cab_number from cabs as c INNER JOIN cab_dealers as d on c.cab_dealerid = d.cab_dealerid where cab_from='"+cab_from+"' and cab_to='"+cab_to+"'"
    else:
        data = "SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealername,d.cab_dealerphone,c.cab_from,c.cab_to,c.cab_number from cabs as c INNER JOIN cab_dealers as d on c.cab_dealerid = d.cab_dealerid"

    cab_data = c.execute(data)
    cab_finaldata = cab_data.fetchall()
    print("{0:15}{1:15}{2:15}{3:15}{4:20}{5:20}{6:15}{7:15}{8:15}".format("cab_id", "Cab Name", "Cab Type", "Cab Model",
                                                                    "Cab Dealer Name","Cab Contact Number", "Cab From", "Cab To",
                                                                    "Cab Number"))
    for d in cab_finaldata:
        print("{0:<15}{1:<15}{2:<15}{3:<15}{4:<20}{5:<20}{6:<15}{7:<15}{8:15}".format(d[0], d[1], d[2], d[3], d[4], d[5], d[6],d[7],d[8]))
    inituser()

def userupdate():
    global userid
    user_email = input("Enter Email to Update : ")
    user_phone = input("Enter Phone no to Update : ")
    upd = "update users set user_email='"+user_email+"',user_phone='"+user_phone+"' where user_id='"+str(userid)+"' "
    c.execute(upd)
    conn.commit()
    print('Updated Successfully')
    inituser()

def change_password():
    global userid
    old_password = input("Enter Old Password : ")
    data=c.execute("SELECT * from users where user_password='"+str(old_password)+"' and user_id='"+str(userid)+"'")
    d = data.fetchall()
    t=len(d)
    if t == 1:
        newpass = input('Enter New Password : ')
        cpass = input('Enter Confirm Password : ')
        if(newpass == cpass):
            upd = "update users set user_password='"+newpass+"' where user_id='"+str(userid)+"'"
            c.execute(upd)
            conn.commit()
            print('Password Changed')
            inituser()
        else:
            print("Password not matching")
            inituser()
    else:
        print('Invalid Old Password')
        inituser()

def admin():
    global adminid
    admin_username = input('Enter Username : ')
    admin_password = input('Enter Password : ')
    data = c.execute(
        "SELECT * from admin where admin_username = '" + admin_username + "' and admin_password = '" + admin_password + "' ")
    d = data.fetchall()
    for a in d:
        adminid = a[0]
    t = len(d)
    if t == 1:
        print('Login Successfully')
        initadmin()
    else:
        print('Invalid email or password')
        a = int(input('1.Try Again \n2.Main Menu : '))
        if a == 1:
            admin()
        elif a == 2:
            init()
        else:
            print('Choose either 1 or 2')

def initadmin():
    global adminid
    ad = int(input('''
                    1.View All Users
                    2.View All Dealers
                    3.View Cabs
                    4.Change Password
                    5.Logout : '''))
    if ad == 1:
        view_users()
    elif ad == 2:
        view_dealers()
    elif ad == 3:
        view_cabs()
    elif ad == 4:
        change_password_admin()
    elif ad == 5:
        del adminid
        init()
    else:
        print('Enter Valid Input')

def view_users():
    print("{0:10} {1:15} {2:30} {3:15}".format("User id","User Name","User Email","User Phone"))
    data = "select * from users"
    al_data = c.execute(data)
    x = al_data.fetchall()
    for a in x:
        print("{0:<10} {1:<15} {2:<30} {3:<15}".format(a[0],a[1],a[3],a[4]))
    t = input("You Want to Delete any User Records y/n : ")
    if t == 'y':
        i = int(input('Enter User ID to delete the record : '))
        deldata = "delete from users where user_id='"+str(i)+"'"
        c.execute(deldata)
        conn.commit()
        print('Record Deleted Successfully')
        view_users()
    elif t == 'n':
        initadmin()
    else:
        print('Invalid!Enter Y else N ')
        initadmin()

def view_dealers():
    print("{0:10} {1:15} {2:30} {3:15}".format("Dealer id","Dealer Name","Dealer Email","Dealer Phone"))
    data = "select * from cab_dealers"
    al_data = c.execute(data)
    x = al_data.fetchall()
    for a in x:
        print("{0:<10} {1:<15} {2:<30} {3:<15}".format(a[0],a[1],a[3],a[4]))
    t = input("You Want to Delete any Dealer Records y/n : ")
    if t == 'y':
        i = int(input('Enter Dealer ID to delete the record : '))
        deldata = "delete from cab_dealers where cab_dealerid='"+str(i)+"'"
        c.execute(deldata)
        conn.commit()
        print('Record Deleted Successfully')
        view_dealers()
    elif t == 'n':
        initadmin()
    else:
        print('Invalid!Enter Y else N ')
        initadmin()

def view_cabs():
    data = "SELECT c.cab_id,c.cab_name,c.cab_type,c.cab_model,d.cab_dealername,d.cab_dealerphone,c.cab_from,c.cab_to,c.cab_number from cabs as c INNER JOIN cab_dealers as d on c.cab_dealerid = d.cab_dealerid"
    cab_data = c.execute(data)
    cab_finaldata = cab_data.fetchall()
    print("{0:15}{1:15}{2:15}{3:15}{4:20}{5:20}{6:15}{7:15}{8:15}".format("cab_id", "Cab Name", "Cab Type", "Cab Model",
                                                                          "Cab Dealer Name", "Cab Contact Number",
                                                                          "Cab From", "Cab To",
                                                                          "Cab Number"))
    for d in cab_finaldata:
        print(
            "{0:<15}{1:<15}{2:<15}{3:<15}{4:<20}{5:<20}{6:<15}{7:<15}{8:15}".format(d[0], d[1], d[2], d[3], d[4], d[5],
                                                                                    d[6], d[7], d[8]))
    t = input("You Want to Delete any Cab Records y/n : ")
    if t == 'y':
        i = int(input('Enter Cab ID to delete the record : '))
        deldata = "delete from cabs where cab_id='" + str(i) + "'"
        c.execute(deldata)
        conn.commit()
        print('Record Deleted Successfully')
        view_cabs()
    elif t == 'n':
        initadmin()
    else:
        print('Invalid!Enter Y else N ')

def change_password_admin():
    global adminid
    old_password = input("Enter Old Password : ")
    data=c.execute("SELECT * from admin where admin_password='"+str(old_password)+"' and admin_id='"+str(adminid)+"'")
    d = data.fetchall()
    t=len(d)
    if t == 1:
        newpass = input('Enter New Password : ')
        cpass = input('Enter Confirm Password : ')
        if(newpass == cpass):
            upd = "update admin set admin_password='"+newpass+"' where admin_id='"+str(adminid)+"'"
            c.execute(upd)
            conn.commit()
            print('Password Changed')
            initadmin()
        else:
            print("Password not matching")
            initadmin()
    else:
        print('Invalid Old Password')
        initadmin()

def init():
    choice = int(input('''
    **Select**
    1.Dealer Registration
    2.Dealer Login
    3.User Registration
    4.User Login
    5.Admin Login
    6.Exit : '''))

    if choice == 1:
        dealer_reg()
    elif choice == 2:
        dealerlogin()
    elif choice == 3:
        user_reg()
    elif choice == 4:
        userlogin()
    elif choice == 5:
        admin()
    elif choice == 6:
        exit()
    elif choice == 7:
        pass

init()
