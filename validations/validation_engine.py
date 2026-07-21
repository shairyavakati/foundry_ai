def validate(data, rules):
    errors = {}
    for field_name, field_rules in rules.items():
        field_value = data.get(field_name)
        if "empty_error" in field_rules:
            if not field_value:
                errors[field_name] = field_rules["empty_error"]
                continue