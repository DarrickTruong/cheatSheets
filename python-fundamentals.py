# Bootstrap and CSS 
{% load static %}
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="{% static 'app_name/css/style.css' %}">    
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>   
<script src="{% static 'app_name/js/script.js' %}"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

Datetime conversion
# Remember this and you didn't need to get confused in datetime conversion again.
String to datetime object = strptime

datetime object to other formats = strftime






# print
name = "Zen"
print("My name is", name)

# concatenation
name = "Zen"
print("My name is " + name)


# F-Strings (Literal String Interpolation) -- print string with integer in string
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")


first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.


# % formatting
# Here is an even older method of string interpolation that you may come across when troubleshooting or researching, 
# so you should know about it. Rather than curly braces, the % symbol is used to indicate a placeholder, a %s for a 
# string and %d for a number.
# After the string, a single % separates the string to be interpolated from the values to be inserted into the string,
#  like so:
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27


# string.upper()
cheese = "i like cheese".upper()
print(cheese)









#Primitive Data Types

# Boolean Values - Assesses the truth value of something. It has only two values: True and False (note the uppercase T and F)
is_hungry = True
has_freckles = False

# Numbers - Integers (whole numbers), floating point numbers (commonly known as decimal numbers), and complex numbers
age = 35 # storing an int
weight = 160.57 # storing a float

# Strings - literal text
name = "Joe Blue"



#Composite Types

# Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. 
# Tuples can contain mixed data types.
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

# Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. 
# When you're ready, you can find more built-in dictionary methods here -- 
# https://www.w3schools.com/python/python_ref_dictionary.asp
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

# Type Casting or Explicit Type Conversion
print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

# type function
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>



# Interate Dictionaries
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)











#Loops

# For Loops with Range
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2


# For Loops through Lists
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz


# For Loops through Dictionaries
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language


my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python


# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)



# While Loops -- While loops are another way of looping while a certain condition is true.
# while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

count = 0
while count < 5:
    print("looping - ", count)
    count += 1


#Else
# There are certain conditions that we give for every loop that we have, but what if the condition was not met and 
# we still would like to do something if that happens? 
# We can then use an else statement with our while loop. Yes, that is right, else in a loop.
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")


# Loop Control

# Break
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r


# Continue
# The continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, 
# or skips, all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop.
# The continue statement is very useful when you want to skip specific iteration(s), but still keep looping to the end.
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1










#Functions
# Wait, but what's the difference between a parameter and an argument? These two words get mixed up a lot in programming. 
# In this example 'name' is a parameter while "Michael", "Anna", and "Eli", are arguments. We define parameters. We pass 
# in arguments into functions.
def say_hi(name):
    print("Hi, " + name)
# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')


# Default Parameters
def beCheerful(name='', repeat=2):		# set defaults when declaring the parameters
	print(f"good morning {name}\n" * repeat)
beCheerful()				# output: good morning (repeated on 2 lines)
beCheerful("tim")		        # output: good morning tim (repeated on 2 lines)
beCheerful(name="john")			# output: good morning john (repeated on 2 lines)
beCheerful(repeat=6)			# output: good morning (repeated on 6 lines)
beCheerful(name="michael", repeat=5)	# output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
beCheerful(repeat=3, name="kb")		# output: good morning kb (repeated on 3 lines)



# Python Swap
# python code below!
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]









# Object Based Programming (OOP)

# class
With OOP, we are able to create our own custom data types!
A class is like a blueprint that ensures the consistent creation of instances.

Here's the syntax for creating a class that we want to call User:
class User:
    pass    # we'll fill this in shortly

And here's how we create a new instance of our class:
michael = User()
anna = User()


# attributes
Attributes: Characteristics shared by all instances of the class type.
With the __init__ method's parameters, we indicate what needs to be provided (i.e. arguments) when the class is instantiated. 
(self is always passed in implicitly.)
class User:		# declare a class and give it name User
    def __init__(self):
        self.name =copy "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance 
The first parameter of every method within a class will be self, and the class's attribute names are also indicated by self.. 
We'll talk more about self later, but for now just follow this pattern: self.<<attribute_name_of_your_choosing>>.
Then to instantiate a couple of new users:

guido = User()
monty = User()

If we want to access our instance's attributes, we can refer to them from our instances by name:
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

We can also set the values for our instance's attributes:
guido.name = "Guido"
monty.name = "Monty"

With the __init__ method's parameters, we indicate what needs to be provided (i.e. arguments) when the class is instantiated. 
(self is always passed in implicitly.)
class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
Now when we want to create users, we must send in the 2 required arguments:
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python



