import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
from datetime import datetime
st.set_page_config(page_title='EMS',page_icon='https://media.istockphoto.com/id/1165699436/vector/creative-workplace-with-computer-monitor-empty-no-people-cabinet-modern-office-furniture-flat.jpg?s=612x612&w=0&k=20&c=6OQYUj6XG_NNqwoaDdf2-L_mdTJQdu4D_xZrF7PHHOE=')
st.sidebar.title('DASHBOARD')
st.sidebar.image('https://cdn.vectorstock.com/i/preview-1x/73/77/business-people-celebrating-victory-team-vector-29597377.jpg')
choice=st.sidebar.selectbox('Menu',('Home',))  
st.sidebar.image('https://media.istockphoto.com/id/512287852/de/vektor/corporate-office-building.jpg?s=612x612&w=0&k=20&c=Zx6VrTMNadGrh7CXztIkmBeKkKBXCA8pLkWxeXrHlNY=')
if(choice=='Home'): # Home
    st.title('Welcome to EMS 😊')
    cu=st.selectbox('Select',('Admin login','Employee login'))
    if(cu=='Admin login'):  # Admin Login
        if 'login' not in st.session_state:
            st.session_state['login']=False
        if(not st.session_state['login']):
            st.header('Kindly enter admin username and password')
            U=st.text_input("Enter Username:")
            P=st.text_input("Enter Password:")
            btn=st.button("Login")
            if btn:
                mydb=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="new")
                c=mydb.cursor()
                c.execute("select * from admin_login")
                for row in c:
                    if(row[0]==U and row[1]==P):
                        st.session_state['login']=True
                        st.rerun()
                        break
                if(not st.session_state['login']):
                    st.header('👎😓Wrong id or password \n Try again')
        if(st.session_state['login']):
            cc=st.sidebar.selectbox('Choose',('Search',"Employee's info",'Leave Monitoring','About','Attendance','Payroll'))
            if(cc=="Employee's info"):
                ce=st.sidebar.selectbox('Category',('Display','Modify'))
                if(ce=='Display'):  # Display
                    st.image('https://images.freeimages.com/clg/istock/previews/9155/91556599-modern-office-interior-workplace-desk.jpg')
                    ch1=st.selectbox('Choose',('All','Personal','Professional','Branch'))
                    if(ch1=='All'): # ALL i.e, BOTH PERSONAL AND PROFESSIONAL DETAILS OF ALL EMPLOYEES
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select e.ID,e.First_Name,e.Last_Name,e.Gender,e.Email_id,e.Age,e.Marital_Status,j.Position,j.Department,j.Branch,j.Years_of_Experience,j.Salary,j.Emp_Satisfaction,j.Performance_Score from emp as e join job as j using(ID) order by e.ID')
                        l=[]
                        for i in c:
                            l.append(i)
                            df=pd.DataFrame(data=l,columns=c.column_names)
                        st.image('https://t4.ftcdn.net/jpg/02/37/37/91/360_F_237379122_uhllhclrtGxvy4lOq1AtF4t8mcneQlTA.jpg')
                        st.dataframe(df)
                    elif(ch1=='Personal'): # PERSONAL
                        st.image('https://static.vecteezy.com/system/resources/thumbnails/001/226/236/small/group-of-smiling-office-workers-or-business-people.jpg')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select * from emp order by ID')
                        l=[]
                        for i in c:
                            l.append(i)
                            df=pd.DataFrame(data=l,columns=c.column_names)
                        st.dataframe(df)
                    elif(ch1=='Professional'):  # PROFESSIONAL
                        st.image('https://img.freepik.com/free-vector/flat-people-business-training-illustration_23-2148921811.jpg')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select * from job order by ID')
                        l=[]
                        for i in c:
                            l.append(i)
                            df=pd.DataFrame(data=l,columns=c.column_names)
                        st.dataframe(df)
                    else:
                        st.image('https://t4.ftcdn.net/jpg/01/18/24/09/360_F_118240954_gtJrYjhrsRrWhQPgTdySQdv9bt78ayk6.jpg')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select Branch,Position,Department,count(ID) as "Total Employees" from job group by (1),(2),(3) order by (1)')
                        l=[]
                        for i in c:
                            l.append(i)
                            df=pd.DataFrame(data=l,columns=c.column_names)
                        st.dataframe(df)
                elif(ce=='Modify'):   # Modify
                    st.image('https://img.freepik.com/premium-vector/secure-safety-online-guard-technology-security-verification-digital-check-software-internet-website-anti-virus-web-protection_212005-265.jpg')
                    ch2=st.selectbox('Select',('Personal','Professional'))
                    if(ch2=='Personal'):      # PERSONAL
                        ch3=st.selectbox('Choose',('Add an employee','Remove an employee',"Change/update"))
                        if(ch3=='Add an employee'):
                            ID=st.number_input('ID of emp:-')
                            fn=st.text_input('First name:-')
                            ln=st.text_input('Last name:-')
                            g=st.text_input('Gender:-')
                            m=st.text_input('email-id :-')
                            age=st.number_input('Age:-')
                            mar=st.text_input('Marital_Status:-')
                            db=st.text_input('Enter DOB in the format - Date Mon(ex-Jan) year:-')
                            bt1=st.button('Add')
                            if bt1:
                                a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                                b=a.cursor()
                                b.execute('insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s)',(ID,fn,ln,g,m,age,mar,db))
                                a.commit()
                                st.header('Added Successfully 😊👍')
                        elif(ch3=='Remove an employee'):
                            ID=st.number_input('ID:-')
                            a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                            b=a.cursor()
                            b.execute('delete from emp where ID=%s',(ID,))
                            a.commit()
                            bt3=st.button('Remove')
                            if bt3:
                                st.header('Removed Successfully 😊👍')
                        elif(ch3=="Change/update"):
                            ch4=st.selectbox('Choose',('AGE','MARITAL_STATUS'))
                            if(ch4=='AGE'):
                                ID=st.number_input('ID:-')
                                age=st.number_input('Age:-')
                                a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                                e=a.cursor()
                                e.execute('update emp set Age=%s where ID=%s',(age,ID))
                                a.commit()
                                bt3=st.button('Update')
                                if bt3:
                                    st.header('Age updated successfully')
                            else:
                                ID=st.number_input('ID:-')
                                mar=st.text_input('Marital_Status')
                                a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                                e=a.cursor()
                                e.execute('update emp set marital_status=%s where ID=%s',(mar,ID))
                                a.commit()
                                bt3=st.button('Update')
                                if bt3:
                                    st.header('Marital_Status updated successfully😊👍')
                    else:  # PROFESSIONAL
                        ch3=st.selectbox('Choose',('Add an employee','Remove an employee',"Change/update an employee's info"))
                        if(ch3=='Add an employee'):
                            Id=st.number_input('ID:-')
                            po=st.text_input('Job Position:-')
                            dp=st.text_input('Department:-')
                            br=st.text_input('Branch:-')
                            yr=st.number_input('Years of Experience:-')
                            s=st.number_input('Salary:-')
                            sa=st.number_input('Employee Satisfaction:-')
                            pr=st.text_input('Performance Score:-')
                            bt1=st.button('Add')
                            if bt1:
                                a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                                b=a.cursor()
                                b.execute('insert into job values(%s,%s,%s,%s,%s,%s,%s,%s)',(Id,po,dp,br,yr,s,sa,pr))
                                a.commit()                    
                                st.header('Added Successfully😊👍')
                        elif(ch3=='Remove an employee'):
                            ID=st.number_input('ID:-')
                            a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                            b=a.cursor()
                            b.execute('delete from job where ID=%s',(ID,))
                            a.commit()
                            bt3=st.button('Remove')
                            if bt3:
                                st.header('Removed Successfully😊👍')
                        else:
                            ch5=st.selectbox('Choose',('POSITION','DEPARTMENT','BRANCH','YEARS_OF_EXPERIENCE','SALARY','EMP_SATISFACTION','SCORE'))
                            a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                            if(ch5=='POSITION'):
                                pt=st.text_input('Job Position:-')
                                ID=st.number_input('ID:-')
                                e=a.cursor()
                                e.execute('update job set position=%s where ID=%s',(pt,ID))
                                a.commit()
                                bt3=st.button('Update')
                                if bt3:
                                    st.header('Job position updated successfully 😊👍')
                            elif(ch5=='DEPARTMENT'):
                                dp=st.text_input('Department:-')
                                ID=st.number_input('ID:-')
                                e=a.cursor()
                                e.execute('update job set department=%s where ID=%s',(dp,ID))
                                a.commit()
                                bt3=st.button('Update')
                                if bt3:
                                    st.header('Department updated successfully 😊👍')
                            elif(ch5=='BRANCH'):
                                br=st.text_input('Branch-')
                                ID=st.number_input('ID:-')
                                e=a.cursor()
                                e.execute('update job set branch=%s where ID=%s',(br,ID))
                                a.commit()
                                bt3=st.button('Update')
                                if bt3:
                                    st.header('Branch updated successfully 😊👍')
                            elif(ch5=='YEARS_OF_EXPERIENCE'):
                                yr=st.number_input('Years of Experience:-')
                                ID=st.number_input('enter the id-')
                                e=a.cursor()
                                e.execute('update job set YEARS_OF_EXPERIENCE=%s where ID=%s',(yr,ID))
                                a.commit()
                                bt3=st.button('Update')
                                if bt3:
                                    st.header('Experience status is updated successfully')
                            elif(ch5=='SALARY'):
                                s=st.number_input('Salary:-')
                                ID=st.number_input('ID:-')
                                e=a.cursor()
                                e.execute('update job set SALARY=%s where ID=%s',(s,ID))
                                a.commit()
                                bt3=st.button('Update')
                                if bt3:
                                    st.header('Salary is updated successfully 😊👍')
                            elif(ch5=='EMP_SATISFACTION'):
                                sa=st.number_input('Employee Satisfaction:-')
                                ID=st.number_input('ID:-')
                                e=a.cursor()
                                e.execute('update job set EMP_SATISFACTION=%s where ID=%s',(sa,ID))
                                a.commit()
                                bt3=st.button('Update')
                                if bt3:
                                    st.header('Employee Satisfaction is updated successfully😊👍')                            
                            elif(ch5=='SCORE'):
                                pr=st.text_input('Performance Score:-')
                                ID=st.number_input('ID:-')
                                e=a.cursor()
                                e.execute('update job set PERFORMANCE_SCORE=%s where ID=%s',(pr,ID))
                                a.commit()
                                bt3=st.button('Update')
                                if bt3:
                                    st.header('PERFORMANCE SCORE is updated successfully😊👍')
            elif(cc=='Search'):  # Search
                st.image('https://www.venminder.com/hubfs/Blog_Images/2022_Blog_Posts/04.12.2022-record-retention-how-long-do-you-keep-vendor-documents-FEATURED.jpg')    
                v=st.checkbox('Employee ID,First and last name')
                if v:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select id,First_Name,Last_Name from emp')
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                    st.dataframe(df)                
                h=st.toggle('Using Employee ID',['ID'])
                if h:
                    bts=st.selectbox( "Using Employee's ID",('Salary','Department','Branch','Age','Job role','Date of Birth','Experience','Job Satisfaction & Performance Score','Payroll Details'))
                    if (bts=='Salary'):
                        i=st.number_input('Employee ID')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select salary from  job join emp using(id) where emp.id=%s',(i,))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Department'):
                        i=st.number_input('Employee ID')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select department from  job join emp using(id) where emp.id=%s',(i,))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Branch'):
                        i=st.number_input('Employee ID')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select branch from  job join emp using(id) where emp.id=%s',(i,))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Age'):
                        i=st.number_input('Employee ID')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select age from  job join emp using(id) where emp.id=%s',(i,))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Job role'):
                        i=st.number_input('Employee ID')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select position from  job join emp using(id) where emp.id =%s',(i,))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Date of Birth'):
                        i=st.number_input('Employee ID')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select DOB as Date_of_Birth from  job join emp using(id) where emp.id =%s',(i,))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Experience'):
                        i=st.number_input('Employee ID')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select years_of_experience  as Experience_in_years  from  job join emp using(id) where emp.id =%s',(i,))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Job Satisfaction & Performance Score'):
                        i=st.number_input('Employee ID')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select emp_Satisfaction as Job_Satisfaction,Performance_Score from  job join emp using(id) where emp.id =%s',(i,))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Payroll Details'):
                        i=st.number_input('Employee ID')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select j.ID,e.First_name,e.Last_name,e.Age,j.Position,j.Department,j.Branch,p.Year,p.Week,p.Grosspay,p.Regularpay,p.Overtime_hours,p.Overtimepay from emp e join job j using(id) join p_roll p using(id) where e.id=%s',(i,))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                h1=st.toggle("Using Employee's Names")
                if h1:
                    bts=st.selectbox( 'Using First and last name',('Salary','Department','Branch','Age','Job role','Date of Birth','Experience','Job Satisfaction & Performance Score','Payroll Details'))
                    if (bts=='Salary'):
                        n=st.text_input('First Name')
                        n1=st.text_input('Last Name')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select salary from  job join emp using(id) where emp.first_name=%s and emp.last_name =%s',(n,n1))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Department'):
                        n=st.text_input('First Name')
                        n1=st.text_input('Last Name')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select department from  job join emp using(id) where emp.first_name=%s and emp.last_name =%s',(n,n1))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Branch'):
                        n=st.text_input('First Name')
                        n1=st.text_input('Last Name')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select branch from  job join emp using(id) where emp.first_name=%s and emp.last_name =%s',(n,n1))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Age'):
                        n=st.text_input('First Name')
                        n1=st.text_input('Last Name')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select age from  job join emp using(id) where emp.first_name=%s and emp.last_name =%s',(n,n1))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Job role'):
                        n=st.text_input('First Name')
                        n1=st.text_input('Last Name')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select position from  job join emp using(id) where emp.first_name=%s and emp.last_name =%s',(n,n1))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Date of Birth'):
                        n=st.text_input('First Name')
                        n1=st.text_input('Last Name')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select DOB as Date_of_Birth from  job join emp using(id) where emp.first_name=%s and emp.last_name =%s',(n,n1))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Experience'):
                        n=st.text_input('First Name')
                        n1=st.text_input('Last Name')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select years_of_experience  as Experience_in_years  from  job join emp using(id) where emp.first_name=%s and emp.last_name =%s',(n,n1))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Job Satisfaction & Performance Score'):
                        n=st.text_input('First Name')
                        n1=st.text_input('Last Name')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select emp_Satisfaction as Job_Satisfaction,Performance_Score from  job join emp using(id) where emp.first_name=%s and emp.last_name =%s',(n,n1))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)
                    elif(bts=='Payroll Details'):
                        n=st.text_input('First Name')
                        n1=st.text_input('Last Name')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select j.ID,e.First_name,e.Last_name,e.Age,j.Position,j.Department,j.Branch,p.Year,p.Week,p.Grosspay,p.Regularpay,p.Overtime_hours,p.Overtimepay from emp e join job j using(id) join p_roll p using(id) where e.first_name=%s and e.last_name=%s',(n,n1))
                        l=[]
                        for i in c:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.table(df)                                                                                                        
            elif(cc=='Leave Monitoring'): # Leave Monitoring
                cl=st.selectbox('Select',('View','Approve',))                
                if(cl=='View'):  # View
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select * from adm_ap')
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                    st.dataframe(df)                    
                else:
                    s=st.number_input('Enter the RegNo. for approval')
                    y=st.text_input('Enter Yes for approval and No for disapproval')
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('update adm_ap set ApprovalStatus=%s where RegNo=%s',(y,s))
                    a.commit()
                    btp=st.button('Okay')
                    if btp:
                        st.header('Done 👍')                        
            elif(cc=='About'):  # Analytics
                a1=st.checkbox('Employees by Branches')
                if a1:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select Branch,count(id)as Total_employees from job group by branch')
                    l=[]
                    for i in c:
                        l.append(i)
                    df=pd.DataFrame(data=l,columns=c.column_names)
                    st.table(df)
                ds=st.checkbox('Employees by department')
                if ds:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select Department,count(id)as Total_employees from job group by (1)')                            
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                    st.bar_chart(df,x='Department',y='Total_employees')
                a2=st.checkbox('Employees by Gender')
                if a2:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select * from emp')
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        p=df['GENDER'].value_counts()
                    d1=(p.iloc[0]/1000)*100
                    d2=(p.iloc[1]/1000)*100
                    co=[d1,d2]
                    pie=px.pie(values=(d1,d2),names=['Male','Female'])
                    st.plotly_chart(pie)
                a3=st.checkbox('Employees by job roles')
                if a3:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select * from job')
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        p=df['POSITION'].value_counts()
                    p1=(p.iloc[0]/1000)*100
                    p2=(p.iloc[1]/1000)*100
                    p3=(p.iloc[2]/1000)*100
                    p4=(p.iloc[3]/1000)*100
                    p5=(p.iloc[4]/1000)*100
                    p6=(p.iloc[5]/1000)*100
                    p7=(p.iloc[6]/1000)*100
                    p8=(p.iloc[7]/1000)*100
                    p9=(p.iloc[8]/1000)*100
                    p10=(p.iloc[9]/1000)*100
                    p11=(p.iloc[10]/1000)*100
                    p12=(p.iloc[11]/1000)*100
                    p13=(p.iloc[12]/1000)*100
                    p14=(p.iloc[13]/1000)*100
                    p15=(p.iloc[14]/1000)*100
                    p16=(p.iloc[15]/1000)*100
                    p17=(p.iloc[16]/1000)*100
                    p18=(p.iloc[17]/1000)*100
                    p19=(p.iloc[18]/1000)*100
                    p20=(p.iloc[19]/1000)*100
                    p21=(p.iloc[20]/1000)*100
                    p22=(p.iloc[21]/1000)*100
                    p23=(p.iloc[22]/1000)*100
                    p24=(p.iloc[23]/1000)*100
                    p25=(p.iloc[24]/1000)*100
                    p26=(p.iloc[25]/1000)*100
                    p27=(p.iloc[26]/1000)*100
                    p28=(p.iloc[27]/1000)*100
                    pr=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28]
                    pie=px.pie(values=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28),names=['Production Technician I', 'Production Manager','Production Technician II', 'Data Analyst','Database Administrator', 'IT Support', 'Administrative Assistant','CIO', 'Accountant I', 'President & CEO','Software Engineering Manager', 'Sr. Accountant', 'Sales Manager','Sr.DBA', 'IT Director', 'Area Sales Manager', 'Data Architect','IT Manager - Infra', 'Software Engineer','Shared Services Manager', 'BI Developer','Director of Operations', 'Principal Data Architect','BI Director', 'Enterprise Architect', 'Director of Sales','Senior BI Developer', 'Sr. Network Engineer'])
                    st.plotly_chart(pie)
                aa=st.checkbox('Job experience and Salary range')
                if aa:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select * from job')
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                    st.scatter_chart(df,x='YEARS_OF_EXPERIENCE',y='SALARY')
                a4=st.checkbox('Employees by Performance Score')
                if a4:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute("select distinct(performance_score)as Score,count(id)as 'Number of Employees' from job group by Score")
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                    st.bar_chart(df,x='Score',y='Number of Employees',color= "#ffaa00")
            elif(cc=='Attendance'):
                d=st.selectbox('Choose',('View attendance report',))
                if(d=='View attendance report'):                    
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select * from log_emp')
                    l=[]
                    for i in c:
                        l.append(i)
                    df=pd.DataFrame(data=l,columns=c.column_names)
                    st.dataframe(df)
            else:
                s=st.selectbox('Choose',('View & Approve','Display Payroll Report'))
                if(s=='View & Approve'):
                    z=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    v=z.cursor()
                    v.execute('select id,year(date)Year,month(date)Month,week(date)Week,sum(hour(out_time)-hour(in_time))as Total_hours, case when sum(hour(out_time)-hour(in_time)) < 0 then -(sum(hour(out_time)-hour(in_time))) end as Total_hours1 from log_emp group by id,year(date),month(date),week(date) order by id')
                    l=[]
                    for i in v:
                        l.append(i)
                    df=pd.DataFrame(data=l,columns=v.column_names)
                    st.dataframe(df)
                    u=st.radio('View the rate of pay employee id wise',['View'])
                    if(u=='View'):
                        i=st.text_input('Enter the id') 
                        db=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        g=db.cursor()
                        g.execute('select * from rate_of_pay_emp where id= %s',(i,))
                        l=[]
                        for i in g:
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=g.column_names)
                        st.dataframe(df)
                        x=st.toggle('Enter')
                        if x:
                            i=st.number_input('Enter the id')                
                            y=st.number_input('Enter the year')
                            w=st.number_input('Enter the week number')
                            time=st.number_input('Total hours worked')
                            rate=st.number_input('Enter rate of pay')                        
                            m=st.button('Click here')
                            if m:
                                if time<40:
                                    grosspay=rate*time
                                    RegularPay = rate*40
                                    OverTime=0
                                    OverTimePay=0
                                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                                    c=a.cursor()
                                    c.execute('insert into p_roll values(%s,%s,%s,%s,%s,%s,%s)',(i,y,w,grosspay,RegularPay,OverTime,OverTimePay))
                                    a.commit()
                                    st.header('Done 😊👍')
                                else:
                                    grosspay=rate*time                    
                                    RegularPay = rate*40 
                                    OverTime = time-40    
                                    OverTimeRate = rate*1.5
                                    OverTimePay = round(OverTimeRate*OverTime,2)
                                    GrossPay = round(RegularPay+OverTimePay, 2)                    
                                    RegularPay = rate*40 
                                    OverTime = time-40    
                                    OverTimeRate = rate*1.5
                                    OverTimePay = round(OverTimeRate*OverTime,2)
                                    GrossPay = round(RegularPay+OverTimePay, 2)
                                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                                    c=a.cursor()
                                    c.execute('insert into p_roll values(%s,%s,%s,%s,%s,%s,%s)' ,(i,y,w,grosspay,RegularPay,OverTime,OverTimePay))
                                    a.commit()
                                    st.header('Done 😊👍')                                                                                                                                       
                elif(s=='Display Payroll Report'):
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select j.ID,e.First_name,e.Last_name,e.Age,j.Position,j.Department,j.Branch,p.Year,p.Week,p.Grosspay,p.Regularpay,p.Overtime_hours,p.Overtimepay from emp e join job j using(id) join p_roll p using(id)')
                    l=[]
                    for i in c:
                        l.append(i)
                    df=pd.DataFrame(data=l,columns=c.column_names)
                    st.dataframe(df)
                    
    elif(cu=='Employee login'):
        if 'login' not in st.session_state:
            st.session_state['login']=False
        if(not st.session_state['login']):
            st.header('Kindly enter employee login id and password')
            U=st.number_input("Enter Employee ID:")
            P=st.text_input("Enter Password:")
            btn=st.button("Login")
            if btn:
                mydb=mysql.connector.connect(host="localhost",user="root",password="abcde123",database="new")
                c=mydb.cursor()
                c.execute("select * from emp_login")
                for row in c:
                    if(row[0]==U and row[1]==P):
                        st.session_state['login']=True
                        st.rerun()
                        break
                if(not st.session_state['login']):
                    st.header('👎😓Wrong id or password \n Try again')
        if(st.session_state['login']):
            cc=st.sidebar.selectbox('Choose',("Employee's info",'Leave Monitoring','About','Attendance','Payroll'))
            if(cc=="Employee's info"):
                ce=st.sidebar.selectbox('Category',('Display','Modify'))
                if(ce=='Display'):  # Display
                    st.image('https://images.freeimages.com/clg/istock/previews/9155/91556599-modern-office-interior-workplace-desk.jpg')
                    ch1=st.selectbox('Choose',('All','Personal','Professional','Branch'))
                    if(ch1=='All'): # ALL i.e, BOTH PERSONAL AND PROFESSIONAL DETAILS OF ALL EMPLOYEES
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select e.ID,e.First_Name,e.Last_Name,e.Gender,e.Email_id,e.Age,e.Marital_Status,j.Position,j.Department,j.Branch,j.Years_of_Experience,j.Salary,j.Emp_Satisfaction,j.Performance_Score from emp as e join job as j using(ID) order by e.ID')
                        l=[]
                        for i in c:
                            l.append(i)
                            df=pd.DataFrame(data=l,columns=c.column_names)
                        st.image('https://t4.ftcdn.net/jpg/02/37/37/91/360_F_237379122_uhllhclrtGxvy4lOq1AtF4t8mcneQlTA.jpg')
                        st.dataframe(df)
                    elif(ch1=='Personal'): # PERSONAL
                        st.image('https://static.vecteezy.com/system/resources/thumbnails/001/226/236/small/group-of-smiling-office-workers-or-business-people.jpg')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select * from emp order by ID')
                        l=[]
                        for i in c:
                            l.append(i)
                            df=pd.DataFrame(data=l,columns=c.column_names)
                        st.dataframe(df)
                    elif(ch1=='Professional'):  # PROFESSIONAL
                        st.image('https://img.freepik.com/free-vector/flat-people-business-training-illustration_23-2148921811.jpg')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select * from job order by ID')
                        l=[]
                        for i in c:
                            l.append(i)
                            df=pd.DataFrame(data=l,columns=c.column_names)
                        st.dataframe(df)
                    else:
                        st.image('https://t4.ftcdn.net/jpg/01/18/24/09/360_F_118240954_gtJrYjhrsRrWhQPgTdySQdv9bt78ayk6.jpg')
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select Branch,Position,Department,count(ID) as "Total Employees" from job group by (1),(2),(3) order by (1)')
                        l=[]
                        for i in c:
                            l.append(i)
                            df=pd.DataFrame(data=l,columns=c.column_names)
                        st.dataframe(df)
                elif(ce=='Modify'):   # Modify
                    st.image('https://img.freepik.com/premium-vector/secure-safety-online-guard-technology-security-verification-digital-check-software-internet-website-anti-virus-web-protection_212005-265.jpg')
                    ch2=st.selectbox('Select',('Personal','Professional'))
                    if(ch2=='Personal'):  # Personal
                        ch4=st.selectbox('Choose',('AGE','MARITAL_STATUS'))
                        if(ch4=='AGE'):
                            ID=st.number_input('ID:-')
                            age=st.number_input('Age:-')
                            a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                            e=a.cursor()
                            e.execute('update emp set Age=%s where ID=%s',(age,ID))
                            a.commit()
                            bt3=st.button('Update')
                            if bt3:
                                st.header('Age updated successfully')
                        else:
                            ID=st.number_input('ID:-')
                            mar=st.text_input('Marital_Status')
                            a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                            e=a.cursor()
                            e.execute('update emp set marital_status=%s where ID=%s',(mar,ID))
                            a.commit()
                            bt3=st.button('Update')
                            if bt3:
                                st.header('Marital_Status updated successfully😊👍')
                    else:   # Professional
                        ch5=st.selectbox('Choose',('POSITION','DEPARTMENT','BRANCH','YEARS_OF_EXPERIENCE','SALARY','EMP_SATISFACTION','SCORE'))
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        if(ch5=='POSITION'):
                            pt=st.text_input('Job Position:-')
                            ID=st.number_input('ID:-')
                            e=a.cursor()
                            e.execute('update job set position=%s where ID=%s',(pt,ID))
                            a.commit()
                            bt3=st.button('Update')
                            if bt3:
                                st.header('Job position updated successfully 😊👍')
                        elif(ch5=='DEPARTMENT'):
                            dp=st.text_input('Department:-')
                            ID=st.number_input('ID:-')
                            e=a.cursor()
                            e.execute('update job set department=%s where ID=%s',(dp,ID))
                            a.commit()
                            bt3=st.button('Update')
                            if bt3:
                                st.header('Department updated successfully 😊👍')
                        elif(ch5=='BRANCH'):
                            br=st.text_input('Branch-')
                            ID=st.number_input('ID:-')
                            e=a.cursor()
                            e.execute('update job set branch=%s where ID=%s',(br,ID))
                            a.commit()
                            bt3=st.button('Update')
                            if bt3:
                                st.header('Branch updated successfully 😊👍')
                        elif(ch5=='YEARS_OF_EXPERIENCE'):
                            yr=st.number_input('Years of Experience:-')
                            ID=st.number_input('enter the id-')
                            e=a.cursor()
                            e.execute('update job set YEARS_OF_EXPERIENCE=%s where ID=%s',(yr,ID))
                            a.commit()
                            bt3=st.button('Update')
                            if bt3:
                                st.header('Experience status is updated successfully')
                        elif(ch5=='SALARY'):
                            s=st.number_input('Salary:-')
                            ID=st.number_input('ID:-')
                            e=a.cursor()
                            e.execute('update job set SALARY=%s where ID=%s',(s,ID))
                            a.commit()
                            bt3=st.button('Update')
                            if bt3:
                                st.header('Salary is updated successfully 😊👍')
                        elif(ch5=='EMP_SATISFACTION'):
                            sa=st.number_input('Employee Satisfaction:-')
                            ID=st.number_input('ID:-')
                            e=a.cursor()
                            e.execute('update job set EMP_SATISFACTION=%s where ID=%s',(sa,ID))
                            a.commit()
                            bt3=st.button('Update')
                            if bt3:
                                st.header('Employee Satisfaction is updated successfully😊👍')                        
                        elif(ch5=='SCORE'):
                            pr=st.text_input('Performance Score:-')
                            ID=st.number_input('ID:-')
                            e=a.cursor()
                            e.execute('update job set PERFORMANCE_SCORE=%s where ID=%s',(pr,ID))
                            a.commit()
                            bt3=st.button('Update')
                            if bt3:
                                st.header('PERFORMANCE SCORE is updated successfully😊👍')
            elif(cc=='Leave Monitoring'): # Leave Monitoring
                cl=st.selectbox('Select',('View','Apply'))
                if(cl=='Apply'):
                    st.write('Choose the leave type :- Casual leave,Sick leave,Maternity/Paternity Leave,Others')
                    r=st.number_input('Enter the RegNo.')
                    i=st.number_input('Enter your ID')
                    l=st.text_input('Enter leave type')
                    d=st.date_input('From date')
                    v=st.date_input('To date')
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute("update adm_ap set id=%s,leave_type=%s,From_date=%s,To_date=%s where RegNo=%s",(i,l,d,v,r))
                    a.commit()
                    ap=st.button('Apply')
                    if ap:
                        st.header('Leave applied successfully \n Waiting for the approval')
                elif(cl=='View'):
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select * from adm_ap')
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                    st.dataframe(df)
            elif(cc=='About'):
                a1=st.checkbox('Employees by Branches')
                if a1:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select Branch,count(id)as Total_employees from job group by branch')
                    l=[]
                    for i in c:
                        l.append(i)
                    df=pd.DataFrame(data=l,columns=c.column_names)
                    st.table(df)
                ds=st.checkbox('Employees by department')
                if ds:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select Department,count(id)as Total_employees from job group by (1)')                            
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                    st.bar_chart(df,x='Department',y='Total_employees')
                a2=st.checkbox('Employees by Gender')
                if a2:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select * from emp')
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        p=df['GENDER'].value_counts()
                    d1=(p.iloc[0]/1000)*100
                    d2=(p.iloc[1]/1000)*100
                    co=[d1,d2]
                    pie=px.pie(values=(d1,d2),names=['Male','Female'])
                    st.plotly_chart(pie)
                a3=st.checkbox('Employees by job roles')
                if a3:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select * from job')
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        p=df['POSITION'].value_counts()
                    p1=(p.iloc[0]/1000)*100
                    p2=(p.iloc[1]/1000)*100
                    p3=(p.iloc[2]/1000)*100
                    p4=(p.iloc[3]/1000)*100
                    p5=(p.iloc[4]/1000)*100
                    p6=(p.iloc[5]/1000)*100
                    p7=(p.iloc[6]/1000)*100
                    p8=(p.iloc[7]/1000)*100
                    p9=(p.iloc[8]/1000)*100
                    p10=(p.iloc[9]/1000)*100
                    p11=(p.iloc[10]/1000)*100
                    p12=(p.iloc[11]/1000)*100
                    p13=(p.iloc[12]/1000)*100
                    p14=(p.iloc[13]/1000)*100
                    p15=(p.iloc[14]/1000)*100
                    p16=(p.iloc[15]/1000)*100
                    p17=(p.iloc[16]/1000)*100
                    p18=(p.iloc[17]/1000)*100
                    p19=(p.iloc[18]/1000)*100
                    p20=(p.iloc[19]/1000)*100
                    p21=(p.iloc[20]/1000)*100
                    p22=(p.iloc[21]/1000)*100
                    p23=(p.iloc[22]/1000)*100
                    p24=(p.iloc[23]/1000)*100
                    p25=(p.iloc[24]/1000)*100
                    p26=(p.iloc[25]/1000)*100
                    p27=(p.iloc[26]/1000)*100
                    p28=(p.iloc[27]/1000)*100
                    pr=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28]
                    pie=px.pie(values=(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28),names=['Production Technician I', 'Production Manager','Production Technician II', 'Data Analyst','Database Administrator', 'IT Support', 'Administrative Assistant','CIO', 'Accountant I', 'President & CEO','Software Engineering Manager', 'Sr. Accountant', 'Sales Manager','Sr.DBA', 'IT Director', 'Area Sales Manager', 'Data Architect','IT Manager - Infra', 'Software Engineer','Shared Services Manager', 'BI Developer','Director of Operations', 'Principal Data Architect','BI Director', 'Enterprise Architect', 'Director of Sales','Senior BI Developer', 'Sr. Network Engineer'])
                    st.plotly_chart(pie)
                aa=st.checkbox('Job experience and Salary range')
                if aa:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select * from job')
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                    st.scatter_chart(df,x='YEARS_OF_EXPERIENCE',y='SALARY')
                a4=st.checkbox('Employees by Performance Score')
                if a4:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute("select distinct(performance_score)as Score,count(id)as 'Number of Employees' from job group by Score")
                    l=[]
                    for i in c:
                        l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                    st.bar_chart(df,x='Score',y='Number of Employees',color= "#ffaa00")
            
                
            elif(cc=='Attendance'):
                d=st.selectbox('Choose',('View my attendance report','Fill my attendance report'))
                if(d=='View my attendance report'):
                    i=st.number_input('Enter your employee id')
                    k=st.button('Show')
                    if k:
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('select * from log_emp where id =%s',(i,))
                        l=[]
                        for i in c:                            
                            l.append(i)
                        df=pd.DataFrame(data=l,columns=c.column_names)
                        st.dataframe(df)                                                                                            
                else:                                                                                
                    e= datetime.now()
                    E=e.strftime("%H:%M:%S")
                    f=st.number_input('Enter your ID')
                    g=st.date_input("Enter today's date")
                    h=st.text_input('Enter finishing time')
                    v=st.button('Okay')
                    if v:
                        a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                        c=a.cursor()
                        c.execute('insert into log_emp values (%s,%s,%s,%s)',(E,f,g,h))
                        a.commit()                        
                        st.header('Attendance report filled successfully')
            else:
                d=st.selectbox('Choose',('View',))
                n=st.number_input('Enter your id')
                if d:
                    a=mysql.connector.connect(host='localhost',user='root',password='abcde123',database='new')
                    c=a.cursor()
                    c.execute('select j.ID,e.First_name,e.Last_name,e.Age,j.Position,j.Department,j.Branch,p.Year,p.Week,p.Grosspay,p.Regularpay,p.Overtime_hours,p.Overtimepay from emp e join job j using(id) join p_roll p using(id) where id=%s',(n,))
                    l=[]
                    for i in c:
                        l.append(i)
                    df=pd.DataFrame(data=l,columns=c.column_names)
                    st.dataframe(df)
                    
                
                                    

                
    
                        
                    

   
                            
                
                        
                
                
            
                
                
            
            
        

