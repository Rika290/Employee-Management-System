EMS or Employee Management System is: 

•	a local web application developed using Python and MySQL database  
•	useful for maintaining both personal and professional  details of employees  

(A) Objectives:-
1. to manage a large number of data
2. to track the record of each  employee working in a Company or Organization -  to reduce the time needed for maintaining such a huge dataset by using this computerized system
 
(B) Libraries and Modules used: 
1. Backend: 
 
•	Pandas   – library used for data manipulation and analysis 
•	MySQL connector – module needed for Python to access database from MySQL  
 
2. Frontend: 
 
•	Streamlit – a simple library  used for creating web apps and acts as an interface 
Data of Employees:- 
-	A dummy data of Employees’ working in a fictitious Company  is created using  
Microsoft Excel and MySQL Workbench 
-	This helps to store a large amount of details that include both personal and official information
  
(C) FEATURES:-
1. Login Page:
- Login page will be displayed in the home screen of the app
- It can be logged in by both Admin as well as Employees
- Credentials are provided in Login Excel Sheet as Admin_Login and Emp_Login.
  
2. Employee’s info
 Display 
 
	To view the employees’ info as personal or professional or both 
 
	To view the info based on different branches 
 
 Modify 
 
	The option Modify includes – Adding new ones, Removing existing  and changing (or) updating the existing details like age, salary etc. 
	This is done by signing in using  Admin username and password which is available from the table called login. 
Leave Monitoring:-
	Employees enter the leave details like date, reason/type of leave 
	Admin approves/disapproves 

3. About:-

	This displays information about the Company like Employees count, Departments , performance of employees and comparison of branch.

4. Attendance:-

	Each employee enters the working time or shift start and end time daily that helps in tracking his/her attendance and approve their leave and payroll etc.

5. Payroll:

	With the help of attendance details and rate of pay per hour of each employee, the gross pay , regular pay and overtime pay are given/approved to each provided the attendance is filled properly 

(D) FRONTEND:- 
	In the script folder of the virtual environment created, the command prompt is opened 
1.Streamlit:-
With the help of Streamlit documentation, many features like toggle, button, input functions are used in order to access and display the information according to the user.
2.Plotly:-
By using plotly, charts/graphs  were created and plotted along with pandas command  for viewing the Company’s info i.e., About option in the Home Screen. 

