import os

files = {}
directory = './' # or '../' if you have more than one directory

for element in os.listdir(directory):
    file = os.path.join(directory, element)
    if os.path.isfile(file):
        ext = os.path.splitext(file)[-1]
        # ext = element.split('.')[-1]
        if ext not in files:
            files[ext] = []
            files[ext].append(element)
        else:
            for el in os.listdir(file):
                f = os.path.join(file, el)
                if os.path.isfile(f):
                    ext = os.path.splitext(f)[-1]
                    # ext = el.split('.')[-1]
                    if ext not in files:
                        files[ext] = []
                        files[ext].append(el)

with open(os.path.join(directory, "report.txt"), "w") as output_file:
    for key, value in sorted(files.items()):
        output_file.write(f"{key}\n")
        for file_name in sorted(value):
            output_file.write(f"- - - {file_name}\n")