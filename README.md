TagZ
-------------

A command line program for Linux that can add tags, description to a file and 
allows you to perform a full text search on those tags to search for files.


### Examples

1. Getting Help

        (venv)khirod@kurosaki:~/Documents/TagZ$ tagz -h
        usage: tagz [-h] [-f FILENAME] [-s]

        optional arguments:
        -h, --help            show this help message and exit
        -f FILENAME, --filename FILENAME
                        you want to index a new file
        -s, --search          search a file

2. Indexing a File

        (venv)khirod@kurosaki:~/Documents/TagZ$ tagz -f LICENSE 
        Tags [separated by a space]: license tagz
        Description [short description]: A GPL V3 license file


3. Searching a File using tags

        (venv)khirod@kurosaki:~/Documents/TagZ$ tagz -s
        Enter tags to be searched [space separated]: license
        Files containing the given tags are: 
        ==============================================
        *  File Name: LICENSE
        *  Description: A GPL V3 license file.
        *  File Path: /home/khirod/Documents/TagZ/LICENSE
        *  File Tags: [u'license', u'tagz']

