# Exercise 0 - Bash commands

Use windows for linux (WSL), ubuntu bash, git bash or terminal in mac to solve all these exercises, **don’t use GUI**. A lot of the training in these exercises are both to search up commands and also to understand the computer science terminology.

**Tips**: work with exercise X alongside with other exercises.

---

## 0. Setup a git repository (\*)

a) Make a directory called Linux-training.
```bash
mkdir Linux-training
```


b) Create the files called

```bash
“note1.txt”, “note2.txt”, “note3.txt”, “note4"
```
```bash
touch note{1..4}.txt
```

---

## 1. Navigating and moving (\*)

a) Make a subdirectory called cool_notes
```bash
mkdir  cool_notes
```


b) Move all .txt files into cool_notes

```bash
$ mv note{1..4}.txt cool_notes
```

c) Delete note4

```bash
$ rm note4.txt
```

d) Change directory to cool_notes and list all the files there

```bash
$ cd cool_notes
```

e) Move note3.txt out from cool_notes into parent directory

```bash
$ mv note3.txt ../
```

f) Navigate to parent directory

```bash
$ cd ../
```

g) From here list all files including hidden files

```bash
$ ls -a
```

h) Change name on note3.txt to note_home.txt

```bash
$ mv note3.txt note_home.txt
```

---

## 2. Printing, variables and manipulating text (\*)

a) Print out “hello from note_home” into bash

```bash
echo "hello from note_home"
```

b) Write this text string into note_home.txt

```bash
$ echo -e  "hello from note_home" note_home.txt
```

c) Print out the “current path is: <your current directory path>” in bash

```bash
$ echo "current path is: $PWD"
```

d) Write this string into note_home in a new line so it should contain

```bash
hello from note_home
current_directory is: <your current directory path>
```
```bash
echo -e  "\ncurrent path is: $PWD\n" >> note_home.txt
```


e) Print out the content of the note_home.txt

```bash
$ cat note_home.txt
```

f) Count the number of words in this file

```bash
$ wc -w  note_home.txt
```

g) Count the number of lines in this file

```bash
$ wc -l  note_home.txt
```

h) Count the number of files in cool_notes

```bash
$ ls cool_notes | wc -l
```

i) Check the disk usage in your directory and make the format human readable

```bash
$ du -sh ../
```

---

## 3. Pokeventure (\*)

a) Create a folder called data with a subfolder called pokemons
```bash
$ mkdir -p data/pokemons
```


b) Create a file called pokemon_list.txt

```bash
touch pokemon_list 
```

c) Type in a random list of pokemons, using echo and the bitshift operator

for example:

```bash
pikachu
voltorb
bulbasaur
mew
zapdos
mewtwo
```

```bash
$ echo -e  "pikachu\ncharizard\nmewtwo\nchandelure\nlopunny\nvanillish\ngyarados" > pokemon_list.txt
```

d) Loop through your file and print out the following

```bash
pokemon: pikachu
pokemon: voltorb
pokemon: bulbasaur
pokemon: mew
pokemon: zapdos
pokemon: mewtwo
```

```bash
while read -r line
do
    echo -e "pokemon: $line"
done < pokemon_list.txt
```

e) Now test out the following api manually in your browser [https://pokeapi.co/api/v2/pokemon-species/voltorb](https://pokeapi.co/api/v2/pokemon-species/voltorb)

```bash
CTRL + Click the link 
```

f) Now test it out using bash, and see that it prints out the same results

```bash
curl https://pokeapi.co/api/v2/pokemon-species/voltorb
```

g) Do a for loop on pokemon_list.txt, pick the pokemons on the file and request the api. Save each pokemon into their respective json file. Important: add a pause of 2 seconds after each iteration. Your structure should look something like this now.

```bash
└── data
    └── pokemons
        ├── bulbasaur.json
        ├── mew.json
        ├── mewtwo.json
        ├── pikachu.json
        ├── pokemon_list.txt
        ├── voltorb.json
        └── zapdos.json
```

```bash
while read -r line
do
     curl https://pokeapi.co/api/v2/pokemon-species/$line > "${line}.json"
     sleep 2
done < pokemon_list.txt
```

h) Remove all files ending with .json using one command

```bash
$ rm -r *.json
```

i) Now move yourself to the same level, i.e. sibling to data directory. Create a bash script file called download_pokemons.sh. Put in bash logic for downloading the pokemons specified in data/pokemon/pokemon_list.txt file and saving it into data/pokemons/ and run it. Your file structure might look like this now. (\*\*)

```bash
├── data
│   └── pokemons
│       ├── bulbasaur.json
│       ├── mew.json
│       ├── mewtwo.json
│       ├── pikachu.json
│       ├── pokemon_list.txt
│       ├── voltorb.json
│       └── zapdos.json
└── download_pokemons.sh
```

```bash

$ nano download_pokemons.sh


#!/bin/bash

cd pokemons

while read -r line
do
     echo -e "Downloading data for pokemon $line"
     curl https://pokeapi.co/api/v2/pokemon-species/$line > "${line}.json"
     sleep 2
     echo -e "Download complete for pokemon $line"
     sleep 1
done < pokemon_list.txt

CTRL + X, Y, ENTER

$ chmod +x download_pokemons.sh

$ ./download_pokemons.sh

```

---

## X. Commands glossary (\*)

Fill in this table. You can do this in any application, it might be too hardcore to do this with terminal only. Tips you can use man command to check documentation. Also try out the different commands to see them in action.

| Command | What does the command do | Some useful options |
| ------- | ------------------------ | ------------------- |
| cd      |    Changes Directory     |                     |
| ls      |    Lists files in CD     |                     |
| touch   | Creates a file or folder |                     |
| wc      |       Word Count         |                     |
| grep    |         Search           |                     |
| mkdir   |     Make Directory       |                     |
| mv      |       Move File          |                     |
| rm      |       Remove File        |                     |
| rmdir   |    Remove Directory      |                     |
| ssh     |                          |                     |
| curl    |                          |                     |
| sudo    |                          |                     |
| apt-get |                          |                     |
| ps      |                          |                     |
| cp      |                          |                     |
| less    |                          |                     |
| top     |                          |                     |
| head    |                          |                     |
| echo    |                          |                     |
| cat     |                          |                     |
| chmod   |                          |                     |
| chown   |                          |                     |
| kill    |                          |                     |
| &&      |                          |                     |
| wget    |                          |                     |
| pwd     |                          |                     |
| >>      |                          |                     |
| >       |                          |                     |
| \*      |                          |                     |
| ./      |                          |                     |
| diff    |                          |                     |
| find    |                          |                     |
