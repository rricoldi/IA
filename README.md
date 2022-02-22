# About the code

* This code represents a graph.
* It has methods to do a Depth First Search and a Iterative Depth First Search.

# Executing the binaries

* In order to run you can just use one of the following commands

```sh
./renan.o

# windows > renan.exe
```

# Exectuion example

```
A -> B, C
B -> D
C -> E, F
D -> G
E ->
F ->
G ->

Height: 4

Depth First Search: A, B, D, G

Iterative Depth First Search:
Limit: 1 | Search: Not found
Limit: 2 | Search: Not found
Limit: 3 | Search: Not found
Limit: 4 | Search: A, B, D, G
```


# Running

```sh
# clone into your machine
https://github.com/rricoldi/IA.git

# enter the folder
cd IA

# change branch
git checkout atividade-3

# install deno
curl -fsSL https://deno.land/x/install/install.sh | sh
# (windows powershell) iwr https://deno.land/x/install/install.ps1 -useb | iex
# (mac) brew install deno


# run deno program with flags
deno run src/index.ts
```