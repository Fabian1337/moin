import json
remove_bs = r'{\"eventVersion\":\"1.05\",\"userIdentity\":{\"type\":\"IAMUser\",\"principalId\":\"AIDAJJM7GL72KEP64JVYG\",\"arn\":\"arn:aws:iam::503068961001:user/abhipandey\",\"accountId\":\"503068961001\",\"accessKeyId\":\"ASIAXKIJ7FDUSMHIHV7G\",\"userName\":\"abhipandey\",\"sessionContext\":{\"attributes\":{\"mfaAuthenticated\":\"false\",\"creationDate\":\"2019-08-10T09:49:34Z\"}},\"invokedBy\":\"signin.amazonaws.com\"},\"eventTime\":\"2019-08-10T09:49:58Z\",\"eventSource\":\"sns.amazonaws.com\",\"eventName\":\"ListSubscriptions\",\"awsRegion\":\"us-west-2\",\"sourceIPAddress\":\"103.214.189.229\",\"userAgent\":\"signin.amazonaws.com\",\"requestParameters\":{\"nextToken\":\"AAHLcEnGPYVVsORCkUMXjJF0FHnYLalrN+BfvizlKzkWvg==\"},\"responseElements\":null,\"requestID\":\"247dc857-993e-5677-a8df-9d9f0cb805dd\",\"eventID\":\"5e726329-2342-48e6-8e00-5c2fa9856ed9\",\"eventType\":\"AwsApiCall\",\"recipientAccountId\":\"503068961001\"}'

clear = remove_bs.replace("\\", "")
json_data = json.loads(clear)

json_string = json.dumps(json_data)
new_clear = json_string.replace("\\", "")
json_data = json.loads(new_clear)
print(json_data)