
import csv
import os
import time
import img2pdf
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

    csvDataPath = input("Enter Student Names file path (csv only) OR press enter to quit: ")
    if csvDataPath == "":
        print("Quitting...")
        time.sleep(2)
        exit()
    csvData = csvDataReader(csvDataPath)
    no_of_fields = len(csvData[0])
    no_of_data = len(csvData)

    attrDataPath = input("Enter Attributes file path (txt only): ")
    attrData = attributeReader(attrDataPath)


    TEMPLATE_PATH = input("Enter Certificate Template Path: ")

    # Output directory input
    output_dir = input("Enter Output Directory: ") or "."

    if output_dir.endswith("/") and os.name == 'nt':
        output_dir += "certificates"
    elif not output_dir.endswith("/") and not output_dir.endswith(".") and os.name == 'nt':
        output_dir += "\\certificates"
    elif output_dir.endswith(".") and os.name == 'nt':
        output_dir = os.getcwd() + "\\certificates"

    # Create attributes directory to save the generated certificates
    os.makedirs(output_dir, exist_ok=True)

    generated_certificates_list = []

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
        
        filename = f"{output_dir}\\{item}_certificate.png"
        generated_certificates_list.append(filename)
        template.save(filename, "PNG")
    
    with open(f"{output_dir}\\Generated_Certificates.pdf", "wb") as pdfFile:
        pdfFile.write(img2pdf.convert(generated_certificates_list))

    print(f"💡 Done!\nCertificates generated successfully along with PDF file!\nCheck at {output_dir}")

while True:
    try:
        certificate_drawer()
    except Exception as e:
        print(e)
    if input("Again?(y/n): ").lower() != "y":
        print("Bye!")
        time.sleep(2)
        break
