from ..database.organization_orm import organizationorm
from ..util.utilities import Utilities
# from ..database.lead_orm import leadorm


class organizationservice(object):
    @staticmethod
    def insert1(data):
        # print(data)

        # Call the ORM or Database Layer

        status, org_id = organizationorm.insert_organization(data)

        return status, org_id

    @staticmethod
    def get_record():
        data = organizationorm.select_organization()
        result = []
        for i in data:
            result.append({
                'organization_id': i[0],
                'organization_name': i[1],
                'website': i[2],
                'industry': i[3],
                'service': i[4],
                'min_revenue': i[5],
                'max_revenue': i[6],
                'country': i[7],
                'location': i[8],
                'number_of_employee': i[9],
                'is_ind_operation': i[10],
                'org_rank': i[11],
                'linkedin_url': i[12],
                'cb_url': i[13],
                'created_by': i[14],
                'dt': str(i[15]),
                'status': i[16],
            })
        return result

    @staticmethod
    def get_recent_ten_record():
        data = organizationorm.select_recent_ten_organization()
        result = []
        for i in data:
            result.append({
                'organization_id': i[0],
                'organization_name': i[1],
                'website': i[2],
                'industry': i[3],
                'service': i[4],
                'min_revenue': i[5],
                'max_revenue': i[6],
                'country': i[7],
                'location': i[8],
                'number_of_employee': i[9],
                'is_ind_operation': i[10],
                'org_rank': i[11],
                'linkedin_url': i[12],
                'cb_url': i[13],
                'created_by': i[14],
                'dt': str(i[15]),
                'status': i[16],
            })
        return result

    @staticmethod
    def get_record_by_id(org_id):
        data = organizationorm.select_organization_by_id(org_id)
        result = []
        for i in data:
            result.append({
                'organization_id': i[0],
                'organization_name': i[1],
                'website': i[2],
                'industry': i[3],
                'service': i[4],
                'min_revenue': i[5],
                'max_revenue': i[6],
                'country': i[7],
                'location': i[8],
                'number_of_employee': i[9],
                'is_ind_operation': i[10],
                'org_rank': i[11],
                'linkedin_url': i[12],
                'cb_url': i[13],
                'created_by': i[14],
                'dt': str(i[15]),
                'status': i[16],
            })
        return result

    @staticmethod
    def edit_record(update_set, org_id):
        status = organizationorm.edit_record(update_set, org_id)
        return status

    @staticmethod
    def search_organization(query_dict):
        where = Utilities.construct_where_clause_from_dict(query_dict)
        data = organizationorm.search_in_org(where)
        result = []
        for i in data:
            result.append({
                'organization_id': i[0],
                'organization_name': i[1],
                'website': i[2],
                'industry': i[3],
                'service': i[4],
                'min_revenue': i[5],
                'max_revenue': i[6],
                'country': i[7],
                'location': i[8],
                'number_of_employee': i[9],
                'is_ind_operation': i[10],
                'org_rank': i[11],
                'linkedin_url': i[12],
                'cb_url': i[13],
                'created_by': i[14],
                'dt': str(i[15]),
                'status': i[16],

            })
        # print(result)
        return result

    @staticmethod
    def getrecordByCompanyName(company_name):
        data = organizationorm.SearchByCompanyName(company_name)
        if len(data) == 0:
            data = organizationorm.search_contains_company_name(company_name)
        result = []
        for i in data:
            result.append({
                'organization_id': i[0],
                'organization_name': i[1],
                'website':i[2],
                'industry': i[3],
                'service': i[4],
                'min_revenue': i[5],
                'max_revenue': i[6],
                'country': i[7],
                'location': i[8],
                'number_of_employee': i[9],
                'is_ind_operation': i[10],
                'org_rank': i[11],
                'linkedin_url': i[12],
                'cb_url': i[13],
                'created_by': i[14],
                'dt': str(i[15]),
                'status': i[16],

            })
        # print(result)
        return result

    @staticmethod
    def getrecordByWebsite(website):
        data = organizationorm.SearchByWebsite(website)
        if len(data) == 0:
            data = organizationorm.Search_by_contains_website(website)
        result = []
        for i in data:
            result.append({
                'organization_id': i[0],
                'organization_name': i[1],
                'website': i[2],
                'industry': i[3],
                'service': i[4],
                'min_revenue': i[5],
                'max_revenue': i[6],
                'country': i[7],
                'location': i[8],
                'number_of_employee': i[9],
                'is_ind_operation': i[10],
                'org_rank': i[11],
                'linkedin_url': i[12],
                'cb_url': i[13],
                'created_by': i[14],
                'dt': str(i[15]),
                'status': i[16],

            })
        # print(result)
        return result