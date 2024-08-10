import argparse
from typing import Sequence
from processor.process_things import process_preoccupation

def str_to_bool(input: str) -> bool:
    """Convert a string to a boolean value."""
    if input.lower() in ('yes', 'y', 'true', 't', '1'):
        return True
    elif input.lower() in ('no', 'n', 'false', 'f', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Sorry, boolean value expected.')

def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="""
            All things must pass. This too, shall be over soon.
        """
    )
    parser.add_argument(
        "-p",
        "--preoccupation",
        type=str,
        action="store",
        help="""
            Whatever's on your mind. You are here, so clearly there are some things.
        """,
    )
    interactive_mode = parser.add_mutually_exclusive_group()
    interactive_mode.add_argument(
        "-n",
        "--nothing-specific",
        action="store_true",
        help="""
            Use this flag when you don't want to, or cannot verbalize what's specifically bothering you.
            Or when you just want to remind yourself to remain stoic. 
        """,
    )

    parser.add_argument(
        "-a",
        "--add-more-preoccupations",
        type=bool,
        default=True,
        help="Add more preoccupations (y/n). Default is yes if not specified.",
    )

    args = parser.parse_args()
    print('works')
    if not args.preoccupation and not args.nothing_specific:
        while args.add_more_preoccupations:
            args.preoccupations = input(
                "What's on your mind? I will process it for you. "
            )
            args.add_more_preoccupations = str_to_bool(input("Anything else? You can tell me. (y/n)"))