# methods
Methods: Actions that an object can perform. A user, for example, should be able to make a deposit or a withdrawal, 
or maybe send money to another user.

guido.make_deposit(100)
To be able to call on this method, it needs to exist. Let's make it!
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

    # adding the deposit method

# instance and objects are the same
# public/private/protected



# Creating Your Own Modules
# Writing your own Python modules is very simple. To create a module, we first create a new .py file with the module 
# name in the same directory as the file that will import the module. Then we import it using the import command and 
# the Python file name (without the .py extension)




# Test-Driven Development

# Test-Driven Development (TDD) is a method of developing software that provides a structure to write good code 
# and ensure an end product that has been tested in each phase of development. The model of TDD is as follows:
# 1.Design a feature
# 2.Write a test that fails (RED). This test will model a specific behavior or outcome in your code
# 3.Write the code that will make your feature work and pass the test (GREEN).
# 4.Refactor your code and improve your design
#  --Also make sure that prior tests still pass!
# 5.Move to the next feature and repeat the process
# As you may have noticed, TDD focuses on testing throughout the entire development process rather than the beginning. 
# Without integrated tests, the software will die as it becomes more complex and ugly because developers don't touch code 
# for fear of breaking it.

# The Benefits
# TDD will allow us to develop in such a way that:
# We have a clear picture of how features should work before building it out
# We can develop without the fear of breaking our apps
# We can encourage improvement and refactoring of the codebase which will lead to cleaner code


# Multiple Arguments
# Splat Operator *
def varargs(arg1, *args):
    print("Got ", arg1, " and ", args)
varargs("one") 			# output: Got one and ()
varargs("one", "two") 	        # output: Got one and ('two',)
varargs("one", "two", "three")  # output: Got one and ('two', 'three')






# Flask 
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id



# Dynamic 
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!
if __name__=="__main__":
    app.run(debug=True)
<h3>My Flask Template</h3>
<p>Phrase: {{ phrase }}</p>
<p>Times: {{ times }}</p>
      
{% for x in range(0,times): %}
    <p>{{ phrase }}</p>
{% endfor %}
      
{% if phrase == "hello" %}
  <p>The phrase says hello</p>
{% endif %}

# flask IN HTML file
<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style.css') }}">
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
<!-- linking an image -->
<body>
    <img src="{% static 'app_name/images/image.jpg' %}" >
</body>


# HTML FORM Submission

from flask import Flask, render_template
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

<h1>Index Page</h1>
<h3>Create a User</h3>
    <form action='/users' method='post'>
    Name: <input type='text' name='name'>
    Email: <input type='text' name='email'>
    <input type='submit' value='create user'>
    </form>


# --  action attribute
# This is the route that will process the form (not the one that shows the form--that's "/"). We'll set this up shortly.

# --  method attribute
# Our options are GET and POST; most likely, we'll want this to be a POST request (but if you don't set it, the default is GET)

# --  input elements
# These are the parts of the form that actually gather data from the user. Check here for type options. Also check here for 
# other form elements like select (dropdowns) and textarea. Each element should have a unique value for its name attribute.

# --  a way to submit the form
# This can either be <input type='submit'> or <button>Submit</button>, but NOT <input type='button'>.

from flask import Flask, render_template, request, redirect # added request
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)

--  Specifying Allowed Methods: methods=['POST']
# If we don't provide a value for methods, only GET requests are allowed. Everything we've done up to this point have been 
# GET requests, so it has been okay, but since we want this method to handle POST requests, we must specify that. 
# Notice it is a list--it's possible to provide more than one value.

--  Accessing Data: request.form['name_of_input']
# The name we gave to each HTML input was significant. On the server-side, we can access data that was input into a field 
# from a user through the request.form dictionary by providing the name of the input as the key. To see what's in your 
# request object, try printing request.form.
# Lastly, note that the type of anything that comes in through request.form will be a "string" no matter what. If you 
# want that value to be identified as an actual number you'll have to type cast it.

 -- Session 
# With session, the user can have a conversation of sorts with a website, where a user makes decisions that can be 
# tracked so the server can create a more cohesive user experience. In a given process (HTTP request/response), 
# we can manage data (search terms and search results for instance) that outlives the process that generated it. 
# This data is called state. 
    
State allows our site to "know" a lot of useful information, like:
# -- Whether there is a user logged in
# -- Who the current user is
# -- What links a user has viewed previously

A Note on Cookies
# You've probably heard of the term cookies before. Some frameworks, including Flask, use cookies to store session data. 
# Flask uses secure hashing of session data to send a packet of information from server to client. This packet is known as a cookie. 
# Once a client's browser has received this cookie, it writes the information contained in it to a small file on their hard drive.

