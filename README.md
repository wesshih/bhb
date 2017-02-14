# BHB

Some code to query and eventually analyze BHBs and dust in the CGM.

  I make no promises as to the state of the code at any given time. Right now, there is no consistancy between any of the files, and its pretty disorganized. Once I've figured out more how I want to do things, I may attempt to make it presentable. 
  For the most part though, things will probably be lumped into one off "do it all" programs. I'll try to add brienf descriptions when I remember or feel like it.

  query.py reads in the fits table, constructs a bunch of queries (overly long and messy strings that bum me out, but too lazy), executes all the queries, matches a result to proper fits entry, then writes a new fits table.

  fields.txt is a list of database elements that will be queried by query.py. Each element should be formatted table.field, and only one per line. no extra white space.

  printStarParams.py simply outputs the various parameters for some bhb to a text file. just a nice way to print and save one star's data. Saves to StarParams.txt.
