![computational_resources_baner](https://github.com/user-attachments/assets/055eb618-923a-4eb3-8d29-c3ae12048247)

* * * * *

> #### Table of Contents
>> ##### [MATHMODE computational resources](#resources)
>> ##### [Use of the servers](#rules)
>> ##### [Useful commands](#commands)
>> ##### [Useful tools](#tools)
>>> ###### [tmux🚧](#tmux)
>>> ###### [Hydra](#hydra)
>>> ###### [Profiler🚧](#profiler)
>> ##### [Frequently Asked Questions](#faq)
>>> ###### [Anaconda doesn't update a package to the version I want](#anaconda)
>>> ###### [Edit file on the server](#edit_file)
>>> ###### [The copying procedure from the server to my local pc and vice versa is so tedious](#copy)
>>> ###### [Can I disconnect from the SSH connection and leave the code running?](#disconnect)
>>> ###### [How can I check if the code ended its execution on the server?](#attach)
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

## tmux<a id="tmux"></a>
🚧

## <a id="hydra"></a>Hydra

Hydra is a framework that facilitates running and collecting results of experiments with multiple variations or combinations of configuration parameters. See the [examples](https://github.com/Mathmode/hydra-examples) on how to use the Hydra Framework to configure and run computational experiments   developed by our colleague [Tomas Teijeiro](https://github.com/tomas-teijeiro).

## Profiler <a id="profiler"></a>
🚧

# <a id="faq"></a>Frequently Asked Questions:
🚧

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

**How can I check if the code ended its execution on the server?**<a name="attach"></a>

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
