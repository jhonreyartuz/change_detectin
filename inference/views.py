# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InferenceResultSerializer
from .task import perform_inference_task

class ChangeDetection(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InferenceResultSerializer(data=request.data)
        if serializer.is_valid():
            # Enqueue inference task to worker
            perform_inference_task.delay(
                request.data['model'].path, request.data['weight'].path,
                request.data['before_image'].path, request.data['after_image'].path
            )
            return Response({'message': 'Inference task submitted'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
