VALIDATION_CONFIG = {

    "user": {

        "name": {
            "required": True,
            "type": str,
            "min_length": 3,
            "max_length": 100
        },

        "age": {
            "required": True,
            "type": int,
            "min_value": 18,
            "max_value": 120
        },

        "email": {
            "required": True,
            "type": str,
            "regex": r"^[\w\.-]+@[\w\.-]+\.\w+$"
        },

        "phone": {
            "required": True,
            "type": str,
            "length": 10,
            "regex": r"^\d{10}$"
        }

    }

}