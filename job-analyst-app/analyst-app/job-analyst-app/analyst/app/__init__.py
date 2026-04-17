from flask_restx import Api
from flask import Blueprint

from .main.constant import paths
from .main.controller.jobpost_wf_controller import api as jobpost
from .main.controller.proposal_controller import api as proposal
from .main.controller.organization_controller import api as organization
from .main.controller.persons_controller import api as person
from .main.controller.login_controller import api as login
from .main.controller.source_controller import api as source
from .main.controller.bench_controller import api as bench
from .main.service.constant_service import ConstantService
from logging.handlers import RotatingFileHandler
import logging
import os



logging.basicConfig(
    handlers=[RotatingFileHandler(os.path.join(paths.LOGPATH, 'srn-analyst-app.log'), maxBytes=1024 * 1024, backupCount=10)],
    level=logging.DEBUG,
    format=f'%(asctime)s %(api_key)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d %(levelname)s %(message)s'
)

old_factory = logging.getLogRecordFactory()
def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.api_key = "SRNAPP00002"
    return record
logging.setLogRecordFactory(record_factory)


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Analyst Microservices',
          version='1.0',
          description='Analyst Microservices',
          doc=False
          )

api.add_namespace(jobpost, path='/prospect')
api.add_namespace(proposal, path='/proposal')
api.add_namespace(organization, path='/organization')
api.add_namespace(person, path='/person')
api.add_namespace(login, path='/login')
api.add_namespace(source, path='/source')
api.add_namespace(bench, path='/bench')
