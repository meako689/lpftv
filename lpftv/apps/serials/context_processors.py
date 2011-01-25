from django.template import RequestContext

def find_text(request):
    try:
        q = request.GET["q"]
    except:
        q = ""
    return {"find_text": q}

