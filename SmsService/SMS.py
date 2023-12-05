import requests

src = "https://ippanel.com/api/select"


def send_password_code_sms(phone_number, code):

    json_request = {

        "op": "pattern",
        "user": "09027235390",
        "pass":  "Faraz@4271393037",
        "fromNum": "+9890000145",
        "toNum": phone_number,
        "patternCode": "4o5fz5mury28oh6",
        "inputData": 	[
            {
                "code": str(code)
            }
        ]
        }

    r = requests.post(src, json=json_request)

    if r.status_code == 200:
        return True, r.content
    else:
        return False, r


def send_signup_successfully_sms(phone_number):

    json_request = {

        "op": "pattern",
        "user": "09027235390",
        "pass":  "Faraz@4271393037",
        "fromNum": "+9890000145",
        "toNum": phone_number,
        "patternCode": "y3fidt3inplmbhm",
        "inputData": 	[
                {
                    "name": ''
                }
            ]
        }

    r = requests.post(src, json=json_request)

    if r.status_code == 200:
        return True, r.content
    else:
        return False, r
