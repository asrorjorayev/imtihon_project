from .models import Tillar

def categoriya(request):
    
    return {"categoriya":Tillar.objects.all()}
