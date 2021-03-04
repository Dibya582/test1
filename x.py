from flask import Flask, render_template
app = Flask(__name__)


all_post = [

        {
          'command':'ls',
          'stands':'stands for list directory',
          'whatdoes': 'It will show all the files inside a particular directory',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ ls'
       },
       {
          'command':'cd',
          'stands':'stands for change directory',
          'whatdoes': 'It will change current location',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ cd Desktop'
       },
       {
          'command':'cd ..',
          'stands':'stands for change directory to previous position',
          'whatdoes': 'It will change current location to previous one',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ cd ..'
       },
       {
          'command':'ls',
          'stands':'stands for list directory',
          'whatdoes': 'It will show all the files inside a particular directory',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ ls'
       },
       {
          'command':'ls -R',
          'stands':'stands for list directory Recursively',
          'whatdoes': 'Not only Show all te files in directories but also subdirectories',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ ls -R'
       },
       {
          'command':'ls -al',
          'stands':'stands for list directory with all information',
          'whatdoes': 'It will show detailded information of the files in a column format',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ ls -al'
       },
       {
          'command':'ls -a',
          'stands':'stands for list directory with hidden file access',
          'whatdoes': 'It will show all the files inside a particular directory including hidden files',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ ls -a'
       },
       {
          'command':'touch',
          'stands':'same as it is a name',
          'whatdoes': 'It will help to create a file',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ touch abc.txt'
       },
       {
          'command':'cat',
          'stands':'stands for concatenate',
          'whatdoes': 'It helps to create a file and add content to it',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ cat > filename'
       },
       {
          'command':'cat filename',
          'stands':'stands for concatenate  a file',
          'whatdoes': 'It helps read file content inside terminal',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ cat filename'
       },
       {
          'command':'cat file1 file2 > file3',
          'stands':'stands for concatenate files',
          'whatdoes': 'It helps to merge two file into one',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ cat > file1 file2 > file3'
       },
       {
          'command':'rm',
          'stands':'stands for remove',
          'whatdoes': 'It helps to remove a file from current location',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ rm filename'
       },
       {
          'command':'mv',
          'stands':'stands for move',
          'whatdoes': 'It helps to move a file to other location',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ mv filename /Desktop/shell'
       },
       {
          'command':'mv ',
          'stands':'stands for move',
          'whatdoes': 'It can also helps to rename a file',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ mv file1 file2'
       },
       {
          'command':'mkdir',
          'stands':'stands for make directory',
          'whatdoes': 'It helps to create a folder',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ mkdir dir1'
       },
       {
          'command':'rmdir',
          'stands':'stands for remove directory',
          'whatdoes': 'It helps to remove directory from cureent working directory',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ rmdir dir1'
       },
       {
          'command':'mv',
          'stands':'stands for move',
          'whatdoes': 'It also can be used to rename a directory',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ mv dir1 dir2'
       },
       {
          'command':'sudo',
          'stands':'stands for root access',
          'whatdoes': 'It helps get root access of system',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ sudo '
       },
       {
          'command':'mv',
          'stands':'stands for move',
          'whatdoes': 'It helps to move a file to other location',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ mv filename /Desktop/shell'
       },
       {
          'command':'mv',
          'stands':'stands for move',
          'whatdoes': 'It helps to move a file to other location',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ mv filename /Desktop/shell'
       },
       {
          'command':'mv',
          'stands':'stands for move',
          'whatdoes': 'It helps to move a file to other location',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ mv filename /Desktop/shell'
       },
       {
          'command':'mv',
          'stands':'stands for move',
          'whatdoes': 'It helps to move a file to other location',
          'example':'HP-240-G5-Notebook-PC:~/Desktop$ mv filename /Desktop/shell'
       }

]


@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/set')
def set():
	return render_template('set.html',sets=all_post)

app.run(debug="True")