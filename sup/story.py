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
from typing import Callable, List, Any, Dict, Union, Iterable, Tuple
from inspect import ismethod
from .storyerror import StoryError

def _story_io(text: str = str(), **kwargs: Union[str, Iterable[str]]) -> str:
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
	if "error" in kwargs:
		print(kwargs["error"])
		return ''
	out = ""
	if "options" in kwargs:
		text = "Choose one:\n"+"\n".join([f"{x+1}) {i}" for x, i in enumerate(kwargs["options"])])
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
	reference: :class:`str`
		A String representing the reference of the story, it can be the path of the sus file that the
		story object will interpret and run or the story scrip directly.
	io: Callable[[:class:`str`, Union[:class:`str`, Iterable[:class:`str`]]], :class:`str`]
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
	reference: str, 
	io_function: Callable[[str, Union[str, Iterable[str]]], str]=_story_io):
		self.reference = reference + ".sus" if not reference.endswith('.sus') else reference
		self.io = io_function
		self.line = 0
		self.sub_story = str()
		self.function_dict = {
		"OPTION": self._option_function,
		"JUMP": self._jump_function,
		"STAY": self._stay_function,
		"TAG": self._stay_function,
		"STORY": self._story_function,
		"END": self._end_function,
		"SKIP": self._skip_function,
		"RETURN": self._return_function,
		"CHECKATTR": self._checkattr_function,
		"CHECKNOTATTR": self._checknotattr_function,
		"ADDATTR": self._addattr_function,
		"DELATTR": self._delattr_function
		}
		self.tags: Dict[str, Tuple[str, int]] = dict()
		self.attributes: List[str] = list()
		if len(self.reference.splitlines()) > 1:
			temp_text = self.reference
		else:
			with open(self.reference, "r", encoding='UTF-8') as sf:
				temp_text = sf.read()
		self.text: List[str] = list()
		temp_lines = str()
		for i in temp_text.splitlines():
			if i and not i.startswith("# "):
				if i.startswith("-") and "{{" in i:
					temp_lines = i.replace("{{", "")
					if "}}" in i:
						temp_lines = temp_lines.replace("}}", "")
						self.text.append(temp_lines.strip())
						temp_lines = str()
					continue
				if temp_lines:
					if "}}" in i:
						temp_lines += i.replace("}}", "")
						self.text.append(temp_lines.strip())
						temp_lines = str()
						continue
					temp_lines += i
					continue
				self.text.append(i.strip())
		if not self.text:
			raise StoryError("Story file is empty")
		if all(findall(r"\[STORY ([a-zA-Z-]+?)\]", i) == [] for i in self.text):
			raise StoryError("No Story sections found")
		self.sub_stories: Dict[str, List[str]] = dict()
		temp_list: List[str] = list()
		for x, i in enumerate(self.text):
			if sub_story := (findall(r"\[STORY ([a-zA-Z-]+?)\]", i)):
				if not self.sub_story:
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
				self.tags[tag] = (temp_list[0], len(temp_list)-1)
			temp_list.append(i)
			if x+1 == len(self.text):
				if len(temp_list) >= 2:
					if sub_story:
						if sub_story[0] in self.sub_stories:
							raise StoryError(f"Duplicate Sub-story: {sub_story}")
					self.sub_stories[temp_list[0]] = temp_list[1:]
				
	def _run_function(self, args: str) -> None:
		arg_list = args.split(" ", 1)
		if not arg_list[0] in self.function_dict:
			raise StoryError(f"Unknown function: {arg_list[0]}")
		func = self.function_dict[arg_list[0]]
		if func.__code__.co_argcount == 1:
			if ismethod(func):
				func()
			else:
				func(self)
		elif func.__code__.co_argcount == 2:
			if ismethod(func):
				func(arg_list[1])
			else:
				func(self, arg_list[1])
		else:
			raise StoryError("Invalid parameters for function: {arg_list[0]}")
					
	def _option_function(self, args: str) -> None:
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
			self._run_function(option_function)
			break
			
	def _jump_function(self, args: str) -> None:
		if args.strip() not in self.tags:
			raise StoryError(f"Tag {args.strip()} doesn't exist.")
		tag = self.tags[args.strip()]
		self.sub_story = tag[0]
		self.line = tag[1]
		
	def _stay_function(self) -> None:
		if self.line+1 >= len(self.sub_stories[self.sub_story]):
			sub_stories = list(self.sub_stories.keys())
			if story_index := (sub_stories.index(self.sub_story))+1 >= len(sub_stories):
				self._end_function()
			self.sub_story = sub_stories[story_index+1]
			self.line = 0
		else:
			self.line += 1
		
	def _story_function(self, args: str) -> None:
		if args.strip() not in self.sub_stories:
			raise StoryError(f"Sub-story {args.strip()} doesn't exist.")
		self.sub_story = args.strip()
		self.line = 0
		
	def _end_function(self) -> None:
		self.end()
		
	def _skip_function(self, args: str) -> None:
		if not args.strip().isdigit():
			raise StoryError(f"SKIP argument should be a number not {args.strip}")
		lines = int(args.strip())
		if lines <= 0:
			raise StoryError("Amount of lines to skip must be positive.")
		for _ in range(lines+1):
			self._stay_function()
			
	def _return_function(self, args: str) -> None:
		if not args.strip().isdigit():
			raise StoryError(F"RETURN argument should be a number not {args.strip}")
		lines = int(args.strip())
		if lines <= 0:
			raise StoryError("Amount of lines to return must be positive.")
		self.line = max(0, self.line-lines)
		
	def _checkattr_function(self, args: str) -> None:
		attr, function = args.split("$$", 1)
		if attr.strip() in self.attributes:
			self._run_function(function)
		
	def _checknotattr_function(self, args: str) -> None:
		attr, function = args.split("$$", 1)
		if not attr.strip() in self.attributes:
			self._run_function(function)
		
	def _addattr_function(self, args: str) -> None:
		if not args in self.attributes:
			self.attributes.append(args)
			
	def _delattr_function(self, args: str) -> None:
		if args in self.attributes:
			self.attributes.remove(args)
			
	def _run_line(self) -> None:
		curr_line = self.sub_stories[self.sub_story][self.line]
		if not any((curr_line.startswith((f"-{i}", f"- {i}"))) for i in self.function_dict):
			self.io(curr_line)
			self._stay_function()
		else:
				temp_line = self.line 
				if curr_line.startswith("- "):
					curr_line = "-" + curr_line[2:]
				self._run_function(curr_line[1:])
				if temp_line == self.line:
					self.line += 1
				
	def start(self) -> None:
		"""The method called to start the story / game of the corresponding :class:`Story` object

		"""
		while True:
				self._run_line()
				
	def end(self) -> None:
		"""The method called when the :class:`Story` object reaches an end by either hitting
		the end of the sus file or the END function being called.

		"""
		print("\n\n====================\nProgram ended, do you want to play again?")
		answer = input("> ")
		if answer.lower().strip() in ["yes", "y"]:
			self.line = 0
			self.sub_story = list(self.sub_stories.keys())[0]
			self.attributes = list()
		else:
			print("Alright, See you next time!")
			quit()

	def io_function(self, function: Callable[[str, Union[str, Iterable[str]]], str]) -> Callable[[str, Union[str, Iterable[str]]], str]:
		"""The method used to set the :class:`Story` Object's I/O function to the corresponding one.
		
		This method is meant to be used as a decorator.
		
		.. versionadded:: 0.1.1
		
		"""
		self.io = function
		return function

	def custom_function(self, name: str) -> Callable[..., Any]:
		"""The method used to add custom functions to the :class:`Story` Object to be handled like
		others sus functions.
		For more info check the SUP documentation.

		This method is meant to be used as a decorator.

		.. versionadded:: 0.1.6

		Parameters
		-----------
		name: :class:`str
			The string representing the name of the function.

		"""
		name = name.strip().upper()
		def inner(function: Callable[..., Any]) -> Callable[..., Any]:
			if name in self.function_dict:
				raise StoryError(f"Duplicate function: {name}")
			self.function_dict[name] = function
			return function
		return inner
