def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """
    groups = {}
    order = []  

    for record in records:
        key = tuple(record[col] for col in key_columns)

        if key not in groups:
            groups[key] = record
            order.append(key)
        else:
            if strategy == "first":
                continue

            elif strategy == "last":
                groups[key] = record

            elif strategy == "most_complete":
                current = groups[key]

                def none_count(r):
                    return sum(v is None for v in r.values())

                if none_count(record) < none_count(current):
                    groups[key] = record

    return [groups[key] for key in order]