# KronaIgnore
# Language: Python
# Input: TXT
# Output: KRONA
# Tested with: PluMA 1.1, Python 3.6

Remove all lines that contain a particular string of text from a Krona file.

Useful for example for removing unclassified taxa, or subspecies

The plugin accepts as input a TXT file of keyword-value pairs:
kronafile: Name of the KRONA file to filter
patternfile: TXT file containing patterns to ignore, one per line

Output is the filtered KRONA File
