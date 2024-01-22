"""Function to check if there are differences between files."""

from gendiff.parsing import get_content
from gendiff.formaters.formater import get_formater
from gendiff.diff import build_diff


def generate_diff(file_path1, file_path2, formater='stylish'):
    """
    Checking and generating differences between two files.
    The argument first_file is path to first file.
    The argument second_file is path to second file.
    The argument format_name is difference output format.
    """

    content1 = get_content(file_path1)
    content2 = get_content(file_path2)
    dicts_diff = build_diff(content1, content2)
    return get_formater(dicts_diff, formater)


# def read_file(file_name):
#     """
#     Accepts a filename.
#     Returns the data of a file and its format.
#     """
#
#     with open(file_name, 'r') as file:
#         file_data = file.read()
#         fyle_format = file_name.split('.')[-1]
#         return file_data, fyle_format
