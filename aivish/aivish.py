import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning, module="tortoise.utils.audio")
from transformers import logging as transformers_logging
transformers_logging.set_verbosity_error()

from torch import cat as torch_cat
from torchaudio import save as torchaudio_save
from tortoise.utils.audio import load_voice
from tortoise.api import TextToSpeech
from time import time
from os import path

from aivish.abuse import check_string


class AIVish():
    def __init__(self):
        self.voices_path = str
        self.clips = []
        self.seed = int(time())

        # Download all the models used by Tortoise from the HuggingFace hub
        print("\n  [-] Downloading models used by Tortoise from HuggingFace. This could take a minute on the first run...")
        self.tts = TextToSpeech()
    
    def split_text(self, tts_text: str) -> list:
        """ Split text into sentences """
        split_text = []
        if "." in tts_text:
            split_text = tts_text.split('.')
        else:
            split_text.append(tts_text)

        # Clean list
        split_text = self.__striped_list(split_text)
        split_text = self.__uniq_list(split_text)
        split_text = [check_string(string) for string in split_text]
        
        return split_text
    
    def generate_clip(self, pretext: str, dir_path: str, quality_level: str, verbose: bool):
        dir_name = path.basename(dir_path)
        parent_dir_path = path.dirname(dir_path) + path.sep

        voice_samples, conditioning_latents = load_voice(dir_name, extra_voice_dirs=[parent_dir_path])

        gen = self.tts.tts_with_preset(
            pretext,
            verbose=verbose,
            voice_samples=voice_samples, 
            conditioning_latents=conditioning_latents,
            preset=quality_level, 
            k=1, 
            use_deterministic_seed=self.seed
        ).squeeze(0).cpu()

        self.clips.append(gen)

    def export_clip(self, output_file: str):
        """ Combine all single sentence clips into one large clip and export """
        full_audio = torch_cat(self.clips, dim=-1)
        torchaudio_save(output_file, full_audio, 24000)

    # Internal Methods ========================================================

    @staticmethod
    def __uniq_list(input_list: list) -> list:
        return [item for item in input_list if item]
    
    @staticmethod
    def __striped_list(input_list: list) -> list:
        return [item.rstrip('\n').strip() for item in input_list]