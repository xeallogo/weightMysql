from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from weights.models import Weight
from weights.serializers import WeightSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def weight_list(request):
    # GET list of weights, POST a new weight, DELETE all weights
    if request.method == 'GET':
            weights = Weight.objects.all()
            
            date = request.GET.get('date', None)
            if date is not None:
                weights = weights.filter(date__icontains=date)

            weight = request.GET.get('weight', None)
            if weight is not None:
                weights = weights.filter(weight__icontains=weight)
            
            weights_serializer = WeightSerializer(weights, many=True)
            return JsonResponse(weights_serializer.data, safe=False)
            # 'safe=False' for objects serialization
    
    elif request.method == 'POST':
            weight_data = JSONParser().parse(request)
            weight_serializer = WeightSerializer(data=weight_data)
            if weight_serializer.is_valid():
                weight_serializer.save()
                return JsonResponse(weight_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(weight_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Weight.objects.all().delete()
        return JsonResponse({'message': '{} Weights were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def weight_detail(request, pk):
    # find weight by pk (id)
    try: 
        weight = Weight.objects.get(pk=pk) 
    except Weight.DoesNotExist: 
        return JsonResponse({'message': 'The weight does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE weight
    if request.method == 'GET': 
        weight_serializer = WeightSerializer(weight) 
        return JsonResponse(weight_serializer.data) 
    
    elif request.method == 'PUT': 
        weight_data = JSONParser().parse(request) 
        weight_serializer = WeightSerializer(weight, data=weight_data) 
        if weight_serializer.is_valid(): 
            weight_serializer.save() 
            return JsonResponse(weight_serializer.data) 
        return JsonResponse(weight_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE': 
        weight.delete() 
        return JsonResponse({'message': 'Weight was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
# @api_view(['GET'])
# def weight_list_published(request):
#     # GET all published weights