# k2pdfopt_PyQt
Gui for k2pdfopt PDF/DJVU files optimizer in PyQt5. 

Demo video: https://drive.google.com/file/d/1hUq_XvkjxM46H_x1nsN1sejTZs5x3zV_/view

## Requirements
* Python 3.7+

## Installation
First you need to install k2pdfopt program (https://www.willus.com/k2pdfopt/):
```shell
sudo apt-get install k2pdfopt
```
Create and activate a python virtual environment:
```shell
virtualenv -p python3 venv
source venv/bin/activate
```
Clone the repository:
```shell
git clone git@github.com:rafalk342/k2pdfopt-PyQt.git
cd k2pdfopt-PyQt
```
Then, install the requirements:
```shell
pip install -r requirements.txt 
```
And finally run the program:
```shell
python main.py
```

## Contributing
You can use Qt Designer to make changes to the UI. 

To generate python ui file you can use this command:
```shell
python -m PyQt5.uic.pyuic ./ui/main_window.ui -o ./ui/main_window.py
```
