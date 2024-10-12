import os
from PIL import Image, ImageDraw, ImageFont


def certificate_generator(
    certificate_template,
    name="Himangshu",
    text_position: tuple = (100, 100),
    font_name: str = "C:\\Windows\\Fonts\\ITCEDSCR.TTF",  # Edwardian Script ITC
    font_size: int = 120,
    color: str = "black",
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
    os.makedirs("certificates", exist_ok=True)
    template_object.save(f"certificates/{name}_certificate.png")


# Main code
try:
    student_name_file = input("Enter student name file path: ")
    template_file_path = input("Enter template file path(*.png only): ")
    color = input("Enter text color: ")
    fontsize = int(input("Enter font size: "))
    textXY = int(input("Enter text position X: ")), int(input("Enter text position Y: "))

    with open(student_name_file, "r") as names:
        name_list = names.read().split(",")
        total = len(name_list)
        count = 0
        for name in name_list:
            certificate_generator(
                template_file_path, name.strip(), textXY, font_size=fontsize, color=color
            )
            count += 1
            print(f"\rProcessing\t\t{count}/{total}")
            

        print("\n\n Done! ")
        print("💡Check at 'certificates' folder")
except Exception as e:
    print(f'Error: {e}')
