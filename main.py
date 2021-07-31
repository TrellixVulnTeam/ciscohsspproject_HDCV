from flask import Flask
import os
import vis_network as vn



# create the web app
app = Flask(__name__)



# default web page
# 127.0.0.1:8080/
@app.route("/") # root path
def index():
    # what the user sees when the page is loaded
    return "Hello World!"



# example data found online from a tutorial, csv format
# 127.0.0.1:8080/example.html
@app.route("/example.html")
def example():
    # check if 'example.html' exists (if not, create it)
    for folder, sub_folders, files in os.walk(vn.DATA_FOLDER):
        if 'example.html' not in files:
            vn.createHTML(vn.EXAMPLE_PATH)

    # return html to be displayed on the web page
    f = open('example.html', 'r')
    html = f.read()
    f.close()
    return html



# data given by mentor, json format
# 127.0.0.1:8080/topology.html
@app.route("/topology.html")
def topology():
    # check if 'topology.html' exists (if not, create it)
    for folder, sub_folders, files in os.walk(vn.DATA_FOLDER):
        if 'topology.html' not in files:
            vn.createHTML(vn.DATA_PATH)

    # return html to be displayed on the web page
    f = open('topology.html', 'r')
    html = f.read()
    f.close()
    return html



'''
requirements.txt specifies dependencies that need to be installed by web server
app.yaml is additional setup - runtime, env variables, static content, etc
'''



# run the app locally
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)