#What Are Frameworks In Python?
#A *framework* is a collection of modules or packages which helps in writing web application
# While working on frameworks in python we don’t have to worry about the low level details such as protocols, sockets or thread management.
#Frameworks make the life of web developers easier by giving them a structure for app development. 
# They provide common patterns in a web application that are fast, reliable and easily maintainable.
# *Flask* is a web framework. This means flask provides you with tools, libraries and technologies that allow you to build a web application. 
# This web application can be some web pages, a blog, a wiki or go as big as a web-based calendar application or a commercial website.

# use python -m venv venv to create a virtual environment in windows.
#use python3-m venv venv to create a virtual environment in mac.
# In Linux and mac you'll have to run a command sudo apt-get install python3.8-venv to install the environment files.

#So here using flask we are creating a web app. for this it is just creating a route using hello World function what does hello World function is returning it is returning a hello world world so when this app route will be called the function will be called which will return hello world word
#  you can return any other word as well.

# https://learning.postman.com/docs/getting-started/sending-the-first-request/

from flask import Flask 
app=Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "I am Sushmita"

@app.route("/contact")
def about2():
    return "My no. is 12345"

if(__name__ == "__main__"):
    app.run(debug=True)