# While hashed, cookies are not incredibly secure, so don't save anything private in them.

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

#  -- Hidden Inputs
<form method="post" action="/process">
    <input type="hidden" name="which_form" value="register">
    <input type="text" name="first_name">
    <input type="text" name="last_name">
    <input type="text" name="email">
    <input type="password" name="password">
    <input type="submit" value="Register">
</form>
<form method="post" action="/process">
    <input type="hidden" name="which_form" value="login">
    <input type="text" name="email">
    <input type="password" name="password">
    <input type="submit" value="Login">
</form>



# Creating a python virtual environment
 Mac/Linux: | python3 -m venv py3Env   
 Windows:   | python -m venv py3Env                 

# Start virtual environment/ python environment / deactivate environment
Mac/Linux: | source py3Env/bin/activate     
# To deactivate:
deactivate
------------------------------------------------------------------
| Windows command prompt : | call py3Env\Scripts\activate       
------------------------------------------------------------------
| Windows git bash : | source py3Env/Scripts/activate         


#  -- Django

# Creating a Django Project
--- *** 1. with Django Virtual environment activated navigate to folder where you want to store/save project
(djangoPy3Env) > cd python/django                       # navigate to django folder      
(djangoPy3Env) > django-admin startproject {{your_project_name_here}}

(djangoPy3Env) > cd your_project_name_here                            # inside folder of project
(djangoPy3Env) > python manage.py runserver                         #start server

--- *** 2. Create APPS Folder within project folder
(djangoPy3Env) your_project_name_here> mkdir apps            # create apps folder
# // THIS STEP CAN ALSO BE DONE BY MANUALLY CREATING A FILE USING A USER INTERFACE OF SOME KIND, 
#     SUCH AS THE FILE CREATION BUTTON IN VSCODE

--- *** 3. For every app we want to add to our project, we'll do the following:
--- *** 3a. Now navigate to the apps folder, we'll use the CLI again 
to create a Django app, with a name of our choosing:

(djangoPy3Env) apps> python ../manage.py startapp {{your_app_name_here}}   --- *** inside the apps folder...
# The apps in a project CANNOT have the same name as the project.


--- 3b. Navigate into the newly created app folder and create an empty file called urls.py. 
#We'll add to this empty file later.
(djangoPy3Env) apps> cd app_name
(djangoPy3Env) your_app_name_here> touch urls.py	// Mac or Git Bash users
#                     OR
# (djangoPy3Env) your_app_name_here> nul>urls.py	// Windows command prompt users; ignore Access Denied warning
# // THIS STEP CAN ALSO BE DONE BY MANUALLY CREATING A FILE USING A USER INTERFACE OF SOME KIND, 
# SUCH AS THE FILE CREATION BUTTON IN VSCODE 

--- 3c. In the VS Code/text editor, find the settings.py file. It should be in a folder with the same name as our project. 
Find the variable INSTALLED_APPS, and let's add our newly created app:

your_project_name_here/your_project_name_here/settings.py

   INSTALLED_APPS = [
       'apps.your_app_name_here', # added this line. Don't forget the comma!!
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',If you see valid patterns in the file then the issue is probably caused by a circular import.

   ]    # the trailing comma after the last item in a list, tuple, or dictionary is commonly accepted in Python

-- 4. For these next few steps, we are creating the route "/" to be associated with a specific function. 
# Trust for now--we'll break this down in greater detail in the next tab. In the project level urls.py file, 
# add a URL pattern for your new app. (You can delete the current admin pattern, or just ignore it for now):

# your_project_name_here/your_project_name_here/urls.py
from django.conf.urls import url, include
urlpatterns = [
    url(r'^', include('apps.{your_app_name_here}.urls')),
]

-- 5. Then, in our app, for every route we want to add, we'll do the following:
-- 5a. In the app level urls.py file, add a URL pattern:
# your_project_name_here/apps/your_app_name_here/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]

-- 5b. And then actually put a function called index in our app's views.py file:
# your_project_name_here/apps/your_app_name_here/views.py
from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
    # or
    return render(request, "app_name/index.html")


-- 6. Start/Test the django server
(djangoPy3Env) your_project_name_here> python manage.py runserver


# ** Note: Do not manually change the name of any of your folders after creation! **

# -- Regular expression (aka regex) patterns
^ - indicates a matching string starts with whatever follows this character
Example: '^a' matches 'anna' but not 'banana'
$ - indicates a matching string ends with whatever precedes this character
Example: 'a$' matches 'anna' and 'banana' but not 'fan'
Example: '^a$' matches only the letter 'a'

