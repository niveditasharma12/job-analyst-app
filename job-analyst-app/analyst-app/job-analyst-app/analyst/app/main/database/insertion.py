from  ..database import connector
from flask import Blueprint,request,jsonify
prospect = Blueprint('prospect',__name__,url_prefix="/api/prospect")

@prospect.route('/prospect',methods=['POST'])
def prospect_details():
    Source = request.json['Source']
    Prospect_id = request.json['Prospect_id']
    Prospect_link = request.json['Prospect_link']
    Tech_Category = request.json['Tech_Category']
    Skill_Domain = request.json['Skill_Domain']
    Primary_skills = request.json['Primary_skills']
    Secondary_skills = request.json['secondary_skills']
    Exp = request.json['Exp']
    Min_Budget = request.json['Min_Budget']
    Max_Budget = request.json['Max_Budget']
    Country = request.json['Country']
    Working_location = request.json['Working_location']
    Min_Duration = request.json['Min_Duration']
    BDE_Name = request.json['BDE_Name']
    Comments = request.json['Comments']
    db= connector.db_connection()
    cmd=db.cursor()
    a='''INSERT INTO table_name (
    Source,
    Prospect_id,
    Prospect_link,
    Tech_Category,
    Skill_domain,
    Primary_skills,
    Secondary_skills,
    Exp,
    Min_Budget_$Hourly,
    Max_Budget_$Hourly,
    Country_or_Region,
    Min_Duration_in_month,
    Working_Location,
    BDE_Name,
    Comments)
    VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}')'''.format(Source,Prospect_id,Prospect_link,Tech_Category,Skill_Domain,Primary_skills,Secondary_skills,Exp,Min_Budget, Max_Budget,Country,Working_location,Min_Duration,BDE_Name,Comments)
    cmd.execute(a)
    db.commit()
    db.close()
    return jsonify({'Message':'record inserted'})