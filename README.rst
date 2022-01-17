.. image:: https://raw.githubusercontent.com/EnokiUN/psup/main/assets/logo.png
    :width: 200
    :alt: logo

----------------------------------------------
PSUP, The Python Story Utility Package Module.
----------------------------------------------
.. image:: https://discord.com/api/guilds/843825546719002645/embed.png
   :target: https://discord.gg/XFrExEJMsK
   :alt: Discord server invite

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

The module has its own file extension (.sus standing for Story Utility Script) where all the
other stuff including the story's script, options, endings, attributes and more are in a way
designed to be fast and simple with basic syntax that's easy to learn and use for even people
with little to no programming knowledge and skill allowing anyone to create their own stories.

Documentation
=============
There is a readthedocs.io documentation which covers all this but with better and greater detail available `here <https://psup.readthedocs.io/en/latest/index.html>`_, feel free to check it out.

Installation:
=============
Install PSUP by simply running ``pip install psup`` in your terminal.

Check out our `pypi page <https://pypi.org/project/psup/>`_!!

Requirements:
=============
`Python 3.8+ <https://www.python.org/downloads/>`_
and that's it!

Usage:
======
Here's a basic story:

.. code-block:: sus

    [STORY main]
    Once upon a time a boy named Jack was strolling by the river.
    Suddenly he heard something move in the bushes.
    Jack was scared as he had no idea what the thing in the bushes could be.
    - OPTION {{
               Run away $$STORY running-away,
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

more examples can be found in the `atlas folder <https://github.com/EnokiUN/psup/blob/main/atlas/>`_.

This might look like a bit too much to understand at once but I'll break it bit by bit.

.. image:: /https://raw.githubusercontent.com/EnokiUN/psup/main/assets/discord.png
    :width: 50
    :alt: discord
    :target: https://discord.gg/XFrExEJMsK
