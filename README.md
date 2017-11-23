# Introduction

`plist2Alfred.py` converts a macOS text substitution `.plist` to a `.alfredsnippets`.

# Prior work

The `LaTeX Subsitutions.plist` comes from [LaTeXSubstitutionPlist](https://github.com/deszoeke/LaTeXSubstitutionsPlist).

The original Python script comes from [alfred-snippets](https://github.com/AndiH/alfred-snippets/blob/master/convert-aText-to-Alfred.py), and I modified it to fit my need.

# Usage

```
    chmod +x ./plist2Alfred.py
    ./plist2Alfred.py plistfilename.plist
```

## LaTeX Snippets

Use it as normal LaTeX symbols but adding a backslash `\` to complete the shortcut to prevent conflicts.

For example: `\alpha\` expands to `α`
