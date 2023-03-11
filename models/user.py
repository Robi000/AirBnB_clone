from models import base_model


class User (base_model.BaseModel):
    email = ""
    first_name = ""
    password = ""
    last_name = ""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
