# Resource importer for iOS and Android

## Setup
* Install python@3.9 with pip (python package manager)
e.g. `brew install python`
* Clone project
* Checkout branch `master`
* Set the virtual environment
`python3 -m venv venv`
* Activate virtual environment
`source venv/bin/activate`
* If you need to deactive it, simply execute `deactivate` command
* Install dependencies
`pip install -r requirements.txt`

## Usage
* Usage `python resource_importer.py [source] [platform] --fileformat [format]`
* Required: `source` and `platform`
* Optional: `--fileformat`
* Available values: 
	* `source`:`local`,`google_sheets` 
	* `platform`:`android`,`ios`
	* `fileformat`:`csv`,`json`,`xml`
* Example: `python resource_importer.py local android --fileformat csv`
* Use `python resource_importer.py --help` to see available options

## References and links
* Homebrew - https://brew.sh/
* Python virtual environment - https://docs.python.org/3/tutorial/venv.html
* Google Sheets API for Python - https://developers.google.com/sheets/api/quickstart/python
* Google Sheets API troubleshooting - https://developers.google.com/sheets/api/quickstart/python#troubleshooting