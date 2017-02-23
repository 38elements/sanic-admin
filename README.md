# sanic-admin

`sanic-admin` is a command line tool for automatically restarting [sanic](https://github.com/channelcat/sanic).  
The code(*.py) under the current working directory is changed, `sanic` will automatically restart.

## Installation

```
pip install sanic-admin
```

## Usage

```
python -m sanic-admin server.py
```

## Setting

You can change the behavior of `sanic-admin` by putting a file named` sanic-admin.json` in current working directory like the contents below.

```
{
    "patterns": ["*.html", "*.css", "*.py"], // default ["*.py"]
    "paths": ["/foo1/bar1", "/foo2/bar2"] // default current working directory
}
```
