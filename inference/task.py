from celery import shared_task
from .modelbuilder import ModelBuilder
from .Models import InferenceResult

@shared_task
def perform_inference_task(model_path, weights_path, before_image_path, after_image_path):
    # Build the model
    model_builder = ModelBuilder()
    model = model_builder.build([model_path, weights_path])

    # Perform inference
    result = model.infer([before_image_path, after_image_path])

    # Process result (save to database, etc.)
    # Example: save result to InferenceResult model
    inference_result = InferenceResult.objects.create(
        before_image=before_image_path,
        after_image=after_image_path,
        result_image=result['result']  # Save the result path
    )

    return result
