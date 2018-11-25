# How to generate output

Once you have your markdown files, you have to be able to output them

You can decide to just output the json file raw, or you can specify an output format json file.
An output format json file has the following format
```javascript
{
  "path"     : "Absolute or relative path of the output file", // str
  "prolog"   : "This is where you include the text that you want to print at the top of the file", // str
  "epilog"   : "This is where you include the test that you want to print at the bottom of the file", // str
  "contents" : // This is a list of format specifications
  [
    // Example of a format specification
    {
      "format"         : "Specify the format name", // str
      "prolog"         : "Prolog for the format", // str
      "divider"        : "Divider string to be inserted between each format" // str
      "comment_format" : "Specify the comment style that the output file has, so that the actual output hides the hash and everything. This string should include @!content!@ to specify where the commented text should go. For example, in c it would be \/\/@!content!@" // str
      "epilog"         : "Epilog for the format" //str
      "sync"           : "Whether or not you want editing the output file to make changes to the original definition."  // ** bool
    }
  ]
}
```

