# Plagiarism-Detector
This plagiarism detector can be used to find similarity between two files. However, it is mainly targeted for source codes.

1. Whitespaces, newlines, tabs are detected and ignored for plagiarism testing
2. Header files are not considered 
3. Macros and preprocessor directives are ignored
4. Single and multi line comments are ignored

### Possible ares of improvement:
1. Detect variables and donot consider variable names for testing.
2. For C, C++, JAVA additional checking can be done by testing the assembly code generated after compilation  

### Instruction:
Put the files to be checked in a directory. Provide the path of the directory as Input.