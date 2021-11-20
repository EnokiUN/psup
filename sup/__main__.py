from .story import Story
from .onlinestory import OnlineStory
from .storyerror import StoryError
from argparse import ArgumentParser


def main():
    # CLI handling
    parser = ArgumentParser(description='Runs a story directly from the terminal')
    parser.add_argument('Story', 'S', type=str, help='Name of the story')
    parser.add_argument('--online-story', dest='online', action='store_const', const=True, default=False,
                        help="(Optional) Tries to fetch the story from the github page")

    print(parser.parse_args())
    input()

if __name__ == '__main__':
    main()
    
    