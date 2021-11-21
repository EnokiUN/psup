Story Utility Script (SUS)
==========================

Introduction
------------
SUS is a semi-programming language format used to make text based games and stories with lightweight syntax.

.. warning::
    While naming Sub-stories, Tags, Attributes and so on its good practice to not use spaces and use ``-`` instead as spaces are unreliable and sometimes unsupported.

    Also everything is case sensitive so be aware of that.

Components
----------
SUS has 4 main components:

* Sub-stories
* Tags
* Attributes
* Functions
  
These four components are the building foundation of any SUS file, they are simple concepts which work together to make complex stories and games.

Sub-stories
-----------
Sub-stories are a easy and convinient way to seperate your SUS file's components to smaller parts to be easier to work with.

They also act as anchor points to navigate while running the SUS file.

To make a Sub-Story simply type:

``[STORY sub-story-name]``

To jump to a story file use the ``STORY`` function.

.. warning::
    If you have a repeating Sub-story name the Interpreter will throw a StoryError at you so dont try it.

.. note:: 
    It's good practice to always start your SUS file with a Sub-story called ``main``

Tags
----
Tags are an easy way to navigate your SUS file as they act as Sub-story dependant anchors that you are able to jump to anywhere in the file using the ``JUMP`` function.

To create a tag type:

``-TAG <tag-name>``

Attributes
----------
Attributes are a way to make your stories and games (mainly) more intruiging and flexible.

Attributes can be used for alot of stuff ranging from checking if the player has been in a certain part of the story before to making game logic (someone even made `rock paper scissors <https://github.com/EnokiUN/sup/blob/main/atlas/rps.sus>`_).

Attributes have a variety of functions ranging from ``ADDATTR`` and ``DELATTR`` to ``CHECKATTR`` and ``CHECKANYATTR`` which are used to make stuff with them.

Functions
---------
Functions are the one undeniable most important building part of SUS.

They are what makes it more than printing stuff to the terminal.

There are a pletohra of functions which do different things from giving the player some options to ending the story.

They are also combined together to make the cogs of SUS.

Functions can be run dependantly in the SUS file using this syntax:

``-FUNCTION [args]``

For this the function must be at the start of the line.

Anything after it in the same line will be treated as it's arguments.

.. note::
    If you want a function's args to span multiple lines you can wrap them in curly braces, example:

    .. code-block:: sus

        -OPTION {{
                  Option 1 $$STAY,
                  Option 2 $$JUMP tag,
                  Option 3 $$STORY sub-story
                }}

The functions are:

TAG
^^^
The function used to create a `tag <#Tags>`_.

Syntax:

``TAG <tag-name>``

.. warning::
    If you have a repeating tag name the Interpreter will throw a StoryError at you.

JUMP
^^^^
The function used to jump to a `Sub-story <#Sub-stories>`_.

Syntax:

``JUMP <sub-story-name>``

SKIP
^^^^
The function used to skip some lines, be pure story lines or lines with functions.

Syntax:

``SKIP <number-of-lines>``

.. warning::
    If you try to pass a negative number or pass text instead the Interpreter will throw a StoryError at you.

.. note::
    If you skip to or past the end of the SUS file the story will end (the :meth:`Story.end` function will be called).

RETURN
^^^^^^
The function used to go back some lines, be pure story lines or lines with functions.

Syntax:

``RETURN <number-of-lines>``

.. warning::
    If you try to pass a negative number or pass text instead the Interpreter will throw a StoryError at you.

.. note::
    If you return to or past the start of the current Sub-story it will just stop at the first line in that Sub-story so use the ``JUMP`` method if you want to go back through Sub-stories.

OPTION
^^^^^^
The function used to provide the player with options and act on them using functions.

Syntax:

``OPTION *<choice>``

The syntax of a choice is ``<choice-text> $$<function>`` and are split using commas ``,``.

.. note::
    Duplicate choices are allowed.

    The layout that options are displayed in the default I/O function is:

    ``<function-number>) <function-text>``

    an example is:

    .. code-block:: sus

        1) Option one
        2) Option two
        3) Option three

STAY
^^^^
This function does nothing.

While it may seem useless at first you will soon realize that it's one of the most important functions esspecially if you're using it in combination with another function.

Syntax:

``STAY``

END
^^^
This function immediately ends the story when ran.

Syntax:

``END``

ADDATTR
^^^^^^^
This function is used to add `attributes <#Attributes>`_ to the player.

Syntax:

``ADDATTR *<attrs>``

.. note::
    If the player already has the attribute the function does nothing.

    Attributes can be split using ``&&``, ``,`` or just spaces.

DELATTR
^^^^^^^
This function is used to remove `attributes <#Attributes>`_ from the player.

Syntax:

``DELATTR *<attrs>``

.. note::
    If the player doesn't have the attribute the function does nothing.

    Attributes can be split using ``&&``, ``,`` or just spaces.

CHECKATTR
^^^^^^^^^
This option is used to check if the player has an `attribute <#Attributes>`_, if so it executes a function.

Syntax:

``CHECKATTR *<attrs> $$<function>``

.. note::
    The function is only executed if **all** the attributes are present with the player.

    Attributes can be split using ``&&``, ``,`` or just spaces.

    You can prefix the attribute with ``!!`` to check if that attribute doesn't exist instead.

CHECKANYATTR
^^^^^^^^^^^^
This option is used to check if the player has any `attribute <#Attributes>`_, if so it executes a function.

Syntax:

``CHECKANYATTR *<attrs> $$<function>``

.. note::
    The function is only executed if **any** attribute is present with the player.

    Attributes can be split using ``&&``, ``,`` or just spaces.

    You can prefix the attribute with ``!!`` to check if that attribute doesn't exist instead.

RANDOM
^^^^^^
This function is used to execute a function from a provided set at random.

Syntax:

``RANDOM *<functions>``

.. note::
    Functions can be split using ``&&``, ``,`` or just spaces.

SAY
^^^
A function used to straight up send something to the terminal.

Syntax:

``SAY <text>``

.. note::
    The arguments of this function are sent to the terminal regardless if they're functions or not.