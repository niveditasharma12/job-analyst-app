import logging
import traceback

from flask import request, send_file, abort, jsonify, session
from flask_cors import cross_origin

from ..database import connector
from flask_restx import Resource
from werkzeug.datastructures import FileStorage

from ..service.person_service import personservice
from ..service.login_service import login_required
from ..service.organization_service import organizationservice
from ..database import connector
from ..util.dto import PersonsDto
from ..util.utilities import Utilities
from ..service.constant_service import ConstantService

api = PersonsDto.api
upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage)
upload_parser.add_argument('source', location='query', type=str)


@api.route('/insert_persons')
class insert_person(Resource):
    @staticmethod
    def validate_person(contact, email):
        result = personservice.get_person()
        print(result)
        for i in result:
            if i['email'] == email:  # or i['contact'] == contact: todo to add contact for verification
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

    @api.doc(params={'data': {'description': 'Input Data',
                              'in': 'body',
                              'type': 'json',
                              'example': {"organization_id": 5,
                                          "name": "test",
                                          "contact": "7812345678",
                                          "alt_contact":"9212345678",
                                          "email":"test@test.com",
                                          "alt_email":"test1@test.com",
                                          "linkedin_url":"linkedin.com/test",
                                          "cb_url":"",
                                          "department":"IT",
                                          "designation":"Analyst",
                                          "is_decision_maker":1}}
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
            # data["created_by"] = ConstantService.getdefaultuser()
            valid_input, msg = Utilities.validate_person_input(data)
            if valid_input:
                # data["contact"] = " "
                contact = data.get("contact")
                email = data.get("email")
                validate_person = insert_person.validate_person(contact, email)
                if validate_person == True:
                    fk_validation = insert_person.validate_org_foreign_key(data.get("organization_id"))
                    if fk_validation:
                        result = personservice.insert1(data)
                        person_id = personservice.get_max_id()
                        person_id = person_id[0]["person_id"]
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
                                "Person_id": person_id,
                                "code": 200,
                            }
                            return jsonify(response)
                    else:
                        response = {
                            "status": False,
                            "message": "Entered Organization_id does not exist in organization table!",
                            "code": 404,
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


@api.route('/searchperson')
class search(Resource):
    @api.doc(params={
        'name': 'name', 'email': 'email', "organization_name": "organization_name",
        "website": "website"
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
            data["email"] = request.args.get('email')
            data["organization_name"] = request.args.get('organization_name')
            data["website"] = request.args.get('website')
            dict_len = 0
            query_dict = {}
            for key, value in data.items():
                if value is not None and not value.startswith(" ") and value.lower() != "none" and value != "":
                    query_dict[key] = value
                    dict_len += 1
            if dict_len > 0:
                result = personservice.search_person(query_dict)
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


@api.route('/getallperson')
class GetAllPerson(Resource):
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
            result = personservice.get_person()
            if result:
                response = {"status": True,
                            "message": "successfully fetch the record",
                            "code": 200,
                            "result": result
                            }
                return jsonify(response)
            else:
                response = {"status": False,
                            "message": "No data in database",
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


@api.route('/getlasttenperson')
class GetRecentPerson(Resource):
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
            result = personservice.get_recent_person()
            if result:
                response = {"status": True,
                            "message": "successfully fetch the record",
                            "code": 200,
                            "result": result
                            }
                return jsonify(response)
            else:
                response = {"status": False,
                            "message": "No data in database",
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


@api.route('/showbypersonid')
class GetPersonByID(Resource):
    @api.doc(params={
        'person_id': 'person_id'
    })
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
            person_id = request.args.get('person_id')
            if person_id is not None and person_id.isdigit():
                result = personservice.get_record_by_person_id(person_id)
                if result:
                    response = {"status": True,
                                "message": "successfully fetch the record",
                                "code": 200,
                                "result": result
                                }
                    return jsonify(response)
                else:
                    response = {"status": False,
                                "message": "Entity does not Exists. Please enter valid Id",
                                "code": 404,
                                }
                    return jsonify(response)
            else:
                response = {
                    "status": False,
                    "message": "Please Enter a valid person id",
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


@api.route('/showbyorganizationid')
class GetPersonByOrgID(Resource):
    @api.doc(params={
        'organization_id': 'organization_id'
    })
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
            org_id = request.args.get('organization_id')
            if org_id is not None and org_id.isdigit():
                result = personservice.get_record_by_organization_id(org_id)
                if result:
                    response = {"status": True,
                                "message": "successfully fetch the record",
                                "code": 200,
                                "result": result
                                }
                    return jsonify(response)
                else:
                    response = {"status": False,
                                "message": "Entity is not Exists. Please enter valid Id",
                                "code": 404,
                                }
                    return jsonify(response)
            else:
                response = {
                    "status": False,
                    "message": "Please Enter a valid organization id",
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
