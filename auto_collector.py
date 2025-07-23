# sending request to web-api.onlinesoccermanager.com port 443
import sys
import json
import requests
from urllib.parse import urlencode
import time

# ✅ Credentials must be declared outside any indented block
###################################################
# write your username and password for you accont #
###################################################
username = "?????????????"
password = "?????????????"
client_id = "jPs3vVbg4uYnxGoyunSiNf1nIqUJmSFnpqJSVgWrJleu6Ak7Ga"
client_secret = "ePOVDMfAvU8zcyfaxLMtqYSmND3n6vmmKx9ZlVnNGjGkzucMCt"

def watched_req(authorization_value):
    url = "https://web-api.onlinesoccermanager.com/api/v1.1/user/videos/watched"
    headers = {
        "Authorization": authorization_value,
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Mozilla/5.0",
        "PlatformId": "14",
        "AppVersion": "3.228.0"
    }
    data = {
        "actionId": "BusinessClub",
        "rewardVariation": "1",
        "capVariation": "2"
    }
    try:
        response = requests.post(url, headers=headers, data=urlencode(data))
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"⚠️ Error in watched_req: {e}")
        return {"error": str(e)}

def consumereward_req(authorization_value, id_value):
    url = "https://web-api.onlinesoccermanager.com/api/v1/user/bosscoinwallet/consumereward"
    headers = {
        "Authorization": authorization_value,
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Mozilla/5.0",
        "PlatformId": "14",
        "AppVersion": "3.228.0"
    }
    data = {
        "rewardId": id_value
    }
    try:
        response = requests.post(url, headers=headers, data=urlencode(data))
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"⚠️ Error in consumereward_req: {e}")
        return {"error": str(e)}

def get_authorization_value(username, password, client_id, client_secret):
    url = "https://web-api.onlinesoccermanager.com/api/token"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Platformid": "14",
        "Appversion": "3.228.0"
    }
    data = {
        "userName": username,
        "grant_type": "password",
        "client_id": client_id,
        "client_secret": client_secret,
        "password": password
    }
    try:
        response = requests.post(url, headers=headers, data=urlencode(data))
        response.raise_for_status()
        return f"Bearer {response.json().get('access_token', '')}"
    except Exception as e:
        print(f"❌ Failed to get authorization: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        while True:
            authorization_value = get_authorization_value(username, password, client_id, client_secret)

            while True:
                id_response = watched_req(authorization_value)

                if "error" not in id_response:
                    try:
                        id_value = id_response[0]["id"]
                    except Exception as e:
                        print(f"⚠️ Failed to extract ID: {e}")
                        break
                else:
                    print(f"🕒 Waiting 56 minutes. Reason: {id_response['error']}")
                    time.sleep(56 * 60)
                    break

                time.sleep(3)

                final_response = consumereward_req(authorization_value, id_value)

                if "amount" in final_response:
                    print(f"\033[92m✅ Collected amount: {final_response['amount']}\033[0m")
                else:
                    print(f"⚠️ Unexpected final response: {final_response}")

                time.sleep(15)

    except KeyboardInterrupt:
        print("\n🛑 Script stopped by user.")
