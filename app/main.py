from fastapi import FastAPI
from typing import List
from app.schemes import Workload
from app.optimizer import optimize

app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello": "World !!!"}

@app.post("/optimize")
def optimize_workloads(workloads: List[Workload]):
    return optimize(workloads)