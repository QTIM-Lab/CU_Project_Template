FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel

# Install vim
RUN apt update -y;
RUN apt-get install vim -y;

# Install Git
## DEBIAN_FRONTEND=noninteractive answers all
## questions asked during install without user input.
RUN DEBIAN_FRONTEND=noninteractive apt install -y git-all

# Install requirements.txt
## You could do this everytime you start the container as you will mount in 
## the directory that has requirements. However that might get annoying to do
## every single time you do docker run -it ...
COPY ./requirements.txt /
RUN pip install -r /requirements.txt
## You can always add something retroactively and just reinstall requirements.txt
## Lastly this requirments.txt is in a different spot than the one in your project.
## It gets copied to / whereas the other copy is in:
## -v $PWD:/CU_Project_Template

CMD ["bash"]