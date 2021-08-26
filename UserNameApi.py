import requests
import json

class UserNameApi(object):
    def getUserApi(number):
        url = "https://reqres.in/api/users?page={}".format(number)
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    
    def totalUserName():
        numberOfUser = 0
        for i in range(1, 12+1):
            responseData = UserNameApi.getUserApi(i)
            if responseData.status_code==200:
                responseData= json.loads(responseData.text)
                if len(responseData['data'])!=0:
                    numberOfUser = numberOfUser+len(responseData)
                else:
                    return {"Total Number Of User" : numberOfUser}
        
        return {"Total Number Of User" : numberOfUser}





print(UserNameApi.totalUserName())

