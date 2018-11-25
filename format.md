# How to generate output

Once you have your markdown files, you have to be able to output them

You can decide to just output the json file raw, or you can specify an output format json file.
An output format json file has the following format

{
  "path"     : "Absolute or relative path of the output file", # type should be string
  "prolog"   : "This is where you include text that you want to print at the top of the file", # type should be string
  "contents" : #this is a list of format specifications
  [
    {
      "format"         : "Specify the format name",
      "prolog"         : "Prolog for the format",
      "divider"        : "Divider string to be inserted between each format
      "comment_format" : "Specify the comment style that the output file has, so that the actual output hides the hash and everything. This string should include @!content!@ to specify where the commented text should go. For example, in c it would be //@!content!@"

    }
  ]

  
}
