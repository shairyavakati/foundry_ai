from validations.validation_config import TYPE_MAPPING

def validate(data: dict, rules: dict) -> dict:

    errors = {}

    for field_name, field_rules in rules.items():
        field_value = data.get(field_name)


        expected_type = TYPE_MAPPING.get(field_rules.get("type"))

        if expected_type is None:
            raise ValueError(
                f"Invalid type '{field_rules.get('type')}' configured for '{field_name}'"
            )

        if field_rules.get("required") and field_value is None:
            errors[field_name] = field_rules.get(
                "required_error",
                "Field is required"
            )
            continue

        if field_value is None:
            continue

        if not isinstance(field_value, expected_type):
            errors[field_name] = field_rules.get(
                "type_error",
                f"Field must be of type {expected_type.__name__}"
            )

    return errors

       
        
        