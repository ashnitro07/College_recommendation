import numpy as np
from sklearn.linear_model import LinearRegression
import sqlite3
from flask import Flask, request, render_template
rank=0
course=''
location=''
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
 return render_template('input.html')
 
@app.route('/read-form', methods=['POST'])
def read_form():
 data = request.form
 return {
        'rank'     : data['rank1'],
        'course' : data['course1'],
        'location'    : data['location1'],
        }



#reading DB
x1=0

conn = sqlite3.connect('database1.db')
cursor = conn.cursor()
for x1 in cursor:
 cursor.execute("SELECT sno,y1, co1, y2, co2, y3, co3, y4, co4, y5, co5 FROM college1;")
 data = cursor.fetchmany()
 sno0,y01, co01, y02, co02, y03, co03, y04, co04, y05, co05 = data
 #regression model
 past_ranks = np.array([[y01,co01], [y02,co02], [y03,co03], [y04,co04],[y05,co05]])
 target_year = 2023
 X = past_ranks[:, 0].reshape(-1, 1)
 y = past_ranks[:, 1]
 model = LinearRegression()
 model.fit(X, y)
 predicted_rank = model.predict([[target_year]])
 p=predicted_rank
 print(p)
 cursor.execute ("UPDATE college1 SET yfin = "+str(p)+" where sno = "+str(sno0)+";")
 conn.commit()
 


#inputs grom user gui
sql_query = "SELECT cname, loc, coname, agp, hostel, zone, yfin FROM college1 WHERE coname = ? AND loc = ? AND ? <= yfin limit 1;"
cursor.execute(sql_query, (course, location, rank))

#cursor.execute("SELECT cname,loc,coname,agp,hostel,zone,yfin FROM college where coname = '"+str(course)+"' , loc = '"+str(location)+"' , "+str(rank)+" <= yfin;")
data = cursor.fetchone()
#cname0,loc0,coname0,agp0,hostel0,zone0,yfin0 = data
if data is not None:
    cname0, loc0, coname0, agp0, hostel0, zone0, yfin0 = data
    # Process the data or perform further operations
    print(cname0, loc0, coname0, agp0, hostel0, zone0, yfin0)
else:
    print("No matching data found.")


#output to user

if __name__ == '__main__':
   app.debug = True
   app.run()


