import logging
import traceback

from flask import request, send_file, abort, jsonify, session
from flask_cors import cross_origin

from flask_restx import Resource
from werkzeug.datastructures import FileStorage

from ..service.source_service import sourceservice
from ..service.login_service import login_required
from ..util.dto import SourceDto
from ..util.utilities import Utilities

api = SourceDto.api
upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage)
upload_parser.add_argument('source', location='query', type=str)


@api.route('/insert_source')
class insert_source(Resource):
    @staticmethod
    def validate_source(source_url):
        result = sourceservice.get_source()
        print(result)
        for i in result:
            if i['source_url'] == source_url:
                return False
            else:
                continue
        return True

    @api.doc(params={'data': {'description': 'Input Data',
                              'in': 'body',
                              'type': 'json',
                              'example': {"source_name": "abc",
                                          "source_url": "www.abc.com",
                                          "source_type": "type",
                                          "is_paid_or_not": 1,
                                          "is_contact": 1,
                                          "is_mail": 0,
                                          "is_social_media": 1,
                                          "is_revenue": 1,
                                          "is_services": 0,
                                          "is_industry": 1
                                          }}
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
            data["created_by"] = session["username"]
            valid_input, msg = Utilities.validate_source_input(data)
            if valid_input:
                source_url = data.get("source_url")
                validate_source = insert_source.validate_source(source_url)
                if validate_source == True:
                    result, source_id = sourceservice.insert_source1(data)
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
                            "Source ID": source_id,
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


@api.route('/searchsource/')
class search(Resource):
    @api.doc(params={
        'source_url': 'source_url', 'source_id': 'source_id',
        'source_name': 'source_name', 'source_type': 'source_type',
        'is_paid_or_not': 'is_paid_or_not', 'is_contact': 'is_contact',
        'is_mail': 'is_mail', 'is_social_media': 'is_social_media',
        'is_revenue': 'is_revenue', 'is_services': 'is_services', 'is_industry': 'is_industry'
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
            data["source_url"] = request.args.get('source_url')
            data["source_id"] = request.args.get('source_id')
            data["source_name"] = request.args.get('source_name')
            data["source_type"] = request.args.get('source_type')
            data["is_paid_or_not"] = request.args.get('is_paid_or_not')
            data["is_contact"] = request.args.get('is_contact')
            data["is_mail"] = request.args.get('is_mail')
            data["is_social_media"] = request.args.get('is_social_media')
            data["is_revenue"] = request.args.get('is_revenue')
            data["is_services"] = request.args.get('is_services')
            data["is_industry"] = request.args.get('is_industry')
            dict_len = 0
            query_dict = {}
            for key, value in data.items():
                if value is not None and not value.startswith(" ") and value.lower() != "none" and value != "":
                    query_dict[key] = value
                    dict_len += 1
            if dict_len > 0:
                result = sourceservice.search_source(query_dict)
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


@api.route('/getallsource/')
class GetAllSource(Resource):
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
            result = sourceservice.get_source()
            if result:
                response = {"status": True,
                            "message": "Successfully fetch the record",
                            "result": result
                            }
                return jsonify(response)
            else:
                response = {"status": False,
                            "message": "Not found",
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


@api.route('/getlasttensource/')
class GetRecentSource(Resource):
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
            result = sourceservice.get_recent_source()
            if result:
                response = {"status": True,
                            "message": "Successfully fetch the record",
                            "result": result
                            }
                return jsonify(response)
            else:
                response = {"status": False,
                            "message": "Not found",
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
