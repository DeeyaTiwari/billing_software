
# All Operation performs in a single program
def menu():
    ch="y"
    while (ch=='y') or (ch=="Y"):
        print("*****Welcome to Billing_Software*****") 
        print("1. Add Record")
        print("2. Update Record")
        print("3. Delete Record")
        print("4. Display Record")
        print("5. Exiting")
        choice= int(input("Enter your choice:"))
        if choice==1:
            adddata()
        elif choice ==2:
            updatedata()
        elif choice == 3:
            deldata()
        elif choice ==4:
            display()
        elif choice ==5:
            print("EXITING")
            break
        else:
            print("Wrong Input")
    ch= input("Do you want to continue or not:")
    
# Show all records of table
def display():
    import mysql.connector
    try:
        db=mysql.connector.connect(host="localhost", charset="utf8", user="root", password="Shubhi@2306", database="billing_software")
        cursor=db.cursor()
        cursor.execute("select * from bill_record")
        results= cursor.fetchall()
        for x in results:
            print(x)
    except:
        print("Error: Unable to fetch data")
        
# Insert new record in the table
def adddata():
    import mysql.connector
    db=mysql.connector.connect(host="localhost", charset="utf8", user="root", password="Shubhi@2306", database="billing_software")
    cursor=db.cursor()
    print("Welcome to bill data entry")
    ans='y'
    while ans=='y' or ans=='Y':
        
        bill_no=int(input("Enter customer's bill no."))
        dated=input("Enter date")
        name= input("Enter customer's name")
        mob_no= int(input("Enter customer's mobile number"))
        address=input("Enter customer's address")
        product=input("Enter name of product")
        quantity=int(input("Enter no. of products"))
        amount=int(input("Enter total amount"))
        cursor.execute("insert into bill_record values({0},'{1}','{2}',{3},'{4}','{5}',{6},{7})".format(bill_no,dated,name,mob_no,address,product,quantity,amount))
        db.commit()
        print("## Record Saved...##")
        ans = input("Add More ?")
    
# Update or modify the record of the table
def updatedata():
    import mysql.connector
    db=mysql.connector.connect(host="localhost", charset="utf8", user="root", password="Shubhi@2306", database="billing_software")
    cursor=db.cursor()
    print("Welcome to billing data entry")
    bill_no=int(input("Enter customer's bill no."))
    query="Select * from bill_record where bill_no={}".format(bill_no)
    cursor.execute(query)
    data= cursor.fetchone()
    if data!=None:
        print("## Record Found - Details are ##")
        print(data)
    ans =input("Are you sure update to bill_record : (Y/N)")
    if ans=="Y" or ans=='y':
        dated= input("Enter new date:")
        name= input ("Enter new name")
        mob_no=int(input("Enter new mobile number"))
        address=input("Enter new address")
        product=input("Enter new name of product")
        quantity=int(input("Enter no. of products"))
        amount=int(input("Enter total amount"))
        query="update bill_record set dated={},name='{}',mob_no={},address='{}',product='{}',quantity={},amount={} where bill_no={}".format(dated,name,mob_no,address,product,quantity,amount,bill_no)
        cursor.execute(query)
        db.commit()
        print("Record is updated")
    else:
        print("Sorry no such record exists")
# Delete record from the table
def deldata():
    import mysql.connector
    db=mysql.connector.connect(host="localhost", charset="utf8",
                               user="root", password="Shubhi@2306", database="billing_software")
    cursor=db.cursor()
    print("Delete Record")
    
    bill_no=int(input("Enter customer's bill no"))
    
    query="Select * from bill_record where bill_no={}".format(bill_no)
    
    cursor.execute(query)
    data= cursor.fetchone()
    if data!=None:
        print("## Record Found - Detaile are ##")
        print(data)
        ans =input("Are you sure delete this record : (Y/N)")
    if ans=="Y" or ans=='y':
        query="delete from bill_record where bill_no={}".format(bill_no)
        cursor.execute(query)
        db.commit()
        print("Record is deleted")
        
# Function Calling
menu()
