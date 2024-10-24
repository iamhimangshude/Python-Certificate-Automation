import csv, os
from PIL import Image, ImageDraw, ImageFont


TEMPLATE_PATH = "D:/Pictures/Certificate-Automation/Certificate-Sample-2-hi-res-jpg.png"

def csvDataReader(file: str = "names.csv "):
    data_list = None
    with open(file, "r") as names:
        csvFile = csv.reader(names)
        data_list = [lines for lines in csvFile]
    return data_list


def coordinatesReader(file: str = "coordinates.txt", fields: int = 1):
    with open(file, "r") as coordinates:
        coordinates_list = []
        for i in range(fields):
            coordinates_list.append(coordinates.readline().split(","))
    return coordinates_list


def certificate_drawer():

    csvData = csvDataReader(input("Enter Student Names file path (csv only): "))
    no_of_fields = len(csvData[0])
    no_of_data = len(csvData)
    coordinateData = coordinatesReader(
        input("Enter Coordinates file path (txt only): "), no_of_fields
    )

    if no_of_data > 1:
        os.makedirs("certificates", exist_ok=True) # Needs to be specified
        for item in range(1,no_of_data):
            template = Image.open(TEMPLATE_PATH) # Needs to change or to be made dynamic
            font = ImageFont.truetype("C:/Windows/Fonts/ITCEDSCR.TTF", 90) # Font needs to be dynamic
            draw = ImageDraw.Draw(template)
            name = csvData[item][1]
            for i in range(no_of_fields):
                try:
                    draw.text(
                        xy=(int(coordinateData[i][1]), int(coordinateData[i][2])),
                        text=csvData[item][i],
                        fill="black", # Color needs to be dynamic
                        stroke_width=2,
                        font=font,)
                except Exception as e:
                    print(e)
            # pass
            template.save(f"certificates/{name.strip()}_certificate.png","PNG")


certificate_drawer()
