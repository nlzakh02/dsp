# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > **pwd** - show current working directory path  
> > **mkdir** - create a directory  
> > **rm -r** - delete a directory  
> > **touch metis.txt** - create a file _metis.txt_ using `touch` command  
> > **rm metis.txt** - delete a file  
> > **mv metis.txt metis1.txt** - rename a file _metis.txt_ to _metis1.txt_  
> > **ls -a** - list hidden files  
> > **cp metis.txt /dsp/metis/** - copy a file _metis.txt_ from current directory to directory _metis_  
> > **cd** - switch to another diresctory  
> > **cat** - output the contents of a file to the terminal  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls`- list all files and directories  
> > `ls -a` - list all contents, including hidden files and directories  
> > `ls -l` - list all contents of a directory in long format  
> > `ls -lh` - list all contents of a directory in long format with human readable file sizes (units of K, M, G)  
> > `ls -lah` - list all contents, including hidden files and directories in long format with human readable file sizes (units of K, M, G)  
> > `ls -t` - list files and directories ordered by the time they were last modified  
> > `ls -Glp` - list all contents of a directory in long format without printing group names with **/** appended to names of directories  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -r` - list files in reverse order  
> > `ls -R` - list subdirectories too  
> > `ls -u` - list files by the file access time  
> > `ls -d` - list only directories  
> > `ls -c` - list files by file timestamp  

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > _xargs_ builds and executes command lines from standard input and converts the result into an argument that can be passed to another command.  
> > Example: **echo 'one two three' | xargs mkdir**  
> > What happens: string'one two three' is accepted by _echo_, parsed at blank spaces into 3 strings ('one', 'two', 'three') that are passed to command _mkdir_ for creating 3 directories with corresponding names   

