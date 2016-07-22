# this is an awesome python project
import pymysql

# Open database connection
db = pymysql.connect("example-db.cqxhwq6fjwe3.us-west-1.rds.amazonaws.com","TRG","67carats","test" );

#Initialize Cursor
cursor = db.cursor();

#Executes query
cursor.execute('SELECT * FROM numeros LIMIT 100;');

result = cursor.fetchall();

for row in result:
    print str(row[0])+' '+ str(row[1])
    
db.close();

