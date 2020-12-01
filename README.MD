
<h1>Hello, this is the employees accounting app</h1>
<p>

It was created to maintain information about the company's employees. 
<br> 
<br>The base contains information about 
<br><i>'first_name'</i> - employee name, 
<br><i>'last_name'</i> - employee surname,
<br><i>'role'</i> - what position does the person hold, 
<br><i>'description'</i> - a summary of the employee, 
<br><i>'start_work'</i> - when an employee started work, 
<br><i>'end_work'</i> - when an employee finished work, 
<br><i>'wage'</i> - how much does the employee earn
</p>

<p> To work with the database, you need to register and receive a token. After that, the token needs to be inserted into the header and get access. Read more in the <a href='https://documenter.getpostman.com/view/13557088/TVetbkxN'>documentation</a>.</p>

<p>- <a href='https://documenter.getpostman.com/view/13557088/TVetbkxN'>Documentation</a><p>
<p>- <a href='https://crudapitest.herokuapp.com/'>Website</a><p>

<h1>New update 1.3</h1>

<ul>
  <li>Regular Token Authentication is returned back</li>
  <li>Superfluous links removed</li>
  <li>Password validator is replaced into the right place</li>
  <li>Added some changes in API syntax</li>
  <li>Added readonly permission for non authenticated users</li>
</ul> 

<h1>Updates 1.2</h1>

<ul>
  <li>Removed one serializer</li>
  <li>Removed methods in UserViewSet</li>
  <li>Added custom password validation</li>
  <quote>Now password must contain at least eight characters, at least one number and uppercase letter.</quote>
  <li>Removed the word 'Token' from Authorization field in headers</li>
</ul> 

<h1>Updates 1.1</h1>

<ul>
  <li>Views.py - changed to ViewSet</li>
  <li>Removed anti pattern 'import *'</li>
  <li>Removed db from git</li>
  <li>Added Dotenv and sample for variables</li>
  <li>Added PostgreSQL in heroku</li>
  <li>Changed User model to AbstractUser model</li>
  <li>Added some changes in API syntax</li>
  <li>and improved some other stuff...</li>
</ul> 