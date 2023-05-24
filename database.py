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
      print (rows)
      if len(rows) == 0:
        return None
      else:
        row = rows[0]
        result_dict = row._asdict()
        return result_dict

      


  
  