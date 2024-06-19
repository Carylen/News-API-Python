import mysql.connector
import xml.etree.ElementTree as ET
import json
from modules.user import User

connection = mysql.connector.connect(user='root', password='', 
                                     host='localhost',
                                     database='mafia_trashbin')

cursor = connection.cursor()

insert_query = """
    INSERT INTO users (name, age, phoneNumber)
    VALUES (%s, %s, %s)
"""

# data = User(
#     name='irhamganteng',
#     age=20,
#     phoneNumber='023994818'
# )
# data.to_dict()

data = ('hamza', 12, '01238819')
cursor.execute(insert_query, data)
connection.commit()

# cursor.close()
# connection.close()
# tree = ET.parse('data.xml')
# data = tree.findall('student')
print(json.dumps(data))