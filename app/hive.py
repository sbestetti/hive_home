import requests
import json

import config


def get_session_id():
    login_data = {
        "sessions": [
            {
                "username": config.USER,
                "password": config.PASSWD,
                "caller": "WEB"
            }]}

    r = requests.post(
        config.BASE_URL + "/auth/sessions",
        data=json.dumps(login_data),
        headers=config.HEADERS)

    if r.status_code != 200:
        print(f"Auth error: {r.status_code}: {r.text}")
        exit()

    response = r.json()

    return response["sessions"][0]["sessionId"]


def toggle_light(id):
    headers = config.HEADERS
    headers["X-Omnia-Access-Token"] = get_session_id()

    current_status_payload = requests.get(
        config.BASE_URL + "/nodes/" + id,
        headers=headers
    )

    if current_status_payload.status_code != 200:
        print(f"Error when getting status: {current_status_payload.status}")
        exit()

    current_status_json = current_status_payload.json()

    current_status = current_status_json["nodes"][0]["features"]["on_off_device_v1"]["mode"]["reportedValue"]

    target = str()
    if current_status == "ON":
        target = "OFF"
    else:
        target = "ON"

    payload = {
        "nodes": [
            {
                "features": {
                    "on_off_device_v1": {
                        "mode": {
                            "targetValue": target
                        }
                    }
                }
            }
        ]
    }

    r = requests.put(
        config.BASE_URL + "/nodes/" + id,
        headers=headers,
        data=json.dumps(payload)
    )

    if r.status_code != 200:
        print(f"Error updating status: {r.status_code} - {r.text}")
        exit()

    return r.status_code
