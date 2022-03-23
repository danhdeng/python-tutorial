# With Python, we can interact with file on the filesystem,
# including reading, writng, creating, and deleting files
# we should always be careful when working with files. so 
# as not to destroy data

# Use Context managers to open files
# here we use a context manager to open and close
# the text file, and readlines() to get the list of lines
# from the file to loop over

with open('./sample_data/book.txt','r') as f:
    data=f.readlines()
    # print(data)
    # print(len(data))
    for line in data:
        #lowercase all words and split on whitespace
        # to form a list of word token
        clean_line=line.lower().split()
        # print(clean_line)
        #check the sentences that contain 'elizabeth' and 'darcy'
        if{'elizabeth', 'darcy'}.issubset(set(clean_line)):
            print(line)