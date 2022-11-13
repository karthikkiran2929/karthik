import datetime 
today=datetime.date.today()
toda=today.strftime("%y-%m-%d")






def connect():
    import time
    import mysql.connector
    global mydb
    mydb= mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "scott",
        database="bank"
        )
    global cur
    cur=mydb.cursor()
 
    print("CONNECTED TO THE SERVER SUCCESSFULLY")
    return

def add1():
    w=cur.rowcount
    a=w+1
    b=input("PLEASE ENTER THE BANK NAME:")
    d=int(input("INPUT THE AMOUNT:"))
    e=float(input("INPUT THE INTEREST RATE:"))
    
    sql= "INSERT INTO credit VALUES(%s, %s, %s, %s)"
    val=[a,b,d,e]
    cur.execute(sql, val)
    mydb.commit()
    
    print("DATA ADDED SUCCESSFULLY")
    return

    

    
#CREDIT SCORE CHECKER
def cs():
    print("A credit score is a numerical expression based on a level analysis of a person's credit files, to represent the creditworthiness of an individual")
    cs=int(input("ENTER THE CREDIT SCORE TO CHECK NYOUR ELIGILIBITY:"))
    if cs<=580:
        print("BAD, TRY TO IMPROVE YOUR SCORE")
    elif cs <=669:
        print("FAIR ENOUGH TO GET A LOAN")
    elif cs <=749:
        print("GOOD,KEEP IT UP")
    elif cs<=799:
        print("VERY GOOD,DONT WORRY ABOUT GETTING LOAN")
    else:
        print("BRAVO,BANK IS WAITING FOR YOU")
    

#DEBIT
def add(c,r):
    a=0
    b=input("PLEASE ENTER THE BANK NAME:")
    d=int(input("INPUT THE AMOUNT:"))
    e=float(input("INPUT THE INTEREST RATE:"))
    if r=="":
         r=input("INPUT THE RATING:")
    sql= "INSERT INTO debit (bankname,type,amount,interest,rating) VALUES (%s, %s, %s, %s, %s)"
    val= (b,c,d,e,r)
    cur.execute(sql, val)
    mydb.commit()
def mb():
    print(" 1.BANK DETAILS")
    print(" 2.ADD TO PORTFOLIO")
    n=int(input("ENTER THE OPTION:"))
    if n==1:
        cur.execute("select * from debit where type='mb'")
        h=cur.fetchall()
        for i in h:
            print(i)
    elif n==2:
        print("STOCK MARKET AND BONDS ARE RISE BASES ON ACTUAL MARKET,PLEASE RATE THE ASSEST AT YOUR OWN")
        c="mb"
        r=""
        add(c,r)
def bond():
    print(" 1.BOND DETAILS")
    print(" 2.ADD TO PORTFOLIO")
    n=int(input("ENTER THE OPTION:"))
    if n==1:
        cur.execute("select * from debit where type='b'")
        h=cur.fetchall()
        for i in h:
            print(i)
    elif n==2:
        c="b"
        r="B"
        add(c,r)
def insu():
    print(" 1.INSURANCE DETAILS")
    print(" 2.ADD TO PORTFOLIO")
    n=int(input("ENTER THE OPTION:"))
    if n==1:
        cur.execute("select * from debit where type='i'")
        h=cur.fetchall()
        for i in h:
            print(i)
    elif n==2:
        c="i"
        r="C"
        add(c,r)
def show1():
    cur.execute("Select * from debit")
    c=cur.fetchall()
    for i in c:
        print(i)
          
def infr():
    print("***INFORMAL OPTIONS ARE NOT CONSIDERED SAFE BECAUSE THEY AE NOTE IN CONTROLL OF RBI***")
    print("***TAKE RISE IN YOUR OWN TERMS***")
    print(" 1.ADD TO PORTFOLIO")
    n=int(input("ENTER THE OPTION:"))
    if n==1:
        c="in"
        r="A"
        add(c,r)
def aexpense():
    
    print("ENTER THE DATA FOR","\n","1.FAMILY","\n","2.PERSONAL")
    s=int(input("ENTER THE OPTION:"))
    if s==1:
        
        fname="family"
    else:
        fname=user
        
    name=input("ENTER THE NAME OF THE EXPENSE:")
    amount=int(input("ENTER THE AMOUNT OF THE EXPENSE:"))
    cur.execute("select curdate()")
    data=cur.fetchone()
    sql="insert into expense (name,amount,entime,fname) values (%s,%s,%s,%s)"
    var=(name,amount,data[0],fname)
    cur.execute(sql,var)
    mydb.commit()
    no=input("CLICK ENTER TO MAIN AND ANY KEY TO ADD EXPENSE AGAIN")
    if no=="":
        main()
    else:
        aexpense()
