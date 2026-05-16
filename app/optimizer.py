def optimize(workloads):

    recommendations = []

    for workload in workloads:

        recommended_cpu = workload.cpu_request
        recommended_memory = workload.memory_request

        reason = "Resource are properly allocated"

        if workload.cpu_request > (workload.cpu_usage_avg * 2):
            recommended_cpu = (workload.cpu_usage_avg * 1.5)

        if workload.memory_request > (workload.memory_usage_avg * 2):
            recommended_memory = (workload.memory_usage_avg * 1.5)

        if recommended_cpu != workload.cpu_request or recommended_memory != workload.memory_request:
            reason = "Average usage significantly below requested resources"
        
        recommendations.append({"deployment" : workload.deployment,
                               "recommended_cpu" : recommended_cpu,
                               "recommended_memory" : recommended_memory,
                               "reason" : reason})
        return recommendations