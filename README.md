# README #

This is LLDB python scripts that help debugging Qt applications. Original code is written by [Paul Perehogih](https://bitbucket.org/pperehogih/lldb-qt-formatters/overview). This particular implementation has been changed to support QString of Qt 4.8 and not 5.5 as in original implementation.

I tested QString and QList only, hoping that the rest of the scripts will be compatible. But I don't know. These types are supported:

- QString
- QUrl
- QVector
- QList
- QPointer

# Installation #

Clone this repo somewhere, e.g. ~/.qtlldb. Then add the following lines to your ~/.lldbinit (create one if does not exist):

```
command script import ~/.qtlldb/QtFormatters.py
command source ~/.qtlldb/QtFormatters.lldb
```
