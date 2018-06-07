from utils.arguments import Arguments

def main():
  args = Arguments()
  print(args.file())
  print("verbose=%s" %(str(args.verbose())))
  return 0

if __name__ == '__main__':
  main()