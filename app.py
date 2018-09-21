from flask import Flask
from flask_restful import Resource, Api
import ldap, json, os

app = Flask(__name__)
api = Api(app)

# From os environment
ldap_binduser = os.environ.get("LDAP_BINDUSER")
ldap_binduser = os.environ.get("LDAP_PASSWORD")

connect = ldap.initialize('ldap://sec.localdomain')
connect.set_option(ldap.OPT_REFERRALS, 0)

connect.simple_bind_s(ldap_binduser, ldap_binduser)

class LDAPsearch(Resource):
    def get(self, sAMAccountName):
        result = connect.search_s('OU=Employees,OU=Users,OU=SEC,DC=sec,DC=receptpartner,DC=se',
                                ldap.SCOPE_SUBTREE,
                                'sAMAccountName=' + sAMAccountName,
                                ['distinguishedName','mail','mobile'])
        return {sAMAccountName: json.dumps(result)}

class email(Resource):
    def get(self, mail):
        result = connect.search_s('OU=Employees,OU=Users,OU=SEC,DC=sec,DC=receptpartner,DC=se',
                                ldap.SCOPE_SUBTREE,
                                'mail=' + mail,
                                ['sAMAccountName'])
        return {mail: json.dumps(result)}


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(LDAPsearch, '/accountname/<string:sAMAccountName>')
api.add_resource(email, '/mail/<string:mail>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
	