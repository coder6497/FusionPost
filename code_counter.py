import json, os

file_and_count = {}
for root, _, files in os.walk(input("Enter filepath >> ")):
    for file in files:
        full_path = os.path.join(root, file)
        filename, ext = os.path.splitext(full_path)
        if ext in ['.py', '.html'] and "migrations" not in filename:
            with open(full_path, 'r', encoding='utf-8') as f:
                file_and_count[full_path] = len(f.readlines())

file_and_count["ALL"] = sum([value for value in file_and_count.values()])

with open("project_lines_count.json", 'w', encoding='utf-8') as f:
    json.dump(dict(sorted(file_and_count.items(), key=lambda x: x[1])), f, indent=4)