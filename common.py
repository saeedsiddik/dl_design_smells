def get_repo_full_name_and_repo_file_path(file_path):
    file_name_parts = file_path.split('$')
    return "/".join([file_name_parts[0], file_name_parts[1]]), "\\".join(file_name_parts[2:])