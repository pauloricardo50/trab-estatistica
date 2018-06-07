import argparse
import os.path as path

class Arguments:

  # Constructor
  def __init__(self):
    self._parser = argparse.ArgumentParser()
    self._parser.add_argument("file", help="data base file csv")
    self._parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    self._parsed = False
  #-

  # Get the file argument
  def file(self):
    file = self._getParsed().file
    if not path.isfile(file):
      if self.verbose():
        print("\n\tfile argument: %s\n" %(str(file)))
      self._parser.error("the file you entered does not exist")
    return file
  #-

  def verbose(self):
    return self._getParsed().verbose
  #-

  # Get parsed arguments
  def _getParsed(self):
    if (not self._parsed):
      self._args = self._parser.parse_args()
      self._parsed = True
    return self._args
  #-

