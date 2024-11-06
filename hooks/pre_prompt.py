import sys


if __name__ == '__main__':
    print("\n\n\n")
    print("#" * 80)
    print("The napari cookiecutter plugin template has been replaced with a copier template!")
    print()
    print("To create a plugin using the new template, run:")
    print()
    print("python -m pip install copier jinja2-time")
    print("python -m pip install npe2")
    print("copier copy --trust https://github.com/napari/napari-plugin-template new-plugin-name")
    print()
    print("For more information, refer to the template README:")
    print("https://github.com/napari/napari-plugin-template")
    print("#" * 80)
    print("\n\n\n")
    sys.exit(1)
