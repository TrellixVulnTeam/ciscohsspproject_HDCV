from flask import Flask

app = Flask(__name__)

@app.route("/") # root path - URL path component 
def index():
    # what the user sees when the page is loaded
    return "Hello World!"

@app.route("/example.html")
def example():
    f = open('example.html', 'r')
    html = f.read()
    f.close()
    return html

'''
requirements.txt specifies dependencies that need to be installed by web server
app.yaml is additional setup - runtime, env variables, static content, etc
'''

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)