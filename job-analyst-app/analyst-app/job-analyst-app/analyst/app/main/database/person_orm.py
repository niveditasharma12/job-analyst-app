from ..database import connector
from datetime import datetime


class person_orm(object):
    def __int__(self):
        pass

    @staticmethod
    def insert_person(data):
        try:
            db = connector.db_connection()
            cmd = db.cursor()
            dt = datetime.now()
            # print(dt)
            status = 1
            a = '''INSERT  INTO persons(
            organization_id, 
            name, 
            contact,  
            alt_contact,
            email,  
            alt_email,
            linkedin_url,
            cb_url,
            department,
            designation,
            is_decision_maker,
            created_by,
            dt,
            status)
        VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')'''.format(
                data.get("organization_id"),
                data.get("name"),
                data.get("contact"),
                data.get("alt_contact"),
                data.get("email"),
                data.get("alt_email"),
                data.get("linkedin_url"),
                data.get("cb_url"),
                data.get("department"),
                data.get("designation"),
                data.get("is_decision_maker"),
                data.get("created_by"),
                dt,
                status,
            )
            cmd.execute(a)
            db.commit()
            db.close()
            return "insert successfully"
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def max_id():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select max(person_id) from persons"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_person():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from persons"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_recent_person():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "SELECT * FROM persons ORDER BY person_id DESC LIMIT 10"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_in_persons(where):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "SELECT p.person_id, p.organization_id, p.name, o.organization_name, o.website, p.contact, p.alt_contact, p.email, p.alt_email, p.linkedin_url, p.cb_url, p.department, p.designation, p.is_decision_maker, p.created_by, p.dt, p.status FROM persons AS p LEFT JOIN organizations AS o ON p.organization_id=o.organization_id " + where + " ORDER BY person_id DESC"
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def person_name(name):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from persons where name='{}'".format(name)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def person_email(email):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from persons where email='{}'".format(email)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_person_id(id):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from persons where person_id={}".format(id)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_organization_id(id):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from persons where organization_id={}".format(id)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data
