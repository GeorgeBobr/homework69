import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest

def index(request, *args, **kwargs):
    return render(request, 'index.html')

def add(request, *args, **kwargs):
    return api_calculator(request, 'add')

def subtract(request, *args, **kwargs):
    return api_calculator(request, 'subtract')

def multiply(request, *args, **kwargs):
    return api_calculator(request, 'multiply')

def divide(request, *args, **kwargs):
    return api_calculator(request, 'divide')

def api_calculator(request, method_calculator):
    try:
        data = json.loads(request.body)
        a = data.get("A")
        b = data.get("B")

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return JsonResponse({"error": "A & B should be numeric values"}, status=400)

        if method_calculator == 'add':
            result = a + b
        elif method_calculator == 'subtract':
            result = a - b
        elif method_calculator == 'multiply':
            result = a * b
        elif method_calculator == 'divide':
            if b == 0:
                return HttpResponseBadRequest(json.dumps({"error": "Division by zero!"}),
                                              content_type="application/json")
            result = a / b
        else:
            return JsonResponse({"error": "Invalid operation"}, status=400)

        return JsonResponse({"answer": result})

    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({"error": "Invalid input data"}, status=400)
