from ..database.person_orm import person_orm
from ..util.utilities import Utilities


class personservice(object):
    @staticmethod
    def insert1(data):
        # print(data)

        # Call the ORM or Database Layer

        status = person_orm.insert_person(data)

        return status

    @staticmethod
    def get_max_id():
        data = person_orm.max_id()
        result = []
        for i in data:
            result.append({
                'person_id': i[0],
            })
        return result

    @staticmethod
    def get_person():
        data = person_orm.select_person()
        result = []
        for i in data:
            result.append({
                'person_id': i[0],
                'organization_id': i[1],
                'name': i[2],
                'contact': i[3],
                'alt_contact': i[4],
                'email': i[5],
                'alt_email': i[6],
                'linkedin_url': i[7],
                'cb_url': i[8],
                'department': i[9],
                'designation': i[10],
                'is_decision_maker': i[11],
                'created_by': i[12],
                'dt': str(i[13]),
                'status': i[14]
            })
        return result

    @staticmethod
    def get_recent_person():
        data = person_orm.select_recent_person()
        result = []
        for i in data:
            result.append({
                'person_id': i[0],
                'organization_id': i[1],
                'name': i[2],
                'contact': i[3],
                'alt_contact': i[4],
                'email': i[5],
                'alt_email': i[6],
                'linkedin_url': i[7],
                'cb_url': i[8],
                'department': i[9],
                'designation': i[10],
                'is_decision_maker': i[11],
                'created_by': i[12],
                'dt': str(i[13]),
                'status': i[14]
            })
        return result

    @staticmethod
    def search_person(query_dict):
        where = Utilities.construct_where_clause_from_dict(query_dict)
        data = person_orm.search_in_persons(where)
        result = []
        for i in data:
            result.append({
                'person_id': i[0],
                'organization_id': i[1],
                'name': i[2],
                'organization_name': i[3],
                'website': i[4],
                'contact': i[5],
                'alt_contact': i[6],
                'email': i[7],
                'alt_email': i[8],
                'linkedin_url': i[9],
                'cb_url': i[10],
                'department': i[11],
                'designation': i[12],
                'is_decision_maker': i[13],
                'created_by': i[14],
                'dt': str(i[15]),
                'status': i[16]
            })
        # print(result)
        return result

    @staticmethod
    def get_person_name(name):
        data = person_orm.person_name(name)
        result = []
        for i in data:
            result.append({
                'person_id': i[0],
                'organization_id': i[1],
                'name': i[2],
                'contact': i[3],
                'alt_contact': i[4],
                'email': i[5],
                'alt_email': i[6],
                'linkedin_url': i[7],
                'cb_url': i[8],
                'department': i[9],
                'designation': i[10],
                'is_decision_maker': i[11],
                'created_by': i[12],
                'dt': str(i[13]),
                'status': i[14]
            })
        # print(result)
        return result

    @staticmethod
    def get_person_by_email(email):
        data = person_orm.person_email(email)
        result = []
        for i in data:
            result.append({
                'person_id': i[0],
                'organization_id': i[1],
                'name': i[2],
                'contact': i[3],
                'alt_contact': i[4],
                'email': i[5],
                'alt_email': i[6],
                'linkedin_url': i[7],
                'cb_url': i[8],
                'department': i[9],
                'designation': i[10],
                'is_decision_maker': i[11],
                'created_by': i[12],
                'dt': str(i[13]),
                'status': i[14]
            })
        # print(result)
        return result

    @staticmethod
    def get_record_by_person_id(id):
        data = person_orm.search_by_person_id(id)
        result = []
        for i in data:
            result.append({
                'person_id': i[0],
                'organization_id': i[1],
                'name': i[2],
                'contact': i[3],
                'alt_contact': i[4],
                'email': i[5],
                'alt_email': i[6],
                'linkedin_url': i[7],
                'cb_url': i[8],
                'department': i[9],
                'designation': i[10],
                'is_decision_maker': i[11],
                'created_by': i[12],
                'dt': str(i[13]),
                'status': i[14]
            })
        # print(result)
        return result

    @staticmethod
    def get_record_by_organization_id(id):
        data = person_orm.search_by_organization_id(id)
        result = []
        for i in data:
            result.append({
                'person_id': i[0],
                'organization_id': i[1],
                'name': i[2],
                'contact': i[3],
                'alt_contact': i[4],
                'email': i[5],
                'alt_email': i[6],
                'linkedin_url': i[7],
                'cb_url': i[8],
                'department': i[9],
                'designation': i[10],
                'is_decision_maker': i[11],
                'created_by': i[12],
                'dt': str(i[13]),
                'status': i[14]
            })
        # print(result)
        return result
