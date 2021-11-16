#
# Electrochemical_ORR_procesing_autolab 
#
# email: www.gasparcarrascohuertas.com
#
tmppwd=$PWD
#Utils
echo "####################################################### "
echo "#INSTALLING UTILS# "
echo "####################################################### "
#wget
sudo apt install git -y
#update_and_upgrade
sudo apt-get update -y
sudo apt-get upgrade -y
#
#Python_modules
echo "####################################################### "
echo "#PYTHON MODULES# "
echo "####################################################### "
#Matplotlib
sudo pip install -U pip
sudo pip install -U matplotlib
#Numpy
sudo pip install numpy
#Pandas
sudo pip install pandas
#Glob
sudo pip install glob3
#shutil
sudo pip install pytest-shutil   
#Astropy
sudo pip install astropy
#update_and_upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

