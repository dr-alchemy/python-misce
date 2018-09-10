fout=open("out.csv","a")

# first file:
for line in open("101.csv"):
    fout.write(line)

# now the rest:
flist = ['102', '103']

for f in flist:
    f = open(f + ".csv")
    f.next() # skip the header

    for line in f:
         fout.write(line)

    f.close() # not really needed

fout.close()