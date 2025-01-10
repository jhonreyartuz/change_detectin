# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InferenceResultSerializer
from .task import perform_inference_task
from rest_framework.parsers import MultiPartParser, FormParser

class ChangeDetection(APIView):
    parser_classes = [MultiPartParser, FormParser]  # Add parsers for multipart requests

    def post(self, request, *args, **kwargs):
        serializer = InferenceResultSerializer(data=request.data)
        if serializer.is_valid():
            # Enqueue inference task to worker
             # Get the temporary file paths for the uploaded files
            model_file_path = request.data['model'].temporary_file_path()
            weight_file_path = request.data['weight'].temporary_file_path()
            before_image_file_path = request.data['before_image'].temporary_file_path()
            after_image_file_path = request.data['after_image'].temporary_file_path()

            perform_inference_task.delay(
                 # Get the temporary file paths for the uploaded files
                model_file_path, weight_file_path, before_image_file_path, after_image_file_path
            )
            return Response({'message': 'Inference task submitted'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
