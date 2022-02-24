# About the code

* This code represents a A* algorithm.
* It has methods to get the best positions from origin to goal.

# Executing the binaries

* In order to run you can just use one of the following commands

```sh
./renan.o

# windows > renan.exe
```

# Exectuion example

```
[
  { x: -3, y: -15 }, { x: -2, y: -14 },
  { x: -1, y: -13 }, { x: 0, y: -12 },
  { x: 1, y: -11 },  { x: 2, y: -10 },
  { x: 3, y: -9 },   { x: 4, y: -8 },
  { x: 5, y: -7 },   { x: 6, y: -6 },
  { x: 7, y: -5 },   { x: 8, y: -4 },
  { x: 9, y: -3 },   { x: 10, y: -2 },
  { x: 10, y: -1 },  { x: 10, y: 0 },
  { x: 10, y: 1 },   { x: 10, y: 2 },
  { x: 10, y: 3 },   { x: 10, y: 4 }
]
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