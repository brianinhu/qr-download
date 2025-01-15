# File download with QR and button

## Description
This project shows how to download an excel file (.xlsx) with a QR generated with the qrcode library and a button. In addition, a local server is implemented using the computer's wifi so that other devices can access the page and download the file.

## Steps
1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Open `views.py` and change the IP address in line 32 to the IP address of your computer.
4. Open the terminal and go to the ..\qr-template directory with the command `cd .\mysite`.
5. Execute the command `py manage.py runserver 0.0.0.0:8000`.
6. Enter the address `http://127.0.0.1:8000/` in your browser to view the page.
7. In the browser of another device, type `http://<computer IP address>:8000/` to view the page.

## Results

- ### Desktop

<img src="mysite/media/desktop.png" alt="Logo de Markdown" width="600">

- ### Mobile

<img src="mysite/media/mobile.png" alt="Logo de Markdown" width="200">