#  -- Capture variables in URL Django
# We'll use a regular expression group in the app's urls.py file, and then take the name(s) specified 
# in the groups as parameters in the associated functions. A few basic regular expression patterns that will 
# come in handy include:

[] - matches any value in a range - Regex
Example: '[a-z]' matches 'abc' and 'xyz' but not 'b7' or 'ABC'
\d+ - matches digits with at least one digit
Example: '\d+' matches '8' and '876' but not '5c' or ''
\w+ - matches a string with at least one character (including numbers, excluding special characters)
Example: '\w+' matches '8' and 'abc123' but not 'a!' or ''
{n} - matches n number of repetitions of the preceding pattern
Example: '[0-9]{2}' matches '36' but not '876' or '2'

# -- Here are a few examples, to demonstrate the syntax:

# -- some_project/apps/some_app/urls.py
urlpatterns = [
        url(r'^bears$', views.one_method),                        # would only match localhost:8000/bears
        url(r'^bears/(?P<my_val>\d+)$', views.another_method),    # would match localhost:8000/bears/23copy
        url(r'^bears/(?P<name>\w+)/poke$', views.yet_another),    # would match localhost:8000/bears/pooh/poke
    	url(r'^(?P<id>[0-9]+)/(?P<color>\w+)$', views.one_more),  # would match localhost:8000/17/bro

# The corresponding functions would then look like this:

# some_project/apps/some_app/views.py
def one_method(request):                # no values passed via URL
    pass                                
def another_method(request, my_val):	# my_val would be a number from the URL
    pass                                # given the example above, my_val would be 23
def yet_another(request, name):	        # name would be a string from the URL
    pass                                # given the example above, name would be 'pooh'
def one_more(request, id, color): 	# id would be a number, and color a string from the URL
    pass                                # given the example above, id would be 17 and color would be 'brown'



# -- Render template/static files in django views

# project_name/apps/app_name/templates/app_name/index.html
from django.shortcuts import render	# notice the import!
def index(request):
    return render(request, "app_name/index.html")

# project_name/apps/app_name/static/app_name/css/style.css

<!DOCTYPE html>
  <html>
    <head>
        <meta charset="utf-8">
        <title>Index</title>
        {% load static %}
        <link rel="stylesheet" href="{% static 'app_name/css/style.css' %}">    
        <script src="{% static 'app_name/js/script.js' %}"></script>
    </head>
    <body>
        <img src="{% static 'app_name/images/image.jpg' %}" />
    </body>




# ---  DJANGO GET vs. POST Requests 

# -- in views
from django.shortcuts import render, redirect
def some_function(request):
    if request.method == "GET":
    	print("a GET request is being made to this route")
    	return render(request, "some_app/some_template.html")
    if request.method == "POST":
        print("a POST request is being made to this route")
    	return redirect("/")

# -- Submitting Form Data
from django.shortcuts import render, redirect
def some_function(request):
    if request.method == "GET":           #for a form that is a GET request
    	print(request.GET)
    if request.method == "POST":          #for a form that is a POST request
        print(request.POST)

# -- One more important thing to note is that any forms being submitted as POST requests must include a CSRF token. 
# This token is used to prevent cross-site request forgery, a malicious kind of attack where a hacker can pretend 
# to be another user and submit data to a site that recognizes that user.

# In HTML - add CSRF token for POST request
<form action="/some_route" method="post">
  {% csrf_token %}
  <p>Field One: <input name="one" type="text"></p>
  <p>Field Two: <input name="two" type="text"></p>
  <button type="submit">Submit</button>
</form>

# EXAMPLE - POST request
from django.shortcuts import render, redirect
def some_function(request):
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
    	val_from_field_two = request.POST["two"]



#  --- DJANGO Sessions
first run migrate command in terminal
(djangoPy3Env) project_name> python manage.py migrate

To use session, we can refer to it in our views.py file. Just as it was in Flask, session is a dictionary 
to which we can add and retrieve values via keys, like so:

# some_project/apps/some_app/views.py
def some_function(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100

# We can also access session directly in our Django templates. Remember, though, that Django templates do not 
# process square brackets, so we'll use dot notation instead
<p>Name in session is: {{request.session.name}}</p>

# -- Useful session methods:
request.session['key']
# This will retrieve (get) the value associated with 'key'

request.session['key'] = 'value'
# Set the value that will be stored by 'key' to 'value'

'key' in request.session
# Returns a boolean of whether a key is in session or not

{{ request.session.name }}
# Use dot notation (.) to access request.session keys from templates since square brackets ([]) aren’t allowed there

# Delete Session
del request.session['key']
# Deletes a session key if it exists, throws a KeyError if it doesn’t. Use along with try and except 
# since it's better to ask for forgiveness than permission


#  --- DJANGO ORM 

# Models - Django Models
models.py
from django.db import models    
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
            return f"<Wizard object: {self.name} {self.house} {self.pet} {self.year} ({self.id})>"

Model Fields
CharField(max_length=45)
# Any text that a user may enter. This has one required parameter, max_length, that is the maximum length of text that can be saved.
TextField()
# Like a CharField, but with no maximum length. Your user could copy the entire text of the Harry Potter series 
into the field and it would save in the database correctly.
IntegerField()
# Holds an integer value
FloatField()
# Holds a float value; this is good for numbers with potentially varying numbers of decimal places
DecimalField()
# This is a good field for a number with a fixed number of decimal places, like currency. There are 2 required parameters: 
# max_digits refers to the total number of digits (before and after the decimal place), and decimal_places refers to how many decimal places.
BooleanField
# Holds a boolean value
DateTimeField
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
# Used for a combination of a specific date and time. This field can take two very useful optional parameters. 
# Setting the auto_now_add argument to True adds the current date/time when an object is created. Setting auto_now=True 
# automatically updates any time the object is modified.
ForeignKeyField
ManyToManyField

Make Migrations/Migrate
# Makemigrations is a kind of staging. When this command runs, Django looks through all our code, finds any changes we made to our 
# models that will affect the database, and then formulates the correct Python code to move on to the next step. Note that if this step has errors, 
# the next step will not work, so you will need to fix any errors before you can move on to migrating.
  > python manage.py makemigrations
  > python manage.py migrate
# --- Never delete migration files and always makemigrations and migrate anytime you change something in your models.py files – 
# that's what updates the actual database so it reflects what's in your models.
# --- For now we are going to be using SQLite, a SQL database that comes pre-packaged with Django. It is best used in a development 
# environment because it is stored as local memory in a file and as such is very fast. It is generally not recommended for use once our application 
# is ready for production. Luckily, changing what kind of database we are using is quite simple. In the deployment section, we'll learn how to switch to a MySQL database.
# --- Django ORM models and queries will always be the same no matter which database we are using.

# --- Django Shell/ipython
To use the shell, we'll run the following command in our terminal from our project's root directory (where our manage.py file is located):
> python manage.py shell

Once we're in the shell, we can access all of our functions and classes in our files. To do so, we just need to specify which modules (files) we need. 
# Since we are interested specifically in working with our models, let's import them:
>>> from apps.your_app_name_here.models import *
# We will need to run this import every time we start the shell.

 --- ORM CRUD Commands (Creating, Reading, Updating, and Deleting) 
-Creating a new record
ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)

# Reading existing records
Methods that return a single instance of a class
---ClassName.objects.first() - gets the first record in the table
---ClassName.objects.last() - gets the last record in the table
---ClassName.objects.get(id=1) - gets the record in the table with the specified id
This method will throw an error unless only and exactly one record matches the query

# Updating an existing record
variable = ClassName.objects.get(id=1)
variable.field_name = "some new value for field_name"
variable.save()

# Deleting an existing record
c = ClassName.objects.get(id=1)
c.delete()

# Displaying records/ Printing records
ClassName.objects.get(id=1).__dict__ - shows all the values of a single record as a dictionary
ClassName.objects.all().values() - shows all the values of a QuerySet (i.e. multiple instances)

# Ordering records
ClassName.objects.all().order_by("field_name") - orders by field provided, ascending
ClassName.objects.all().order_by("-field_name") - orders by field provided, descending

# CREATING
To add a new record to a table:
1. --- ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)
# SQL Equivalent: "INSERT INTO tablename (field1, field2) VALUES ('value for field1', 'value for field2');"

