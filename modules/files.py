def append_to_file(path, appendix):
    with open(path, 'a', encoding='UTF-8') as file:
        file.write(f'{appendix}\n')