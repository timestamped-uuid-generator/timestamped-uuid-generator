from core.models import TimeStampedUUID
from django.http.response import JsonResponse

def timestamped_uuid_gen(request):
    TimeStampedUUID.objects.create()
    timestamped_uuid_qs = TimeStampedUUID.objects.order_by('-timestamp')    
    
    data = {}
    for obj in timestamped_uuid_qs:
        key = obj.timestamp.strftime('%Y-%m-%d %H:%M:%S %f')
        value = obj.uuid.hex
        data[key] = value

    return JsonResponse(data)