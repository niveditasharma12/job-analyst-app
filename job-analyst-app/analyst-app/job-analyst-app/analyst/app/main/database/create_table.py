from flask import Flask, render_template, request
from analyst.app.main.database import connector
import pymysql as sql
db= connector.db_connection()
cmd=db.cursor()
q='''create table Prospect(
    S_no int NOT NULL AUTO_INCREMENT,
    Source varchar(225),
    Prospect_id varchar(50) NOT NULL,
    Prospect_link varchar(500),
    Tech_Category varchar(100),
    Skill_domain varchar(300),
    Primary_skills varchar(100),
    Secondary_skills varchar(100),
    Exp varchar(50),
    Min_Budget_$Hourly varchar(100),
    Max_Budget_$Hourly varchar(100),
    Country_or_Region varchar(100),
    Min_Duration_in_month varchar(100),
    Working_Location varchar(100),
    BDE_Name varchar(100),
    Comments varchar(200),
    PRIMARY KEY (S_no) )'''
cmd.execute(q)
print("TABLE CREATED...")
db.close()

