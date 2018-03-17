log_file = open('vagrant-log.txt', 'r')

min_count = {}

def write_csv(key, value):
  with open('my.csv', "a") as outfile:
    outfile.write(str("{0},{1}".format(key, value)))
    outfile.write('\n')

def split_lines(line):
  words = line.split(":")
  if words[0] != '\n':
    key = "{0}:{1}".format(words[0], words[1])
    if key not in min_count:
      min_count[key] = 1
    else:
      min_count[key] += 1
  else:
      print("Line is empty")

def read_lines(filename):
  for line in filename:
    split_lines(line)

def messages_per_min(dictionary):
  for key, value in dictionary.items():
    write_csv(key, value)


read_lines(log_file)
messages_per_min(min_count)
log_file.close()
