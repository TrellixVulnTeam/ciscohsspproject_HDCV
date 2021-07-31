# Cisco High School Shadow Program Project

---

## What this app does

This is a Python network visualization *web application*. The default page simply displays 'Hello World.' However, given a specific URL, the app will route you to a simple and interactive network topology map that displays router info and connections.

---

## Requirements

There are none. Python 3.8 and all used libraries are installed in the virtual environment (venv) folder.

---

## How to run the app

1. Clone this GitHub repository.
2. Open your computer's terminal or command line and navigate to where the repo was downloaded and into the 'ciscohsspproject' folder.
3. If you are on MacOS or another Unix-based operating system, run `source venv/bin/activate`. If you are on the Windows operating system, run `venv\Scripts\activate.bat`. This will activate the virtual environment.
4. Run `python3 main.py`.
5. Open your web browser and enter the URL **127.0.0.1:8080**. You should see a web page with 'Hello World' on it.
6. Enter the same URL as step 4, but add **/topology.html** (127.0.0.1:8080/topology.html). You should see the interactive network topology on the web page.
7. When you're done, go back to your terminal and type `Ctrl`+`C`. The program will then stop running.
8. Finally, enter `deactivate` to exit the virtual environment.

If you want to use this program again, repeat steps 2-8.

---

## Brief functionality overview

`main.py` creates a web app using Flask and displays "Hello World!" when you open the local URL. If you add a '/topology.html' to the URL, the file `topology.html` is created and displayed–– an interactive network topology graph.

`vis_network.py` accesses a data file from the data folder and creates a network topology graph using the NetworkX and PyVis modules, and then stores it in an html file. `main.py` accesses the html file and displays it.

`venv` is a virtual environment for testing the app.

Comments are included in the code. Feel free to read through!

---