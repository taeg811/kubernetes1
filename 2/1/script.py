#from kubernetes import client, config
#import requests
import mysql.connector
from mysql.connector import connect, Error
from random import randrange
import time
import os

#MYSQL_ROOT_PASSWORD="admin"
#MYSQL_DB_NAME="tempesta"
#MYSQL_USERNAME="root"
#HOST="172.17.0.16"

MYSQL_ROOT_PASSWORD = os.environ['MYSQL_ROOT_PASSWORD']
MYSQL_DB_NAME = os.environ['MYSQL_DB_NAME']
MYSQL_USERNAME = os.environ['MYSQL_USERNAME']
HOST = os.environ['HOST']

# 2 times in minute
period = 120
local_time = float(period)

working = True
while working:
  article = str(randrange(5)+1)
#  print(article)
  try:
      with connect(
          host=HOST,
          user=MYSQL_USERNAME,
          password=MYSQL_ROOT_PASSWORD,
          database=MYSQL_DB_NAME,
      ) as connection:

         with connection.cursor() as cursor:
           query = "SELECT title, text from articles where id='"+article+"' " 
           cursor.execute(query)
           result = cursor.fetchall()
           for row in result:
#             print("Title:", row[0])
#             print("Article:", row[1])
           #create html file
             table_file = open('./result/index.html', 'w')
             table_file.write('<!DOCTYPE html><html><head><title>'+row[0]+'</title></head><body><p>'+row[1]+'</p></body>')
             table_file.close()

  except Error as e:
    print(e)
    working = False

  time.sleep(local_time)
