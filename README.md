# Excel-Driven Web Form Automation

A Python + Selenium script that reads rows from an Excel file and automatically fills and submits a web form for each row.

## Features
- Reads records (Name, Email, Phone, Service, Details) from `data1.xlsx` with Pandas
- Opens Chrome with Selenium WebDriver and loads a sample "Get a Quote" form (`index.html`)
- Fills text fields and selects the service from a dropdown for every row
- Clicks **Get Quote** to submit, then moves to the next record
- Includes the demo form and sample Excel data, so it runs end-to-end out of the box

## Tech Stack
Python, Selenium WebDriver, Pandas, OpenPyXL, HTML/CSS (demo form)

## Setup
```bash
cd Read_data_from_excel
pip install -r requirment.txt
```
Update the form path in `main.py` to your local copy of `index.html`:
```python
driver.get(r"file:///<your-path>/Read_data_from_excel/index.html")
```
Then run:
```bash
python main.py
```
Requires Google Chrome (Selenium Manager downloads the matching driver automatically).

## Excel Format
| Name | Email | Phone | Service | Details |
|------|-------|-------|---------|---------|

`Service` must match a dropdown option in the form (e.g. Web Development, Testing, SEO).

## Project Structure
```
Read_data_from_excel/
  main.py          # automation script
  index.html       # sample quote form
  data1.xlsx       # sample input data
  requirment.txt   # dependencies
```

## Author
**Ritik Kumar**
