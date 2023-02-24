import csv
import tabula
from flask import Flask, request, jsonify
import os


def convert_pdfs_to_csv(pdfs):
    csv_data = []
    for pdf in pdfs:
        tabula.convert_into(pdf, 'converted.csv',
                            output_format="csv", pages="all", area=(80, 30, 1080, 810))
        with open('converted.csv', 'r') as file:
            reader = csv.reader(file)
            csvvalues = list(reader)
            csv_data.append(csvvalues)
    return csv_data


app = Flask(__name__)


@app.route('/convert', methods=['POST'])
def convert():
    pdfs = request.files.getlist('pdfs')
    csv_data = convert_pdfs_to_csv(pdfs)
    return jsonify({'data': csv_data})


if __name__ == '__main__':
    app.run(debug=True)


# import csv
# import tabula
# tabula.convert_into('data.pdf', 'converted.csv',
#                     output_format="csv", pages="all", area=(80, 30, 1080, 810))
# with open('converted.csv', 'r') as file:
#     reader = csv.reader(file)
#     csvvalues = list(reader)

# import os
# import csv
# import tabula

# files = os.listdir()
# for file in files:
#     if file.endswith(".pdf"):
#         tabula.convert_into(file, 'converted.csv', output_format="csv",
#                             pages="all", area=(80, 30, 1080, 810))

#         csvvalues = []
#         for file in files:
#             if file.endswith(".csv"):
#                 with open(file, 'r') as file:
#                     reader = csv.reader(file)
#                     csvvalues.extend(list(reader))

#                     with open('merged.csv', 'w', newline='') as file:
#                         writer = csv.writer(file)
#                         writer.writerows(csvvalues)
