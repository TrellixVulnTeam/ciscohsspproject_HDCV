from flask import Flask
import os
import vis_network as vn

app = Flask(__name__)

@app.route("/") # root path - URL path component 
def index():
    # what the user sees when the page is loaded
    return "Hello World!"

# example data found online from a tutorial, csv format
@app.route("/example.html")
def example():
    for folder, sub_folders, files in os.walk(vn.DATA_FOLDER):
        if 'example.html' not in files:
            vn.createHTML(vn.EXAMPLE_PATH)

    f = open('example.html', 'r')
    html = f.read()
    f.close()
    return html

# data given by mentor, json format
@app.route("/topology.html")
def topology():
    for folder, sub_folders, files in os.walk(vn.DATA_FOLDER):
        if 'topology.html' not in files:
            vn.createHTML(vn.DATA_PATH)

    f = open('topology.html', 'r')
    html = f.read()
    f.close()
    return html

'''
requirements.txt specifies dependencies that need to be installed by web server
app.yaml is additional setup - runtime, env variables, static content, etc
'''

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)