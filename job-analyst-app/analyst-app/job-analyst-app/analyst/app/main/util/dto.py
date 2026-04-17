from flask_restx import Namespace, fields


class JobPostDto:
    api = Namespace('Prospect', description='User Interface for Prospect table')
    raw = api.model('prospect', {})


class ProposalDto:
    api = Namespace('Proposal', description='User Interface for Proposal table')
    raw = api.model('proposal', {})


class OrganizationDto:
    api = Namespace('Organization', description='User Interface for Organization table')
    raw = api.model('organization', {})


class PersonsDto:
    api = Namespace('Person', description='User Interface for Persons table')
    raw = api.model('person', {})


class LoginDto:
    api = Namespace('Login', description='User Login')
    raw = api.model('login', {})


class SourceDto:
    api = Namespace('Sources', description='User Interface for Source table')
    raw = api.model('source', {})


class BenchDto:
    api = Namespace('Bench', description='User Interface for Bench table')
    raw = api.model('bench', {})
