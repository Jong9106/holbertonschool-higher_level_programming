![enter image description here](https://i.imgur.com/OlHbnFw.png)
# 0x14. JavaScript - Web scraping

-   Foundations - Higher-level programming ― JavaScript
-   By Guillaume, CTO at Holberton School
-   Ongoing project - started 05-04-2021, must end by 05-05-2021 (in about 11 hours) - you're done with  0% of tasks.
-   Checker was released at 05-04-2021 12:00 PM
-   QA review fully automated.

## Resources

**Read or watch**:

-   [Working with JSON data](https://intranet.hbtn.io/rltoken/RmDpb2gJfPrMar05QdxYvw "Working with JSON data")
-   [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.hbtn.io/rltoken/ibqGcS_YNbtWO8nPIlM2Ug "The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco")
-   [request module](https://intranet.hbtn.io/rltoken/9L4UYvlIwDVDoObD7zpJZQ "request module")
-   [Modern JS](https://intranet.hbtn.io/rltoken/Zf5LCjoTEuIXWWxoH_dGVQ "Modern JS")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/BoEglaE5YtXYeUQQyGL2cg "explain to anyone"),  **without the help of Google**:

### General

-   Why JavaScript programming is amazing
-   How to manipulate JSON data
-   How to use  `request`  and fetch API
-   How to read and write a file using  `fs`  module

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 14.04 LTS using  `node`  (version 10.14.x)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/node`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should be  `semistandard`  compliant.  [Rules of Standard](https://intranet.hbtn.io/rltoken/c82PxNOgt77URzBvKDVcqg "Rules of Standard")  +  [semicolons on top](https://intranet.hbtn.io/rltoken/GEBmmrmMUnGd20y4k6_4OA "semicolons on top"). Also as reference:  [AirBnB style](https://intranet.hbtn.io/rltoken/B5xrtt_3vxQFbcCpW5rVsw "AirBnB style")
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   You are not allowed to use  `var`

## More Info

### Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation](https://intranet.hbtn.io/rltoken/GEBmmrmMUnGd20y4k6_4OA "Documentation")

```
$ sudo npm install semistandard --global

```

### Install  `request`  module and use it

[Documentation](https://intranet.hbtn.io/rltoken/9L4UYvlIwDVDoObD7zpJZQ "Documentation")

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules

```

**Notes:**  Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).
## Author
 
 - **Juan Carlos Hernández** : Twitter - [@luigi_jong](https://twitter.com/luigi_jong)
 
##  info

 - Date 04/05/2021
 - Holberton school Colombia 
 - Cohort #13 BOG0920
