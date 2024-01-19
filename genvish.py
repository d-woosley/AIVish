from argparse import ArgumentParser, FileType
import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices
from tortoise.utils.text import split_and_recombine_text
from time import time
import os

def main():
    # Parse the given flags
    args = load_args()

    # Define output location
    output_folder = os.path.join(args.NAME)
    output_file = os.path.join(output_folder, args.OUTPUT)

    # This will download all the models used by Tortoise from the HuggingFace hub.
    tts = TextToSpeech()

    # Generate random input seed?... I think
    seed = int(time())

    # Load voice samples
    voice_samples, conditioning_latents = load_voice(args.NAME)

    # Split text into smaller parts by "."
    speaker_text = args.TEXTFILE.read()
    if "." in speaker_text:
        speaker_text_split = speaker_text.split('.')
    else:
        speaker_text_split = speaker_text

    # Enum over split text and generate voice
    audio_clips = []
    for clip_name, text_part in enumerate(speaker_text_split):
        gen = tts.tts_with_preset(text_part, voice_samples=voice_samples, conditioning_latents=conditioning_latents,preset=args.QUALITY, k=1, use_deterministic_seed=seed)
        gen = gen.squeeze(0).cpu()
        torchaudio.save(os.path.join(output_folder, f'{clip_name}.wav'), gen, 24000)
        audio_clips.append(gen)

    # Combine all parts into single clip
    full_audio = torch.cat(audio_clips, dim=-1)
    torchaudio.save(output_file, full_audio, 24000)
    print(" [+] Complete! The output file can be found at: {}".format(output_file))
    

def load_args():
    # Parse out the given flags
    parser = ArgumentParser(
        description="Generate a text for a cloned voice",
        epilog="by: Duncan Woosley",
    )

    # Add Global Flag
    parser.add_argument(
        "-n", "--name",
        dest="NAME",
        help='The name of the folder that contains the audio samples (".wav") of the voice to clone. Place mutiple files in the /tortoise/voices/<name> folder (minimum=2. ideal=5)',
        type=str,
        required=True
    )
    parser.add_argument(
        "-i", "--pretext-file",
        dest="TEXTFILE",
        help="The text file of sentences that the cloned voice will say",
        required=True,
        type=FileType("r", encoding="UTF-8")
    )
    parser.add_argument(
        "-q",
        dest="QUALITY",
        help="The quality level of the output: ultra_fast, fast, standard, high_quality (Default)",
        type=str,
        choices=['ultra_fast','fast','standard','high_quality'],
        default="high_quality"
    )
    parser.add_argument(
        "-o", "--output",
        dest="OUTPUT",
        help='The output file name of the cloned voice audio file (Default="voice_clone.wav")',
        default="voice_clone.wav",
        type=str
    )

    # Parse Arguments given in command
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:  # Catch Ctrl+C
        print("\n\n [!] Keyboard Interrupted! (Ctrl+C Pressed). Shutting down...")
        exit()
