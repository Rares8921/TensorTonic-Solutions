def schedule_pipeline(tasks, resource_budget):
    """
    Schedule ETL tasks respecting dependencies and resource limits.
    """
    tasks_by_name = {t["name"]: t for t in tasks}
    completed = set()
    started = set()
    running = []
    schedule = []
    time = 0

    while len(completed) < len(tasks):
        running.sort()

        while running and running[0][0] <= time:
            _, name = running.pop(0)
            completed.add(name)

        used = sum(tasks_by_name[name]["resources"] for _, name in running)

        ready = sorted(
            t["name"]
            for t in tasks
            if t["name"] not in started
            and all(d in completed for d in t["depends_on"])
        )

        for name in ready:
            task = tasks_by_name[name]
            if used + task["resources"] <= resource_budget:
                started.add(name)
                schedule.append((name, time))
                running.append((time + task["duration"], name))
                used += task["resources"]

        if len(completed) < len(tasks):
            time = min(end for end, _ in running)

    return sorted(schedule, key=lambda x: (x[1], x[0]))