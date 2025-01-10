def get_model_builder_class():
    from .modelbuilder import ModelBuilder
    return ModelBuilder


model_builder_class = get_model_builder_class()
inference_metadata = {
    'input_format': 'Image files (before and after)',
    'output_format': 'Inference result image'
}
