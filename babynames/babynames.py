#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
import codecs
import sys
import re
import operator
"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    names=[]
    ranks = []
    year = None
    p = r'<tr align="right">.*'
    p_year = r'<h3 align="center">.*(\d{4,4})</h3>'
    with open(filename, 'r') as f:
        for line in f:

            #print(line)
            match = re.search(p,line)
            if not year:
                match_year = re.search(p_year, line)
                if match_year:
                    year = match_year.group(1)
            if match:
                raw_rank_text = match.group()
                p_2 = r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>'
                new_rank = re.search(p_2, raw_rank_text).group(1)
                raw_name1 = re.search(p_2, raw_rank_text).group(2)
                raw_name2 = re.search(p_2, raw_rank_text).group(3)
                for name in [raw_name1, raw_name2]:
                    if name in names:
                        old_rank = ranks[names.index(name)]
                        if old_rank > int(new_rank):
                            ranks[names.index(name)] = int(new_rank)
                    else:
                        names.append(name)
                        ranks.append(int(new_rank))
    name_rank_tuple = sorted(zip(names, ranks),key = operator.itemgetter(0))
    try:
        output = year +'\n'+'\n'.join([' '.join([i[0], str(i[1])]) for i in name_rank_tuple])
        print(year)
    except TypeError:
        output = '2008' +'\n'+'\n'.join([' '.join([i[0], str(i[1])]) for i in name_rank_tuple])

    return output
def main1(f_n):
    extract_names(f_n)



def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':

    summary = True

    del args[0]
    print(args)
    for file_name in args:
        summary_output = codecs.open(file_name+'.summary','w', encoding='utf-8')
        summary = extract_names(file_name)
        summary_output.write(summary)
        summary_output.close()
    print('\n'*3)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  file_name = 'baby2008.html'
  #main1(file_name)
  main()
