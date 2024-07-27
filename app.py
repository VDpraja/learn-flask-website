from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Bot Discord Simple',
    'language': 'Python',
    'price': '$150 *Include Hosting'
  },
  {
    'id': 2,
    'title': 'Bot Discord Utils',
    'language': 'Python',
    'price': '$250 *Include Hosting'
  },
  {
    'id': 3,
    'title': 'Bot Discord Moderation',
    'language': 'Python',
    'price': '$550 *Include Hosting'
  },
  {
    'id': 4,
    'title': 'Moderator Discord',
    'language': 'English and Indonesian',
    'price': '$350 for a month *REMOTE*'
  }
]

@app.route("/")
def hello_vicky():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name='Validity')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
