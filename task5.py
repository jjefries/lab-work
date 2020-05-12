# This is fifth task

def sed(file_name_1, file_name_2):
  with open(file_name_1, mode='r') as f1:
    with open(file_name_2, mode='w') as f2:
      for line in f1:
        f1.readline()
        for line_1 in f2:
          f2.write(line_1)
try:
  print("Successfully copied the contents from one file to another")
except FileNotFoundError:
  print("File is not found. Therefore cannot copy the contents or read the contents")

sed(r"/content/text1.txt", r"/content/text.txt")
