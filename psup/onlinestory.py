"""
MIT License

Copyright (c) 2021-present EnokiUN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from urllib.request import urlopen

from .errors import StoryError
from .story import Story


class OnlineStory(Story):
    """The class to play stories from the ones existing in the GitHub repository.

    To get your own story added make a pull request with it to the atlas folder.
    It will get reviewed and pulled if is passes the review.

    This class inherits from :class:`.Story` and hence shares all the methods and attributes.
    The only difference is the reference is the file's name from the GitHub repo.
    """

    def _get_text(self) -> str:
        text = (
            urlopen(
                f"https://raw.github.com/EnokiUN/psup/master/atlas/{self.reference}"
            )
            .read()
            .decode("UTF-8")
        )
        if len(text.splitlines()) <= 2:
            raise StoryError(f"Story not found: {self.reference}")
        return text
