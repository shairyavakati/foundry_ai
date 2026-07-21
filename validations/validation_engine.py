def validate(data, rules):
    errors = {}
    for field_name, field_rules in rules.items():
        field_value = data.get(field_name)
        if field_rules.get("required"):
            if field_value is None or field_value == "":
                errors[field_name] = field_rules.get("empty_error", "Field is required")
                continue
    return errors
        