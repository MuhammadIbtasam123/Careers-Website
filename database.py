# your database should be there for better encapsulation of code.
# this is nedded to establish connection with database MS-SQL server
from sqlalchemy import create_engine,text
import pyodbc
import sqlalchemy as sa
# Developing a Connection
engine = sa.create_engine('mssql+pyodbc://IBTASAM_PC\SQLEXPRESS/Careers?driver=SQL+Server+Native+Client+11.0',echo = True)

def get_jobs_from_db():
  with engine.connect() as con:
    # this will fetch all the data from the job table
    result = con.execute(text("SELECT * FROM JOBS"))
    jobData = []
    for row in result:
        jobs = {
            'id': row[0],
            'title': row[1],
            'location': row[2],
            'salary': row[3],
            'currency': row[4],
            'responsibilities': row[5],
            'requirements': row[6]
        }
        jobData.append(jobs)

    return jobData
  
def job_by_id(id):
    with engine.connect() as con:
      job = con.execute(text("SELECT * from jobs where id = :val"), {"val": id})
      rows = job.fetchall()
      if len(rows) == 0:
        return None
      else:
        row = rows[0]
        result_dict = row._asdict()
        return result_dict


def store_Data_in_DB(id, application):
    with engine.connect() as con:
        query = text("INSERT INTO Application (job_id, first_name, email, linkedin_url, resume_url) VALUES (:job_id, :first_name, :email, :linkedin_url, :resume_url)")
        con.execute(query, job_id=id, first_name=application['first_name'], email=application['email'], linkedin_url=application['linkedin_url'], resume_url=application['resume_url'])
    return True


# def store_Data_in_DB(id, data):
#     with engine.connect() as con:
#       query = text("INSERT INTO Careers.Application (id,job_id, first_name, email, linkedin_url, resume_url) VALUES (:job_id, :first_name, :email, :linkedin_url, :resume_url)")
#       VALUES = {'job_id': id,
#             'first_name':data['first_name'],
#             'email':data['email'],
#             'linkedin_url':data['linkedin_url'],
#             'resume_url':data['resume_url']}
#       con.execute(query,VALUES)



  
  