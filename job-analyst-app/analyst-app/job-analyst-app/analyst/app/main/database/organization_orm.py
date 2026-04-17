# import data as data
from ..database import connector
from datetime import datetime
from flask import session


class organizationorm(object):
    def __int__(self):
        pass

    @staticmethod
    def insert_organization(data):
        try:
            db = connector.db_connection()
            cmd = db.cursor()
            dt = datetime.now()
            status = 1
            a = '''INSERT  INTO organizations(
            organization_name,
            website,
            industry,
            service,
            min_revenue,
            max_revenue,
            country,
            location,
            no_emp,
            is_ind_operation,
            org_rank,
            linkedin_url,
            cb_url,
            created_by,
            dt,status
            )
        VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}')'''.format(
                data.get("organization_name"),
                data.get("website"),
                data.get("industry"),
                data.get("service"),
                data.get("min_revenue"),
                data.get("max_revenue"),
                data.get("country"),
                data.get("location"),
                data.get("no_emp"),
                data.get("is_ind_operation"),
                data.get("org_rank"),
                data.get("linkedin_url"),
                data.get("cb_url"),
                data.get("created_by"),
                dt,
                status
               )
            cmd.execute(a)
            b = "SELECT LAST_INSERT_ID();"
            cmd.execute(b)
            data = cmd.fetchall()
            org_id = list(data)[0][0]
            db.commit()
            db.close()
            return "insert successfully", org_id
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def select_organization():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from organizations"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_recent_ten_organization():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "SELECT * FROM organizations ORDER BY organization_id DESC LIMIT 10"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_organization_by_id(org_id):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from organizations where organization_id={}".format(org_id)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def edit_record(update_set, org_id):
        # print(data)
        db = connector.db_connection()
        cmd = db.cursor()
        dt = datetime.now()
        status = 1
        a = "UPDATE organizations " + update_set + ''',dt="%s",status="%s" where organization_id=%s''' % (
            dt, status, org_id)
        # print("query--", a)
        cmd.execute(a)
        db.commit()
        db.close()
        return "updated successfully"

    @staticmethod
    def search_in_org(where):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from organizations " + where + " ORDER BY organization_id DESC"
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def SearchByCompanyName(company_name):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from organizations where organization_name='{}'".format(company_name)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_contains_company_name(company_name):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from organizations where organization_name like '%{}%'".format(company_name)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def SearchByWebsite(website):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from organizations where website='{}'".format(website)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def Search_by_contains_website(website):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from organizations where website like '%{}%'".format(website)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data
