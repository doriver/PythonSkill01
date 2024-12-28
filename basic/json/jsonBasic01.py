import json

json_data = '''
{
    "mentor": {
        "Name" : "Tom",
        "Age" : 20
    },
    "mentee" : {
        "Name" : "Eric",
        "Age" : 13
    }
}
'''
# json.loads() : json데이터 파징
json_obj = json.loads(json_data)

print(json_obj)
print("Mentor : " + json_obj['mentor']['Name'])
print("Mentee : " + json_obj['mentee']['Name'])