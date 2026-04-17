from ..database import connector
from flask import session
import jwt


class login_orm(object):
    def __init__(self):
        pass

    @staticmethod
    def login(username, password):
        db = connector.db_connection()
        cmd = db.cursor()
        cmd.execute('SELECT * FROM login WHERE email_id = %s AND password = %s', (username, password,))
        account = cmd.fetchone()
        db.commit()
        db.close()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            session['designation'] = account[5]
            return True
        else:
            return False

    @staticmethod
    def get_rows(cursor, tables):
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in tables]
        return rows

    @staticmethod
    def profile(jwt_key):
        db = connector.db_connection()
        cmd = db.cursor()
        if 'loggedin' in session:
            cmd.execute('SELECT * FROM login WHERE id = %s', (session['id'],))
            account = cmd.fetchone()

            res = {
                "id": account[0],
                "email": account[1],
                "name": account[3],
                "role": account[4],
                "designation": account[5],
                "status": account[8]
            }
            encoded_jwt_token = jwt.encode(res, jwt_key, algorithm="HS256")

            return res, encoded_jwt_token

        db.commit()
        db.close()
        return False
