import view
import model


FILENAME_DATA = 'phonebook.txt'


def select_action():
    while True:
        data = view.show_main_menu()
        if not data or data == 6: break

        if data == 1:
            surname = view.show_surname()
            name = view.show_name()
            tel = view.show_telephone()
            description = view.show_description()
            entry = model.create_contact(surname, name, tel, description)
            model.add_contact(FILENAME_DATA, entry)

        if data == 2:
            filename_import = view.show_filename()
            model.import_csv(filename_import, FILENAME_DATA)

        if data in [3, 4, 5]:  
            phonebook = model.get_all_entries(FILENAME_DATA)
            filename_export = view.show_filename()
            if data == 3:
                csv = model.generate_csv(phonebook)
                model.write_to_file(filename_export, csv)
            if data == 4:
                xml =  model.generate_xml(phonebook)
                model.write_to_file(filename_export, xml)
            if data == 5:
                json = model.generate_JSON(phonebook)
                model.write_to_file(filename_export, json)
    return