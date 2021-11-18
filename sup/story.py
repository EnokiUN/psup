"""MIT License

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

from re import findall
from sys import stdout
from time import sleep
from random import uniform
from typing import Callable, List

class StoryError(BaseException):
	"""The base Exception class for SUP.
	
	.. versionadded:: 0.1.1
	
	These exceptions are almost always present because of a syntax error
	present in your Story Utility Script (sus) file.

	"""
	def __str__(self):
		return f"{self.args[0]}, for more info check the the SUP docs."

def _story_io(text: str = None, options: List[str] = None, error: str = None) -> str:
	"""The default I/O (input and output) function for the :class:`Story` class
	
	.. versionadded:: 0.1.1
	
	Parameters
	-----------
	text: :class:`str`
		The story script and text to be sent to the desired location.
	options: List[:class:`str`]
		The options to be displayed for the user / player to choose one.
	error: :class:`str`
		The player /user action relatted error for handling small mistakes like wrong input.
		
	"""
	if error:
		print(error)
		return None
	out = ""
	if options:
		text = "Choose one:\n" + " | ".join(options)
		out = "\n> "
	for x in text:
		print(x, end='')
		stdout.flush()
		sleep(uniform(0, 0.01))
	return input(out)

class Story:
	"""The base class for interpreting sus files.
	
	..  versionadded:: 0.1.1
	
	Attributes
	-----------
	path: :class:`str`
		A String representing the path of the sus file that the story object will interpret and run.
	io: Callable[[:class:`str`], :class:`str`]
		A function that handles the input and output of data from the :class:`Story`
		object to the desired location.
	line: :class:`int`
		The Integer representing the current line number in the current Sub-story.
	sub_story: :class:`str`
		The Sting representing the current Sub-story.
	function_dict: Dict[:class:`str`, Callable[[Union[:class:`str`, None]], None]]
		The Dictionary that has the pairs of all function names and their corresponding python functions.
	tags: Dict[:class:`str`, Itterable[:class:`str`, :class:`int`]]
		The Dictionary containing all the tags and their corresponding Lists that contain the name of
		their Sub-story and the line they're in.
	attributes: List[:class:`str`]
		The List that contains all the Attributes the user / player has gained while using the
		:class:`Story` Object.
	text: List[:class:`str`]
		The List containing every line of text in the sus file that isn't a comment / empty line
		
	Example
	-----------
	Low-level use of the story class to make a terminal based story / game with all the
	features from a sus file.
	.. code-block:: python3
	
		from sup import Story
		Story("story").start()
		
	"""
	def __init__(self,
	story_path: str, 
	io_function: Callable[[str],str]=_story_io):
		self.path = story_path + ".sus" if not story_path.endswith('.sus') else story_path
		self.io = io_function
		self.line = 0
		self.sub_story = None
		self.function_dict = {
		"OPTION": self.__option_function__,
		"JUMP": self.__jump_function__,
		"STAY": self.__stay_function__,
		"TAG": self.__stay_function__,
		"STORY": self.__story_function__,
		"END": self.__end_function__,
		"SKIP": self.__skip_function__,
		"RETURN": self.__return_function__,
		"CHECKATTR": self.__checkattr_function__,
		"CHECKNOTATTR": self.__checknotattr_function__,
		"ADDATTR": self.__addattr_function__,
		"DELATTR": self.__delattr_function__
		}
		self.tags = dict()
		self.attributes = list()
		with open(self.path, "r", encoding='UTF-8') as sf:
			temp_text = sf.read()
		self.text = list()
		temp_lines = str()
		for i in temp_text.splitlines():
			if i and not i.startswith("# "):
			    if temp_lines:
			    	if "}}" in i:
			    		temp_lines += i.replace("}}", "")
			    		self.text.append(temp_lines.strip())
			    		temp_lines = str()
			    		continue
			    	temp_lines += i
			    	continue
			    if i.startswith("-") and "{{" in i:
			    	temp_lines = i.replace("{{", "")
			    	continue
			    self.text.append(i.strip())
		if self.text == []:
			raise StoryError("Story file is empty")
		if all(findall(r"\[STORY ([a-zA-Z-]+?)\]", i) == [] for i in self.text):
			raise StoryError("No Story sections found")
		self.sub_stories = dict()
		temp_list = list()
		for x, i in enumerate(self.text):
			if sub_story := (findall(r"\[STORY ([a-zA-Z-]+?)\]", i)):
				if self.sub_story is None:
					self.sub_story = sub_story[0]
				if len(temp_list) >= 2:
					if sub_story[0] in self.sub_stories:
						raise StoryError(f"Duplicate Sub-story: {sub_story}")
					self.sub_stories[temp_list[0]] = temp_list[1:]
				temp_list = [sub_story[0]]
				continue
			if i.startswith(("-TAG", "- TAG")):
				if i.startswith("- "):
					i = "-" + i[2:]
				tag = i.split(" ", 2)[1]
				if tag in self.tags:
					raise StoryError(f"Duplicate Tag: {tag}")
				self.tags[tag] = [temp_list[0], x]
			temp_list.append(i)
			if x+1 == len(self.text):
				if len(temp_list) >= 2:
					if sub_story:
						if sub_story[0] in self.sub_stories:
							raise StoryError(f"Duplicate Sub-story: {sub_story}")
					self.sub_stories[temp_list[0]] = temp_list[1:]
				
	def __run_function__(self, args: str) -> None:
		if len(args.split()) == 1:
			if not args in self.function_dict:
				raise StoryError(f"Unknown function: {args}")
			self.function_dict[args]()
		else:
			func, args = args.split(" ", 1)
			if not func in self.function_dict:
				raise StoryError(f"Unknown function: {func}")
			self.function_dict[func](args)
					
	def __option_function__(self, args: str) -> None:
		option_functions = [i[0].strip() for i in findall(r"\$\$(.+?)(,|$)", args)]
		for i in option_functions:
				if i.split()[0] not in self.function_dict:
					raise StoryError(f"Invalid function {i.split()[0]} in Option")
		option_titles = [i[1].strip() for i in findall(r"(,|^)(.+?)\$\$", args)]
		while True:
			option = self.io(options=option_titles).strip()
			if option.isdigit():
				if int(option)-1 > len(option_titles):
					self.io(error="Invalid option, try again")
					continue
				option_function = option_functions[int(option)-1]
			else:
				if not option in option_titles:
					self.io(error="Invalid option, try again")
					continue
				option_function = option_functions[option_titles.index(option)]
			self.__run_function__(option_function)
			break
			
	def __jump_function__(self, args: str) -> None:
		if args.strip() not in self.tags:
			raise StoryError(f"Tag {args.strip()} doesn't exist.")
		tag = self.tags[args.strip()]
		self.sub_story = tag[0]
		self.line = tag[1]
		
	def __stay_function__(self) -> None:
		if self.line+1 >= len(self.sub_stories[self.sub_story]):
			sub_stories = [i for i in self.sub_stories]
			if story_index := (sub_stories.index(self.sub_story))+1 >= len(sub_stories):
				self.__end_function__()
			self.sub_story = sub_stories[story_index+1]
			self.line = 0
		else:
			self.line += 1
		
	def __story_function__(self, args: str) -> None:
		if args.strip() not in self.sub_stories:
			raise StoryError(f"Sub-story {args.strip()} doesn't exist.")
		self.sub_story = args.strip()
		self.line = 0
		
	def __end_function__(self) -> None:
		quit()
		
	def __skip_function__(self, args: str) -> None:
		if not args.strip().isdigit():
			raise StoryError(f"SKIP argument should be a number not {args.strip}")
		lines = int(args.strip())
		if lines <= 0:
			raise StoryError("Amount of lines to skip must be positive.")
		for _ in range(lines):
			self.__stay_function__()
			
	def __return_function__(self, args: str) -> None:
		if not args.strip().isdigit():
			raise StoryError(F"RETURN argument should be a number not {args.strip}")
		lines = int(args.strip())
		if lines <= 0:
			raise StoryError("Amount of lines to return must be positive.")
		self.line = max(0, self.line-lines)
		
	def __checkattr_function__(self, args: str) -> None:
		attr, function = args.split("$$", 1)
		if attr.strip() in self.attributes:
			self.__run_function__(function)
		
	def __checknotattr_function__(self, args: str) -> None:
		attr, function = args.split("$$", 1)
		if not attr.strip() in self.attributes:
			self.__run_function__(function)
		
	def __addattr_function__(self, args: str) -> None:
		if not args in self.attributes:
			self.attributes.append(args)
			
	def __delattr_function__(self, args: str) -> None:
		if args in self.attributes:
			self.attributes.remove(args)
			
	def __run_line__(self) -> None:
		curr_line = self.sub_stories[self.sub_story][self.line]
		if not any((curr_line.startswith((f"-{i}", f"- {i}"))) for i in self.function_dict):
			self.io(curr_line)
			self.__stay_function__()
		else:
				temp_line = self.line 
				if curr_line.startswith("- "):
					curr_line = "-" + curr_line[2:]
				self.__run_function__(curr_line[1:])
				if temp_line == self.line:
					self.line += 1
				
	def start(self) -> None:
		"""The method to start the story / game of the corresponding :class:`Story` class
		"""
		while True:
				self.__run_line__()
				
	def io_function(self, func: Callable[[str], None]) -> None:
		"""The method used to set the :class:`Story` Object's I/O function to the corresponding one.
		
		This method is meant to be used as a decorator.
		
		.. versionadded:: 0.1.1
		
		"""
		self.io = func
