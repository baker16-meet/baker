from flask import Flask, render_template, for_url
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("Main.html")

@app.route('/Last')
def Last():
	return render_template("Last.html")

@app.route('/project')
def project():
	return render_template("project.html")


if __name__ == "__main__": 
	app.run() 
