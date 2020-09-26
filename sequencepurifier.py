####### print("This program purifies the sequences. Some sequences have NNNNN, this program removes those sequences")#######
fileread=[]#This is an empty list which will be used to save sequences after splitting for \n
# filename=input("Enter the file name with its extension(.txt/.fasta). Remember to input a single line fasta file")#uncomment this line incase you want to input files after running the program
count=0#a counter which will incremented on every encounter of the no-base character & that will be used to check and print the purified sequences 
with open("test.txt","r") as file:#open and read the file that you wnat to check 
    read1=file.readlines()#all the lines are read one-by-one
for i in range(len(read1)):#loop iterating over the number of lines in the file
    nameseq=read1[i].split("\n")#each items in read1 list is split on the basis of \n and stored in nameseq
    fileread.append(nameseq[0])#each split element in read1 will be either a header or sequence as the first element in nameseq and \n as the second element.So, we capture only the first element
for i in range(len(fileread)):#Another loop over all the elements in the list fileread
    char=fileread[i].strip()#with this for loop we actually remove any whitespaces present before and after the elements
    if(">" in char):#we are checking for the headers in the element selected 'char'
        header=char#whichever element shows '>' mark it becomes the header
    else:#if you don't find '>' the nit's a sequence so we take that sequence in the else part 
        for every in char:#now every nucleotide in the element char is checked for 
            if (every!='A' and every!='T' and every!='G' and every!='C' ):#here, we have the test alphabets
                count=count+1#if the alphabets deviate from the above (A,T,G,C) the count increases by 1 
        if(count==0):#what happens when the count is Zero? It shows that only ATGC existed in the sequences
            with open("purified.txt","a") as file1:#so now we get the sequences printed: First we go with the header
                file1.write(header+"\n")#here, is the header
                file1.write(char+"\n")#next we go with the seqnece
    count=0#here we need to re-intialize the count