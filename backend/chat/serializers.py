from datetime import datetime

def success_response(reply):
    return {
        "status": "success",
        "data": {
            "reply": reply,
            "timestamp": str(datetime.utcnow())
        }
    }


def error_response(message):
    return {
        "status": "error",
        "message": message
    }
