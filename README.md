# AIVish
Generate voice cloned audio recordings using tortoise-tts for security awareness testing.

# Disclaimer
As with any pentesting tool, this should only be used only with proper authorization during security awareness training (vishing). There are a number of checks to prevent abusive use of the tool for anything related to extortion, threats, slurs and foul language, and anything sexual or content related to war and terrorism.

# Installation
You can run this tool on any system, however, it's designed to work with NVIDIA GPUs and you may loose quality if your not on a system with a NVIDIA GPU. In the most extreme case, I have gotten AIVish to run on a small Kali VM running on a laptop. Note that AIVish is **VERY** resource intensive and also requires about takes \~20 gigs of storage. If you don't have any system that can handle that, you can spin up a G4dn.xlarge (_Cheapest NVIDIA GPU on AWS_) to run this tool. I have tested this tool on a G4dn.xlarge (~$0.50 an hour) running the `Deep Learning Proprietary Nvidia Driver AMI GPU PyTorch` community AMIs and it works well!

```bash
pip install git+https://github.com/d-woosley/AIVish
```

# Run
You will need a zip file containing 3-5 audio clips (around 10 seconds each) of the voice you want to clone (.wav format).

> **NOTE**: I've used [Audacity](https://www.audacityteam.org/) to get these clips from YouTube in the past. 

```bash

     e      888 Y88b      / ,e,        888
    d8b     888  Y88b    /   "   d88~\ 888-~88e
   /Y88b    888   Y88b  /   888 C888   888  888
  /  Y88b   888    Y888/    888  Y88b  888  888
 /____Y88b  888     Y8/     888   888D 888  888
/      Y88b 888      Y      888 \_88P  888  888

usage: aivish [-h] -d <DIRECOTRY> [-i <FILE>] [-q {ultra_fast,fast,standard,high_quality}] [-o <FILE_NAME>] [-v]

Generate voice cloned audio recordings using tortoise-tts for security awareness testing

options:
  -h, --help            show this help message and exit
  -d <DIRECOTRY>, --dir <DIRECOTRY>
                        The path to the directory that contains the audio samples (".wav") of the voice to clone.
                        (minimum=3, ideal=5 clips of 10 seconds)
  -i <FILE>, --pretext-file <FILE>
                        The text to be generated into speech using given voice (If not given, you will be prompted)
  -q {ultra_fast,fast,standard,high_quality}
                        The quality level of the output: ultra_fast, fast, standard, high_quality (Default: high_quality)
  -o <FILE_NAME>, --output <FILE_NAME>
                        The output file name of the cloned voice audio file (Default="voice_clone.wav")
  -v, --verbose         Make the screen output verbose (show progress bars when generating clips)

by: Duncan Woosley (github.com/d-woosley)
```


**Quick Run**
```bash
aivish -d audio_files -i prompt.txt
```

> **NOTE**: If no text file is provided using the `-i` flag, you will be prompted on the screen for input

**Run with Lower Quality**
```bash
aivish -d audio_files -q fast
```

**Define Output File Name**
```bash
aivish -d audio_files -o jdoe_missedcall.wav
```

# Example Run
```bash
~/AIVish/tests$ aivish -d jdoe_clips -i pretext.txt -q ultra_fast

     e      888 Y88b      / ,e,        888
    d8b     888  Y88b    /   "   d88~\ 888-~88e
   /Y88b    888   Y88b  /   888 C888   888  888
  /  Y88b   888    Y888/    888  Y88b  888  888
 /____Y88b  888     Y8/     888   888D 888  888
/      Y88b 888      Y      888 \_88P  888  888


  [-] Downloading models used by Tortoise from HuggingFace. This could take a minute on the first run...

  [-] Loading voice from /home/ubuntu/AIVish/tests/jdoe_clips

  [-] Generating 3 sentences

    [+] Sentence 1 generated in 28.46 seconds. (Estimated Completion Time: 21.34 seconds)
    [+] Sentence 2 generated in 16.24 seconds. (Estimated Completion Time: 12.19 seconds)
    [+] Sentence 3 generated in 13.98 seconds. Done!

 [+] Complete! voice_clone.wav created!
```

# Someday-Maybe Additions:
 - Web interface to upload, generate, and download voice clips via the local network
 - Integrate RVC for live voice cloning
 - Integrate with PBX to fully handle calls as web softphone
 - Separate controller host from worker hosts and allow for dynamically spinning up instances in the cloud for compute
