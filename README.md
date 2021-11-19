# SUP
The git for the Python Story Utility Package library. 

## Installation:
Install SUP by simply running **`pip install psup`** in your terminal.

Check out our [pypi page](https://pypi.org/project/psup/)!!

## Requirements:
[Python 3.8+](https://www.python.org/downloads/)

## Usage:
Here's a basic story:

```py
from sup import Story

story = Story("story")
story.run()
```

That's all the code you have to type to make a terminal based text story / game.
As for the actual story script, options paths and more that's all handled automatically from what you've written in your Story Utility Script (sus) file.

An example of a story
```
[STORY main]
Once upon a time a boy named Jack was strolling by the river.
Suddenly he heard something move in the bushes.
Jack was scared as he had no idea what the thing in the bushes could be.
- OPTION {{
	 Run away $$JUMP running-away,
	 Go towards the Bush $$STAY,
	 Do nothing $$SKIP 5
	 }}
As Jack slowly moved towards the Bush the sound became louder.
The Bush started shaking violently, Leaves scattered everywhere.
Jack grabs a stick from the ground to defend himself.
- ADDATTR stick
Suddenly, a giant boar emerged from the Bush.
The Boar started shouting, nearby birds started flying away and animals slowly emptied the area.
Even the fish in the river had become restless.
Upon hearing the Boar's shout Jack fell on his feet and started trembling.
The boar approached Jack.
- OPTION {{
	 Attack the Boar $$CHECKATTR stick $$JUMP fight,
	 Jump in the river $$STORY the-river
	 }}
Jack tried to attack the Boar with his fists but alas, it was useless.
The boar slowly approached Jack, it's shouts becoming louder and louder.
Jack started to shed tears of fear. 
The Boar rushed at Jack.....
...
It took the meat from Jack's bag and then left him alone.
Jack returned to his house while still trembling in fear.
- END
- TAG fight
Jack immediately started swinging his stick around, trying to get the Boar to run away.
The Boar was un-phased by Jack's attacks and started running towards him, now angrier than before.
The Boar attacked Jack...
Luckily a man with an axe appeared in the last moment and struck the Boar.
Jack saw the man and ran away to his house.
- END

[STORY running-away]
Jack ran away from the Bush.
As he ran away he bumped into a man with an axe.
- TAG hunter
That man was a hunter, he was looking for a Giant Boar that had escaped from him.
The hunter told Jack to stay safe and what the route out of the forest was.
Jack returned home safely. 
- END

[STORY the-river]
Jack jumped into the river.
The river swept Jack away.
Jack started to slowly drown but a man helped him get out of the river safely.
- JUMP hunter
```
*more examples can be found in the [atlas folder](https://github.com/EnokiUN/sup/blob/main/atlas/).*

This might look like a bit too much to understand at once but I'll break it bit by bit.

## The Syntax:
So there are a set of functions you can use in a sus file, being:
- `TAG` Creates a tag at the line that it's on.
- `JUMP` Jumps to a tag ignoring which sub-story it exists in.
- `SKIP` Skips a provided amount of lines.
- `RETURN` Goes back a provided amount of lines.
- `OPTION` Makes options, each option has some text and the function ran when that option is selected separated by `$$`.
- `STAY` Does nothing, used with other functions to do nothing.
- `END` Ends the whole story.
- `ADDATTR` Adds an attribute to the player.
- `DELATTR` Deleted an attribute from the player.
- `CHECKATTR` Checks if the played has an attribute, if so it runs the function supplied by `$$`.
- `CHECKNOTATTR` does the opposite of `CHECKATTR`.

You can also specify sub stories by typing `[STORY sub-story-name]`.
lines that are empty or start with `# ` are regarded as comments and are treated as if they don't exist.