def sexpence():
    
    print("SHOW THE DATA FOR","\n","1.FAMILY","\n","2.PERSONAL")
    s=int(input("ENTER THE OPTION:"))
    en=input("ENTER FOR DATE BASED EXPENSE AND ANY KEY FOR ALL DATA: ")
    if en=="":
        print("1.TODAY DATE","\n","2.ENTER DATE")
        o=int(input("ENTER THE OPTION:"))
        if o==1:
            entime=toda
        else:
            
            
            day=str(int(input("ENTER THE DATE:")))
            month=str(int(input("ENTER THE MONTH:")))
            year=str(int(input("ENTER THE YEAR:")))
            entime=str(year+"-"+month+"-"+day)
    else:
        entime=""
    if s==1:
        
        
        sql=("select * from expense WHere fname='family' and entime=%s ")
        var=tuple(year-month-day)
        
        
                
    else:
        cur.execute("select distinct(fname) from expense")
        f=cur.fetchall()
        for i in range(1,len(f)+1):
            print(i,f[i-1])
        s=int(input("ENTER THE OPTION:"))
        name=f[s-1]
        var=(name[0],entime)
        sql=("select * from expense WHere fname=%s and entime=%s")
    cur.execute(sql,var)
    b=cur.fetchall()
            
    print("NAME OF THE EXPENSE   AMOUNT SPEND  DATE ")
    for i in b:
                
        print(i)
    main()    
def totexpense():
    
    print("ENTER THE DATA FOR","\n","1.FAMILY","\n","2.PERSONAL")
    s=int(input("ENTER THE OPTION:"))
    if s==1:
        cur.execute("select sum(amount) from expense WHere fname='family' ")

    else:
        cur.execute("select distinct(fname) from expense")
        f=cur.fetchall()
        for i in range(1,len(f)+1):
                print(i,f[i-1])
        s=int(input("ENTER THE OPTION:"))
        name=f[s-1]
                
        sql=("select sum(amount) from expense WHere fname=%s")
        cur.execute(sql,name)
    b=cur.fetchone()
    print("THE AMOUNT IS",b[0])
#YOUR ACCOUNT
def account():
    print("1.YOUR TOTAL CREDIT")
    print("2.YOUR TOTAL DEBIT ")
    print("3.YOUR OVERALL SURPLUS")
    print("4.EXIT")
    n=int(input("ENTER THE OPTION:"))
    if n==1:
        tot1()
    elif n==2:
        tot2()
    elif n==3:
        overall()
    elif n==4:
        return
    else:
        print("INVALID OPTION")
def tot1():
    cur.execute("select * from credit")
    global a1
    a1=0
    b=cur.fetchall()
    for i in b:
        a1=a1+i[2]
    print("THE TOTAL CREDIT IS",a1)
    
def tot2():
    cur.execute("select * from debit")
    global b1
    b1=0
    a=cur.fetchall()
    for i in a:
        b1=b1+i[3]

    print("THE TOTAL DEBIT IS",b1)
    return b1
def overall():
    tot1()
    tot2()
    c=b1-a1
    if c<0:
        print("YOU HAVE MORE CREDIT THAN SAVINGS:",int(c))
    else:
        print("YOU ARE IN THE SAFER SIDE:",c)

def emi():
    
    p=int(input("ENTER THE LOAN AMOUNT:"))
    print("TENURE IN:","\n","1.MONTHS","\n","2.YEARS")
    n=int(input("ENTER THE OPTION:"))
    if n==1:
        n=int(input("ENTER LOAN TERMS(MONTHS):"))
    else:
        n=int(input("ENTER LOAN TERMS IN YEARS:"))
        n=n*12
    r=float(input("ENTER THE INTEREST RATE(%):"))
    r=r/1200
    x=(1+r)**n
    
    emi=(p*r*x)/((x)-1)
    print("YOUR EMI IS  ₹",round(emi))
    print("YOUR TOTAL PAYABLE AMOUNT IS  ₹",round(emi*n))
    print("YOUR PAYABLE INTEREST IS  ₹",round((emi*n)-p))
