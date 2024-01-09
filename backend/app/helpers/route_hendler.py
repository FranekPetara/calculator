from fastapi import Depends, HTTPException, Body
from importlib import import_module
from pathlib import Path
from pydantic import BaseModel, ValidationError
from typing import Type


class RouteHendler():

    @staticmethod
    def get_operation_module_names():
        current_folder = Path(__file__).parent.parent
        operations_path = current_folder.joinpath("operation")
        
        module_names = []
        for item in operations_path.iterdir():
            if item.is_file() and item.suffix == '.py' and item.stem != "__init__":
                module_names.append(item.stem)
        return module_names

    @staticmethod
    def get_operation_module(module_name: str = Depends(get_operation_module_names)):
        return import_module(f"app.operation.{module_name}")

    @staticmethod
    def respond_modificator(respond):
        if respond["result"] % 2:
            respond["color"] = "red"
        else:
            respond["color"] = "green"
        return respond

    def get_operation_handler(self, obj, input_model: Type[BaseModel]):
        async def handler(input_data: input_model = Body(...)):
            try:
                calculate_result = obj().calculate(**input_data.dict())
                result = {"result": calculate_result}
                result = self.respond_modificator(result)
                return result
            except ValidationError as e:
                raise HTTPException(status_code=422, detail=str(e))

        return handler


    @staticmethod
    def get_operation_classes(module):
        return [name for name in dir(module) if
                callable(getattr(module, name)) and hasattr(getattr(module, name), 'calculate')]


    @staticmethod
    def get_schemas_module(module_name):
        return import_module(f"app.schemas.{module_name}")


    def register_operation_endpoints(self,app):
        operation_modules = self.get_operation_module_names()
        for module_name in operation_modules:
            module = self.get_operation_module(module_name)
            schemas_module_name = f'{module_name}_schema'
            schemas_module = self.get_schemas_module(schemas_module_name)
            for class_name in self.get_operation_classes(module):
                obj = getattr(module, class_name)
                schemas_obj_name = f'{class_name}InputSchema'
                schemas_obj = getattr(schemas_module, schemas_obj_name)
                operation_name = class_name.lower()
                handler = self.get_operation_handler(obj, schemas_obj)
                app.api_route(f"/calculate/{operation_name}", name=operation_name, methods=['POST'])(handler)

