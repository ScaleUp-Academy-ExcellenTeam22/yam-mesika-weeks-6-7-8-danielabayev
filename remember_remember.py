from PIL import Image


def read_photo_message(file_path: str):
    """
    This function receive path to image, read the image and print the encrypted message.
    :param file_path: The path to the image.
    """
    image = Image.open(file_path)
    pixel = image.load()
    for col in range(image.size[0]):
        for row in range(image.size[1]):
            if pixel[col, row] == 1:
                print(chr(row), end="")


if __name__ == "__main__":
    read_photo_message(r"{path}".format(path=input("insert file path")))
    # C:\Users\dan52\PycharmProjects\pythonWeeks6 - 7 - 8\code.png
