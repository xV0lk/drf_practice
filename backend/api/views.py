from django.http import JsonResponse

def api_test(request):
    """Returns a test response

    Args:
        request (_type_): _description_

    Returns:
        JsonResponse: Json de prueba
    """
    return JsonResponse({"clase_de_prueba": "Esto es una prueba en clase"})

