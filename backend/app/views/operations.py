from fastapi import APIRouter
from app.helpers.route_hendler import RouteHendler


class OperationsRouter:

    def __init__(self):
        self.rute_hendler = RouteHendler()
        self.router = APIRouter()
        self.router.add_api_route("/operations", self.list_operations, methods=["GET"])

    def list_operations(self):
        operation_names = []
        for module_name in self.rute_hendler.get_operation_module_names():
            module = self.rute_hendler.get_operation_module(module_name)
            for class_name in self.rute_hendler.get_operation_classes(module):
                operation_names.append(class_name.lower())
        return operation_names
    

