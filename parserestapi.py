import json, httplib

# connection = httplib.HTTPSConnection("api.parse.com", 443)
# connection.connect()
#
# connection.request('POST', '/1/classes/TestApp', json.dumps({
#     "score": 1337,
#     "playerName": "Sean Plott",
#     "cheatMode": False
# }), {
#     "X-Parse-application-id": "2iry8fnPW5GtD3bUaEBO1PdkwR2CJKYZh1sKqivi",
#     "X-Parse-REST-API-Key": "DfSbqKuFE6CnLpffKRo1dFEDdAKRnnB7AWNh8lkn",
#     "Content-type": "application/json"
# })
#
# result = json.loads(connection.getresponse().read())

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('GET', '/1/classes/TestApp/pjyOHm9Fzn', '', {
       "X-Parse-Application-Id": "2iry8fnPW5GtD3bUaEBO1PdkwR2CJKYZh1sKqivi",
       "X-Parse-REST-API-Key": "DfSbqKuFE6CnLpffKRo1dFEDdAKRnnB7AWNh8lkn"
     })
result = json.loads(connection.getresponse().read())
print result

