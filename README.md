Kanban builder
==============

A word of warning: this as niche as it gets. Imagine, if you will, the following scenario:

* you want to share a Kanban board with your team
* there's no Trello, Jira, Rally, Dashing, nothing
* even if you're prepared to put up with a single user spreadsheet your users can't get to it easily

But, and there's always a but, you have a VCS and you decide to use the one file you can manipulate easily without firing off pull requests every time you move a task along: the one and only README.md.

Now if you find you'd like to drop a Git(Hub|Lab|NextCoolThing) flavoured Markdown table in there, you may find this Kanban builder useful.

Build
-----
```
$ virtualenv ve
$ source ve/bin/activate
$ pip install pybuilder
$ pyb install_dependencies
$ pyb
```

Usage
-----
```
$ python [relative/path/to/]kanban_builder.py [input.yml]
```

Sample input file input.yml
---------------------------

```
columns:
- 'To do'
  - A
  - B
  - C is longer than B
- 'Doing'
  - D
  - E 
  - F 
- 'Done'
  - G
  - H
  - I 
```

Sample output
-------------
|**To do**         |**Doing**|**Done**|
|:-----------------|:--------|:-------|
|A                 |D        |G       |
|B                 |E        |H       |
|C is longer than B|F        |I       |

Output source
-------------
```
|**To do**         |**Doing**|**Done**|
|:-----------------|:--------|:-------|
|A                 |D        |G       |
|B                 |E        |H       |
|C is longer than B|F        |I       |
```

Exceedingly rarely asked questions
----------------------------------
Q: what have I gained?
A: it's much faster moving tasks along by yanking lines in vi and putting them in the next column array; moving cells up and down in visual mode is so tedious nobody would dream of doing it twice

