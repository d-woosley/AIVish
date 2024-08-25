from sys import exit as sys_exit
from time import time

from aivish.keyexcept_decorator import keyboard_interrupt_handler
from aivish.input_args import load_args
from aivish.aivish import AIVish
from aivish.logo import ascii_logo


@keyboard_interrupt_handler
def main():
    ascii_logo()
    args = load_args()
    session = AIVish()

    print(f"\n  [-] Loading voice from {args.input_dir}")
    if args.pretext_file:
        with open(args.pretext_file, 'r') as pretext_file:
            split_pretext = session.split_text(pretext_file.read())
    else:
        pretext = input("\n  [-] Type the text you want to generate: ")
        split_pretext = session.split_text(pretext)

    split_pretext_len = len(split_pretext)
    if split_pretext_len > 1:
        print(f"\n  [-] Generating {split_pretext_len} sentences\n")
    else:
        print(f"\n  [-] Generating {split_pretext_len} sentence\n")

    counter = 0
    completed_words = 0
    total_runtime = float(0)
    word_count = sum(len(string.split(" ")) for string in split_pretext)
    for partial_text in split_pretext:
        counter += 1

        # Generate clip and count time delta
        start_time = time()
        session.generate_clip(partial_text, args.input_dir, args.quality_level, args.verbose)
        end_time = time()
        completed_words += len(partial_text.split(" "))
        elapsed_time = end_time - start_time
        total_runtime += elapsed_time
        est_time = (total_runtime / completed_words) * (word_count - completed_words)

        if args.verbose:
            print()  # Pad status bars
        if counter == len(split_pretext):
            print(f"    [+] Sentence {counter} generated in {elapsed_time:.2f} seconds. Done!")
        else:
            print(f"    [+] Sentence {counter} generated in {elapsed_time:.2f} seconds. (Estimated Completion Time: {est_time:.2f} seconds)")
        if args.verbose:
            print()  # Pad status bars

    session.export_clip(args.output_file)

    if not args.verbose:
        print()  # Pad complete message when verbose is not used

    print(f" [+] Complete! {args.output_file} created!")
    sys_exit(0)


if __name__ == "__main__":
    main()