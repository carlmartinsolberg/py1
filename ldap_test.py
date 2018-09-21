import ldap
import json
connect = ldap.initialize('ldap://sec.localdomain')
connect.set_option(ldap.OPT_REFERRALS, 0)
connect.simple_bind_s('CN=Martin Solberg,OU=Employees,OU=Users,OU=SEC,DC=sec,DC=receptpartner,DC=se', 'MI66okavd1!')
result = connect.search_s('OU=Employees,OU=Users,OU=SEC,DC=sec,DC=receptpartner,DC=se',
                          ldap.SCOPE_SUBTREE,
                          'sAMAccountName=solbemar',
                          ['distinguishedName','mail','mobile'])

print result
print json.dumps(result)
print "----"