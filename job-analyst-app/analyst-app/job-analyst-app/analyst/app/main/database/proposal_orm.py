from ..database import connector
from datetime import datetime

class ProposalOrm(object):
    def __init__(self):
        pass

    @staticmethod
    def insert_proposal(data):
        db = connector.db_connection()
        cmd = db.cursor()
        dt = datetime.now()
        status = 1
        q = '''insert into proposals (prospect_id,organization_id,proposal_types,prospect_analysis,
         proposal_offers, proposal_priority,
         proposal_assignee,dt,status)values ({0},{1},'{2}','{3}','{4}','{5}','{6}',
        '{7}','{8}')'''.format(
        data.get("prospect_id"),data.get("organization_id"),
        data.get("proposal_types"),data.get("prospect_analysis"),data.get("proposal_offers"),
        data.get("proposal_priority"),data.get("proposal_assignee"),
        dt,status)
        cmd.execute(q)
        db.commit()
        id_gen=cmd.lastrowid
        db.close()
        return id_gen

    @staticmethod
    def search_in_proposals(where):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from proposals " + where + " ORDER BY proposal_id DESC"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_prospect():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from proposals"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_recent_prospect():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "SELECT * FROM proposals ORDER BY proposal_id DESC LIMIT 10"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_organization_id(organization_id):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from proposals where organization_id={0}".format(organization_id)
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_prospect_id(prospect_id):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from proposals where prospect_id={0}".format(prospect_id)
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

#---------------------------------------------------------Proposal_Info---------------------------------------------------------------

from ..database import connector
from datetime import datetime

class Proposal_Info_Orm(object):
    def __init__(self):
        pass

    @staticmethod
    def insert_proposal_info(data):
        db = connector.db_connection()
        cmd = db.cursor()
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        today_date = datetime.now().strftime("%Y-%m-%d")
        status = 1
        q ='''insert into proposal_info (proposal_id , proposal_type , proposal_sender , proposal_detail, 
        proposal_date, dt, status)values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')'''.format(
        data.get("proposal_id"), data.get("proposal_type"),data.get("proposal_sender"),data.get("proposal_detail"),
        today_date, dt, status)
        cmd.execute(q)
        db.commit()
        gen_id = cmd.lastrowid
        db.close()
        return gen_id

    @staticmethod
    def select_prospect_info():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from proposal_info"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def select_recent_prospect_info():
        db = connector.db_connection()
        cmd = db.cursor()
        a = "SELECT * FROM proposal_info ORDER BY proposal_info_id DESC LIMIT 10"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_in_proposal_info(where):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from proposal_info " + where + " ORDER BY proposal_info_id DESC"
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_proposal_status(proposal_status):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from proposal_info where proposal_id='{0}'".format(proposal_status)
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_by_proposal_date(proposal_date):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from proposal_info where proposal_date='{0}'".format(proposal_date)
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data

    @staticmethod
    def search_similar_proposal_date(proposal_date):
        db = connector.db_connection()
        cmd = db.cursor()
        a = "select * from proposal_info where proposal_date like '{0}'".format(proposal_date)
        cmd.execute(a)
        data = cmd.fetchall()
        db.commit()
        db.close()
        return data
