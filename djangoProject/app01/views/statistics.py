from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from app01.views.cookie import checkToken, TokenCheckFailedException
from app01.views.unjson import UnJson
from djangoProject.serializer import EventSerializer, OldPersonSerializer, EmployeeSerializer, VolunteerSerializer
from app01.models import event_info, oldperson_info, employee_info, volunteer_info


class eventList(APIView):
    def get(self, request):
        serialize = EventSerializer(instance=event_info.objects.all(), many=True)
        return Response(serialize.data)


# 获取照片，id为imgid
@api_view(['GET'])
def getImg(request, type, id):
    try:
        data = UnJson(request.data)
        token = request.headers.get('Authorization')
        checkToken(token)
        if type == '0':
            results = oldperson_info.objects.filter(ID=id).values('profile_photo')
            path = [result['profile_photo'] for result in results]
            path_str = ''.join(path)
        elif type == '1':
            results = employee_info.objects.filter(ID=id).values('profile_photo')
            path = [result['profile_photo'] for result in results]
            path_str = ''.join(path)
        elif type == '2':
            results = volunteer_info.objects.filter(ID=id).values('profile_photo')
            path = [result['profile_photo'] for result in results]
            path_str = ''.join(path)
        else:
            return HttpResponse('type 和 id 为必填字段 0 代表老人 1 代表工作人员 2 代表义工')
        image_data = open(path_str, "rb").read()
        return HttpResponse(image_data, content_type="image/jpg")
    except TokenCheckFailedException as e:
        return JsonResponse(e.res, status=402)


@api_view(['POST'])
def uploadAvatar(request):
    """
    上传接口 type：0 代表老人 1 代表工作人员 2 代表义工
    :param request:
    :return:
    """
    try:
        token = request.headers.get('Authorization')
        checkToken(token)
        upload_file = request.FILES.get('file')
        request.data.pop('file')
        data = UnJson(request.data)
        obj = ''
        try:
            type = data.type
            id = data.id
        except BaseException:
            return HttpResponse('type 和 id 为必填字段 0 代表老人 1 代表工作人员 2 代表义工')

        try:
            print(id)
            if type == '0':
                type = "oldperson"
                obj = oldperson_info.objects.get(ID=id)
                serializer = OldPersonSerializer(obj)
            elif type == '1':
                type = "employee"
                obj = employee_info.objects.get(id=id)
                serializer = EmployeeSerializer(obj)
            elif type == '2':
                type = "volunteer"
                obj = volunteer_info.objects.get(id=id)
                serializer = VolunteerSerializer(obj)
            else:
                return HttpResponse('type 和 id 为必填字段 0 代表老人 1 代表工作人员 2 代表义工')
        except  employee_info.DoesNotExist or oldperson_info.DoesNotExist or volunteer_info.DoesNotExist:
            return HttpResponse('找不到该' + type)

        print(upload_file)
        url = './img/avatar/' + type + id + '-av-' + upload_file.name
        file = open(url, 'wb+')
        for chunk in upload_file.chunks():
            file.write(chunk)

        obj.profile_photo = url
        obj.save()
        return Response(serializer.data)
    except TokenCheckFailedException as e:
        return JsonResponse(e.res, status=402)