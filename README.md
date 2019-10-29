# vscode Language Server 插件测试

## Install Server Dependencies

1. Install `pygls` following this [README](https://github.com/openlawlibrary/pygls)
1. Create `.vscode/settings.json` file and set `python.pythonPath` to point to your python environment where `pygls` is installed

## Install Client Dependencies

Open terminal and execute following commands:

1. `npm install`
1. `cd client/ && npm install`

## Run Example

1. RUN `python __main__.py --tcp`
1. Open this directory in VS Code
1. Open debug view (`ctrl + shift + D`)
1. Select `Server + Client` and press `F5`
