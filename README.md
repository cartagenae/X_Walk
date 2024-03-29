<img width="248" alt="x_walk" src="https://user-images.githubusercontent.com/6395465/59654061-6551a380-9149-11e9-8e5e-6756ac522262.png">

* Automatically rename your files documented on your excel spreadsheet.
* __Useful if you have thousands of files stored in your file system that you wish to rename.__

## Overview

<img width="770" alt="overview_01" src="https://user-images.githubusercontent.com/6395465/61194978-0fa1e580-a67a-11e9-8756-fbcc63a49386.png">

<img width="768" alt="overview_02" src="https://user-images.githubusercontent.com/6395465/61194979-12043f80-a67a-11e9-8e55-ef9652f3a31e.png">

### sample.xls
<img width="588" alt="overview_03" src="https://user-images.githubusercontent.com/6395465/61194984-20eaf200-a67a-11e9-9d2c-9c05c3612cdb.png">

> NOTE:
> * The files retain their original formats and extensions.
> * The data (in this example the Profile column) does not get overwritten within the spreadsheet.

## Requirements

### Git

##### Mac
https://git-scm.com/download/mac

##### Windows
https://git-scm.com/download/win

##### Linux
https://git-scm.com/download/linux

### Python
> NOTE: Install the latest version of Python 3

##### Mac
https://www.python.org/downloads/mac-osx/

##### Windows
https://www.python.org/downloads/windows/

##### Linux
https://www.python.org/downloads/source/

##

###### Check if you have Python installed on your machine:
```
python --version
```
<img width="571" alt="Screen Shot 2020-03-31 at 5 48 49 PM" src="https://user-images.githubusercontent.com/6395465/78088083-fc55b800-7377-11ea-84eb-e054e0602d38.png">

###### Check if you have Git installed on your machine:
```
git --version
```
<img width="573" alt="Screen Shot 2020-03-31 at 5 48 11 PM" src="https://user-images.githubusercontent.com/6395465/78088116-142d3c00-7378-11ea-8db0-775f037cd10a.png">

## Installation

### Run each line seperately in your terminal / command prompt

### Mac / Linux
```
• git clone https://github.com/cartagenae/X_Walk/
• cd X_Walk/
• pip3 install --upgrade pip
• pip3 install -r requirements.txt
```

### Windows
```
• git clone https://github.com/cartagenae/X_Walk/
• cd X_Walk/
• pip install --upgrade pip
• pip install -r requirements.txt
```

__After installing the requirements file:__

* Place the x_walk.py file in the same folder where the Excel file you're working with is located at.
* Make sure your Excel spreadsheet is on the same folder as your files you wish to rename and your x_walk.py file.

<img width="771" alt="Screen Shot 2019-06-19 at 2 44 20 AM" src="https://user-images.githubusercontent.com/6395465/59755888-901d2400-923d-11e9-82e9-5d0371eae5bd.png">

* Within your terminal/command prompt, navigate to the directory where all your files are located.

<img width="571" alt="installation_02" src="https://user-images.githubusercontent.com/6395465/61241999-816d4400-a6f9-11e9-8994-c5eb9c29f884.png">

> NOTE: The path varies depending on where you placed your files.

## How to Use ...

__In your terminal / command prompt...__
* Enter 'python3 x_walk.py'
* If you're using __Windows__, enter __'python x_walk.py'__

<img width="570" alt="Usage_1" src="https://user-images.githubusercontent.com/6395465/59801226-26ccfd80-929d-11e9-8c33-1827167149a2.png">

X Walk will scan all your Excel files located on its folder and list them alphabetically.<br />
<br />
Enter the option number your Excel file is located at.

<hr />

<img width="570" alt="Usage_02" src="https://user-images.githubusercontent.com/6395465/61194098-3b21d180-a674-11e9-890c-440b482e3f73.png">

After choosing your file, X Walk scans all the columns within your spreadsheet and lists them.<br />
<br />
Enter the option number of the column containing the files you wish to rename.

<hr />

<img width="570" alt="Usage_03" src="https://user-images.githubusercontent.com/6395465/61194112-4f65ce80-a674-11e9-80f3-34876db49580.png">

Enter the option number of the column you are using to rename your original file.

<hr />

<img width="569" alt="Usage_04" src="https://user-images.githubusercontent.com/6395465/61194115-52f95580-a674-11e9-8df6-5ae2ba429e6f.png">

Enter 'y'(es) or 'n'(o) to use another column.

<hr />

<img width="568" alt="Usage_07" src="https://user-images.githubusercontent.com/6395465/61194118-55f44600-a674-11e9-87c0-f70127a3bd91.png">

After selecting all the columns you wish to use by entering 'n', enter 'y' to rename your chosen files.

<hr />

<img width="766" alt="Usage_08" src="https://user-images.githubusercontent.com/6395465/59806920-ef654d80-92aa-11e9-973c-ba854f3dd817.png">

Check your folder to confirm your files have been renamed.

<hr />

<img width="570" alt="Usage_09" src="https://user-images.githubusercontent.com/6395465/59806634-e4f68400-92a9-11e9-850c-b4c58a431ab7.png">

Type 'x' to close the program

<img width="568" alt="Usage_10" src="https://user-images.githubusercontent.com/6395465/59806657-f6d82700-92a9-11e9-818a-892651affda9.png">

## License

X Walk is released under the **MIT License**. See the bundled <a href='https://github.com/cartagenae/X_Walk/blob/master/LICENSE' alt='x walk license file'>**LICENSE**</a> file for details.
