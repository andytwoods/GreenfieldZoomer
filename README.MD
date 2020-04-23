# Greenfield Zoomer

## Installing on your local system

* Clone from github

* Install requirements

```pip install -r requirements.txt```

* Use PyInstall to create a distribution using the zoomer.spec file for instructions

```pyinstaller zoomer.spec```

## Useful info
* you need to specify files you want to include in the bundle in zoomer.spec (this was done for joinButton.png).
* using [PyInstaller](https://www.pyinstaller.org/) which hopefully means app will work on PC, MAC or Linux, with an easy installation.
* using [PyaAutoGUI](https://automatetheboringstuff.com/2e/chapter20/) to manipulate the operating system into opening up zoom, pasting details in correct places etc.

## Things to do
* Best we don't add teachers' zoom creds to our git repo ;)

## Things to do
* GUI. Perhaps a grid of teachers' faces
* figure out how to make a file for circulation
* cross platform support?