import os

def find_files(file_name, search_path):
   result = []
# walking top-down from the root
   for root, dir, files in os.walk(search_path):
      if file_name in files:
         result.append(os.path.join(root, file_name))
   return result
