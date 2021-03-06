# sanic-admin

`sanic-admin` is a command line tool for automatically restarting [sanic](https://github.com/channelcat/sanic).  
The code(*.py) under the current working directory is changed, `sanic` will automatically restart.

## Installation

```
pip install sanic-admin
```

## Usage

#### Auto reload

```
sanic-admin server.py
```

#### Display urls

```
sanic-admin -urls server.py
```

## Setting

You can change the behavior of `sanic-admin` by putting a file named` sanic-admin.json` in current working directory like the contents below.

```
{
    // Patterns of filename to be watched
    // default ["*.py"]
    "patterns": ["*.html", "*.css", "*.py"],
    // Paths to be watched
    // default current working directory
    "paths": ["/foo1/bar1", "/foo2/bar2"],
    // File to be executed when sanic-admin starts
    // default None
    "before": "before.py",
    // File to be executed before sanic restarts
    // default None
    "before_each": "before_each.py",
    // File to be executed when sanic-admin exits
    // default None
    "after": "after.py",
    // File to be executed after sanic restarts
    // default None
    "after_each": "after_each.py",
    // Variable name of sanic instance 
    // default "app" 
    "app": "app"
}
```
