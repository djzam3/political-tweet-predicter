from flask import Flask, request, render_template
import interfaceWebsite as iw

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
	if request.method == 'POST':
		handle = request.form
		n = handle['twiterHandle'] #get name from input
		posts = iw.grabTweets(n)
		if (posts):
			return render_template('hello.html', posts=posts, full=True, twitHandle=n) #able to obtain tweets
		else:
			return render_template('hello.html', posts=posts, full=False, twitHandle=n) #unable to obtain tweets
	else:
		return render_template('hello.html', posts=None, full=False, twitHandle=False)
