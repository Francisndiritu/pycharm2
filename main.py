# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pymysql as pymysql
# import pgAdmin4
from flask import *
main = Flask(__name__)


@main.route('/gdev' , methods =['POST' , 'GET'])
def gdev():
    import re

    if request.method == 'POST':
         email= request.form['email']
         password =request.form['password']
         confirm = request.form['confirm']
         REG_NO = request.form['REG_NO']

         if password != confirm:
             return render_template('gdev.html' , msg = 'password do not match')
         elif len(password)<8:
             return render_template('gdev.html', msg='password must be atleast 8 characters')
         elif not re.search('0-9', password):
             return render_template('gdev.html', msg='must contain a NUMERICS ')
         elif not re.search('A-Z', password):
             return render_template('gdev.html', msg='must contain a capital letter ')

         elif not re.search('a-z', password):
             return render_template('gdev.html', msg='must contain a capital letter ')

         # elif len(REG_NO) >=17:
         #     return render_template('gdev.html'), msg='invalid reg no ')
         #
         #
         # elif len(email) >50:
         #     return render_template('gdev.html'),msg = 'invalid email')

         else :

             connection = pymysql.connnect(host='localhost', password='', user='root', database='gdev   ')
             cursor = connection.cursor()

             cursor.execute('INSERT INTO registration (email ,password,password) values (%s ,%s,%s)',
                            email, password ,REG_NO)
             connection.commit()
             return render_template('ACTIVITIES.html', success='Registered Successfully')


















@main.route('/gallery<id>')
def gallery(id):
            connection = pymysql.connnect(host='localhost', password='', user='root@localhost', database='gdev')

            cursor = connection.cursor()

            cursor.execute('SELECT * FROM gallery WHERE ProductID= %S' ,(id))
            row = cursor.fetchone()
            return render_template('gallery.html' , row=row)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main.run(debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
