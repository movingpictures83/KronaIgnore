import sys
import PyPluMA

class KronaIgnorePlugin:
    def input(self, filename):
        infile = open(filename, 'r')
        self.parameters = dict()
        for line in infile:
            line = line.strip()
            contents = line.split('\t')
            self.parameters[contents[0]] = contents[1]

        self.kronafile = open(PyPluMA.prefix()+"/"+self.parameters["kronafile"], 'r')
        self.patternfile = open(PyPluMA.prefix()+"/"+self.parameters["patternfile"], 'r')

    def run(self):
        self.patterns = []
        for line in self.patternfile:
           self.patterns.append(line.strip())

    def output(self, filename):
        outfile = open(filename, 'w')
        for line in self.kronafile:
            line = line.strip()
            flag = False
            for pattern in self.patterns:
                if pattern in line:
                    flag = True

            if (line.count(' ') != 1 and (not flag)):
               outfile.write(line+"\n")


