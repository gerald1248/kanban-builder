Kanban builder
==============

A word of warning: this is as niche as it gets. Imagine, if you will, the following scenario:

* you want to share a Kanban board with your team
* there's no Trello, Jira, Rally, Dashing, nothing
* even if you're prepared to put up with a single user spreadsheet your users can't get to it easily

But, and there's always a but, you have a VCS and you decide to use the one file you can manipulate easily without firing off pull requests every time you move a task along: the one and only README.md.

Now if you find you'd like to drop a Git(Hub|Lab|NextCoolThing) flavoured Markdown table in there, you may find this Kanban builder useful.

Usage
-----
```
$ python [relative/path/to/]kanban_builder.py [input.yml]

Arguments:
--rows=N: display no more than N rows (default is 20)
--help/-h: display this text
```

Build
-----
```
$ virtualenv ve
$ source ve/bin/activate
$ pip install pybuilder
$ pyb install_dependencies
$ pyb
```

Sample input file input.yml
---------------------------
```
- 'To do':
  - A
  - B
  - C is longer than B
- 'Doing':
  - D
  - E 
  - F 
- 'Done':
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

A: Let's say you want to move 'C is longer than B' from 'To do' to 'Doing'. In vi you would type:

```
4Gddp:x
```

To achieve the same by editing the markdown source, you would need to jump into visual mode and:

* cut out 'C is longer than B'
* add a new row at the bottom of the table
* shunt down 'D', 'E' and 'F'
* insert 'C is longer than B' at the top of the Doing column
* adjust the column widths
