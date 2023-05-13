from compliment import app, render_template, request
import random

@app.route('/', methods=['GET', 'POST'])
def index():
    line = ''  # Initialize line with a default value
    if request.method == "POST":
        userTrigger = True
        fileObject = open("compliments.txt", "r")
        line = random.choice(fileObject.readlines())
    else:
        userTrigger = False
    return render_template('compliment.html', line=line, userTrigger=userTrigger)
