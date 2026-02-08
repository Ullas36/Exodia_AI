from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .services import process_chat
from .validators import validate_message
from .serializers import success_response, error_response
from .weaviate_helper import clear_history


@csrf_exempt
def chat(request):

    if request.method != "POST":
        return JsonResponse(error_response("Only POST allowed"))

    try:
        data = json.loads(request.body)
        user_message = data.get("message", "").strip()

        valid, msg = validate_message(user_message)

        if not valid:
            return JsonResponse(error_response(msg))

        ai_reply = process_chat(user_message)

        return JsonResponse(success_response(ai_reply))

    except Exception as e:
        return JsonResponse(error_response(str(e)))


@csrf_exempt
def reset(request):
    clear_history()
    return JsonResponse({"status": "cleared"})
