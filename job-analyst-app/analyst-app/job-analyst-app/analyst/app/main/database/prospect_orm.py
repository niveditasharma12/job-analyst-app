from ..database import connector
from datetime import datetime
from flask import session

class ProspectOrm(object):
    def __init__(self):
        pass

    @staticmethod
    def insert_prospect(data):
        try:
            db = connector.db_connection()
            cmd = db.cursor()
            dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # dt = datetime(dt)
            # print(dt)
            status = 1
            a = '''INSERT INTO prospects (prospect_id, organization_id, prospect_title, prospect_type, source, account_at_source, prospect_link, is_fte, job_role,technologies, job_location, min_cost, max_cost, duration, engagement_mode, working_mode, timezone,post_date, contact_person_ids, prospect_analysis, proposal_offers, comments, created_by, dt, status) VALUES({0}, {1}, "{2}", "{3}", "{4}","{5}", "{6}", {7}, "{8}", "{9}", "{10}", {11}, {12}, "{13}", "{14}", "{15}", "{16}", "{17}", "{18}", "{19}", "{20}", "{21}", "{22}", "{23}", "{24}");'''.format(
                0, data.get("organization_id"), data.get("prospect_title"), data.get("prospect_type"), data.get("source"), data.get("account_at_source"), data.get("prospect_link"),
                data.get("is_fte"), data.get("job_role"), data.get("technologies"),data.get("job_location"), data.get("min_cost"),
                data.get("max_cost"), data.get("duration"), data.get("engagement_mode"), data.get("working_mode"),data.get("timezone"),
                data.get("post_date"), data.get("contact_person_ids"), data.get("prospect_analysis"), data.get("proposal_offers"), data.get("comments"),
                data.get("created_by"), dt, status)
            cmd.execute(a)
            b = "SELECT LAST_INSERT_ID();"
            cmd.execute(b)
            data = cmd.fetchall()
            prospect_id = list(data)[0][0]
            db.commit()
            db.close()
            return "insert successfully", prospect_id
        except Exception as e:
            print(e)
            return None


    @staticmethod
    def select_prospect():
        db = connector.db_connection()
        cmd = db.cursor()
        if session['designation'] == "INTERN":
            a = "select * from prospects where created_by = '" + session['username'] + "'"
        else:
            a = "select * from prospects"
        cmd.execute(a)
        data = cmd.fetchall()
        #print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_recent_ten_prospect():
        db = connector.db_connection()
        cmd = db.cursor()
        if session['designation'] == "INTERN":
            a = "select * from prospects where created_by = '" + session['username'] + "' ORDER BY prospect_id DESC LIMIT 10"
        else:
            a = "SELECT * FROM prospects ORDER BY prospect_id DESC LIMIT 10"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def get_record_by_id(prospect_id):
        db = connector.db_connection()
        cmd = db.cursor()
        if session['designation'] == "INTERN":
            a = "select * from prospects where prospect_id={}".format(prospect_id) + " and created_by = '" + session['username'] + "'"
        else:
            a = "select * from prospects where prospect_id={}".format(prospect_id)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def delete_record(prospect_id):
        db = connector.db_connection()
        cmd = db.cursor()
        if session['designation'] == "INTERN":
            q = "select * from prospects where prospect_id={}".format(prospect_id) + " and created_by = '" + session['username'] + "'"
        else:
            q = "select * from prospects where prospect_id={}".format(prospect_id)

        cmd.execute(q)
        data = cmd.fetchall()
        if data:

            a = "DELETE FROM prospects WHERE prospect_id={} ".format(prospect_id)
            cmd.execute(a)
            db.commit()
            db.close()
            return None
        else:
            return "Please Enter a valid Entity"

    @staticmethod
    def update_prospect(update_set, prospect_id):
        db = connector.db_connection()
        cmd = db.cursor()
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = 1
        a = "UPDATE prospects " + update_set + ''', dt="%s", status=%s where prospect_id=%s''' % (
            dt, status, prospect_id)

        # print("query-", a)
        cmd.execute(a)
        db.commit()
        db.close()
        return "updated successfully"

    @staticmethod
    def search_in_prospect(where):
        db = connector.db_connection()
        cmd = db.cursor()
        if session['designation'] == "INTERN":
            a = "select * from prospects " + where + " and created_by = '" + session['username'] + "' ORDER BY prospect_id DESC"
        else:
            a = "select * from prospects " + where + " ORDER BY prospect_id DESC"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_in_prospect_with_org_rank(where):
        db = connector.db_connection()
        cmd = db.cursor()
        join_cols = "p.prospect_id, p.organization_id, p.prospect_title, p.prospect_type, p.source, p.account_at_source, p.prospect_link, p.is_fte, p.job_role, p.technologies, p.job_location, p.min_cost, p.max_cost, p.duration, p.engagement_mode, p.working_mode, p.timezone, p.post_date, p.contact_person_ids, p.prospect_analysis, p.proposal_offers, p.comments, p.progress, p.created_by, p.dt, p.status, o.org_rank"
        if "DATE(dt)" in where:
            where = where.replace("DATE(dt)", "DATE(p.dt)")
        if session['designation'] == "INTERN":
            a = "select " + join_cols + " from prospects AS p LEFT JOIN organizations AS o ON p.organization_id=o.organization_id " + where + " and created_by = '" + session[
                'username'] + "' ORDER BY prospect_id DESC"
        else:
            a = "select " + join_cols + " from prospects AS p LEFT JOIN organizations AS o ON p.organization_id=o.organization_id " + where + " ORDER BY prospect_id DESC"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data


    @staticmethod
    def SearchByJobrole(job_role):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from prospects where job_role='{}'".format(job_role)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def SearchSimilarJobrole(job_role):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from prospects where job_role like '%{}%'".format(job_role)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def SearchBytechnologies(technologies):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from prospects where technologies='{}'".format(technologies)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def SearchSimilartechnologies(technologies):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from prospects where technologies like '%{}%'".format(technologies)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def SearchByProgress(progress):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from prospects where progress='{}'".format(progress)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def SearchBypostdate(post_date):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from prospects where post_date='{}'".format(post_date)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def SearchSimilarpostdate(post_date):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from prospects where post_date like '%{}%'".format(post_date)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def update_prospect_progress(prospect_id, progress):
        db = connector.db_connection()
        cmd = db.cursor()
        q = "select * from prospects where prospect_id = {0}".format(prospect_id)
        cmd.execute(q)
        result = cmd.fetchall()
        if result:
            dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status = 1
            if progress:
                a = '''UPDATE prospects set progress="%s", dt="%s", status=%s where prospect_id =%s;''' % (progress, dt, status, prospect_id)
                cmd.execute(a)
                db.commit()
                db.close()
                return "updated successfully"
            else:
                return None
        else:
            return None

    @staticmethod
    def SearchBymaxcost(max_cost):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from prospects where max_cost='{}'".format(max_cost)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def SearchBymincost(min_cost):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from prospects where min_cost='{}'".format(min_cost)
        # print(a)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def insert_follow_up(data):
        try:
            db = connector.db_connection()
            cmd = db.cursor()
            date_and_time = datetime.now()
            # print(date_and_time)
            status = 1
            a = '''INSERT INTO followup(
                    followup_id, referenced_id, comments, followuper, dt, status
                    ) VALUES("{0}", {1}, "{2}", "{3}","{4}", "{5}")'''.format(
                0, data.get('referenced_id'),
                data.get('comments'), data.get('followuper'), date_and_time, status
            )
            cmd.execute(a)
            db.commit()
            g_id = cmd.lastrowid
            db.close()
            return g_id
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def get_record_follow_up(id):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from followup where referenced_id={};".format(id)
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def get_all_follow_up():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from followup"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data

    @staticmethod
    def get_recent_ten_follow_up():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "SELECT * FROM followup ORDER BY followup_id DESC LIMIT 10"
        cmd.execute(a)
        data = cmd.fetchall()
        # print(data)
        db.commit()
        db.close()
        return data
