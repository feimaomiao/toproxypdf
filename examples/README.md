# Examples

In this file, you will see how different flags will alter the output file and the console output.  
Because of formatting issues and size concerns, only the first "page" of the output will be displayed.  

Required Argument:  

- [folder](#folder)  

Optional Arguments

- [-h help functions](#help)  
- [-o output file selection](#output)
- [-e exclude filenames](#exclude)
- [-d dpi](#dpi)

## folder

Folder has to be designated while initiating the program  
Possible program calls:  

- `toproxypdf folder`
- `toproxypdf folder [arguments]`  
- `toproxypdf [arguments] folder`
- `toproxypdf [arguments] folder [arguments]`

Folder has to be a valid folder path or `FileNotFoundError` will be raised  
Folder must contain valid images or `IndexError` will be raised  
  
  A normal output looks like this:  

```none
> toproxypdf images
 
Reading from folder:    images
Outputting to file:     output.pdf
Overwrite existing file:False
Excluded Files:
Output DPI:             1000
Repeats:                1
Corner:                 False
Verbosity:              1
....
  ```  

  ![A normal output file](.images/0.png)  

## help

`toproxypdf -h`  or `--help` both displays the help menu.

```none
> toproxypdf -h

usage: toproxypdf [-h] [-o OUTPUT] [-e EXCLUDED [EXCLUDED ...]] [-d DPI] [-c--corner] [-r REPEAT] [--overwrite] [-v | -q] folder

...
```

## output

`toproxypdf -o FILENAME` or `--output FILENAME` sets the output of this program to FILENAME  
The default output file is called `output.pdf`  
If the designated output file has been taken, `FileExistsError` will be raised, you can prevent this by using the flag [--overwrite](#overwrite)  

File Name behaviors:  
  
If designated output file ends with extension ".pdf": designated output filename will be used.  
`toproxypdf -o "tasigur control.pdf"` -> "tasigur control.pdf"

If designated output file does not have extension ".pdf", it will be manually added  
`toproxypdf -o "tasigur control"` -> "tasigur control.pdf"

## exclude

Unwanted files can be excluded from the output file with the -e or --exclude flag following the beginning of file name  
For example:  
`toproxypdf -e force images`  
would ignore every file in images that starts with "force", i.e. Force of will and Force of Negation.  
The output would look like this:

```None
Reading from folder:    images
...
Excluded Files:         force
...
Excluded file name              |Reason
Force of Negation.png           |is in excluded list
Force of Will (2XM Showcase).png|is in excluded list
...
```  

![Output file excluding force of will and force of negation](./.images/1.png)  
If you want to exclude files more specifically, you can use quotation marks.  
For example, if we only want to exclude Force of Will:  

```None
> toproxypdf images -e "force of will"

...
Excluded Files:         force of will
...
Excluded file name              |Reason
Force of Will (2XM Showcase).png|is in excluded list
...
```

![Output file that only excludes force of will](./.images/2.png)  

You can also exclude different files separated by spaces  
For example, if we want to exclude both Pact of Negation and Tainted Pact:  

```None
> toproxypdf images -e tainted pact
(argparse treats "tainted" and "pact" as two different arguments, therefore files starting with "tainted" i.e. tainted pact, and files starting with "pact", i.e. pact of negation will both be excluded)

...
Excluded Files:         tainted /pact
...
Excluded file name  |Reason
Pact of Negation.png|is in excluded list
Tainted Pact (b).png|is in excluded list
...
```

![output file excluding both tainted pact and pact of negation](./.images/8.png)

## dpi

DPI, or dots per pixel, is directly correlated with the file size and how detailed the images originally is, it is defaulted to 1000 and can be changed through the -d or --dpi flag.  
Note that the final output file size and processing time of the images are both directly correlated with the dpi.  

```None
toproxypdf images -d 300
...
Output DPI:             300
...
```
