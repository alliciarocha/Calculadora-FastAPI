from fastapi import FastAPI, HTTPException
from models import OperationRequest, OperationResponse
from operations import add, subtract, multiply, divide, exponentiation, rooting

app = FastAPI()

@app.post("/add")
def add(operation: OperationRequest):
    return OperationResponse(result=add(operation.a, operation.b))

@app.post("/subtract")
def subtract(operation: OperationRequest):
    return OperationResponse(result=subtract(operation.a, operation.b))

@app.post("/multiply")
def multiply(operation: OperationRequest):
    return OperationResponse(result=multiply(operation.a, operation.b))

@app.post("/divide")
def divide(operation: OperationRequest):
    if operation.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return OperationResponse(result=divide(operation.a, operation.b))

@app.post("/exponentiation")
def exponentiation_route(operation: OperationRequest):
    return OperationResponse(result=exponentiation(operation.a, operation.b))

@app.post("/root")
def rooting_route(operation: OperationRequest):
    if operation.b == 0:
        raise HTTPException(status_code=400, detail="Root degree cannot be zero")
    try:
        return OperationResponse(result=rooting(operation.a, operation.b))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))