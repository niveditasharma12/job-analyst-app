from ..database import connector
from datetime import datetime


class source_orm(object):
    def __int__(self):
        pass

    @staticmethod
    def insert_source(data):
        try:
            db = connector.db_connection()
            cmd = db.cursor()
            dt = datetime.now()
            # print(dt)
            status = 1
            a = '''INSERT  INTO sources(
            source_name,
            source_url,
            source_type,
            is_paid_or_not,
            is_contact,
            is_mail,
            is_social_media,
            is_revenue,
            is_services,
            is_industry,
            created_by,
            dt,
            status)
        VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format(
                data.get("source_name"), data.get("source_url"),
                data.get("source_type"), data.get("is_paid_or_not"),
                data.get("is_contact"), data.get("is_mail"),
                data.get("is_social_media"),
                data.get("is_revenue"), data.get("is_services"), data.get("is_industry"),
                data.get("created_by"),
                dt,
                status,
            )
            cmd.execute(a)
            b = "SELECT LAST_INSERT_ID();"
            cmd.execute(b)
            data = cmd.fetchall()
            source_id = list(data)[0][0]
            db.commit()
            db.close()
            return "insert successfully", source_id
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def source_max_id():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select max(source_id) from sources"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_source():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from sources"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_recent_source():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "SELECT * FROM sources ORDER BY source_id DESC LIMIT 10"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_in_sources(where):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from sources " + where + " ORDER BY source_id DESC"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_url(source_url):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from sources where source_url='{}'".format(source_url)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_similar_url(source_url):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from sources where source_url like '%{}%'".format(source_url)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_id(source_id):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from sources where source_id='{}'".format(source_id)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data
