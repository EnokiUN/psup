"""The Story Utility Package (SUP for short) Module.

SUP makes making text based stories or games with options, diverging paths, different endings
and more take you a minimum of 3 lines of code.

All the other stuff including the story's script, options, endings, attributes and more is
handled in a Story Utility Script (sus for short) file in a way designed to be fast and simple.

"""

__title__ = 'SUP'
__author__ = 'EnokiUN'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2021-present EnokiUN'
__version__ = '0.1.1.8a'

__all__ = ["Story", "StoryError"]

from .story import Story
from .storyerror import StoryError
