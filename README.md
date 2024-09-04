![computational_resources_baner](https://github.com/user-attachments/assets/055eb618-923a-4eb3-8d29-c3ae12048247)

* * * * *

> #### Table of Contents
>> ##### [MATHMODE computational resources](#resources)
>> ##### [Use of the servers](#rules)
>> ##### [Useful commands](#commands)
>> ##### [Useful tools](#tools)
>>> ###### [Use environments to manage Python packages: Miniconda🚧](#conda)
>>> ###### [IDE for scientific programming in the Python: Spyder](#spyder)
>>> ###### [Persistent sessions: tmux🚧](#tmux)
>>> ###### [Multiple configurations: Hydra](#hydra)
>>> ###### [Profiling🚧](#profiler)
>> ##### [Frequently Asked Questions](#faq)
>>> ###### [Anaconda doesn't update a package to the version I want](#anaconda)
>>> ###### [Edit file on the server](#edit_file)
>>> ###### [The copying procedure from the server to my local pc and vice versa is so tedious](#copy)
>>> ###### [Can I disconnect from the SSH connection and leave the code running?](#disconnect)
>>> ###### [How can I run the code in one GPU and limit its memory?](#limit_GPU)
* * * * *

#  MATHMODE computational resources <a name="resources"></a>
The Group of Applied Mathematical Modeling, Static and Optimization ([MATHMODE](https://www.mathmode.science/))
has available the following computational resources:
| Server name |   IP address  | CPU | GPU | RAM|
| :---:   | :---: | :---: | :---: | :---: |
| ρK ("La roca")   | 10.227.85.95 | 40 cores. (2x) CPU: Intel(R) Xeon(R) Gold 6230 CPU @ 2.10GHz | (2x) NVIDIA RTX A4500 20GB GDDR6| 768GB (12x) Samsung M386A8K40CM2-CVF 64GB DDR4|
|David  | 10.10.15.21 |40 cores. (1x) AMD EPYC 9474F @ 3.6GHz | (2x) NVIDIA Quadro GV100; 32GB| 384GB (6x/12) DDR5 4800MHz 32GB ECC REG|
|Goliat | 10.10.15.20 |128 cores. (2x) AMD EPYC 7763 @ 2.45GHz | (2x) NVIDIA Quadro GV100; 32GB <br/> (3x) NVIDIA L40S; 48GB| 512GB (8x/32) DDR4 3200MHz 64GB ECC REG|

# <a id="rules"></a> Use of the servers
* The use of the servers is limited to the members of the MATHMODE group and its collaborators. The account holder undertakes not to store illicit files, private data, and, in general, any data that is not related to your research. If you want an account, email David Pardo.
* To connect with the server, you need to do it through the UPV/EHU intranet which requires a secure connection. You will be able to connect to `vpn.ehu.es` by using your LDAP and password. See https://www.ehu.eus/es/web/ikt-tic/vpn and install the software AnyConnect.
* All the software you need has to be installed locally. We encourage the use of [Miniconda](https://docs.anaconda.com/miniconda/miniconda-install/) for that purpose.

## Limitations of use:
- One user per server/workstation at the same time!
- A user can only use one GPU!
- Reservation of all GPU memory is not allowed. Limit the VRAM memory you need to use!
- Exceeding 25% occupied cores by a user is not allowed!

We have a WhatsApp group to promote coexistence and dialogue. If you need to exceed these rules, please ask in the WhatsApp group. If we can arrive at agreements, these rules can be relaxed. Otherwise, these rules will be strictly applied, and users reported by others in the group providing evidence could be temporarily banned.

# <a id="commands"></a> Useful commands
* Test the connection with Goliat
   ```
   ping 10.10.15.20
   ```
* Connect via ssh to the server Goliat
   ```
   ssh username@10.10.15.20
   ```
* secure copy of a folder that is in my Desktop to Goliat `scp -r <origin> <destination>`
   ```
   scp -r Desktop/folder_name username@10.10.15.20
   ```
* monitor the server processes 
   ```
   htop
   ```
* monitor the GPU processes 
   ```
   watch -n 1 nvidia-smi
   ```
* execute your code limiting the cores used 
   ```
   taskset –ac 0-15 python myscript.py #(instead 0-15 put the free cores you want to use)
   ```
# <a id="tools"></a>Useful Tools

## Use environments to manage Python packages: Miniconda<a id="conda"></a>
Anaconda and Miniconda are a distributions of the Python and R programming languages for scientific computing that aims to simplify package management and deployment.
Both Anaconda Distribution and Miniconda include the conda package and environment manager. The main difference is that Anaconda has a graphical interface form manage and includes more python packages (250+) than Miniconda(<70). **If you use our servers you have to install there Miniconda.** We also recomend this distribution for your computer and we encourage that you use it from the terminal.

### Basic usage guide
Conda allows you to create separate environments, each containing their own files, packages, and package dependencies. The contents of each environment do not interact with each other.

The basic way to create a new environment (with name tf) is:
   ```
   conda create -n tf
   ```
You can see the list of the environments you have
  ```
  conda env list
  ```
To go inside the environment we have created we need to activate it
   ```
   conda activate tf
   ```
Then we can install Python packages
   ```
   conda install numpy
   ```
but sometimes a package you want is located in another channel, such as conda-forge, you can manually specify the channel when installing the package:
   ```
   conda install conda-forge::tensorflow==2.15
   ```
Occasionally a package needed which is not available as a conda package but is available on PyPI and can be installed with pip. In these cases, trying to use conda and pip makes sense.
   ```
    conda install pip
   ```
   ```
   pip install keras==3.0
   ```

We also can install packages while creating an environment, specify them after the environment name:
   ```
   conda create -n tf python==3.9 numpy matplotlib
   ```
We can do exactly the same but using a YAML file [`tf.yml`](https://github.com/Mathmode/server_tools/blob/main/code/tf.yml)
   ```
   conda env create -f tf.yml 
   ```
You can make an exact copy of an environment (tf) by creating a clone (tf_clone) of it:
   ```
   conda create --name tf_clone --clone tf
   ```
To list all of the packages in the active environment:
  ```
  conda list
  ```
To remove a package such as keras in the current environment:
  ```
  conda remove keras
  ```
To remove an environmet you need to be outside.
  ```
  conda deactivate
  ```
  ```
  conda remove --name tf --all
  ```
🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧
## IDE for scientific programming in the Python: Spyder<a id="spyder"></a>
[Spyder](https://www.spyder-ide.org/) is an open-source cross-platform Integrated Development Environment (IDE) for scientific programming in the Python language.
![alt text](https://raw.githubusercontent.com/spyder-ide/spyder/5.x/img_src/screenshot.png)

## Persistent sessions: tmux<a id="tmux"></a>
tmux is a program which runs in a terminal and allows multiple other terminal programs to be run inside it. Each program inside tmux gets its own terminal managed by tmux, which can be accessed from the single terminal where tmux is running.

tmux, and any programs running inside it, may be detached from the terminal where it is running (the outside terminal) and later reattached to the same or another terminal.

The main uses of tmux are to:

   * Protect running programs on a remote server from connection drops by running them inside tmux.

   * Allow programs running on a remote server to be accessed from multiple different local computers.

   * Work with multiple programs and shells together in one terminal, a bit like a window manager.
     
A simple use of use tmux to run our code is explained in [this FAQ](#disconnect).

🚧🚧🚧🚧🚧🚧🚧

## <a id="hydra"></a>Multiple configurations: Hydra

Hydra is a framework that facilitates running and collecting results of experiments with multiple variations or combinations of configuration parameters. See the [examples](https://github.com/Mathmode/hydra-examples) on how to use the Hydra Framework to configure and run computational experiments   developed by our colleague [Tomas Teijeiro](https://github.com/tomas-teijeiro).

## Profiling <a id="profiler"></a>

### CPU profiling

For CPU profiling, we recommend the combination of the standard module [cProfile](https://docs.python.org/3/library/profile.html) and the [snakeviz](https://jiffyclub.github.io/snakeviz/) viewer. Just two commands are enough to get started:
 ```
$ python -m cProfile -o output_profiling_file script.py
$ snakeviz output_profiling_file
 ```

### Memory profiling

For memory profiling, we recommend the use of [memray](https://bloomberg.github.io/memray/).

# <a id="faq"></a>Frequently Asked Questions:

**What can I do if Anaconda doesn't update a package to the version I want?**<a name="anaconda"></a>

You can try to install pip in your environment 
```conda install pip```
and force the desired package installation 
``` pip install tensorflow==2.15.0```

**How can I edit a file on the server?**<a name="edit_file"></a>

use `vi filename` or `vim filename` (which does not require a graphical interface)

 |Command |Description|
 | :---:   | :---: |
 |Esc | to exit of one mode|
 |i   | enables insert-mode|
 |:w  | save changes|
 |:q! | quit without changes|
 |:q  | quit|
 |:x  | save and quit|

**The copying procedure from the server to my local pc and vice versa is so tedious. Can I do something?**<a name="copy"></a>

Sure! We recommend you install [FileZilla Client](https://filezilla-project.org/). You need to

**Can I disconnect from the SSH connection and leave the code running?**<a name="disconnect"></a>

 When you stop the SSH connection, the process that is in the server dies. To avoid this, you need to use `tmux` as follows
 
  1) Activate the conda environment
  2) Create a new session by the command:
     ```
     tmux new -s session_name
     ```
  3) Run your code
  4) Detach the session: press `CTRL+b`, then release both keys and press `d`
  5) Disconnect from the server

To check if the code ended its execution on the server:

1) Connect to the server via SSH
2) Attach to the session created before
   ```
   tmux attach -t session_name
   ```
3) Remember to kill the session after the simulation is finished!}
   ```
   tmux kill-session -t \textit{name}
   ```

To get a list of the currently running sessions:
   ```
   tmux ls
   ```

**How can I run the code in one GPU and limit its memory?**<a name="limit_GPU"></a>
🚧
