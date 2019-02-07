# hw2grading

You will have to download each student assignment into the directory containing `grader.py` and `nodes.py`.
Then, simply run `python grader.py`. You'll have to grade the slice method by hand.

In order for this to work, the student assignments must be named `hw2.py`. 

Please remember that this is not the final test to see how well a student did on the assignment. It's more like a tool that will help you decide how carefully you need to look at the student's code. If everything passes, you won't have to look so hard.
 
 `[PASSED]` means it works as expected; just glance at their implementation to make sure it looks good.
 
 `[ERROR]` means there are some problems with the class. The issues should be listed directly above the tag.
 
 There are two types of issues:
 
   `ERROR:root:_____crashed!` tags mean some sort of exception occurred. This could be a syntax problem, name discrepancies, the code could just flat out not be there, etc. The method where the exception occurred is listed above the tag.

   `<method name> mismatch` indicates that the method in question didn't return the proper output.

  
 Hopefully this is more of a help than a hindrance! Good luck.
