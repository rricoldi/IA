# About the code

* This code is a basic agent elevator that receives rules, and based on the environment, change its state and the environment.
* It has the capability of always getting to the called story.

# Running

```sh
# clone into your machine
https://github.com/rricoldi/IA.git

# enter the folder
cd IA

# change branch
git checkout atividade-1

# install deno
curl -fsSL https://deno.land/x/install/install.sh | sh
# (windows powershell) iwr https://deno.land/x/install/install.ps1 -useb | iex
# (mac) brew install deno


# run deno program with flags
deno run src/index.ts
```