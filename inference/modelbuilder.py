from .models import Model

class ModelBuilder:
    def build(self, model_file_paths: list[str], *args, **kwargs) -> Model:
        model_path, weights_path = model_file_paths
        # Return a Model instance after building it with the necessary files
        return Model()
