# Append-Markdown

Append-Markdown is a program intended to make keeping track of markdown notes easier.

## Features
* Json Output
* Output to a file following a given output format

## Goals
Make the program read in a certain format to look out for in markdown files, in which it will then scan the files and put the text within the format into a seperate file. (Done)

Make it so that changing the text in the generated file will also update the file in the seperate file (for certain ones). (Under works)

Make the format special characters customizable, in case the default one will be used in practice.

## Formats
A 'format' is a label that encases a text block of your choice.

For example,
@!Definition
some text
!@Definition

is an example where 'some text' is enclosed by a 'format' called Definition.

This will then all get copied to which ever file you wanted the generated text to go into.

