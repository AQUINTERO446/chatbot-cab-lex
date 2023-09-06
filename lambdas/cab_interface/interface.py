import json


def cab_request(event, context):
    body = {
        "time_to_arrive_in_seconds": 600,
        "available": True,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
