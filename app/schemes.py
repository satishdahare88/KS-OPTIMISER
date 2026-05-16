from pydantic import BaseModel

class Workload(BaseModel):
    deployment : str
    cpu_request : int
    cpu_usage_avg : int
    memory_request : int
    memory_usage_avg : int