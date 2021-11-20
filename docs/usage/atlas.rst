Online Atlas
============

SUP provides a built-in way to view and play SUScript files without installing them, you could also add your own SUScript for them to be accessible for anyone to give them a try.

To view all the SUScript files in the Atlas visit the SUP `GitHub page <https://github.com/EnokiUN/sup/blob/main/atlas/>`_.

Similarly to add your own SUScript files to the Atlas just make a Pull Request in the GitHub page to the Atlas file and it will get reviewed and accepted if it runs without issues.

To run a SUScript file from the atlas there are two methods:

* Run it directly from the terminal by typing: (reccomended)

  ``sup <story-name> -online``.
  
  for more info on the SUP CLI check the `CLI doccumentation <doccumentation/cli.html>`.

* Run it with Python:
  
  To run a SUScript file with Pyhton make a .py file in the story's directory and type in it:

  .. code-block:: python3
    
    from sup import OnlineStory
    
    story = OnlineStory("story-name")
    story.start()
