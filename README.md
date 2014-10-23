# kapai-django

## Overview

This project was a custom-built website designed specifically for a World of Warcraft guild. The guild ([http://www.kapaiguild.com/](Ka Pai)) has been defunt for quite some time, but I decided to open-source the code for other guilds to potentially fork and use. It contains a number of nice features (detailed below) that a typical guild might need, and should be relatively easy to build on top of.

It also happens to be a codebase that I spent a reasonable amount of time on, and wanted to share as sample work! :)

For the most interesting code, refer to the /raidtool directory.

Note that the project hasn't been updated in a long while. For example it uses South for migrations (recent versions of Django have migrations rolled in). Some changes may be required to use it with recent frameworks/tools.

## Features

There are a number of features built into the project, some more custom that others:

* Homepage - includes news, progression, gallery, and recruitment
* News/Gallery - self explanatory... gallery was a new feature and could use some improvement
* Progression - set up instances, bosses, and boss "details" (e.g. Heroic or other incremental progression)
* Recruitment - does what you'd imagine :)
*   Raid Tool - probably the most interesting part of the site:

    Users can log in using their forum (phpBB) credentials

    Can either create new characters, or (preferably) "claim" existing characters - the guild roster can be imported using an EPGP export

    Users can specify ahead of time which gear they are interested in for specific characters and encounters

    Then, during raid time, raid leaders can pull up a list of all encounters in a given instance

    Characters can be filtered to those actually in a given raid through use of a companion addon

    Then, it becomes trivial to rotate in and out characters who need gear from a given encounter, simply by looking at the encounter list

    As characters actually get gear, removing them from the list is a single click (plus confirmation)

* Redirects - set up simple URLs such as /apply or /charter and have them redirect to forum topics etc - note that this requires some custom coding to work correctly