# The create method returns an instance of the model with the values that were just added. This means that if we wanted to do 
# something with the instance after creating in our database, we could set a variable and use it like so:
newly_created_movie = Movie.objects.create(title="The Princess Bride",description="the best movie ever",release_date="1987-09-25",duration=98)
print(newly_created_movie.id)	# view the new movie's id

# To add a new row to database/New instance
2. --- newly_created_movie = Movie(title="The Princess Bride",description="the best movie ever",release_date="1987-09-25",duration=98)
newly_created_movie.save()


# READING
There are several ways that we might want to retrieve records from the database.

# Multiple Records
There are several different methods that will return multiple records (or lists of instances).

# All
To get all the rows from a given table:

ClassName.objects.all()
# SQL Equivalent: "SELECT * FROM tablename;"
# The all method returns a list (technically a QuerySet) of instances of the model.
all_movies = Movie.objects.all()


# Filter (WHERE) Select More than one / multiple records
To specify criteria for retrieving rows from a given table:

ClassName.objects.filter(field1="value to match", field2="another value", etc.)
# SQL Equivalent: "SELECT * FROM tablename WHERE field='value to match' AND field2='another value';"
# The filter method also returns a list (technically a QuerySet) of instances of the model.  
some_movies = Movie.objects.filter(release_date='2018-11-16')

