from ..database.source_orm import source_orm
from ..util.utilities import Utilities


class sourceservice(object):
    @staticmethod
    def insert_source1(data):
        # print(data)

        # Call the ORM or Database Layer

        status, source_id = source_orm.insert_source(data)

        return status, source_id

    @staticmethod
    def get_max_source_id():
        data = source_orm.source_max_id()
        result = []
        for i in data:
            result.append({
                'source_id': i[0],
            })
        return result

    @staticmethod
    def get_source():
        data = source_orm.select_source()
        result = []
        for i in data:
            result.append({
                "source_id": i[0],
                "source_name": i[1],
                "source_url": i[2],
                "source_type": i[3],
                "is_paid_or_not": i[4],
                "is_contact": i[5],
                "is_mail": i[6],
                "is_social_media": i[7],
                "is_revenue": i[8],
                "is_services": i[9],
                "is_industry": i[10],
                "created_by": i[11],
                "dt": str(i[12]),
                "status": i[13]
            })
        return result

    @staticmethod
    def get_recent_source():
        data = source_orm.select_recent_source()
        result = []
        for i in data:
            result.append({
                "source_id": i[0],
                "source_name": i[1],
                "source_url": i[2],
                "source_type": i[3],
                "is_paid_or_not": i[4],
                "is_contact": i[5],
                "is_mail": i[6],
                "is_social_media": i[7],
                "is_revenue": i[8],
                "is_services": i[9],
                "is_industry": i[10],
                "created_by": i[11],
                "dt": str(i[12]),
                "status": i[13]
            })
        return result

    @staticmethod
    def search_source(query_dict):
        where = Utilities.construct_where_clause_from_dict(query_dict)
        data = source_orm.search_in_sources(where)
        result = []
        for i in data:
            result.append({
                "source_id": i[0],
                "source_name": i[1],
                "source_url": i[2],
                "source_type": i[3],
                "is_paid_or_not": i[4],
                "is_contact": i[5],
                "is_mail": i[6],
                "is_social_media": i[7],
                "is_revenue": i[8],
                "is_services": i[9],
                "is_industry": i[10],
                "created_by": i[11],
                "dt": str(i[12]),
                "status": i[13]
            })
        return result

    @staticmethod
    def search_source_by_id(source_url):
        data = source_orm.search_by_id(source_url)
        result = []
        for i in data:
            result.append({
                "source_id": i[0],
                "source_name": i[1],
                "source_url": i[2],
                "source_type": i[3],
                "is_paid_or_not": i[4],
                "is_contact": i[5],
                "is_mail": i[6],
                "is_social_media": i[7],
                "is_revenue": i[8],
                "is_services": i[9],
                "is_industry": i[10],
                "created_by": i[11],
                "dt": str(i[12]),
                "status": i[13]
            })
        return result
