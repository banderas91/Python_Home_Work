

def create_contact(surname: list, name: list, telephone: list, description: list) -> dict:
    return {
        "surname": surname,
        "name": name,
        "telephone": telephone,
        "description": description
    }


def add_contact(filename, contact: dict):
    with open(filename, mode='a', encoding="utf-8") as f:
        f.write(str(contact) + '\n')






