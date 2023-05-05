FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel

# Install vim
RUN apt update -y;
RUN apt-get install vim -y;

# Install Git
## DEBIAN_FRONTEND=noninteractive answers all
## questions asked during install without user input.
RUN DEBIAN_FRONTEND=noninteractive apt install -y git-all
## Not ideal but since we are root here and not your
## normal user, we have to give git permission to
## allow a non-normal user (root) to do git commands
RUN git config --global --add safe.directory /CU_Project_Template

# Working directory
WORKDIR /CU_Project_Template

# Install requirements.txt
## You could do this everytime you start the container as you will mount in 
## the directory that has requirements. However that might get annoying to do
## every single time you do docker run -it ...
COPY ./requirements.txt /CU_Project_Template
RUN pip install -r /CU_Project_Template/requirements.txt
## You can always add something retroactively and just reinstall requirements.txt

CMD ["bash"]