import csv
import argparse
import os


def main(argv):

    wanted_cols = [
        "HaveWorkedLanguage",
        "HaveWorkedFramework",
        "HaveWorkedDatabase",
        "HaveWorkedPlatform",
        "IDE",
        "Methodology",
        "VersionControl",
    ]

    wanted_cols_index = []

    with open(argv.raw, newline='') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',')


        output = argv.output if argv.output else 'data/processed/'
        filename = argv.processed if argv.processed else 'extracted_technologies.csv'

        headers = next(csv_data)
        # get the indexes of the wanted_cols
        for technologie_col in wanted_cols:
            index = headers.index(technologie_col)

            if index or index == 0:
                wanted_cols_index.append(index)
                # remove them from the headers
                del headers[index]

        # created processed files in output dir
        # (one for the extracted data and one for the original data without extracted data)
        extracted = open(output + filename, 'w+')
        ogpreocessed = open(output + 'survey_results_clean.csv', 'w+')
        # write headers in new files
        extracted.write('Respondent,Technologies\n')
        ogpreocessed.write(';:'.join(headers) + '\n')

        # get the data of the wanted cols
        for row in csv_data:
            id = row[0]
            technologies = []

            # extract the data of the wanted cols
            for i in wanted_cols_index:
                # skip NA
                if (row[i] != "NA"):
                    technologies += row[i].split(';')
                # remove wanted cols
                del row[i]

            for tech in technologies:
                extracted.write(id + ',' + tech.lstrip() + '\n')

            # write line without the wanted cols in prcessed original file
            ogpreocessed.write(';:'.join(row) + '\n')


if __name__ == "__main__":
    # initiate parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--raw", "-r", help="name of the file containing the raw data", required=True)
    parser.add_argument("--processed", "-p", help="name for the processed file")
    parser.add_argument("--output", "-o", help="destination path for processed data")

    # read arguments from cli
    args = parser.parse_args()

    main(args)
