import logging
import traceback

from flask import request, send_file, abort, jsonify, session
from flask_cors import cross_origin

from ..database import connector
from flask_restx import Resource
from werkzeug.datastructures import FileStorage

from ..service.proposal_service import ProposalService
from ..service.proposal_service import Proposal_Info_Service
from ..service.prospect_service import ProspectService
from ..service.login_service import login_required
from ..util.dto import ProposalDto
from ..util.utilities import Utilities
from ..service.constant_service import ConstantService
api = ProposalDto.api
upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage)
upload_parser.add_argument('source', location='query', type=str)


@api.route('/insert_proposal')
class Insert_Proposal(Resource):
    @staticmethod
    def validate_prospect_foreign_key(prospect_id):
        result = ProspectService.get_record_by_id(prospect_id)
        if len(result) > 0:
            return True
        return False

    @api.doc(params={'prospect_id':'prospect_id','organization_id':'organization_id','proposal_types':'proposal_types',
                     'proposal_analysis':'proposal_analysis','proposal_offers':'proposal_offers',
                     'proposal_priority':'proposal_priority','proposal_assignee':'proposal_assignee'
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
                "prospect_id": request.args.get('prospect_id'),
                'organization_id': request.args.get('organization_id'),
                'proposal_types': str(request.args.get('proposal_types')),
                'prospect_analysis': str(request.args.get('proposal_analysis')),
                'proposal_offers': str(request.args.get('proposal_offers')),
                'proposal_priority': request.args.get('proposal_priority'),
                'proposal_assignee': session["username"],
            }
            # data = request.get_json()
            valid_input, msg = Utilities.validate_proposal_input(data)
            if valid_input:
                prospect_id = data.get("prospect_id")
                validate_proposal = ProposalService.validate_proposal(prospect_id)
                if validate_proposal == True:
                    fk_validation = ProposalService.validate_org_foreign_key(data.get("organization_id"))
                    if fk_validation:
                        prospect_fk_validation = Insert_Proposal.validate_prospect_foreign_key(prospect_id)
                        if prospect_fk_validation:
                            # Run Service Layer & Run the Business Logic Layer
                            result = ProposalService.Insert1(data)
                            if result==None:
                                response={
                                    "status": False,
                                    "message": "Unable to insert",
                                    "code": 404,
                                    }

                                return jsonify(response)
                            else:
                                response = {
                                    "status": True,
                                    "message": "successfully insert the record",
                                    "Proposal_id": result,
                                    "code": 200,
                                 }

                                return jsonify(response)
                        else:
                            response = {
                                "status": False,
                                "message": "Entered prospect_id does not exist in prospects table!",
                                "code": 404,
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
                        "message": "prospect_id already exists!",
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


@api.route('/get_all_proposal')
class ShowRecord(Resource):
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
            result = ProposalService.get_record()
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


@api.route('/get_last_ten_proposal')
class GetRecentProposal(Resource):
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
            result = ProposalService.get_recent_record()
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


@api.route('/search_proposal')
class Searchproposal(Resource):
    @api.doc(params={'proposal_types':'proposal_types', 'from_date':'from_date', 'to_date':'to_date'})
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
            data = {
                'proposal_types': str(request.args.get('proposal_types')),
                'from_dt': str(request.args.get('from_date')),
                'to_dt': str(request.args.get('to_date'))
            }
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
                    result = ProposalService.search_proposal(query_dict)
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


@api.route('/search_proposal_by_prospect_id_organization_id')
class SearchRecord(Resource):
    @api.doc(params={'prospect_id':'prospect_id','organization_id':'organization_id'})
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
            data = {
                'prospect_id': str(request.args.get('prospect_id')),
                'organization_id': str(request.args.get('organization_id'))
            }
            dict_len = 0
            query_dict = {}
            for key, value in data.items():
                if value is not None and not value.startswith(" ") and value.lower() != "none" and value != "":
                    query_dict[key] = value
                    dict_len += 1
            if dict_len > 0:
                result = ProposalService.search_proposal(query_dict)
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


#------------------------------------Proposal_Info-----------------------------------------------------------------------------------

@api.route('/insert_proposal_info')
class Insert_Proposal_Info(Resource):
    @staticmethod
    def validate_proposal_info(proposal_info_id, proposal_type):
        result = Proposal_Info_Service.get_record_proposal_info()
        for i in result:
            if i['proposal_id'] == int(proposal_info_id):
                return False
            elif i["proposal_type"] == proposal_type:
                return 2
            else:
                continue
        return True

    @staticmethod
    def validate_foreign_key(proposal_id):
        result = ProposalService.get_record()
        for i in result:
            if i['proposal_id'] == int(proposal_id):
                return True
            else:
                continue
        return False

    @api.doc(params={'proposal_id': 'proposal_id','proposal_type':'proposal_type','proposal_sender':'proposal_sender','proposal_detail':'proposal_detail'
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
                "proposal_id": request.args.get('proposal_id'),
                "proposal_type": request.args.get('proposal_type'),
                'proposal_sender': request.args.get('proposal_sender'),
                'proposal_detail': request.args.get('proposal_detail')
            }
            # data = request.get_json()
            valid_input, msg = Utilities.validate_proposal_info_input(data)
            if valid_input:
                proposal_info_id = data.get("proposal_id")
                proposal_type = data.get("proposal_type")
                validate_proposal = Insert_Proposal_Info.validate_proposal_info(proposal_info_id,proposal_type)
                if validate_proposal == True:
                    fk_validation = Insert_Proposal_Info.validate_foreign_key(data.get("proposal_id"))
                    if fk_validation:
                        result = Proposal_Info_Service.Insert_Propoal_Info(data)
                        if result==None:
                            response={
                                "status": False,
                                "message": "unsuccessful to insert",
                                "code": 404,
                                }

                            return jsonify(response)
                        else:
                            response = {
                                "status": True,
                                "message": "successfully insert the record",
                                "proposal_info_id": result,
                                "code": 200,
                             }

                            return jsonify(response)
                    else:
                        response = {
                            "status": False,
                            "message": "Entered Proposal_id does not exist in proposals table!",
                            "code": 404,
                        }
                        return jsonify(response)
                elif validate_proposal == False:
                    response = {
                        "status": False,
                        "message": "proposal_id is already exist!",
                        "code": 404,
                    }
                    return jsonify(response)
                else:
                    response = {
                        "status": False,
                        "message": "proposal_type is already exist!",
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


@api.route('/get_all_proposal_info')
class ShowRecord1(Resource):
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
            result = Proposal_Info_Service.get_record_proposal_info()
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


@api.route('/get_last_ten_proposal_info')
class GetRecentProposalInfo(Resource):
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
            result = Proposal_Info_Service.get_recent_proposal_info()
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


@api.route('/search_proposal_info_by_proposal_id_proposal_date')
class SearchRecord1(Resource):
    @api.doc(params={'proposal_id':'proposal_id','proposal_date':'proposal_date'})
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
            data = {
                'proposal_id': request.args.get('proposal_id'),
                'proposal_date': request.args.get('proposal_date')
            }
            dict_len = 0
            query_dict = {}
            for key, value in data.items():
                if value is not None and not value.startswith(" ") and value.lower() != "none" and value != "":
                    query_dict[key] = value
                    dict_len += 1
            if dict_len > 0:
                result = Proposal_Info_Service.search_proposal_info(query_dict)
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
