Online SUSMon
=============

PSUP provides a built-in way to view and play SUScript files without installing them, you could also add your own SUScript for them to be accessible for anyone to give them a try.

To view all the SUScript files in the SUSMon visit the PSUP `GitHub page <https://github.com/EnokiUN/psup/blob/main/SUSMon/>`_.

Similarly to add your own SUScript files to the SUSMon just make a Pull Request in the GitHub page to the SUSMon file and it will get reviewed and accepted if it runs without issues.

To run a SUScript file from the SUSMon there are two methods:

* Run it directly from the terminal by typing: (reccomended)

  ``psup <story-name> -online``.
  
  for more info on the PSUP CLI check the `CLI documentation <cli.html>`_.

* Run it with Python:
  
  To run a SUScript file with Pyhton make a .py file in the story's directory and type in it:

  .. code-block:: python3
    
    from psup import OnlineStory
    
    story = OnlineStory("story-name")
    story.start()

