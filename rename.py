import os
import glob


def list_files(directory, extension):
    return glob.glob(f"{directory}/*.{extension}")

def rename_file(file_name):
    new_file_name = file_name.replace("Certificado", "Curso")
    os.rename(file_name, new_file_name)

if __name__ == "__main__":
    directory = "Certificates"
    extension = "pdf"
    files = list_files(directory, extension)
    for file in files:
        rename_file(file)
    files = list_files(directory, extension)
    print("\n".join(files))
    # print("\n".join(files).replace("Certificado", "Curso"))
