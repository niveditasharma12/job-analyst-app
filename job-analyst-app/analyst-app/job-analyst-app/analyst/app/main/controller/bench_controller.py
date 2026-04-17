import logging
import traceback

from flask import request, send_file, abort, jsonify, session
from flask_cors import cross_origin

from flask_restx import Resource
from werkzeug.datastructures import FileStorage

from ..service.bench_service import bench_service
from ..service.login_service import login_required
from ..util.dto import BenchDto
from ..util.utilities import Utilities

api = BenchDto.api
upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage)
upload_parser.add_argument('source', location='query', type=str)


@api.route('/insert_bench')
class insert_add_bench(Resource):
    @staticmethod
    def validate_bench(client_id):
        result = bench_service.get_bench()
        for i in result:
            if i['client_id'] == client_id:
                return False
            else:
                continue
        return True

    @api.doc(params={'data': {'description': 'Input Data',
                              'in': 'body',
                              'type': 'json',
                              'example': {
                                  "client_id": "1011",
                                  "name": "rishav",
                                  "contact": "1234567890",
                                  "alternate_contact": "0987654321",
                                  "email": "rt@gmail.com",
                                  "alternate_email": "r00@gmail.com",
                                  "exp": "11",
                                  "domain": "IT",
                                  "primary_skill": "Python",
                                  "secondary_skill": "C",
                                  "current_role": "Tech",
                                  "qualification": "Btech",
                                  "resume": "okay",
                                  "bench_start_dt": "2022-02-01",
                                  "bench_end_dt": "2022-02-27",
                              }
                              }
                     })
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def post(self):
        try:
            login_result = login_required()
            if not login_result:
                response = {
                    "status": False,
                    "code": 111,
                    "message": "Login required",
                }
                return jsonify(response)
            data = request.get_json()
            valid_input, msg = Utilities.validate_bench_input(data)
            if valid_input:
                client_id = data.get("client_id")
                validate_bench = insert_add_bench.validate_bench(client_id)
                if validate_bench == True:
                    data["bench_status"] = "1"
                    data["created_by"] = session["username"]
                    result = bench_service.insert_bench1(data)
                    if result == None:
                        response = {
                            "status": False,
                            "message": "unsuccessful to insert",
                            "code": 404,
                        }
                        return jsonify(response)
                    else:
                        response = {
                            "status": True,
                            "message": "successfully insert the record",
                            "code": 200,
                        }
                        return jsonify(response)
                else:
                    response = {
                        "status": False,
                        "message": " already exist!!",
                        "code": 404,
                    }
                    return jsonify(response)
            else:
                response = {
                    "status": False,
                    "message": msg,
                    "code": 404,
                }
                return jsonify(response)
        except Exception as e:
            print(str(traceback.format_exc()))
            logging.error(str(e))
            response = {
                "status": False,
                "message": "Sorry an error occurred",
                "error": str(e),
                "code": 500,
            }
            return jsonify(response)


@api.route('/edit_bench')
class Editbench(Resource):
    @api.doc(params={'data': {'description': 'Input Data',
                              'in': 'body',
                              'type': 'json',
                              'example': {
                                  "bench_id": "1",
                                  "client_id": "1011",
                                  "name": "rishav",
                                  "contact": "1234567890",
                                  "alternate_contact": "0987654321",
                                  "email": "rt@gmail.com",
                                  "alternate_email": "r00@gmail.com",
                                  "exp": "11",
                                  "domain": "IT",
                                  "primary_skill": "Python",
                                  "secondary_skill": "C",
                                  "current_role": "Tech",
                                  "qualification": "Btech",
                                  "resume": "okay",
                                  "bench_start_dt": "2022-02-01",
                                  "bench_end_dt": "2022-02-27",
                              }
                              }
                     })
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def put(self):
        try:
            login_result = login_required()
            if not login_result:
                response = {
                    "status": False,
                    "code": 111,
                    "message": "Login required",
                }
                return jsonify(response)
            data = request.get_json()
            bench_id = data.pop("bench_id", "key not found")
            if bench_id == "key not found" or bench_id is None or str(bench_id).startswith(" ") or bench_id == "" or not str(bench_id).isdigit():
                response = {
                    "status": False,
                    "message": "Enter valid bench_id",
                    "code": 404,
                }
                return jsonify(response)
            else:
                dict_len, update_dict = Utilities.validate_update_input(data)
                if dict_len > 0:
                    valid_input, msg = Utilities.validate_org_input(update_dict)
                    if valid_input:
                        check_bench_by_id = bench_service.get_bench_by_id(bench_id)
                        if len(check_bench_by_id) > 0:
                            update_dict['created_by'] = session["username"]
                            update_dict["bench_status"] = "1"
                            update_set = Utilities.create_update_set_from_dict(update_dict)
                            result = bench_service.edit_record(update_set, bench_id)
                            if result == None:
                                response = {
                                    "status": False,
                                    "message": "Not Able to update",
                                    "code": 404
                                }
                                return jsonify(response)
                            else:
                                response = {
                                    "status": True,
                                    "message": "Updated successfully",
                                    "code": 201
                                }
                                return jsonify(response)
                        else:
                            response = {
                                "status": False,
                                "message": "bench_id does not exist in Bench table",
                                "code": 404
                            }
                            return jsonify(response)
                    else:
                        response = {
                            "status": False,
                            "message": msg,
                            "code": 404,
                        }
                        return jsonify(response)
                else:
                    response = {
                        "status": False,
                        "message": "Atleast one field along with organization_id is required",
                        "code": 404
                    }
                    return jsonify(response)
        except Exception as e:
            print(str(traceback.format_exc()))
            logging.error(str(e))
            response = {
                "status": False,
                "message": "Sorry an error occurred",
                "error": str(e),
                "code": 500,
            }
            return jsonify(response)


