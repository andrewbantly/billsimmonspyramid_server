# import os
# import json
# from django.conf import settings

# def read_json_files(data_folder):
#     json_data = []

#     # Get a list of all files in the "data" folder
#     file_list = os.listdir(settings.BASE_DIR, data_folder)

#     for filename in file_list:
#         # Check if the file is a JSON file
#         if filename.endswith('.json'):
#             file_path = os.path.join(data_folder, filename)
#             with open(file_path, 'r') as file:
#                 # Load the JSON data from the file and append it to the list
#                 json_data.append(json.load(file))

#     return json_data

# # print test:
# print(read_json_files("data"))