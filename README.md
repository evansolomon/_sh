# _sh (the _s shell)

`_sh` is a command line tool to generate forks of the [_s](https://github.com/Automattic/_s) WordPress starter theme.  It uses [underscores.me](http://underscores.me/) to create the fork, but lets you do it entirely from the command line.

It lives at [https://github.com/evansolomon/_sh](https://github.com/evansolomon/_sh).

## Installation

`_sh` is written in Python, so you'll need to have it installed and have a way to interact with it on the command line, like in Terminal.app.

The easiest way to use `_sh` is to put it in a place that your `PATH` can access it. First, `clone` this repository.

```shell
git clone git@github.com:evansolomon/_sh.git /path/to/wherever/you/want/to/save/it
```

From the directory that you cloned `_sh`, you can run the `setup.py` installer script to create a symlink.

```shell
python setup.py
```

That will give you a prompt where you can type the directory that you want to link `_sh` to.  Here I'll set it up to live in me `~/bin` directory.

```
Welcome to _sh.

Where do you want to symlink _sh? ~/bin



Running...

ln -s /Users/evan/code/_sh/_sh /Users/evan/bin
```

## Usage

Assuming you've setup `_sh` to be accessible in your `PATH`, to use it you can just call `_sh` on the command line from anywhere.

When you call `_sh` you'll get an interactive prompt that will walk you through setting up your theme. The new theme will get created in a child directory of wherever the command is run from. Here's an example:

```shell
mkdir -p ~/code/themes && cd ~/code/themes && _sh
```
Once I run the `_sh` command I'll get an interactive prompt with a few questions to setup my new theme. It's hard to tell from here, but the introduction and questions all come from `_sh`, and the answers come from me, typed into an interactive prompt in Terminal. Most of these questions are optional; the only one you must answer is the theme's name.

```
I'm going to ask you for some information about your theme.

You have to give your theme a name but you can leave the others blank if you want.

Let's get started.

Name? Stella and Mojo
Slug? stellaandmojo
Author? Evan Solomon
Author URI? http://evansolomon.me
Description? It's a theme named after dogs, because why the hell not.
```

At this point, `_sh` will make a request to [underscores.me](http://underscores.me), download a ZIP file with my new theme, and unzip it. Then I'll have a directory in `~/code/themes/stellaandmojo` with my theme files.

That's it, now I've got a new fork on _s with all of my customizations setup.
