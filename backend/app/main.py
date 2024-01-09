from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.helpers.route_hendler import RouteHendler
from app.views.operations import OperationsRouter



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
rute_hendler = RouteHendler()
rute_hendler.register_operation_endpoints(app)
app.include_router(OperationsRouter().router)

