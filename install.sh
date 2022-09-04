# need to ubuntu
sudo apt-get install libportaudio2
sudo apt-get install libasound-dev
#pyaudio error solved
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg libav-tools
sudo pip install pyaudio

python3 -m venv venv 
source venv/bin/activate

. ./env.sh


python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools
pip3 install -r requirements.txt