import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import re

from ..constant import paths


class MailUtilities(object):
    @staticmethod
    def progress_approved_notification(emails, prospect_id):
        raw_body = '''
        <body style="font-family:arial;">
                    Hi,<br><br>

                    <table style="text-align:left;width:100%;font-family:arial">
                         <tr>
                            <td style="padding-bottom:10px;">{head_message}</td>
                         </tr>
                    </table>
                        <br><br><br><br><br><br><br>
        			Regards,
                    <br><span style="color:#0073A5">Analyst App</span>
                    <br><span style="color:#0073A5">Sroniyan Platform</span>
                </html>
        '''

        head_message = f"The progress of Prospect with prospect_id = {prospect_id}, has been updated to 'APPROVED'."

        to = emails
        cc = ""  # paths.CC
        subject = "Prospect Progress updated to approved"

        head_message.format(type="Quarterly")
        body = raw_body.format(head_message=head_message)

        MailUtilities.sendHtmlMail(to, cc, subject, body)

    @staticmethod
    def sendPlainMail(to=None, cc=None, subject=None, body=None):

        status = False

        frm = ""  # todo to add the from email address
        all_add = cc.split(',') + [to]
        msg = MIMEMultipart()
        msg['From'] = frm
        msg['To'] = to
        msg['Cc'] = cc
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        try:
            s_mail = smtplib.SMTP("smtp.gmail.com", 587)
            s_mail.set_debuglevel(2)
            s_mail.ehlo()
            s_mail.starttls()
            s_mail.ehlo()
            s_mail.login("", "")  # todo ("username", "password") to be added
            time.sleep(3)
            s_mail.sendmail(frm, all_add, text)
            status = True
            print("Email has been sent")
            '''logger.logg(debug_msg='Error while sending mail.',
                        info_msg='Mail has been sent',
                        warning_msg=None,
                        error_msg='Module = ' + "mailer.py",
                        critical_msg=None)'''
        except Exception as e:
            ''' logger.logg(debug_msg='Error while sending mail.',
                         info_msg='Mail could not be sent',
                         warning_msg='Error in sending mail',
                         error_msg='Module = ' + "mailer.py",
                         critical_msg=str(e))'''

        return status

    @staticmethod
    def sendHtmlMail(to=None, cc=None, subject=None, body=None):

        status = False
        # logger = Logger()

        frm = ""  # todo to add the from email address
        all_add = cc.split(',') + [to]
        msg = MIMEMultipart()
        msg['From'] = frm
        msg['To'] = to
        msg['Cc'] = cc
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        try:
            s_mail = smtplib.SMTP("smtp.gmail.com", 587)
            s_mail.set_debuglevel(2)
            s_mail.ehlo()
            s_mail.starttls()
            s_mail.ehlo()
            s_mail.login("", "")  # todo ("username", "password") to be added
            time.sleep(3)
            s_mail.sendmail(frm, all_add, text)
            status = True
            print("Email has been sent")
            '''logger.logg(debug_msg='None.',
                        info_msg='Mail has been sent',
                        warning_msg="None",
                        error_msg='Module = ' + "mailer.py",
                        critical_msg="None")'''
        except Exception as e:
            pass
            '''logger.logg(debug_msg='Error while sending mail.',
                        info_msg='Mail could not be sent',
                        warning_msg='Error in sending mail',
                        error_msg='Module = ' + "mailer.py",
                        critical_msg=str(e))'''

        return status

    @staticmethod
    def validate_email(input_email):
        reg = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if re.fullmatch(reg, input_email):
            return True
        else:
            return False
