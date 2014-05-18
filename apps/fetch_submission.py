#!/usr/bin/python2

import MySQLdb

db = MySQLdb.connect("localhost", "root", "iloveinfor", "tioj_dev");
cursor = db.cursor(MySQLdb.cursors.DictCursor);
command = "SELECT `id`, `code`, `compiler`, `problem_id`,"
command += "`user_id` FROM submissions WHERE `result` = 'queued' OR `result` = '' "
command += "ORDER BY `id` ASC LIMIT 1"
cursor.execute(command);

data = cursor.fetchone();
if data == None :
   print -1
else :
   print data['id']
   print data['problem_id']
   #print data['user_id']
   print data['compiler']
   print data['code']

db.close()