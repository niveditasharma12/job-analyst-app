from ..database.prospect_orm import ProspectOrm
from ..service.proposal_service import ProposalService
from ..util.utilities import Utilities
from ..util.mail_utilities import MailUtilities
from flask import session


class ProspectService(object):


    @staticmethod
    def insert1(data):

        # print(data)

        # Call the ORM or Database Layer

        status, prospect_id = ProspectOrm.insert_prospect(data)

        return status, prospect_id

    @staticmethod
    def get_record():
        data = ProspectOrm.select_prospect()
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25]
            })
        # print(result)
        return result

    @staticmethod
    def get_recent_ten_records():
        data = ProspectOrm.select_recent_ten_prospect()
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25]
            })
        # print(result)
        return result

    @staticmethod
    def get_record_by_id(id):
        data = ProspectOrm.get_record_by_id(id)
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25]
            })
        # print(result)
        return result

    @staticmethod
    def delete_record(id):
        status = ProspectOrm.delete_record(id)
        return status

    @staticmethod
    def updateRecord(update_set, prospect_id):
        status = ProspectOrm.update_prospect(update_set, prospect_id)

        return status

    @staticmethod
    def update_progress(prospect_id, progress):
        status = ProspectOrm.update_prospect_progress(prospect_id, progress)
        return status

    @staticmethod
    def add_prospect_to_proposal(prospect_id):
        result = ProspectService.get_record_by_id(prospect_id)
        result = result[0]
        data = {'prospect_id': result['prospect_id'], 'organization_id': result['organization_id'],
                'proposal_types': "MAIL, CALL, SM", 'prospect_analysis': result['prospect_analysis'],
                'proposal_offers': result['proposal_offers'], 'proposal_priority': 5,
                'proposal_assignee': session["username"]}
        proposal_id = ProposalService.Insert1(data)
        if proposal_id is not None:
            return proposal_id
        return False

    @staticmethod
    def search_prospect(query_dict):
        where = Utilities.construct_where_clause_from_dict(query_dict)
        data = ProspectOrm.search_in_prospect(where)
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25]
            })
        return result

    @staticmethod
    def search_prospect_org_rank(query_dict):
        where = Utilities.construct_where_clause_from_dict(query_dict)
        data = ProspectOrm.search_in_prospect_with_org_rank(where)
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25],
                "org_rank": i[26]
            })
        return result


    @staticmethod
    def getrecordByjobrole(job_role):
        data = ProspectOrm.SearchByJobrole(job_role)
        if len(data) == 0:
            data = ProspectOrm.SearchSimilarJobrole(job_role)
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25]
            })
        # print(result)
        return result

    @staticmethod
    def getrecordByprogress(progress):
        data = ProspectOrm.SearchByProgress(progress)
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25]
            })
        # print(result)
        return result

    @staticmethod
    def getrecordBytechnologies(technologies):
        data = ProspectOrm.SearchBytechnologies(technologies)
        if len(data) == 0:
            data = ProspectOrm.SearchSimilartechnologies(technologies)
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25]
            })
        # print(result)
        return result

    @staticmethod
    def getrecordBypostdate(post_date):
        data = ProspectOrm.SearchBypostdate(post_date)
        if len(data) == 0:
            data = ProspectOrm.SearchSimilarpostdate(post_date)
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25]
            })
        # print(result)
        return result

    @staticmethod
    def getrecordBymaxcost(max_cost):
        data = ProspectOrm.SearchBymaxcost(max_cost)
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25]
            })
        # print(result)
        return result

    @staticmethod
    def getrecordBymincost(min_cost):
        data = ProspectOrm.SearchBymincost(min_cost)
        result = []
        for i in data:
            result.append({
                "prospect_id": i[0],
                "organization_id": i[1],
                "prospect_title": i[2],
                "prospect_type": i[3],
                "source": i[4],
                "account_at_source": i[5],
                "prospect_link": i[6],
                "is_fte": i[7],
                "job_role": i[8],
                "technologies": i[9],
                "job_location": i[10],
                "min_cost": i[11],
                "max_cost": i[12],
                "duration": i[13],
                "engagement_mode": i[14],
                "working_mode": i[15],
                "timezone": i[16],
                "post_date": str(i[17]),
                "contact_person_ids": i[18],
                "prospect_analysis": i[19],
                "proposal_offers": i[20],
                "comments": i[21],
                "progress": i[22],
                "created_by": i[23],
                "dt": str(i[24]),
                "status": i[25]
            })
        # print(result)
        return result

    @staticmethod
    def insert_follow_up(data):

        # print(data)

        # Call the ORM or Database Layer

        status = ProspectOrm.insert_follow_up(data)

        return status

    @staticmethod
    def get_record_followup(id):
        data = ProspectOrm.get_record_follow_up(id)
        result = []
        for i in data:
            result.append({
                "followup_id": i[0],
                "referenced_id": i[1],
                "comments": i[2],
                "followuper": i[3],
                "dt": str(i[4]),
                "status": i[5]
            })
        # print(result)
        return result

    @staticmethod
    def get_all_followup():
        data = ProspectOrm.get_all_follow_up()
        result = []
        for i in data:
            result.append({
                "followup_id": i[0],
                "referenced_id": i[1],
                "comments": i[2],
                "followuper": i[3],
                "dt": str(i[4]),
                "status": i[5]
            })
        # print(result)
        return result

    @staticmethod
    def get_recent_ten_followup():
        data = ProspectOrm.get_recent_ten_follow_up()
        result = []
        for i in data:
            result.append({
                "followup_id": i[0],
                "referenced_id": i[1],
                "comments": i[2],
                "followuper": i[3],
                "dt": str(i[4]),
                "status": i[5]
            })
        # print(result)
        return result