connect()
def fd():
    p=int(input("ENTER THE PRINCIPAL AMOUNT:"))
    print("TIME PERIOD IN:","\n","1.MONTHS","\n","2.YEARS")
    n=int(input("ENTER THE OPTION:"))
    if n==1:
        n=int(input("ENTER TIME PEROID(MONTHS):"))
    else:
        n=int(input("ENTER TIME PEROID IN YEARS:"))
        n=n*12
    r=float(input("ENTER THE INTEREST RATE(%):"))
    c=(1+r/100)**(n/12)
    a=p*c
    interest=a-p
    print("YOUR PROFIT RETURN IS  ₹",round(interest))
def rd():
    p=int(input("ENTER THE MONTHLY INSTALLMENT:"))
    print("TIME PERIOD IN:","\n","1.MONTHS","\n","2.YEARS")
    n=int(input("ENTER THE OPTION:"))
    if n==1:
        n=int(input("ENTER TIME PEROID(MONTHS):"))
    else:
        n=int(input("ENTER TIME PEROID IN YEARS:"))
        n=n*12
    r=float(input("ENTER THE INTEREST RATE(%):"))
    c=p*(1+r/400)**(n/3)
    
    print("YOUR TOTAL VALUE IS ₹",(p*n)+(round(c-p)*n/2))
    print("YOUR ESTIMATED RETURN IS  ₹",round(c-p)*n/2)
    print("YOUR INVESTED AMOUNT IS ₹",p*n)
def ppf():
    a=int(input("ENTER THE DEPOSIT AMOUNT:"))
    t=input("ENTER THE TIME PEROID OF THE FUND(MORE THAN 15 YEARS OR ENTER FOR DEFAULT TIME PEROID:)")
    print("RATE OF THE INTEREST IS 7.1%")
    r=7.1
    if t=="":
        t=15
    else:
        t=t
    tempamt=a
    totint=0
    for i in range(0,t):
        interest=(tempamt*r)/100
        tempamt=tempamt+interest+a
        totint=totint+interest
    print("TOTAL MATURITY AMOUNT AFTER ",t," YEARS AT 7.1% IS ",tempamt-a)
    print("TOTAL INTEREST EARNED IS",totint)
def main():
    print("1.INCOME")
    print("2.EXPENCE")
    print("3.INVESTMENT")
    print("4.FINANCIAL CALCULATOR")
    n=int(input("ENTER THE OPTION:"))
    exit=0
    if n==1:
        while exit==0:
            print("1.SALARY")
            print("2.OTHER INCOMES")
            print("3.EXIT")
            n=int(input("ENTER THE OPTION:"))
            a=""
            while n==1:
                if a=="":
                    sql=("select * from salary where salary='monthly' and user=%s")
                    var=(user,)
                    cur.execute(sql,var)
                    
                    b=cur.fetchall()
                    
                        
                    
                    if b==[]:
                        a=int(input("INPUT YOUR MONTHLY SALARY:"))
                        sql=("insert into salary (salary,amount,user) values(%s,%s,%s)")
                        val=("monthly",a,user)
                        cur.execute(sql, val)
                        mydb.commit()
                    else:
                        print(b)
                        a=b[0][1]
                        pass
                print("BASED ON 20:30:50 RULE")
                print("1.KNOW ABOUT SAVINGS RULE")
                print("2.CALCULATE YOUR SAVINGS")
                print("3.EXIT")
                n=int(input("ENTER THE OPTION:"))
                if n==1:
                    print("50/30/20 is a simple yet intuitive and effective plan that helps people meet their financial plan. The rule requires you to spend no more than 50% of your after-tax income on must-have needs. Next comes utilizing 20% on savings and debt repayments, whereas 30% of the money is spent on personal interest things.")
                    n=1
                elif n==2:
                    print("THE AMOUNT FOR YOUR NEED IS:",a*0.50)
                    print("THE AMOUNT FOR YOUR WANTS IS:",a*0.30)
                    print("THE AMOUNT FOR YOUR SAVINGS IS:",a*0.20)
                    n=1
            
                elif n==3:
                    n=0 
            while n==2:
                type1=input("THE SOURCE OF INCOME:")
                amo=int(input("ENTER THE INCOME:"))
                sql=("insert into salary (salary,amount) values(%s,%s)")
                val=(type1,amo)
                cur.execute(sql, val)
                mydb.commit()
                n=1
            if n==3:
                 main()
                    
    elif n==2:
        print("1.ADD EXPENCES")
        print("2.SHOW EXPENCES")
        print("3.CHECK TOTAL EXPENSE")
        n=int(input("ENTER THE OPTIONS:"))
        if n==1:
            aexpense()
        elif n==2:
            sexpence()
        elif n==3:
            totexpense()
            
    elif n==3:
        print("1.NEW INVESTMENT")
        print("2.EXISTING INVESTMENT")
        print("3.TOTAL INVESTMENT")
        n=int(input("ENTER THE OPTION:"))
        if n==1:
            print("1.MUTUAL BONDS")
            print("2.BONDS")
            print("3.INSURANCE")
            print("4.INFORMAL")
            n=int(input("ENTER THE OPTION:"))
            if n==1:
                
                mb()
            elif n==2:
                bond()
            elif n==3:
                insu()
            elif n==4:
                infr()
            else:
                print("INFORMATION NOT AVAILABLE")
        elif n==2:
            cur.execute("select * from debit")
            a=cur.fetchall()
            for i in a:
                print(i)
        elif n==3:
            tot1()
    elif n==4:
        print("1.EMI CALCULATOR")
        print("2.CREDIT CARD ELIGIBILITY")
        print("3.FD CALCULATOR")
        print("4.RD CALCULATOR")
        print("5.PPF CALCULATOR")
        n=int(input("ENTER THE OPTION:"))
        if n==1:
            emi()
        elif n==2:
            cs()
        elif n==3:
            fd()
        elif n==4:
            rd()
        elif n==5:
            ppf()
        
