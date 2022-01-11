"""
----
PSUP
----
The Python Story Utility Package Module.

PSUP helps making stories or games with options, diverging paths, different endings and so on.

You can run a story in a minimum of 2 lines of code / 1 terminal command.

.. code-block:: python3

    from psup import Story

    Story("YourStoryName").start()

``psup yourstoryname``

You can also run stories online without installing them or upload your own for others to play.
You can find / upload stories in the `GitHub repo's atlas folder <https://github.com/EnokiUN/psup>`_.

.. code-block:: python3

    from psup import OnlineStory

    OnlineStory("OnlineStoryName").start()

``psup onlinestoryname -online``

The module has its own file extention (.sus standing for Story Utility Script) where all the
other stuff including the story's script, options, endings, attributes and more are in a way
designed to be fast and simple with basic syntax that's easy to learn and use for even people
with little to no programming knowledge and skill allowing anyone to create their own stories.
"""

__title__ = "PSUP"
__author__ = "EnokiUN"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2021-present EnokiUN"
__version__ = "1.0.0-rc1"

from .errors import StoryError
from .onlinestory import OnlineStory
from .story import Story

__all__ = ["Story", "StoryError", "OnlineStory"]
