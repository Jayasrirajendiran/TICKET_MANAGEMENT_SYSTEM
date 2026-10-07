class ModelHelper:

    @staticmethod
    def from_schema(model_class, schema):
        return model_class(**schema.dict())