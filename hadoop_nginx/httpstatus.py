#!/usr/bin/env python

from mrjob.job import MRJob
from mrjob.job import MRStep
import re

class MRCounter(MRJob):
    def mapper(self,key,line):
        i = 0
        for httpcode in line.split():
            if i==8 and re.match(r"\d{1,3}",httpcode):
                print "--------------------------->",httpcode
                yield httpcode, 1
            i += 1
  
    def reducer(self,httpcode,occurrences):
        yield httpcode, sum(occurrences)
         
    def steps(self):
        return [MRStep(mapper=self.mapper),
                MRStep(reducer=self.reducer)]


if  __name__ =='__main__':
    MRCounter.run()
