from ..database.proposal_orm import ProposalOrm
from ..database.proposal_orm import Proposal_Info_Orm
from ..util.utilities import Utilities
from ..service.organization_service import organizationservice


class ProposalService(object):
    def __init__(self):
        pass

    @staticmethod
    def validate_proposal(prospect_id):
        result = ProposalService.get_record()
        for i in result:
            if i['prospect_id'] == int(prospect_id):
                return False
            else:
                continue
        return True

    @staticmethod
    def validate_org_foreign_key(org_id):
        result = organizationservice.get_record()
        for i in result:
            if i['organization_id'] == int(org_id):
                return True
            else:
                continue
        return False

    @staticmethod
    def Insert1(data):
        # Call the ORM or Database Layer
        status = ProposalOrm.insert_proposal(data)
        return status

    @staticmethod
    def get_record():
        data = ProposalOrm.select_prospect()
        result = []
        for i in data:
            result.append({
                "proposal_id":i[0],
                "prospect_id":i[1],
                "organization_id":i[2],
                "proposal_types":i[3],
                "proposal_analysis":i[4],
                "proposal_offers": i[5],
                "proposal_priority":i[6],
                "proposal_status":i[7],
                "proposal_assignee":i[8],
                "dt": str(i[9]),
                "status":i[10]
            })
        return result

    @staticmethod
    def get_recent_record():
        data = ProposalOrm.select_recent_prospect()
        result = []
        for i in data:
            result.append({
                "proposal_id": i[0],
                "prospect_id": i[1],
                "organization_id": i[2],
                "proposal_types": i[3],
                "proposal_analysis": i[4],
                "proposal_offers": i[5],
                "proposal_priority": i[6],
                "proposal_status": i[7],
                "proposal_assignee": i[8],
                "dt": str(i[9]),
                "status": i[10]
            })
        return result

    @staticmethod
    def search_proposal(query_dict):
        where = Utilities.construct_where_clause_from_dict(query_dict)
        data = ProposalOrm.search_in_proposals(where)
        result = []
        for i in data:
            result.append({
                "proposal_id": i[0],
                "prospect_id": i[1],
                "organization_id": i[2],
                "proposal_types": i[3],
                "proposal_analysis": i[4],
                "proposal_offers": i[5],
                "proposal_priority": i[6],
                "proposal_status": i[7],
                "proposal_assignee": i[8],
                "dt": str(i[9]),
                "status": i[10]
            })
        return result

    @staticmethod
    def search_by_organization_id(organization_id):
        data = ProposalOrm.search_by_organization_id(organization_id)
        result = []
        for i in data:
            result.append({
                "proposal_id": i[0],
                "prospect_id": i[1],
                "organization_id": i[2],
                "proposal_types": i[3],
                "proposal_analysis": i[4],
                "proposal_offers": i[5],
                "proposal_priority": i[6],
                "proposal_status": i[7],
                "proposal_assignee": i[8],
                "dt": str(i[9]),
                "status": i[10]
            })
        return result

    @staticmethod
    def search_by_proposal_id(prospect_id):

        data = ProposalOrm.search_by_prospect_id(prospect_id)
        result = []
        for i in data:
            result.append({
                "proposal_id": i[0],
                "prospect_id": i[1],
                "organization_id": i[2],
                "proposal_types": i[3],
                "proposal_analysis": i[4],
                "proposal_offers": i[5],
                "proposal_priority": i[6],
                "proposal_status": i[7],
                "proposal_assignee": i[8],
                "dt": str(i[9]),
                "status": i[10]
            })
        return result


#--------------------------------------------Proposal_Info----------------------------------------------------------------------------

class Proposal_Info_Service(object):
    def __init__(self):
        pass

    @staticmethod
    def Insert_Propoal_Info(data):
        # Call the ORM or Database Layer
        status = Proposal_Info_Orm.insert_proposal_info(data)
        return status

    @staticmethod
    def get_record_proposal_info():
        data = Proposal_Info_Orm.select_prospect_info()
        result = []
        for i in data:
            result.append({
                "proposal_info_id": i[0],
                "proposal_id": i[1],
                "proposal_type": i[2],
                "proposal_sender": i[3],
                "proposal_status": i[4],
                "proposal_date": str(i[5]),
                "proposal_detail": i[6],
                "dt": str(i[7]),
                "status": i[8]
            })
        return result

    @staticmethod
    def get_recent_proposal_info():
        data = Proposal_Info_Orm.select_recent_prospect_info()
        result = []
        for i in data:
            result.append({
                "proposal_info_id": i[0],
                "proposal_id": i[1],
                "proposal_type": i[2],
                "proposal_sender": i[3],
                "proposal_status": i[4],
                "proposal_date": str(i[5]),
                "proposal_detail": i[6],
                "dt": str(i[7]),
                "status": i[8]
            })
        return result

    @staticmethod
    def search_proposal_info(query_dict):
        where = Utilities.construct_where_clause_from_dict(query_dict)
        data = Proposal_Info_Orm.search_in_proposal_info(where)
        result = []
        for i in data:
            result.append({
                "proposal_info_id": i[0],
                "proposal_id": i[1],
                "proposal_type": i[2],
                "proposal_sender": i[3],
                "proposal_status": i[4],
                "proposal_date": str(i[5]),
                "proposal_detail": i[6],
                "dt": str(i[7]),
                "status": i[8]
            })
        return result

    @staticmethod
    def search_by_proposal_status(proposal_status):
        data = Proposal_Info_Orm.search_by_proposal_status(proposal_status)
        result = []

        for i in data:
            result.append({
                "proposal_info_id": i[0],
                "proposal_id": i[1],
                "proposal_type": i[2],
                "proposal_sender": i[3],
                "proposal_status": i[4],
                "proposal_date": str(i[5]),
                "proposal_detail": i[6],
                "dt": str(i[7]),
                "status": i[8]
            })
        return result

    @staticmethod
    def search_by_proposal_date(proposal_date):
        data = Proposal_Info_Orm.search_by_proposal_date(proposal_date)
        if len(data) == 0:
            data = Proposal_Info_Orm.search_similar_proposal_date(proposal_date)
        result = []
        for i in data:
            result.append({
                "proposal_info_id": i[0],
                "proposal_id": i[1],
                "proposal_type": i[2],
                "proposal_sender": i[3],
                "proposal_status": i[4],
                "proposal_date": str(i[5]),
                "proposal_detail": i[6],
                "dt": str(i[7]),
                "status": i[8]
            })
        return result
