import re


class Utilities:
    @staticmethod
    def get_domain_name(url):
        url = url.rstrip('/')
        url = url.rstrip('#')
        url = url.rstrip('/')
        url = url.replace('http://', '')
        url = url.replace('https://', '')
        url = url.replace('www.', '')
        url = url.strip()
        url = url.lower()
        res = url.split('/')
        url = res[0].strip()
        url = url.split(":")[0].strip()
        return url

    @staticmethod
    def construct_where_clause_from_dict(query_dict):
        if len(query_dict) > 0:
            where = "where "
            for key, value in query_dict.items():
                if key.__contains__("date"):
                    where = where + str(key) + " >= '" + str(value) + "' and "
                elif key == "from_dt":
                    where = where + "DATE(dt) >= '" + str(value) + "' and "
                elif key == "to_dt":
                    where = where + "DATE(dt) <= '" + str(value) + "' and "
                elif key == "dt":
                    where = where + "DATE(dt) = '" + str(value) + "' and "
                elif value.isdigit():
                    where = where + str(key) + " like '" + str(value) + "' and "
                else:
                    where = where + str(key) + " like '%" + str(value) + "%' and "
            where = where.strip(" and ")
            return where
        else:
            return ""

    @staticmethod
    def validate_org_input(data):
        string_values = ["organization_name", "website", "location", "linkedin_url"]
        string_no_num_values = ["industry", "service", "country", "org_rank"]
        int_values = ["no_emp", "is_ind_operation"]
        double_values = ["min_revenue", "max_revenue"]
        for key, value in data.items():
            if key in string_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should not be empty or None"
                    return False, msg
            elif key in string_no_num_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should should not be empty or None"
                    return False, msg
                else:
                    if key == "org_rank":
                        if not value.isalpha():
                            msg = str(
                                key) + " should only contain alphabets, not numbers or special characters or white spaces"
                            return False, msg
                    else:
                        value_list = value.split(" ")
                        for val in value_list:
                            if not val.isalpha():
                                msg = str(key) + " should only contain alphabets, not numbers or special characters"
                                return False, msg
            elif key in int_values:
                if value is None or not value.isdigit():
                    msg = str(key) + " should not be empty and should be of integer type"
                    return False, msg
            elif key in double_values:
                if value is None or not value.isdigit():
                    msg = str(key) + " should not be empty and should be of integer or double type"
                    return False, msg
            else:
                continue
        return True, ""

    @staticmethod
    def is_invalid_email_address(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)):
            return False
        else:
            return True

    @staticmethod
    def validate_person_input(data):
        string_values = ["linkedin_url"]
        alpha_values = ["name", "department", "designation"]
        int_values = ["organization_id", "is_decision_maker"]
        contact_values = ["contact"]
        mail_string = ["email"]
        none_contact = ["alt_contact"]
        none_mail = ["alt_email"]
        for key, value in data.items():
            if key in int_values:
                if value is None or not str(value).isdigit() or str(value).startswith(" ") or str(value) == "":
                    msg = str(key) + " should not be empty and should be of integer type"
                    return False, msg
            elif key in contact_values:
                pass  # todo add below validation when contact is mandatory again
                # if value is None or not value.isdigit() or len(value) < 10:
                #     msg = str(key) + "should not be empty and Contact number should be properly filled"
                #     return False, msg
            elif key in none_contact:
                pass
                # if value is not None and not value.startswith(" "):
                #     if not value.isdigit() or len(value) < 10:
                #         msg = str(key) + "Contact number should be properly filled"
                #         return False, msg
            elif key in none_mail:
                if value is not None and value.startswith(" "):
                    if Utilities.is_invalid_email_address(value):
                        msg = str(key) + " - Email address should be properly filled"
                        return False, msg
            elif key in mail_string:
                if value is None or Utilities.is_invalid_email_address(value):
                    msg = str(key) + " - Email address should not be none and should be properly filled"
                    return False, msg
            elif key in string_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should not be empty or None"
                    return False, msg
            elif key in alpha_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should not be empty or None"
                    return False, msg
                else:
                    value_list = value.split(" ")
                    for val in value_list:
                        if not val.isalpha():
                            msg = str(key) + " should only contain alphabets, not numbers or special characters"
                            return False, msg
            else:
                continue
        return True, ""

    @staticmethod
    def is_int_or_float(value):
        if type(value) == int:
            return True
        if type(value) == float:
            return True
        return False

    @staticmethod
    def validate_prospect_input(data):
        string_values = ["prospect_title", "prospect_type", "source", "account_at_source", "prospect_link", "is_fte", "job_role", "technologies", "job_location", "duration", "engagement_mode", "working_mode", "timezone", "post_date", "prospect_analysis", "proposal_offers"]
        int_values = ["organization_id"]
        double_values = ["min_cost", "max_cost"]
        num_string_values = ["contact_person_ids"]
        for key, value in data.items():
            if key in int_values:
                if value is None or not str(value).isdigit() or str(value).startswith(" ") or str(value) == "":
                    msg = str(key) + " should not be empty and should be of integer type"
                    return False, msg
            elif key in double_values:
                if value is None or not Utilities.is_int_or_float(value):
                    msg = str(key) + " should not be empty and should be of integer or double type"
                    return False, msg
            elif key in string_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should not be empty or None"
                    return False, msg
            elif key in num_string_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should not be empty or None"
                    return False, msg
                else:
                    value_list = value.split(",")
                    for val in value_list:
                        if not val.isdigit():
                            msg = str(key) + " should only contain comma separated numbers"
                            return False, msg
            else:
                continue
        return True, ""

    @staticmethod
    def validate_proposal_input(data):
        string_values = ["proposal_types", "prospect_analysis", "proposal_offers", "proposal_priority", "proposal_status"]
        int_values = ["prospect_id", "organization_id"]
        for key, value in data.items():
            if key in int_values:
                if value is None or not str(value).isdigit() or str(value).startswith(" ") or str(value) == "":
                    msg = str(key) + " should not be empty and should be of integer type"
                    return False, msg
            elif key in string_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should not be empty or None"
                    return False, msg
            else:
                continue
        return True, ""

    @staticmethod
    def validate_proposal_info_input(data):
        string_values = ["proposal_type", "proposal_detail", "proposal_status", "proposal_date", "proposal_sender"]
        int_values = ["proposal_id"]
        for key, value in data.items():
            if key in int_values:
                if value is None or not str(value).isdigit() or str(value).startswith(" ") or str(value) == "":
                    msg = str(key) + " should not be empty and should be of integer type"
                    return False, msg
            elif key in string_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should not be empty or None"
                    return False, msg
            else:
                continue
        return True, ""

    @staticmethod
    def validate_followup_input(data):
        int_values = ["referenced_id"]
        string_values = ["comments"]
        for key, value in data.items():
            if key in int_values:
                if value is None or not str(value).isdigit() or str(value).startswith(" ") or str(value) == "":
                    msg = str(key) + " should not be empty and should be of integer type"
                    return False, msg
            elif key in string_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should not be empty or None"
                    return False, msg
            else:
                continue
        return True, ""

    @staticmethod
    def validate_source_input(data):
        string_values = ["source_name", "source_url", "source_type"]
        int_values = ["is_paid_or_not", "is_contact", "is_mail", "is_social_media", "is_revenue", "is_services", "is_industry"]
        for key, value in data.items():
            if key in int_values:
                if value is None or not str(value).isdigit() or str(value).startswith(" ") or str(value) == "":
                    msg = str(key) + " should not be empty and should be of integer type"
                    return False, msg
            elif key in string_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should not be empty or None"
                    return False, msg
            else:
                continue
        return True, ""

    @staticmethod
    def create_update_set_from_dict(query_dict):
        update_set = " set "
        for key, value in query_dict.items():
            update_set = update_set + str(key) + "=\"" + str(value) + "\", "
        update_set = update_set.strip(", ")
        return update_set

    @staticmethod
    def validate_update_input(data):
        dict_len = 0
        update_dict = {}
        for key, value in data.items():
            if value is not None and not str(value).startswith(" ") and value != "":
                update_dict[key] = value
                dict_len += 1
        return dict_len, update_dict

    @staticmethod
    def validate_bench_input(data):
        string_values = ["name", "domain", "primary_skill", "secondary_skill", "current_role", "qualification", "resume", "bench_start_dt", "bench_end_dt", "bench_status"]
        double_values = ["exp"]
        int_values = ["client_id"]
        contact_values = ["contact"]
        mail_string = ["email"]
        none_contact = ["alternate_contact"]
        none_mail = ["alternate_email"]
        for key, value in data.items():
            if key in int_values:
                if value is None or not str(value).isdigit() or str(value).startswith(" ") or str(value) == "":
                    msg = str(key) + " should not be empty and should be of integer type"
                    return False, msg
            elif key in contact_values:
                if value is None or not value.isdigit() or len(value) < 10:
                    msg = str(key) + "should not be empty and Contact number should be properly filled"
                    return False, msg
            elif key in none_contact:
                if value is not None and not value.startswith(" "):
                    if not value.isdigit() or len(value) < 10:
                        msg = str(key) + "Contact number should be properly filled"
                        return False, msg
            elif key in none_mail:
                if value is not None and value.startswith(" "):
                    if Utilities.is_invalid_email_address(value):
                        msg = str(key) + " - Email address should be properly filled"
                        return False, msg
            elif key in mail_string:
                if value is None or Utilities.is_invalid_email_address(value):
                    msg = str(key) + " - Email address should not be none and should be properly filled"
                    return False, msg
            elif key in string_values:
                if value is None or value.startswith(" ") or value == "":
                    msg = str(key) + " should not be empty or None"
                    return False, msg
            elif key in double_values:
                if value is None or not value.isdigit():
                    msg = str(key) + " should not be empty and should be of integer or double type"
                    return False, msg
            else:
                continue
        return True, ""
