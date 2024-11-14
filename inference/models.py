from django.db import models
from opencd.apis import OpenCDInferencer
from django.core.files.storage import FileSystemStorage

# Create your models here.


class Model:
    def infer(self, input_file_paths: list[str], *args, **kwargs) -> dict:
        # Assuming input_file_paths contain before and after image paths
        before_image_path, after_image_path = input_file_paths

        # Load the model and weights
        inference = OpenCDInferencer(
            model=args[0], weights=args[1], 
            classes=('unchanged', 'changed'), palette=[[0, 0, 0], [255, 255, 255]]
        )

        # Perform inference
        result = inference([[before_image_path, after_image_path]], out_dir='media', return_vis=True,
                            return_datasamples=True, img_out_dir='result')

        return {
            'result': result,
            'before_image': before_image_path,
            'after_image': after_image_path
        }



# Create your models here.
fs_before = FileSystemStorage(location="/media/before_image")
fs_after = FileSystemStorage(location="media/after_image")
fs_result = FileSystemStorage(location="media/result_image")

class InferenceResult(models.Model):
    before_image = models.ImageField(storage=fs_before)
    after_image = models.ImageField(storage=fs_after)
    result_image = models.FileField(storage=fs_result, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inference Result {self.id}"
    