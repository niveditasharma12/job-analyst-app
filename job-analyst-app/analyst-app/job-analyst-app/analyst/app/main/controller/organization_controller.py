# import data as data
import logging
import traceback

from flask import request, send_file, abort, jsonify, session
from flask_cors import cross_origin

from flask_restx import Resource
from werkzeug.datastructures import FileStorage

from ..service.organization_service import organizationservice
from ..util.dto import OrganizationDto
from ..service.constant_service import ConstantService
from ..service.login_service import login_required
from ..util.utilities import Utilities

api = OrganizationDto.api
upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage)
upload_parser.add_argument('source', location='query', type=str)


@api.route('/insert-organization')
class insert_org(Resource):
    @staticmethod
    def validate_lead(website):
        result = organizationservice.get_record()
        # print("result", result)
        for i in result:
            if i['website'] == website:
                return False
            else:
                continue
        return True

    @api.doc(params={
        'organization_name': 'organization_name', 'website':'website','industry': 'industry','service':'service','min_revenue':'min_revenue'
        ,'max_revenue':'max_revenue','country': 'country',
        'location': 'location', 'no_of_employees': 'no_of_employees','is_ind_operation':'is_ind_operation','rank':'rank','linkedin_url':'linkedin_url','cb_url':'cb_url'
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
            data = {
                "organization_name" : request.args.get('organization_name'),
                'website': request.args.get('website'),
                'industry': request.args.get('industry'),
                'service': request.args.get('service'),
                'min_revenue':  request.args.get('min_revenue'),
                'max_revenue': request.args.get('max_revenue'),
                'country': request.args.get('country'),
                'location': request.args.get('location'),
                'no_emp': request.args.get('no_of_employees'),
                'is_ind_operation': request.args.get('is_ind_operation'),
                'org_rank': request.args.get('rank'),
                'linkedin_url': request.args.get('linkedin_url'),
                'cb_url': request.args.get('cb_url'),
                'created_by': session["username"]
                # 'created_by': ConstantService.getdefaultuser()
            }
            # data = request.get_json()
            # print(data)
            valid_input, msg = Utilities.validate_org_input(data)
            if valid_input:
                data["website"] = Utilities.get_domain_name(data.get("website"))
                website = data.get("website")
                validate_lead = insert_org.validate_lead(website)
                if validate_lead == True:
                    result, org_id = organizationservice.insert1(data)
                    if result == None:
                        response = {
                            "status": False,
                            "message": "Failed to insert record",
                            "code": 404,
                        }
                        return jsonify(response)
                    else:
                        response = {
                            "status": True,
                            "message": "successfully inserted the record",
                            "organization id": org_id,
                            "code": 200,
                        }
                        return jsonify(response)
                else:
                    response = {
                        "status": False,
                        "message": " Organization already exists in data!!",
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


@api.route('/edit-organization')
class Edit(Resource):
    @api.doc(params={'organization_id': 'organization_id',
        'organization_name': 'organization_name', 'website': 'website', 'industry': 'industry', 'service': 'service',
        'min_revenue': 'min_revenue'
        , 'max_revenue': 'max_revenue', 'country': 'country',
        'location': 'location', 'no_of_employees': 'no_of_employees', 'is_ind_operation': 'is_ind_operation',
        'rank': 'rank', 'linkedin_url': 'linkedin_url', 'cb_url': 'cb_url'
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
            data= {
                "organization_name": request.args.get('organization_name'),
                'website': request.args.get('website'),
                'industry': request.args.get('industry'),
                'service': request.args.get('service'),
                'min_revenue': request.args.get('min_revenue'),
                'max_revenue': request.args.get('max_revenue'),
                'country': request.args.get('country'),
                'location': request.args.get('location'),
                'no_emp': request.args.get('no_of_employees'),
                'is_ind_operation': request.args.get('is_ind_operation'),
                'org_rank': request.args.get('rank'),
                'linkedin_url': request.args.get('linkedin_url'),
                'cb_url': request.args.get('cb_url'),
                # 'created_by': ConstantService.getdefaultuser()
            }

            # data = request.get_json()
            org_id = request.args.get('organization_id')
            if org_id != None and str(org_id).isdigit():
                dict_len, update_dict = Utilities.validate_update_input(data)
                if dict_len > 0:
                    valid_input, msg = Utilities.validate_org_input(update_dict)
                    if valid_input:
                        check_org_by_id = organizationservice.get_record_by_id(org_id)
                        if len(check_org_by_id) > 0:
                            update_dict['created_by'] = session["username"]
                            if "website" in update_dict:
                                update_dict["website"] = Utilities.get_domain_name(update_dict["website"])
                            update_set = Utilities.create_update_set_from_dict(update_dict)
                            result = organizationservice.edit_record(update_set, org_id)
                            if result == None:
                                response = {
                                    "status": False,
                                    "message": "Not able to update record",
                                    "code": 404
                                }
                                return jsonify(response)
                            else:
                                response = {
                                    "status": True,
                                    "message": "Updated the data successfully",
                                    "code": 201
                                }
                                return jsonify(response)
                        else:
                            response = {
                                "status": False,
                                "message": "organization_id does not exist in organization table",
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
            else:
                response = {
                    "status": False,
                    "message": "Enter valid organization id",
                    "code": 201
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


@api.route('/search-organization')
class search(Resource):
    @api.doc(params={
        'organization_name': 'Organization_name', 'website': 'Website', "from_dt": "From Date", "to_dt": "To date",
        'org_rank': "Organization Rank"
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
            data["organization_name"] = str(request.args.get('organization_name'))
            data["website"] = str(request.args.get('website'))
            data["from_dt"] = str(request.args.get("from_dt"))
            data["to_dt"] = str(request.args.get("to_dt"))
            data["org_rank"] = str(request.args.get("org_rank"))
            dict_len = 0
            query_dict = {}
            for key, value in data.items():
                if value is not None and not value.startswith(" ") and value.lower() != "none" and value != "":
                    query_dict[key] = value
                    dict_len += 1
            if dict_len > 0:
                if 'from_dt' in query_dict and 'to_dt' in query_dict:
                    if query_dict['to_dt'] >= query_dict['from_dt']:
                        dt_validate = True
                    else:
                        dt_validate = False
                elif 'from_dt' not in query_dict and 'to_dt' not in query_dict:
                    dt_validate = True
                else:
                    dt_validate = False
                if dt_validate:
                    result = organizationservice.search_organization(query_dict)
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
                                "message": "To search by date please enter both 'from date' and 'to date', and to date should be greater than from date.",
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


@api.route('/getorgbyid')
class OrgByID(Resource):
    @api.doc(params={
        'organization_id': 'organization ID'
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
            company_id = request.args.get('organization_id')
            # print(company_id)
            if company_id is not None:
                result = organizationservice.get_record_by_id(company_id)
                if result:
                    response = {"status": True,
                                "message": "Successfully fetched the record",
                                "result": result
                                }
                    return jsonify(response)
                else:
                    response = {"status": False,
                                "message": "Organization id not found in the data",
                                "code": 404,
                                }
                    return jsonify(response)
            else:
                response = {"status": False,
                            "message": "'Organization_id' field should not be empty",
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

@api.route('/getallorg')
class GetAllOrg(Resource):
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
            result = organizationservice.get_record()
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


@api.route('/getlasttenorg')
class GetRecentOrg(Resource):
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
            result = organizationservice.get_recent_ten_record()
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
