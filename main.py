import csv
import os
from PIL import Image, ImageDraw, ImageFont


# Function to read CSV data
def csvDataReader(file: str = "names.csv"):
    with open(file, "r") as names:
        csvFile = csv.reader(names)
        data_list = [lines for lines in csvFile]
    return data_list

# Function to read coordinates and details from the txt file
def attributeReader(file: str = "attributes.txt"):
    attr_list = []
    with open(file, "r") as coordinates:
        for no, line in enumerate(coordinates):
            if no == 0:
                continue
            details = line.strip().split(",")
            attr_list.append({
                "field": details[0],  # Field name (e.g., Name, School)
                "x": int(details[1]),  # X position
                "y": int(details[2]),  # Y position
                "font_name": details[3].strip(),  # Font name
                "font_size": int(details[4]),  # Font size
                "color": details[5].strip(),  # Text color
            })
    return attr_list

# Function to draw the certificates
def certificate_drawer():

    # Read the CSV data (names, positions, etc.)
    csvDataPath = input("Enter Student Names file path (csv only): ")
    csvData = csvDataReader(csvDataPath)
    no_of_fields = len(csvData[0])
    no_of_data = len(csvData)

    # Read the coordinates and other details for the text
    attrDataPath = input("Enter Coordinates attributes path (txt only): ")
    attrData = attributeReader(attrDataPath)

    # Input of template path
    TEMPLATE_PATH = input("Enter Certificate Template Path: ")

    # Output directory input
    output_dir = input("Enter Output Directory: ")
    output_dir += "/certificates" if not output_dir.endswith("/certificates") else ""
    
    # Create attributes directory to save the generated certificates
    os.makedirs(output_dir, exist_ok=True)

    # Loop over each student's data from the CSV
    for item in range(1, no_of_data):
        template = Image.open(TEMPLATE_PATH)

        # Prepare the font object (default to ITCEDSCR.TTF, can be dynamic)
        draw = ImageDraw.Draw(template)

        # Loop over each field (name, school, etc.) and draw them on the template
        for i in range(no_of_fields):
            text = csvData[item][i]
            # Get corresponding field details from the coordinates file
            coord = attrData[i]
            font = ImageFont.truetype(coord["font_name"], coord["font_size"])

            # Draw the text at the specified coordinates, size, and color
            draw.text(
                xy=(coord["x"], coord["y"]),
                text=text,
                fill=coord["color"],  # Use the color from coordinates.txt
                font=font
            )

        # Save the certificate with the student's name as the filename
        template.save(f"{output_dir}/{item}_certificate.png", "PNG")

    print(f"💡 Done!\nCertificates generated successfully!\nCheck at {output_dir}")

while True:
    certificate_drawer()
    if input("Again?(y/n): ").lower() == "n":
        break
