import logging
import traceback
from flask import request, send_file, abort, jsonify, session
from flask_cors import cross_origin

from flask_restx import Resource
from werkzeug.datastructures import FileStorage
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity

from ..service.proposal_service import ProposalService
from ..service.prospect_service import ProspectService
from ..service.login_service import login_required
from ..util.dto import JobPostDto
from ..util.utilities import Utilities
from ..util.mail_utilities import MailUtilities
from ..service.constant_service import ConstantService

api = JobPostDto.api
upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage)
upload_parser.add_argument('source', location='query', type=str)


@api.route('/insertprospect')
class insert1(Resource):
    @staticmethod
    def validate_prospect(prospect_link):
        result = ProspectService.get_record()
        # print(result)
        for i in result:
            if i['prospect_link'] == prospect_link:
                return False

            else:
                continue

        return True

    @api.doc(
        params={'data': {'description': 'Input Data',
                         'in': 'body',
                         'type': 'json',
                         'example': {"account_at_source": "https://www.dice.com/company/10513378",
                                     "comments": "",
                                     "contact_person_ids": 1,
                                     "duration": "12 Months",
                                     "engagement_mode": "Contract",
                                     "is_fte": "1",
                                     "job_location": "Texas, US",
                                     "job_role": "Senior UI developer",
                                     "max_cost": 0,
                                     "min_cost": 0,
                                     "organization_id": 5,
                                     "post_date": "2022-09-10",
                                     "proposal_offers": "",
                                     "prospect_analysis": "",
                                     "prospect_link": "https://www.dice.com/jobs/detail/Senior-UI-Developer-Digital-Minds-Technologies-Inc.---/10513378/7589276",
                                     "prospect_title": "Title",
                                     "prospect_type": "JOB-POST-WF",
                                     "source": "Dice.com",
                                     "technologies": "HTML, CSS, Javascript",
                                     "timezone": "",
                                     "working_mode": "Remote"}}
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
            valid_input, msg = Utilities.validate_prospect_input(data)
            if valid_input:
                validate_prospect = insert1.validate_prospect(data["prospect_link"])
                if validate_prospect == True:
                    # Run Service Layer & Run the Business Logic Layer
                    data["created_by"] = session["username"]
                    result, prospect_id = ProspectService.insert1(data)
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
                            "prospect_id": prospect_id,
                            "code": 200,
                         }

                        return jsonify(response)
                else:
                    response = {
                        "status": False,
                        "message": "prospect already exists!",
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


@api.route('/getallprospect')
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
            result = ProspectService.get_record()
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


@api.route('/getlasttenprospects')
class ShowRecentRecord(Resource):
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
            result = ProspectService.get_recent_ten_records()
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


@api.route('/getprospectbyid')
class Show(Resource):
    @api.doc(
        params={'prospect_id': {'description': 'Prospect ID', 'in': 'query', 'type': 'str'}})
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
            prospect_id = request.args.get("prospect_id")
            if prospect_id is not None and prospect_id.isdigit():
                result = ProspectService.get_record_by_id(prospect_id)
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
                    "message": "Please Enter a integer value only",
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


@api.route('/deleteprospectbyid')
class delete_record(Resource):
    @api.doc(
        params={'prospect_id': {'description': 'Prospect ID', 'in': 'query', 'type': 'str'}})
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def delete(self):
        try:
            login_result = login_required()
            if not login_result:
                response = {
                    "status": False,
                    "code": 111,
                    "message": "Login required",
                }
                return jsonify(response)
            prospect_id = request.args.get("prospect_id")
            if prospect_id != None and prospect_id.isdigit():
                result = ProspectService.delete_record(prospect_id)
                if result == None:
                    response = {
                        "status": True,
                        "message": "Deleted Successfully",
                        "code": 204
                    }

                    return jsonify(response)
                else:
                    response={
                        "status":False,
                        "message":"Please Enter a Valid Entity",
                        "code": 404
                    }
                    return jsonify(response)
            else:
                response = {
                    "status": False,
                    "message": "Please Enter a integer value only",
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


@api.route('/updateprospect')
class updateRecord(Resource):
    @api.doc(
        params={'data': {'description': 'Input Data',
                         'in': 'body',
                         'type': 'json',
                         'example': {"prospect_id": 2,
                                     "account_at_source": "https://www.dice.com/company/10513378",
                                     "comments": "",
                                     "contact_person_ids": 1,
                                     "duration": "12 Months",
                                     "engagement_mode": "Contract",
                                     "is_fte": "1",
                                     "job_location": "Texas, US",
                                     "job_role": "Senior UI developer",
                                     "max_cost": 0,
                                     "min_cost": 0,
                                     "organization_id": 5,
                                     "post_date": "2022-09-10",
                                     "progress": "IN-REVIEW",
                                     "proposal_offers": "",
                                     "prospect_analysis": "",
                                     "prospect_link": "https://www.dice.com/jobs/detail/Senior-UI-Developer-Digital-Minds-Technologies-Inc.---/10513378/7589276",
                                     "prospect_type": "JOB-POST-WF",
                                     "source": "Dice.com",
                                     "technologies": "HTML, CSS, Javascript",
                                     "timezone": "",
                                     "working_mode": "Remote"}}
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
            prospect_id = data.pop("prospect_id", "key not found")
            if prospect_id == "key not found" or prospect_id is None or str(prospect_id).startswith(" ") or prospect_id == "" or not str(prospect_id).isdigit():
                response = {
                    "status": False,
                    "message": "prospect_id should not be empty or None",
                    "code": 404,
                }
                return jsonify(response)
            dict_len, update_dict = Utilities.validate_update_input(data)
            if dict_len > 0:
                valid_input, msg = Utilities.validate_prospect_input(update_dict)
                if valid_input:
                    check_prospect_by_id = ProspectService.get_record_by_id(prospect_id)
                    if len(check_prospect_by_id) > 0:
                        update_set = Utilities.create_update_set_from_dict(update_dict)
                        # Run Service Layer & Run the Business Logic Layer
                        result = ProspectService.updateRecord(update_set, prospect_id)
                        if result==None:
                            response = {
                                "status": False,
                                "message": "Not able to update",
                                "code": 404
                            }
                            return jsonify(response)
                        else:
                            if "progress" in update_dict:
                                if update_dict["progress"] == "APPROVED":
                                    validate_proposal = ProposalService.validate_proposal(prospect_id)
                                    if validate_proposal == True:
                                        proposal_id = ProspectService.add_prospect_to_proposal(prospect_id)
                                        if proposal_id is not False:
                                            proposal_insert_msg = f"Prospect successfully inserted to proposal. Proposal id = {proposal_id}"
                                        else:
                                            proposal_insert_msg = "Prospect was not inserted into proposal"
                                        response = {
                                            "status": True,
                                            "message": "Updated Successfully",
                                            "prospect update": proposal_insert_msg,
                                            "code": 201
                                        }
                                        return jsonify(response)
                                    else:
                                        response = {
                                            "status": True,
                                            "message": "Updated Successfully",
                                            "prospect update": "Prospect already exist in proposal table",
                                            "code": 201
                                        }
                                        return jsonify(response)
                            else:
                                response = {
                                   "status": True,
                                   "message": "Updated Successfully",
                                   "code": 201
                                }
                                return jsonify(response)
                    else:
                        response = {
                            "status": False,
                            "message": "Prospect_id does not exist in prospect table",
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
                    "message": "Atleast one field along with prospect_id is required",
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


@api.route('/updateprospectprogress')
class UpdateProspectProgress(Resource):
    @api.doc(
        params={"prospect_id": "",
                "progress": ""}
    )
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
            prospect_id = request.args.get('prospect_id')
            progress = request.args.get('progress')
            if prospect_id is not None and not prospect_id.startswith(" ") \
                    and progress is not None and not progress.startswith(" "):
                result = ProspectService.update_progress(prospect_id, progress)
                if result is not None:
                    if progress == "APPROVED":
                        # result = ProspectService.get_record_by_id(prospect_id)
                        # result = result[0]
                        # emails = result["created_by"] + ", " + session["username"]
                        # MailUtilities.progress_approved_notification(emails, result["prospect_id"])
                        validate_proposal = ProposalService.validate_proposal(prospect_id)
                        if validate_proposal == True:
                            proposal_id = ProspectService.add_prospect_to_proposal(prospect_id)
                            if proposal_id is not False:
                                proposal_insert_msg = f"Prospect successfully inserted to proposal. Proposal id = {proposal_id}"
                            else:
                                proposal_insert_msg = "Prospect was not inserted into proposal"
                            response = {
                                "status": True,
                                "message": "Updated Successfully",
                                "prospect update": proposal_insert_msg,
                                "code": 201
                            }
                        else:
                            response = {
                                "status": True,
                                "message": "Updated Successfully",
                                "prospect update": "Prospect already exist in proposal table",
                                "code": 201
                            }
                    else:
                        response = {
                            "status": True,
                            "message": "Updated Successfully",
                            "code": 201
                        }
                    return jsonify(response)
                else:
                    response = {
                        "status": False,
                        "message": "Not able to update",
                        "code": 404
                    }
                    return jsonify(response)
            else:
                response = {
                    "status": False,
                    "message": "'prospect_id' and 'progress' field should not be empty.",
                    "code": 400
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


@api.route('/search')
class search(Resource):
    @api.doc(params={"job_role": "",
                     "progress": "",
                     "technologies": "",
                     "post_date": "",
                     "min_cost": "",
                     "max_cost": "",
                     "insertion_date": ""
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
            # data = request.get_json()
            data = {}
            data["job_role"] = str(request.args.get('job_role'))
            data["progress"] = str(request.args.get('progress'))
            data["technologies"] = str(request.args.get('technologies'))
            data["post_date"] = str(request.args.get('post_date'))
            data["min_cost"] = str(request.args.get('min_cost'))
            data["max_cost"] = str(request.args.get('max_cost'))
            data["dt"] = str(request.args.get('insertion_date'))
            dict_len = 0
            query_dict = {}
            for key, value in data.items():
                if value is not None and not value.startswith(" ") and value.lower() != "none" and value != "":
                    query_dict[key] = value
                    dict_len += 1
            if dict_len > 0:
                result = ProspectService.search_prospect(query_dict)
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


@api.route('/search_with_org_rank')
class searchWithOrgRank(Resource):
    @api.doc(params={"job_role": "",
                     "progress": "",
                     "technologies": "",
                     "post_date": "",
                     "min_cost": "",
                     "max_cost": "",
                     "insertion_date": "",
                     "org_rank": ""
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
            # data = request.get_json()
            data = {}
            data["job_role"] = str(request.args.get('job_role'))
            data["progress"] = str(request.args.get('progress'))
            data["technologies"] = str(request.args.get('technologies'))
            data["post_date"] = str(request.args.get('post_date'))
            data["min_cost"] = str(request.args.get('min_cost'))
            data["max_cost"] = str(request.args.get('max_cost'))
            data["dt"] = str(request.args.get('insertion_date'))
            data["org_rank"] = str(request.args.get('org_rank'))
            dict_len = 0
            query_dict = {}
            for key, value in data.items():
                if value is not None and not value.startswith(" ") and value.lower() != "none" and value != "":
                    query_dict[key] = value
                    dict_len += 1
            if dict_len > 0:
                result = ProspectService.search_prospect_org_rank(query_dict)
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


@api.route('/insertfollow_up')
class insert_follow_up(Resource):
    '''
    @staticmethod
    def validate_prospect(prospect):
        result = ProspectService.get_record()
        print(result)
        for i in result:
            if i['prospect'] == prospect:
                return False

            else:
                continue

        return True
    '''

    @api.doc(
        params={'data': {'description': 'Input Data',
                         'in': 'body',
                         'type': 'json',
                         'example': {"referenced_id": 5, "comments": "ABCD"}}
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
            data["followuper"] = session["username"]
            valid_input, msg = Utilities.validate_followup_input(data)
            if valid_input:
                result = ProspectService.insert_follow_up(data)
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
                            "follow_up_id" : result,
                            "code": 200,
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


@api.route('/getAllFollowupByReferenceId')
class ShowFollow(Resource):
    @api.doc(
        params={'referenced_id': {'description': 'referenced_id', 'in': 'query', 'type': 'str'}})
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
            follow_up_id = request.args.get('referenced_id')
            if follow_up_id != None and follow_up_id.isdigit():
                result = ProspectService.get_record_followup(follow_up_id)
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
                    "message": "Please enter a valid field",
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

@api.route('/getallfollowup')
class GetAllFollowUp(Resource):
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
            result = ProspectService.get_all_followup()
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


@api.route('/getlasttenfollowup')
class GetRecentFollowUp(Resource):
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
            result = ProspectService.get_recent_ten_followup()
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