@api.route('/searchbench/')
class searchbench(Resource):
    @api.doc(params={
        'name': 'name', 'contact': 'contact', 'exp': 'exp', 'domain': 'domain', 'primary_skill': 'primary_skill',
        'secondary_skill': 'secondary_skill', 'bench_status': 'bench_status'
    })
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def get(self):
        try:
            login_result = login_required()
            if not login_result:
                response = {
                    "status": False,
                    "code": 111,
                    "message": "Login required",
                }
                return jsonify(response)
            data = {}
            data["name"] = request.args.get('name')
            data["contact"] = request.args.get('contact')
            data["exp"] = request.args.get('exp')
            data["domain"] = request.args.get('domain')
            data["primary_skill"] = request.args.get('primary_skill')
            data["secondary_skill"] = request.args.get('secondary_skill')
            data["bench_status"] = request.args.get('bench_status')
            dict_len = 0
            query_dict = {}
            for key, value in data.items():
                if value is not None and not value.startswith(" ") and value.lower() != "none" and value != "":
                    query_dict[key] = value
                    dict_len += 1
            if dict_len > 0:
                result = bench_service.search_bench(query_dict)
                if result:
                    response = {"status": True,
                                "message": "successfully fetch the record",
                                "code": 200,
                                "result": result
                                }

                    return jsonify(response)
                else:
                    response = {"status": False,
                                "message": "Data not found",
                                "code": 404,
                                }
                return jsonify(response)
            else:
                response = {"status": False,
                            "message": "Please Enter atleast one entity to search",
                            "code": 404,
                            }
                return jsonify(response)
        except Exception as e:
            print(str(traceback.format_exc()))
            logging.error(str(e))
            response = {
                "status": False,
                "message": "Sorry an error occurred",
                "error": str(e),
                "code": 500,
            }
            return jsonify(response)

@api.route('/getallbenchdata')
class GetAllBench(Resource):
    @api.doc(params={
    })
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def get(self):
        try:
            login_result = login_required()
            if not login_result:
                response = {
                    "status": False,
                    "code": 111,
                    "message": "Login required",
                }
                return jsonify(response)
            result = bench_service.get_bench()
            if result:
                response = {"status": True,
                            "message": "Successfully fetched the record",
                            "result": result
                            }
                return jsonify(response)
            else:
                response = {"status": False,
                            "message": "Data not found",
                            "code": 404,
                            }
                return jsonify(response)
        except Exception as e:
            print(str(traceback.format_exc()))
            logging.error(str(e))
            response = {
                "status": False,
                "message": "Sorry an error occurred",
                "error": str(e),
                "code": 500,
            }
            return jsonify(response)


@api.route('/getlasttenbenchdata')
class GetRecentBench(Resource):
    @api.doc(params={
    })
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def get(self):
        try:
            login_result = login_required()
            if not login_result:
                response = {
                    "status": False,
                    "code": 111,
                    "message": "Login required",
                }
                return jsonify(response)
            result = bench_service.get_recent_bench()
            if result:
                response = {"status": True,
                            "message": "Successfully fetched the record",
                            "result": result
                            }
                return jsonify(response)
            else:
                response = {"status": False,
                            "message": "Data not found",
                            "code": 404,
                            }
                return jsonify(response)
        except Exception as e:
            print(str(traceback.format_exc()))
            logging.error(str(e))
            response = {
                "status": False,
                "message": "Sorry an error occurred",
                "error": str(e),
                "code": 500,
            }
            return jsonify(response)