# Exclude (WHERE NOT)
To specify criteria for filtering out records to retrieve:

ClassName.objects.exclude(field1="value to match", field2="another value", etc.)
# SQL Equivalent: "SELECT * FROM tablename WHERE NOT (field='value to match' AND field2='another value');"
# The exclude method also returns a list (technically a QuerySet) of instances of the model.  
other_movies = Movie.objects.exclude(release_date='2018-11-16')

# When we have a list of instances, we can iterate through that list and view each instance and its values:
for m in all_movies:    # m represents each movie instance as we iterate through the list
    print(m.title)	# that means m has all the properties of the Movie class, including title, release_date, etc.


# --- Single Records
There are also several different methods that will return a single instance of a class.

# Get
To get a specific row from the table, specify a field and value.

ClassName.objects.get(field1="unique value")
# SQL Equivalent: "SELECT * FROM tablename WHERE field1='unique value' LIMIT 1;"
# The get method returns a single instance of the model.
one_movie = Movie.objects.get(id=7)

# If our specified value(s) finds no matching results or more than one matching result from the database, we will get an error. 
# This is why we should really only use fields that we know will be unique, with values that we are certain are in the database. 
# For this reason, id is the most common field to use with get.


# First
To get the first row from the table:

ClassName.objects.first()
# SQL Equivalent: "SELECT * FROM tablename ORDER BY id LIMIT 1;"
# The first method returns a single instance of the model. If no order is specified before calling the first method, the data is ordered by the primary key.
first_movie = Movie.objects.first()


# Last
To get the last row from the table:

ClassName.objects.last()
# SQL Equivalent: "SELECT * FROM tablename ORDER BY id DESC LIMIT 1;"
# The last method returns a single instance of the model. Again, if no order is specified before calling the last method, the data is ordered by the primary key.
last_movie = Movie.objects.last()
# When we are working with a single instance, we can access any of the instance's values with dot notation. 
# For example:
print("Movie 7", one_movie.title)
print("First movie", first_movie.release_date)
print("Last movie", last_movie.description)

# UPDATING
In order to update an existing record, we first need to obtain the instance of the record we want to modify and 
then use the save method to commit those changes to the database. 
# For example:
movie_to_update = Movie.objects.get(id=42)	# let's retrieve a single movie,
movie_to_update.description = "the answer to the universe"	# update one/some of its field values
movie_to_update.title = "The Hitchhiker's Guide to the Galaxy"
movie_to_update.save()	# then make sure all changes to the existing record get saved to the database

# DELETING
In order to delete an existing record, we again need to obtain the instance of the record and then use the delete method. 
# For example:
movie_to_delete = Movie.objects.get(id=2)	# let's retrieve a single movie,
movie_to_delete.delete()	# and then delete it

# Helpful Tip/Printing Objects
You've probably noticed in the shell that printing whole objects just results in something like <Movie Object (1)>, 
# which is not particularly helpful. To change how our models display, we can override the __repr__ method in the class.
#  This is pretty handy and shows how we can leverage some of Python's magic methods to make our lives easier.
 class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()
    def __repr__(self):
        return f"<Wizard object: {self.name} {self.house} {self.pet} {self.year} ({self.id})>"

OPTIONAL: iPython
Also, if you would like, you could also install iPython (pip install ipython). This replaces the default shell with a prettier one 
(TAB indent works, line numbers, syntax highlighting, etc).



# --- Queries in view.py and templates Django
apps/my_app/views.py 
# other imports
from .models import Movie
# show all of the data from a table
def index(request):
    context = {
    	"all_the_movies": Movie.objects.all()
    }
    return render(request, "my_app/index.html", context)

apps/my_app/templates/my_app/index.html
    <h1>All Movies</h1>
    <ul>
    {% for movie in all_the_movies %}
        <li>{{ movie.title }}</li>
    {% endfor %}
    </ul>



