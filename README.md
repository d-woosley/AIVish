# AIVish
Generate voice cloned audio recording using tortoise-tts for security awareness testing.

# Disclaimer
This project is not complete and the below notes and script in this project are just a proof-of-concept. I do intend to clean it up down the road but please submit pull requests and issues for suggested improvements.

> **NOTE**: As with any pentesting tool, this should only be used only with proper authorization during security awareness training.

# Setup
 1. Create new instance in AWS
  - AMI: Deep Learning Proprietary Nvidia Driver AMI GPU PyTorch 2.0.1 (Ubuntu 20.04) 20240116 _(Under Community AMIs)_
  - Instance: G4dn.xlarge (_Cheapest NVIDIA GPU on AWS_)
 2. SSH to new instance
```bash
ssh -i <KEY> ubuntu@<PUBLIC_IP>
```
 3. Setup Conda
```bash
conda init
*exit and rejoin ssh session to reload shell*
```

> **NOTE**: Conda may be unneeded but I'm not 100% sure. I need to test again without it to confirm.

 4. Install TorToiSe and Torch Audio
```bash
pip install tortoise-tts
pip install torchaudio
```
 5. Create new folder (name what you will put as the name in genvish.py) in TorToiSe install location, add recording to location

> **NOTE**: By default, the TorToiSe install location is `/opt/conda/lib/python3.10/site-packages/tortoise/voices/` when installed with conda like the instructions above. If this is the case, you can just create a folder inside that directory and add your audio files to the folder.
  
 5. Run genvish.py (Found on this GitHub site)

You will need to create a basic text file in tell the TTS what text to generate. I would suggest only doing one sentence at a time as anything more can take a very long time to generate! If needed, you can merge multiple clips together afterwards in Audacity.

```bash
python genvish.py -n <Audio Folder Name> -i <Input Text File>
```
> **NOTE**: as it stands right now you will need to create a folder named the same thing as your Audio folder in the local directory

> **NOTE**: Input audio should be in WAV format and you should have 3-5 clips of about 10 seconds in length. (Audio files capture in Audacity in the past)


## Example:
```bash
scp -i <SSH_KEY> jdoe.zip ubuntu@<IP>:/opt/conda/lib/python3.10/site-packages/tortoise/voices/
ssh -i <SSH_KEY> ubuntu@<IP>
cd /opt/conda/lib/python3.10/site-packages/tortoise/voices/
mkdir jdoe
unzip jdoe.zip
mv *.wav ./jdoe
rm jdoe.zip
cd ~
vim clonetext.txt
mkdir jdoe
python genvish.py -n jdoe -i clonetext.txt
exit
scp -i <SSH_KEY> ubuntu@<IP>:/home/ubuntu/jdoe/voice_clone.wav
```
