def validate_records(records, schema):
    """
    Validate records against a schema definition.
    """
    type_map = {
        "int": int,
        "float": float,
        "str": str
    }

    results = []

    for idx, record in enumerate(records):
        errors = []

        for col_def in schema:
            column = col_def["column"]

            if column not in record:
                errors.append(f"{column}: missing")
                continue

            value = record[column]

            if value is None:
                if not col_def["nullable"]:
                    errors.append(f"{column}: null")
                continue

            expected = col_def["type"]

            if expected == "float":
                valid_type = type(value) in (int, float)
            else:
                valid_type = type(value) is type_map[expected]

            if not valid_type:
                errors.append(
                    f"{column}: expected {expected}, got {type(value).__name__}"
                )
                continue

            if expected in ("int", "float"):
                if "min" in col_def and value < col_def["min"]:
                    errors.append(f"{column}: out of range")
                elif "max" in col_def and value > col_def["max"]:
                    errors.append(f"{column}: out of range")

        results.append((idx, len(errors) == 0, errors))

    return results