from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def root():
    return render_template('root.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')


if __name__ =="__main__":
    app.run(host='0.0.0.0',port=5000 )
