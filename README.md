## Gettings Started
You will need python 3.6. 

* [How to set up a virtual environment:](https://python-scripts.com/virtualenv)



### Install and run
```bash
$ git clone https://github.com/BobrovPavel/task.git
$ cd task
$ pip install -r requirements.txt
$ pytest path/to/test
```
or
```bash
$ pytest --browser=firefox path/to/test
```
## Webdrivers

### Downloading
* [ChromeDriver](http://chromedriver.chromium.org/) -  for Chrome Browser
* [GeckoDriver](https://github.com/mozilla/geckodriver/releases) - for Firefox Browser

### Install on Ubuntu
1. Unzip webDriver files
2. Move the file to /usr/bin directory
```
$ sudo mv chromedriver /usr/bin
```
3. Go to /usr/bin directory and run next command to mark it executable
```
$ chmod a+x chromedriver
```
or
```
$ chmod a+x geckodriver
```

### Install on Windows
1. Unzip webDriver files
2.  [Add the path to the folder with the drivers in the PATH system variable
](https://www.computerhope.com/issues/ch000549.htm) 
