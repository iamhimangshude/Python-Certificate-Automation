import os
from PIL import Image, ImageDraw, ImageFont


def certificate_generator(
    certificate_template,
    name="Himangshu",
    text_position: tuple = (100, 100),
    font_name: str = "C:\\Windows\\Fonts\\ITCEDSCR.TTF",  # Edwardian Script ITC
    font_size: int = 120,
    color: str = "black",
    output: str = "."
):
    font_object = ImageFont.truetype(font_name, font_size)
    template_object = Image.open(certificate_template)
    draw_object = ImageDraw.Draw(template_object)

    draw_object.text(
        text_position,
        name,
        align="m",
        fill=color,
        font=font_object,
    )
    os.makedirs(output + "certificates", exist_ok=True)
    template_object.save(output + f"certificates\\{name}_certificate.png")


# Main code
while True:
    try:
        student_name_file = input("Enter student name file path: ")
        template_file_path = input("Enter template file path(*.png only): ")
        color = input("Enter text color: ")
        fontsize = int(input("Enter text size: "))
        textXY = int(input("Enter text position X: ")), int(input("Enter text position Y: ")) # Getting the coordinates to draw the text
        outputFolder = input("Enter output folder path: ")

        # Existence of files being checked
        if not os.path.exists(student_name_file):
            raise FileNotFoundError
        if not os.path.exists(template_file_path):
            raise FileNotFoundError

        with open(student_name_file, "r") as names:
            name_list = names.read().split(",")
            total = len(name_list)
            count = 0
            for name in name_list:
                certificate_generator(
                    template_file_path, name.strip(), textXY, font_size=fontsize, color=color, output=outputFolder
                )
                count += 1
                print(f"\rProcessing\t\t{count}/{total}", end=" ")
                

            print("\n\n Done! ")
            print(f"💡Check at '{outputFolder}certificates' folder")
            print('Again? (y/n)')
            if input().lower() != 'y':
                break
    except Exception as e:
        print(f'Error: {e}')
        print('Retry? (y/n)')
        if input().lower() != 'y':
            break
