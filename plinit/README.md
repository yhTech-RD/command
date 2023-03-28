# plinit
A command to init YHCN, At the moment we think this command would to do this:
1. Initialize network
2. Create needed folder or file
3. ......

## useage
1. Install `Python3.9.x` in you develop environment.
2. Create a virtual enviroment in which path you like
3. Run `pip/pip3 install -r plinit/requirements.txt` to install needed package
4. Run `pyinstaller plinit/optimize.py`, get a dist folder
5. Copy `plinit/dist/optimize` to which path you like and give a `x` privilege to `plinit/dist/optimize/optimize`
6. Then you can run it on you shell

>> we suggest you that Copy this folder to `/usr/bin/`
>> and write a `alias` for it, it will be useful

## Comming soon