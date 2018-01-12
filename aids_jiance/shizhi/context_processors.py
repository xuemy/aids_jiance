from .models import Shizhi

def fangan(request):
    return {
        'fangan': Shizhi.FANGAN_CHOICES,

    }
