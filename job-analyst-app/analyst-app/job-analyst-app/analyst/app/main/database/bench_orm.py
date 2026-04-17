from ..database import connector
from datetime import datetime


class bench_orm(object):
    def __int__(self):
        pass

    @staticmethod
    def insert_bench(data):
        try:
            db = connector.db_connection()
            cmd = db.cursor()
            dt = datetime.now()
            status = 1
            a = '''INSERT INTO bench(client_id, 
            name, contact, alternate_contact, email, 
            alternate_email, exp, domain, primary_skill, 
            secondary_skill, current_role, qualification, resume, 
            bench_start_dt, bench_end_dt, bench_status, created_by, 
            dt, status)VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}',
            '{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}')'''.format(
                data.get("client_id"), data.get("name"), data.get("contact"),
                data.get("alternate_contact"), data.get("email"), data.get("alternate_email"),
                data.get("exp"), data.get("domain"), data.get("primary_skill"),
                data.get("secondary_skill"), data.get("current_role"), data.get("qualification"),
                data.get("resume"), data.get("bench_start_dt"), data.get("bench_end_dt"),
                data.get("bench_status"), data.get("created_by"), dt, status)
            cmd.execute(a)
            db.commit()
            db.close()
            return "insert successfully"
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def select_bench():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from bench"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_recent_ten_bench():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "SELECT * FROM bench ORDER BY bench_id DESC LIMIT 10"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_bench_by_id(bench_id):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from bench where bench_id={}".format(bench_id)
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def edit_bench(update_set, id):
        db = connector.db_connection()
        cmd = db.cursor()
        dt = datetime.now()
        status = 1
        a = "UPDATE bench " + update_set + ''', dt="%s", status="%s" where bench_id=%s''' % (
            dt, status, id)
        # print("query--", a)
        cmd.execute(a)
        db.commit()
        db.close()
        return "updated successfully"

    @staticmethod
    def search_in_bench(where):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from bench " + where + " ORDER BY bench_id DESC"
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_name(name):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from bench where name='{}'".format(name)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    # name, contact, exp, domain, primary_skill, secondary_skill,bench_status

    @staticmethod
    def search_by_contact(contact):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from bench where contact='{}'".format(contact)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_exp(exp):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from bench where exp='{}'".format(exp)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_domain(domain):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from bench where domain='{}'".format(domain)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_primary_skill(primary_skill):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from bench where primary_skill='{}'".format(primary_skill)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_secondary_skill(secondary_skill):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from bench where secondary_skill='{}'".format(secondary_skill)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_bench_status(bench_status):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from bench where bench_status='{}'".format(bench_status)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data
