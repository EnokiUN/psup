----------
Quickstart
----------

To make your first PSUP story you need one main thing, a sus file so go ahead and make a file called ``yourstory.sus``.

Now open that file in your preferred text editor and write some SUScript in it, refer to `the SUScript documentation </sus.html>`_.

Now you have to ways to run your story / game:

* Run it directly from the terminal by typing:

  ``sup <path-to-your-story>``

  or cd to the directory with it and type
  
  ``sup <story-name>``.

  for more info on the PSUP CLI check the `CLI documentation <cli.html>`.

* Run it with Python: (recommended)
  
  To run a SUScript file with Pyhton make a .py file in the story's directory and type in it:

  .. code-block:: python3
    
    from psup import Story
    
    story = Story("your-story-name")
    story.start()

  The reason this method is reccomended is so that IF you want to change the I/O methods of the Story class or want to change how it start/runs/ends thats doable by either using the provided decorators or directly subclassing the :class:`Story` class.

And that's it, now you created a SUScript file and ran it, give yourself a pat on the pat!
