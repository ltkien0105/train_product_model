import csv
import requests

with open('Medicine_Details.csv', 'r') as med_detail_file:
    medicine_details = csv.reader(med_detail_file, delimiter=',', quotechar='"')
    target = 'val'
    i = 1
    for index, row in enumerate(medicine_details):
        url = row[4]
        
        extension = url.split('.')[-1]
        response = requests.get(url)
        file_path = f'dataset/{target}/Medicine/medicine_{i}.{extension}'
        
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
                print(f'File {i} downloaded successfully')
        else:
            print('Failed to download file')
        i += 1