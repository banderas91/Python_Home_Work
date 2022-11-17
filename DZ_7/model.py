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


def get_all_entries(filename) -> list:
    result = []
    with open(filename, mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline().strip()
            if not line: break
            else:
                result.append(line)
    return result


def parse_contact(entry: str) -> dict:
    entry1 = entry[1:-1]
    result = {}
    contact = entry1.split(',')
    for item in contact:
        key, value = item.split(':')
        result[key.strip()[1:-1]] = value.strip()[1:-1]
    return result


def generate_csv(phonebook: list):
    csv_text = ''
    for entry in phonebook:
        contact = parse_contact(entry)
        line = "#".join(contact.values())
        csv_text += line + '\n'
    return csv_text


def import_csv(filename_import, filename_phonebook_data):
    entries = get_all_entries(filename_import)
    for entry in entries:
        surname, name, telephone, description = entry.split('#')
        contact = create_contact(surname, name, telephone, description)
        add_contact(filename_phonebook_data, contact)


def generate_xml(phonebook: list):
    xml_text = '<?xml version="1.0" encoding="UTF-8" ?><phonebook>\n'
    for entry in phonebook:
        contact = parse_contact(entry)
        contact_str = '<Entry>\n'
        for key,value in contact.items():
            contact_str += f'<{key}>{value}</{key}>\n'
        xml_text+=contact_str+'</Entry>\n'
    xml_text += '</phonebook>'
    return xml_text


def generate_JSON(phonebook: list):
    result = "[\n" + ",\n".join([str(parse_contact(c)).replace("'", '"') for c in phonebook]) + "\n]"
    return result


def write_to_file(filename, data):
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(data)