import urllib3
from datetime import datetime, timezone, timedelta
import json
import os

http = urllib3.PoolManager()


def lambda_handler(event, context):
    # print(f"event: {event}")  # log event

    event_name = event["Records"][0]["eventName"]
    event_time = (
        datetime.fromisoformat(event["Records"][0]["eventTime"].replace("Z", "+00:00"))
        .replace(tzinfo=timezone.utc)
        .astimezone(timezone(timedelta(hours=9)))
        .strftime("%Y-%m-%d %H:%M:%S")
    )
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    object_name = event["Records"][0]["s3"]["object"]["key"]
    user_name = event["Records"][0]["userIdentity"]["principalId"].split(":")[-1]

    try:
        url = os.environ["SLACK_WEBHOOK_URL"]
        msg = {
            "channel": "hasan-test",
            "username": "WorksXpert",
            "text": f"*Event: {event_name}*",
            "attachments": [
                {
                    "color": "#097969",
                    "text": f"Event Time: {event_time} KST\nBucket Name: {bucket_name}\nObject Name: {object_name}\nUser: {user_name}",
                }
            ],
        }

        encoded_msg = json.dumps(msg).encode("utf-8")
        resp = http.request("POST", url, body=encoded_msg)
        print(
            {
                "message": msg,
                "status_code": resp.status,
                "response": resp.data,
            }
        )

    except Exception as e:
        print("Failed to send Slack message")
        print(e)
