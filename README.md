# CU_Project_Template
A template for using the CU environments and tracking generated data

# Infrastructure
This is always changing but ultimately the plan is to back data up on the CU Ophthalmology Isilon. That will have this structure:

/Some_Parent_Lab_Folder
  /data
    /public
	/private
  /projects
    /<git repo>
	/<git repo>
	/<git repo>
	...

Right now we have these machines:
  * linux-tower1 (public only)
  * linux-tower2 (public only)
  * gpu-server (public and private PHI data)

Until further notice linux-tower1 will be the main source but on machines we will likely need to partition data and projects as all data won't fit on one server. That is where the isilon above comes in but we need to wait for that and or the RAID (more details on that later, but it's a mountable data source that mimics the isilon).

* People should work in their home directories and clone git code there.
* A corresponding folder with the same exact name should be under /projects
* Any folders under /projects/<git repo> should have a manually made README with 3 things:
  - Github repo link
  - Commit hash that made this data
  - .env used with code that stores /data source and any other config

Ex: Organization with this very repo:
```bash
/data
  /...data used
/projects
  /CU_Project_Template
    /sample_analysis
/home/bearceb/CU_Project_Template
```

# Virtualenv based project
Frankly unless absolutely necessary using virtualenvs is better than using docker containers. It allows us to use proper permissions so we don't delete things. I highly HIGHLY recommend this and will demo this first for that reason.

Setup (use any other virtualenv technology you like for use with requirements.txt):
```bash
mkdir ~/.virtualenvs
python3 -m venv ~/.virtualenvs/venv3.10.6
# ls ~/.virtualenvs # to see it
. ~/.virtualenvs/venv3.10.6 # activate it for your project
```

You should be here:
```bash
(venv3.10.6) bearceb@OPH-D-JJ526S3:~/CU_Project_Template$
```

# Docker based project