Errors with changing models after initial creation
# You are trying to add a non-nullable field ... (the database needs something to populate existing row)
# To make sure our existing data maintains integrity, we need to provide a value for this new field for any 
# existing rows of data.
Option 1 - have the shell add a default for you
# provide a one-off default now for prexisting rows/instances. 
# the value must match the field type
for DateField or DateTimeField add timezone.now

Option 2 - Add a default in manually in the models.py
# Set a default or make nullable for prexisting rows/instances
age = models.IntegerField(default=200)	# if no age is entered for a new/existing, age will be set to 200
age = models.IntegerField(null=True)	# if no age is provided, the field will remain empty

Option 3 - Starting the database over from scratch
# To do this, you will need to delete the following files/directories:
db.sqlite3
your_app_name/migrations
your_app_name/__pycache__
# After you delete these, you will need to re-run your makemigrations and migrate commands. When you make your
# migrations, you will need to include the app name:
python manage.py makemigrations your_app_name
python manage.py migrate



One to Many Relationships - DJANGO Models
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

Creating One to Many relation
# Remember that by default, all fields are required. The created_at and updated_at fields will be populated automatically,
#  but the other two fields must be set upon creation. Since title is a CharField, we can pass it a string; but the author 
#  field is expecting an instance of the Author class. So to create a record that has this foreign key relationship, we 
#  first need to have an instance of an Author, and then we can pass it like we have any other field:
this_author = Author.objects.get(id=2)	# get an instance of an Author
my_book = Book.objects.create(title="Little Women", author=this_author)	# set the retrieved author as the author of a new book
# or in one line...
my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))


Reading One to Many - Joining happens automatically
this_author = Author.objects.get(id=2)
books = Book.objects.filter(author=this_author)
# one-line version:
books = Book.objects.filter(author=Author.objects.get(id=2))


Reverse Lookup with related_name
# When we create a relationship in a Django model, Django places a field in the corresponding table, which we can access by 
# the related_name we provide. This means that when we added the author field in our Book class, Django has also placed a field 
# in the Author class that holds information about all of a given author's books. To keep track of this, it may help to add that
# field in as a comment so that you remember how to access it.


