def get_model():
    from .Models import Model  # Import inside the function to avoid circular dependency
    return Model


class ModelBuilder:
    def build(self, model_file_paths: list[str], *args, **kwargs):
        model_path, weights_path = model_file_paths

        # Lazily load the Model class
        Model = get_model()

        # Return a Model instance
        return Model()
