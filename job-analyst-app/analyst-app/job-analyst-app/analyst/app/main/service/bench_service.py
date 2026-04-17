from ..database.bench_orm import bench_orm
from ..util.utilities import Utilities
# from ..util.utilities import Utilities


class bench_service(object):
    @staticmethod
    def insert_bench1(data):
        status = bench_orm.insert_bench(data)
        return status

    @staticmethod
    def get_bench():
        data = bench_orm.select_bench()
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result

    @staticmethod
    def get_recent_bench():
        data = bench_orm.select_recent_ten_bench()
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result

    @staticmethod
    def get_bench_by_id(bench_id):
        data = bench_orm.select_bench_by_id(bench_id)
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result

    @staticmethod
    def edit_record(update_set, id):
        status = bench_orm.edit_bench(update_set, id)
        return status

    @staticmethod
    def search_bench(query_dict):
        where = Utilities.construct_where_clause_from_dict(query_dict)
        data = bench_orm.search_in_bench(where)
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result

    @staticmethod
    def getrecordByname(name):
        data = bench_orm.search_by_name(name)
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result

    @staticmethod
    def getrecordBycontact(contact):
        data = bench_orm.search_by_contact(contact)
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result

    @staticmethod
    def getrecordByexp(exp):
        data = bench_orm.search_by_exp(exp)
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result

    @staticmethod
    def getrecordBydomain(domain):
        data = bench_orm.search_by_domain(domain)
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result

    @staticmethod
    def getrecordByprimaryskill(primary_skill):
        data = bench_orm.search_by_primary_skill(primary_skill)
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result

    @staticmethod
    def getrecordBysecondaryskill(secondary_skill):
        data = bench_orm.search_by_secondary_skill(secondary_skill)
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result

    @staticmethod
    def getrecordBybenchststus(bench_status):
        data = bench_orm.search_by_bench_status(bench_status)
        result = []
        for i in data:
            result.append({
                'client_id': i[0], 'bench_id': i[1], 'name': i[2], 'contact': i[3], 'alternate_contact': i[4],
                'email': i[5], 'alternate_email': i[6], 'exp': i[7], 'domain': i[8], 'primary_skill': i[9],
                'secondary_skill': i[10],
                'current_role': i[11], 'qualification': i[12], 'resume': i[13],
                'bench_start_dt': str(i[14]), 'bench_end_dt': str(i[15]), 'bench_status': i[16], 'created_by': i[17],
                'dt': str(i[18]), 'status': i[19]
            })
        return result