Many To Many Relationships - DJANGO Models
class Book(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Publisher(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    # Unlike with a ForeignKey, it doesn't matter which model has the ManyToManyField. The model 
    # would still work if the Book model has a field named publishers instead (though we would need 
    # to put the Publisher class first).
# --- Adding a relationship between two existing records is simple:
this_book = Book.objects.get(id=4)	# retrieve an instance of a book
this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher
# 2 options that do the same thing:
this_publisher.books.add(this_book)		# add the book to this publisher's list of books
# OR
this_book.publishers.add(this_publisher)	# add the publisher to this book's list of publishers

# --- And to remove a relationship between two existing records:
this_book = Book.objects.get(id=4)	# retrieve an instance of a book
this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher
    
# 2 options that do the same thing:
this_publisher.books.remove(this_book)		# remove the book from this publisher's list of books
# OR
this_book.publishers.remove(this_publisher)	# remove the publisher from this book's list of publishers

The two methods for adding shown above are equivalent because a ManyToManyField is automatically symmetrical. 
That is, by adding a book to a publisher, Django will also automatically add the publisher to the book. 
This means that we can add or look up from the other end without issue.

# Aggregation -- DJANGO Query Aggregation -- https://docs.djangoproject.com/en/2.2/topics/db/aggregation/
from django.db.models import Sum
def checkout(request):
    context = {
        'total_price_all' : Order.objects.all().aggregate(Sum('total_price')),
        'order' : Order.objects.last(),
        'total_quantity' : Order.objects.all().aggregate(Sum('quantity_ordered'))
    }
    return render(request, "store/checkout.html", context)

# in HTML
<body>
    <h3>Thank you for your business!</h3>
    <p>We charged your credit card for ${{order.total_price}}</p>
    <p>You have ordered #{{total_quantity.quantity_ordered__sum}} items so far and spent ${{total_price_all.total_price__sum}} with Amadon.com!</p>
    <p><a href="/">Go Back</a></p>



# --- Form Validations - Django Validations
Form validation is a key component of any back-end developer's arsenal. Validation is more of a logical 
challenge than a whole bunch of new code to learn. Common validation rules include:
# Checking that the data is present
# Making sure the data is in the correct format


--- Example of Form Validations

# Inside your app's models.py file
from __future__ import unicode_literals    #add this line!!!!!!!!!!!!
from django.db import models
# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors
Now to link our BlogManager to our Blog class, we are going to override the objects property 
and have it reference our newly created manager, like so:
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()    # add this line!

Now in our views.py file, we can use Blog.objects.basic_validator(postData):
# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages    #import messages
   
from .models import Blog
def update(request, id):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Blog.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/blog/edit/'+id)
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        blog = Blog.objects.get(id = id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        messages.success(request, "Blog successfully updated")
        # redirect to a success route
        return redirect('/blogs')

# Notice in the code above we are using Django's messages framework. 
There is one more step to get these messages to display on our page. Somewhere in our HTML template 
(the same template that contains the form!), place the following lines of HTML. The errors will display 
wherever you put this, so putting it just above the form is probably a good idea.
In Html on template with form
# Django if statements
{% if messages %}
<ul class="messages">    
    {% for message in messages %}    
        <li {% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>    
    {% endfor %}
</ul>
{% endif %}

 {% if id == session_id  %}
    <a href='/dashboard' class='btn btn-secondary text-white'> Back to dashboard </a>
    {% endif %}

# Django reverse list / reversed for loop
reversed list / reversed for loop
{% for review in reviews reversed %}


# Unique Input
all_shows = Show.objects.all()
for k in all_shows:
    if k.title == request.POST['title']:
        errors['title'] = "This title already exists"
        print('errors title', errors['title'])

# Show NOT in list
def books(request, book_id):
    # print(book_id)
    # print('books with id', Books.objects.get(id=book_id))
    book = Books.objects.get(id=book_id)
    print('authors of book', book.authors.all())
    current_authors = []
    for i in book.authors.all():
        current_authors.append(i.id)
    context = {
        'book_of_id' : Books.objects.get(id=book_id),
        'authors_of_book' : book.authors.all(),
        'authors_to_add' : Authors.objects.exclude(id__in=current_authors),
    }
    return render(request, 'books_authors_app/books.html', context)

Regex Validations
# some_project/apps/some_app/models.py
import re              # the regex module -- import this line
class BlogManager(models.Manager):
    def basic_validator(self, postData):    
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        phone_regex = re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
        website_regex = re.compile(r'^[a-zA-Z]+\.[a-zA-Z0-0.+_-]+\.[a-zA-Z]+\/[a-zA-Z0-0.+_-]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        return errors



# Securing Passwords - Hashing
"one way" encryption
Never store passwords in database

Hashing Algorithm 

Bcrypt
# >>> import bcrypt
# >>> hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
# >>> print(hash1)
# $2b$12$Wdc2qwiP6u0WdQdKwmer7.DMIcY6q76GxvrJgaodnpRDmpP8mwkDa

Note for Django 2+ users: Before saving the hashed password into the database, decode it. If the above line 
were in our registration method, we would save the user with the decoded password: User.objects.create(password=hash1.decode(),
 etc.). (Don't worry: decoding != dehashing)

# Validating a Password
To compare passwords to verify a user, the user input must be hashed with the same salt and compared. If the hashed passwords 
match, then the user is logged in. To do this, we can use the checkpw method. Try it in the shell as shown below:

def validate_login(request):
    user = User.objects.get(email=request.POST['email'])  # hm...is it really a good idea to use the get method here???????
    if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
        print("password match")
    else:
        print("failed password")
# Note: the order of the 2 arguments matters--the first should be the input being tested, and the second is the value
# that has already been hashed.


Password Hashing: Login vs. Registration
# Hashing on Registration
Let's see how some of our code may look when we are creating a user. In the example below, we did not include validations, 
but of course you would validate the user input before adding it to the database.

def register():    
    # include some logic to validate user input before adding them to the database!
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # create the hash    
    print(pw_hash)      # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'    
    # be sure you set up your database so it can store password hashes this long (60 characters)
    # make sure you put the hashed password in the database, not the one from the form!
    User.objects.create(username=request.POST['username'], password=pw_hash) 
    return redirect("/") # never render on a post, always redirect!    

Compare on Login
# Here's how our code may look when a user logs in. We'll need to check the provided password with the hash in the database:
def login():
    # see if the username provided exists in the database
    user = User.objects.filter(username=request.POST['username']) # why are we using filter here instead of get?
    if user: # note that we take advantage of truthiness here: an empty list will return false
        logged_user = user[0] 
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['userid'] = logged_user.id
            # never render on a post, always redirect!
            return redirect('/success')
    # if we didn't find anything in the database by searching by username or if the passwords don't match, 
    # redirect back to a safe route
    return redirect("/")




# openpyxl excel
# in python cli (terminal)

import openpyxl
import os #change directory
openpyxl.__version__ # to get version

os.chdir("your folder directory")

wb = openpyxl.load_workbook("file name here")
wb.sheetnames  #get sheet names
sheet = wb['Sheet name here']


