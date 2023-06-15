import os

def replace_file_paths(directory, old_path, new_path):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Replace with the desired file extension
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                content = file.read()

            updated_content = content.replace(old_path, new_path)

            with open(file_path, 'w') as file:
                file.write(updated_content)

            print(f"Updated file: {filename}")

# Usage example
directory = 'C:/Users/tajvd/OneDrive - education.wa.edu.au/School/2023/Notes/content/notes'  # Replace with the actual directory path
old_path = ''  # Replace with the old file path
new_path = ''  # Replace with the new file path

replace_file_paths(directory, old_path, new_path)
