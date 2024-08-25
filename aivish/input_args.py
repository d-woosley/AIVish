from argparse import ArgumentParser, FileType
from os import path
from sys import exit as sys_exit


def load_args():
    # Parse out the given flags
    parser = ArgumentParser(
        description="Generate voice cloned audio recordings using tortoise-tts for security awareness testing",
        epilog="by: Duncan Woosley (github.com/d-woosley)",
    )

    # Add Global Flag
    parser.add_argument(
        "-d", "--dir",
        dest="input_dir",
        metavar="<DIRECOTRY>",
        help='The path to the directory that contains the audio samples (".wav") of the voice to clone (minimum=3, ideal=5 clips of 10 seconds).',
        type=dir_path,
        required=True
    )
    parser.add_argument(
        "-i", "--pretext-file",
        dest="pretext_file",
        metavar="<FILE>",
        help="The text to be generated into speech using given voice (If not given, you will be prompted)",
        type=str,
        required=False
    )
    parser.add_argument(
        "-q",
        dest="quality_level",
        help="The quality level of the output: ultra_fast, fast, standard, high_quality (Default: high_quality)",
        type=str,
        choices=['ultra_fast','fast','standard','high_quality'],
        default="high_quality",
        required=False
    )
    parser.add_argument(
        "-o", "--output",
        dest="output_file",
        metavar="<FILE_NAME>",
        help='The output file name of the cloned voice audio file (Default="voice_clone.wav")',
        type=str,
        default="voice_clone.wav",
        required=False
    )
    parser.add_argument(
        "-v", "--verbose",
        dest="verbose",
        help='Make the screen output verbose (show progress bars when generating clips)',
        default=False,
        action="store_true",
        required=False
    )

    # Parse Arguments given in command
    args = parser.parse_args()

    return args


def dir_path(string):
    if path.isdir(string):
        return path.abspath(string)
    else:
        print(f"\n  [!] {string} is not a valid directory\n")
        sys_exit(1)