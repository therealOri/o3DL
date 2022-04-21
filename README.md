# o3DL
YouTube video downloader.


# About
You can use o3DL to download youtube videos and to extract audio from video files.

![image](https://user-images.githubusercontent.com/45724082/164530024-8dcfe32b-c47b-4441-a3ca-2897b040edbe.png)

<br />
<br />

# Installation
```zsh
git clone https://github.com/therealOri/o3DL.git
cd o3DL
virtualenv o3ENV
source o3ENV/bin/activate
pip install -r requirements.txt
```
<br />
<br />

# WARNING!!! 
After installing pytube, you will need to use the patched `cypher.py` file provided here for pytube to work propperly. (untill they get it to work on their end). Check out the [Pytube Patch](https://github.com/therealOri/o3DL/discussions/2) discussions page for more info on how to do this.
