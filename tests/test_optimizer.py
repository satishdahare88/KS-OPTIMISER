from app.optimizer import optimize
from app.schemes import Workload

# checks did optimizer reduce the oversized resources and provided a recommendation
def test_overprovinced_workload():
    data = [
        {
        "deployment": "api-service",
        "cpu_request": 1000,
        "cpu_usage_avg": 180,
        "memory_request": 2048,
        "memory_usage_avg": 700
        }
        ]
    workload = Workload(**data[0])
    result = optimize([workload])
    assert result[0]["recommended_cpu"] < 1000
    assert result[0]["recommended_memory"] < 2048

# check that optimizer does not change the resources if they are properly allocated
def test_properly_allocated_workload():

    data = [
        {
        "deployment": "worker-service",
        "cpu_request": 500,
        "cpu_usage_avg": 450,
        "memory_request": 1024,
        "memory_usage_avg": 900
        }
        ]
    workload = Workload(**data[0])
    result = optimize([workload])
    assert result[0]["recommended_cpu"] == 500
    assert result[0]["recommended_memory"] == 1024