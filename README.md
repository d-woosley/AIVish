# AIVish
Voice Cloning with AI for Vishing

# Setup
 1. Create new instance in AWS
  - AMI: Deep Learning Proprietary Nvidia Driver AMI GPU PyTorch 2.0.1 (Ubuntu 20.04) 20240116
  - Instance: G4dn.xlarge (Cheapest NVIDIA GPU on AWS)
 2. SSH to new instance
 3. Setup Conda (Maybe unneeded?)
```bash
conda init
*exit and rejoin ssh session to reload shell*
```
 4. Install TorToiSe and Torch Audio
```bash
pip install tortoise-tts
pip install torchaudio
```
 5. Create new folder (name what you will put as the name in genvish.py) in TorToiSe install location, add recording to location

> **NOTE**: By default, the TorToiSe install location is `/opt/conda/lib/python3.10/site-packages/tortoise/voices/` when installed with conda like the instructions above. If this is the case, you can just create a folder inside that directory and add your audio files to the folder.
  
 5. Run genvish.py (Found on this GitHub site)
```bash
python genvish.py -n <Audio Folder Name> -i <Input Text File>
```
> **NOTE**: as it stands right now you will need to create a folder named the same thing as your Audio folder in the local directory
