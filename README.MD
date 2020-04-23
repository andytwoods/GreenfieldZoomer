# Greenfield Zoomer

## Installing on your local system

* Clone from github

* Create a virtual environment (I'm using Python 3.6)

* Install requirements

```pip install -r requirements.txt```

* Use PyInstaller to create a distribution using the zoomer.spec file for instructions

```pyinstaller zoomer.spec```

## Useful info
* You need to specify files you want to include in the bundle in zoomer.spec (this was done for joinButton.png).
* using [PyInstaller](https://www.pyinstaller.org/) which hopefully means app will work on PC, MAC or Linux, with an easy installation.
* Using [PyaAutoGUI](https://automatetheboringstuff.com/2e/chapter20/) to manipulate the operating system into opening up zoom, pasting details in correct places etc.

## Best to take care of the following
* Best we don't add teachers' zoom creds to our git repo ;)

## Things to do
* GUI. Perhaps a grid of teachers' faces
* Figure out how to make a file for circulation
* Cross platform support?