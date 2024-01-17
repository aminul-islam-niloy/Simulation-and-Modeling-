def critical_path_method(tasks):
    task_data = {}
    for task in tasks:
        task_data[task["name"]] = {
            "duration": task["duration"],
            "dependencies": task["dependencies"],
            "early_start": 0,
            "early_finish": 0,
            "late_start": float("inf"),
            "late_finish": float("inf"),
            "slack": 0,
            "is_critical": False
        }

    # Forward pass (calculate early start and finish times)
    for task_name in task_data:
        if not task_data[task_name]["dependencies"]:
            task_data[task_name]["early_start"] = 0
        else:
            max_early_finish = 0
            for dependency in task_data[task_name]["dependencies"]:
                max_early_finish = max(max_early_finish, task_data[dependency]["early_finish"])
            task_data[task_name]["early_start"] = max_early_finish
        task_data[task_name]["early_finish"] = task_data[task_name]["early_start"] + task_data[task_name]["duration"]

    # Backward pass (calculate late start and finish times)
    project_end_time = max(task["early_finish"] for task in task_data.values())
    for task_name in reversed(list(task_data.keys())):
        if not task_data[task_name]["dependencies"]:
            task_data[task_name]["late_finish"] = project_end_time
        for successor in [task for task in tasks if task_name in task["dependencies"]]:
            task_data[task_name]["late_finish"] = min(task_data[task_name]["late_finish"], task_data[successor["name"]]["late_start"])
        task_data[task_name]["late_start"] = task_data[task_name]["late_finish"] - task_data[task_name]["duration"]

    # Calculate slack and identify critical tasks
    for task_name in task_data:
        task_data[task_name]["slack"] = task_data[task_name]["late_start"] - task_data[task_name]["early_start"]
        task_data[task_name]["is_critical"] = task_data[task_name]["slack"] == 0

    # Print task information
    print("Task Information:")
    for task_name, task_info in task_data.items():
        print(f"{task_name}: Duration={task_info['duration']} ES={task_info['early_start']} EF={task_info['early_finish']} LS={task_info['late_start']} LF={task_info['late_finish']} Slack={task_info['slack']} Critical={task_info['is_critical']}")

    # Find the critical path
    critical_path = [task_name for task_name, task_info in task_data.items() if task_info["is_critical"]]

    # Print the critical path
    if critical_path:
        print("Critical Path:", " -> ".join(critical_path))
    else:
        print("No Critical Path")

    return critical_path

# Example usage:
custom_tasks = [
    {"name": "Task1", "duration": 3, "dependencies": []},
    {"name": "Task2", "duration": 4, "dependencies": ["Task1"]},
    {"name": "Task3", "duration": 2, "dependencies": ["Task1"]},
    {"name": "Task4", "duration": 5, "dependencies": ["Task2"]},
    {"name": "Task5", "duration": 1, "dependencies": ["Task3"]},
    {"name": "Task6", "duration": 2, "dependencies": ["Task3"]},
    {"name": "Task7", "duration": 4, "dependencies": ["Task4"]},
    {"name": "Task8", "duration": 3, "dependencies": ["Task6", "Task7"]},
]

result = critical_path_method(custom_tasks)
