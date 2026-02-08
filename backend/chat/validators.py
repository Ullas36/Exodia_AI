def validate_message(msg):

    if not msg:
        return False, "Message cannot be empty"

    if len(msg) > 2000:
        return False, "Message too long"

    return True, ""
