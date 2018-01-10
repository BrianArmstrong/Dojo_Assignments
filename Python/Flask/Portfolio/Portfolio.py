from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def main():
	return render_template("Portfolio.html")
@app.route('/projects')
def main2():
	return render_template("projects.html")
# @app.route('/about')
app.run(debug=True)