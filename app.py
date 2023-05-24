from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
# here database create act as a module from where we call functions. like header file in c++.
from database import get_jobs_from_db, job_by_id
from sqlalchemy import text

app = Flask(__name__)

@app.route("/")
def hello_careers():
  jobs = get_jobs_from_db()
  # Using jinja templating tmethid to return dynamic data from server to render oin html.
  return render_template("home.html",jobs=jobs)

@app.route("/api/jobs")
def jobs():
    jobs = get_jobs_from_db()
    #other way usng API-JSON
    return jsonify(jobs=jobs)
  
@app.route("/jobs/<id>")
def show_Jobs(id):
    job = job_by_id(id)
    if not job:
      return "Not Found",404
    return render_template("jobs_detail.html",job=job)

@app.route("/jobs/<id>/apply", methods=['POST'])
def apply_Jobs(id):
    # data = request.args #when use routing method
    data = request.form # when use post method in form
    #store this in db
    #show acknowledgement
    return jsonify(data)

if __name__ == "__main__":
  app.run( host='0.0.0.0',debug=True)