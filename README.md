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
 5. Run genvish.py (Found on this GitHub site)
```bash
python genvish.py -n <Audio Folder Name> -i <Input Text File>
```

