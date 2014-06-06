KTagZ
-------------

A command line program for Linux that can add tags, description to a file and 
allows you to perform a full text search on those tags to search for files.

### Note

This package is for demonstration purposes only. A full fledged package is yet to come. Please raise issues on github. And feel free to fork and contribute.

### Installlation

1. You need xapian to run. So install using

        sudo apt-get install python-xapian libxapian-dev

2. Create a virtual environment to install ktagz

        virtualenv --system-site-packages venv
        source venv/bin/activate
        pip install ktagz


### Running Examples

1. Getting Help

        khirod@kurosaki:~/Documents/KTagZ$ ktagz -h
        usage: ktagz [-h] [-f FILENAME] [-st] [-sd] [-sn]

        optional arguments:
        -h, --help            show this help message and exit
        -f FILENAME, --filename FILENAME
                              you want to index a new file
        -st, --searchtags     search for a file based on tags
        -sd, --searchdescription
                              search for a file based on its description
        -sn, --searchname     search for a file based on its name


2. Indexing a File

        (venv)khirod@kurosaki:~/Documents/KTagZ$ ktagz -f LICENSE 
        Tags [separated by a space]: license
        Description [short description]: A GPL V3 license file


        (venv)khirod@kurosaki:~/Documents/KTagZ$ ktagz -f LICENSE.txt
        Tags [separated by a space]: license ktagz
        Description [short description]: A GPL V2 license file


3. Searching a File using tags

        (venv)khirod@kurosaki:~/Documents/TagZ$ ktagz -st
        Enter tags to be searched [space separated]: license

        Results are
        --------------------------------------

        *  File Name: LICENSE
        *  Description: A GPL V3 license file.
        *  File Path: /home/khirod/Documents/KTagZ/LICENSE
        *  File Tags: [u'license']

        *  File Name: LICENSE.txt
        *  Description: A GPL V2 license file.
        *  File Path: /home/khirod/Documents/KTagZ/LICENSE.txt
        *  File Tags: [u'license', u'ktagz']

        
        LICENSE appears as top result, because we gave only one tag license and that is satisfied with LICENSE while 
        LICENSE.txt also had 'ktagz' as a tag hence it got a lower score and appeared lower.


4. Search a File using description

        (venv)khirod@kurosaki:~/Documents/TagZ$ ktagz -sd
        Rough description to be searched: license V2 file

        Results are
        --------------------------------------

        *  File Name: LICENSE.txt
        *  Description: A GPL V2 license file.
        *  File Path: /home/khirod/Documents/KTagZ/LICENSE.txt
        *  File Tags: [u'license', u'tagz']

        *  File Name: LICENSE
        *  Description: A GPL V3 license file.
        *  File Path: /home/khirod/Documents/KTagZ/LICENSE
        *  File Tags: [u'license', u'tagz']

        Here LICENSE.txt appears as top result because the description only LICENSE.txt had all the three words we mentioned 
        in description while LICENSE had only two.
