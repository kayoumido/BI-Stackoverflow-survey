# Code

## extract_technologies.py

This script will go through raw data and look for the technologies that are **used** by the developers that filled the survey.

* Respondent
* Gender
* HaveWorkedLanguage
* HaveWorkedFramework
* HaveWorkedPlatform
* IDE
* Methodology
* VersionControl

Once found it will generate two processed csv files, one with the technologies and the other will contain pretty much the same data as the raw version the only difference being is it wont contain technologies columns.

### How to use

```
$ python code\scripts\extract_technologies.py --help
usage: extract_technologies.py [-h] --raw RAW [--processed PROCESSED]
                               [--output OUTPUT]

optional arguments:

  -h, --help            show this help message and exit
  --raw RAW, -r RAW     name of the file containing the raw data
  --processed PROCESSED, -p PROCESSED
                        name for the processed file
  --output OUTPUT, -o OUTPUT
                        destination path for processed data
```
