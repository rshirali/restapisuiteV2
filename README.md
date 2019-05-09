# Project Name
* Software Engineer in Test
* Coding Challenge Version 0.0.1

## General info
Build an automated “test suite” for the VIPER Video Comments API. 
Requirements and implementation for this API linked below …
## Technologies
* Python 3.6
* Docker
* Pytest
*pylint

## Setup and test suite execution
* Describe how to install / setup your local environement
* Perform Git clone/pull on the branch.
* All the files/folders should appears in /viper-assignment
* Keep in mind the docker build might take few minutes
* to complete.
* cd //viper-assignment
* At the prompt enter:
*	docker build  -t myapp:v0.1 .
*	docker run -it myapp:v0.1 /bin/bash
## For storing the results in a .txt file
* docker run -it myapp:v0.1 /bin/bash > filename.txt

Expected:
* Pytest shall run all the test cases at the entrypoint
* from the dockerfile.

## Features
List of features ready and TODOs for future development

To-do list:
TODO/Observations/Notes:
1]Perform an exhaustive validation on the collection
returned.
	1] def test_get_comments_categories():
	2] def test_get_comments_catgs_byid():

2] def test_post_comm_categs_count_limit():
Test data challenge. There's no easy way
to load/insert 100 categories with unique id/names
using the endpoint. It might be possible with some 
form of a data loader from the backend. I shall
continue to work on this one till the last day.

3] Add a logging feature to log the test execution results

4] Exhaustive validation of combination of optional/mandatory
	fields as defined in the schema.

5] Refactor the test suite.
	a] Reduce code repeat in some of the modules
	b] I am thinking of encapsulating the service layer
	   in a class, and using the methods in the test module.
	   I shall perform another push on the last day of the
	   assignment.
## Notes
This entry each module allows for unit testing the module 
# For Unit testing this module
if __name__ == "__main__":
    test_get_comments_catgs_byid()

## Status
Project is: _in progress_. See TODO list above.
Defects Observed: 
1] def test_post_comm_categ_nm_unique():
	* Uniqness not enforced
2] test_get_comments_posts_arch_datefilter_yyyy():
	* yyyy > 1992 requirement not enforced
3] def test_post_comm_posts_bodylimit():
	* Body should not exceed 1000 characters not enforced
4] def test_post_comm_posts_pubdatevalid():
	* Service/endpoint allowing dates other than today's date
5] def test_post_comm_posts_titlelimit():
	Title does not exceed 100 characters not enforced

## Inspiration
Project inspired by John and his team from the Viper Group

## Contact
Created by [rajeevshirali@gmail.com] - feel free to contact me!
