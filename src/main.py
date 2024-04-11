# coding=utf-8

import subprocess
from flask import Flask, jsonify, redirect, render_template, request, url_for
from .entities.entity import Session, engine, Base
from .entities.Log import Log, LogSchema
from .entities.Cmd import Cmd, CmdSchema
from flask_cors import CORS

import os

app = Flask(__name__)
# Enable method override
app.config['METHOD_OVERRIDE'] = True
# method_override = MethodOverride(app)
CORS(app)

# generate database schema
Base.metadata.create_all(engine)

# app.secret_key = os.getenv("SECRET_KEY") # Set the secret key to the value of the SECRET_KEY environment variable
username = ""
save_path = ("./buckot")
dictname = "abcdefgjklmnopqrstuvwxyz"
command = 'ls -l'
methods = ['GET', 'POST', 'DELETE'] 
# this is like this for now, but it will be changed later
# PUT is for the html endpoints to edit a file. we arent using it yet, but we will later

# def checkOriginalNameInDir(save_path, dictname):
#     import os
#     for file in os.listdir(save_path):
#         if file == dictname:
#             return True
#     return False

# def randomizer(stt):
#     import random
#     import string
#     stt = ''.join(random.choice(string.ascii_lowercase) for i in range(10) + randint)
#     return stt

@app.route('/commands', methods=['POST'])
def add_command():
    # mount object
    posted_command = CmdSchema(only=('name', 'cmd'))\
    .load(request.get_json())
    command = Cmd(**posted_command.data, created_by="HTTP post request")

    # persist command
    session = Session()
    session.add(command)
    session.commit()

    # return created command
    new_command = CmdSchema().dump(command).data;
    session.close()
    return jsonify(new_command), 201

# def find_files_indexNum(path):
#     import subprocess

#     cmd = f'find {path} -type f'
#     result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
#     return result.stdout.split('\n')

# def writeFile():
#     file_content = commandGet()
#     if (checkOriginalNameInDir(save_path, dictname)):
#         dictname = randomizer(dictname) + find_files_indexNum(save_path)
#         print("File already exists! Wrote a new name.") 
#     file_path = "./buckot/" + dictname + ".txt"
    
#     with open(file_path, "w") as file:
#         file.write(file_content)
#         file.close()
#         redirect(url_for('choices'))
#     return "File written successfully!"

@app.route("/")
def hello_world():
    redirect(url_for('login'))

@app.route("/<username>/allCommands")
def getCommands():
    commands = request.args.get('allCommands');
    if commands is None:
        print("No commands found")
        # redirect(url_for('login'))
    return commands

@app.route("/<username>/commandGet")
def commandGet():
    command = request.args.get('commandGet');
    if command is None:
        print("No command found")
        execute_cmd_file(command)
        # redirect(url_for('login'))
    return command

# @app.route("/user/get<username>")
# def get_user():
#     username = request.args.get('username')
#     return "Hello, " + username

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

# @app.route("/<username>/<routecmd>")
# def routeCmd():
#     command = request.args.get('routecmd')
#     if command is None:
#         print("No command found")
#         redirect(url_for('login'))
#     else:
#         execute_cmd_file(command)
#         return command

# @app.route('/cmds')
# def get_cmds():
#     session = Session()
#     cmd_objects = session.query(Cmd).all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        render_template('login.html')
        session['username'] = request.form['username']
        return redirect(url_for('choices'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

# @app.route('/choices')
# def choices():
#     if 'username' in session:
#         return render_template('choices.html')
#     if request.args.get('username') is None:
#         return redirect(url_for('login'))
#     elif request.args.get() == 'username/load-commands': # if the user wants to load commands then after that it goes straight to execution
#         return redirect(url_for('load_commands'))
#     elif request.args.get() == 'username/commandGet': # if the user wants to execute a command it goes straight to execution
#         return redirect(url_for('commandGet'))
#     elif request.args.get() == 'username/writeFile': # if the user wants to save a file that came from the url then after that it goes straight to execution
#         return redirect(url_for('writeFile'))

# def checkLogin(username, password):
#     if (username == None or password == None):
#         return 
#     else:
#         redirect(url_for('login'))

# @app.route("/load-commands")
# def load_commands():
#     # Load saved commands from a file
#     file_path = "./buckot/saved_commands.txt"
#     with open(file_path, "r") as file:
#         saved_commands = file.read().splitlines()

#     return render_template("load_commands.html", commands=saved_commands)

@app.route("/execute-command", methods=["POST"])
def execute_command():
    selected_command = request.form.getlist("selected_command")

    # Execute the selected commands
    for command in selected_command:
        # Execute the command here
        execute_cmd_file(command)
        print("Executing command:", command)

    return "Commands executed successfully!"

def execute_cmd_file(command):
    cons = subprocess
    cons.run('gnome-terminal -- bash -c ' + command)
    output = cons.getoutput(command.cmd)
    check = cons.check_call()
    checkII = subprocess.CompletedProcess(cons)
    if check == 0:
        return(output + '/n' + check + '/n' + checkII)
    else:
        return("Console needs user input " + output + '/n' + check + '/n' + checkII)

# delete_cmd_file = lambda command: os.remove(f"./buckot/{command}.txt")

# def retOutputWithResponce():
#     cons = subprocess
#     cons.check_call

# @app.route("/delete-command", methods=["DELETE"])
# def delete_command():
#     selected_command = request.form.getlist("selected_command")

#     # Delete the selected commands
#     for command in selected_command:
#         # Delete the command here
#         delete_cmd_file(command)
#         print("Deleting command:", command)
#         return "Commands deleted successfully!"

#     # war weapons ready

# # start session
session = Session()

# check for existing data
Cmds = session.query(Cmd).all()
Logs = session.query(Log).all()

if len(Logs) == 0:
    # create and persist mock Cmd
    python_Log = LogSchema(only=('title', 'description'))\
        .load(request.get_json)
    session.add(python_Log)
    session.commit()
    session.close()

if len(Cmds) == 0:
    # create and persist mock Cmd
    python_Cmd = CmdSchema(only=('name', 'cmd'))\
        .load(request.get_json)
    session.add(python_Cmd)
    session.commit()
    session.close()

    # reload Cmds
    Cmds = session.query(Cmd).all()
    Logs = session.query(Log).all()
# show existing Cmds
print('### Cmds:')
for Cmd in Cmds:
    print(f'({Cmd.id}) {Cmd.name} - {Cmd.cmd}')

print('### Logs:')
for Log in Logs:
    print(f'({Log.id}) {Log.title} - {Log.description}')