def login():
    
    print("1.LOGIN")
    print("2.CREATE NEW ACCOUNT")
    print("3.CREATE NEW FAMILY ACCOUNT")
    print("4.exit")
    n=int(input("ENTER THE OPTION:"))
    if n==1:
        password=input("ENTER THE FAMILY PASSWORD:")
        global user
        user=input("ENTER THE USERNAME:")
        cur.execute("select*from account4")
        usepass=cur.fetchall()
        cur.execute("select*from account3")
        usepass1=cur.fetchall()
        for i in usepass:
            for a in i:
                
                if user==a and password==usepass1[0][1]:
                    
                    print("welcome",user)
                    
                    main()
                    
                elif user!=a and password!=usepass1[0][1]:
                    print("EITHER PASSWORD OR USERNAME IS WRONG ENTER THE CORRECT USER NAME AND PASSWORD")
                    continue
        
                
                    
                    

    elif n==2:
        user=input("ENTER THE USERNAME:")
        cur.execute("select * from account3")
        b=cur.fetchone()
        password=input("ENTER THE FAMILY PASSWORD:")
        if password==b[1]:
            try:
                sql=("insert into account4 (e_name) values (%s)")
                var=(user,)
                cur.execute(sql,var)
                mydb.commit()
            except:
                print("ACCOUNT ALREADY EXISTS")
            print("LOGIN SUCCESSFUL")
        else:
             print("WRONG PASSWORD")
        login()     
    elif n==3:
        try:
            a=1 
            sql1=("insert into faze(ju) values (%s)")
            z=(a,)
            cur.execute(sql1,z)
            mydb.commit()
            print("--CREATE YOUR FAMILY ACCOUNT--")
            g=0
            passcode=input("ENTER THE FAMILY PASSWORD:")
            if (len(passcode)>=4):
                print("VALID PASSWORD")
                g=0
            else:
                print("INVALID PASSWORD")
                g="A"
                while g=="A":
                    passcode=input("ENTER THE FAMILY PASSWORD:") 
                    if (len(passcode)>=4):
                        print("VALID PASSWORD")
                        g=0
            repass=input("ENTER YOUR PASSWORD AGAIN:")
            if repass==passcode:
                print("SUCCESSFUL")
                f_name=input("ENTER YOUR FAMILY NAME")
                sql="insert into account3(username,password)values(%s,%s)"
                var=(f_name,passcode)
                cur.execute(sql,var)
                mydb.commit()
        
            else:
                while repass!=passcode:
                    repass=input("ENTER YOUR PASSWORD AGAIN:")
                    print("SUCCESSFUL")
                    f_name=input("ENTER YOUR FAMILY NAME")
                    ql=("insert into account3 (username,password) values (%s,%s)")
                    var=(f_name,passcode)
                    cur.execute(sql,var)
                    mydb.commit()
        except:
            print('account already created')
        login()    
main()
        
  
