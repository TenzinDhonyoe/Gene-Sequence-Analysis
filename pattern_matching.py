from math import log
def matches(target, pattern, limit):
    #limit is the allowed number of mismatches
    #pattern = consensus sequence, majority letters
    count = 0
    for i in range(len(target)):
        if target[i] != pattern[i]:
            count += 1
    return count <= limit
            
# result = matches('TGGAGG', 'AGGAGG', 1)
# print(result)

#important one captures the idea of what wer trying to do. Matches consensus seqquence
def findpattern(seq, pattern, start, end, incr, limit):
    for i in range(start, end, incr): #start where you want to look for the pattern, end is where you are gonna stop
        result = matches(seq[i:len(pattern)], pattern, limit)
        if result:
            return i
        else:
            return -1
            
# res = findpattern('ATTCATGGG', 'CAT', 0, 6, 1, 0) #should return the index of where it found the pattern

# for value in res:
#     print(value, end = ' ')

def findstop(seq, start, end, incr, minlength):
    for i in range(start, end, incr):
        target = seq[i: i+incr]
        if target == "TGA" or target == "TAG" or target == "TAA":
            length = i-start+3
            if length >= minlength:
                return i
    return -1

# resul = findstop('ATTCATGGGTTAG', 4, 12, 3, 90)
# print(resul)
        
def findshine(seq, atgpos, limit):
    return findpattern(seq, 'AGGAGG', atgpos-13, atgpos-8, 1, limit)

result = findshine('GGCCCAGGAGGATTCATGGGTTAG', 15, 1)
print(result)

def matchespromoter(seq, start, limit):
    target35 = seq[start: start+6]
    if not matches(target35, 'TTGACA', limit):
        return False
    #yes TTGACA is there
    for i in range(start+21, start+6+20, 1):
        target17 = seq[i: i+6]
        if matches(target17, 'TATAAT', limit):
            return True
    return False
    
def findpromoter(seq, shinepos, limit):
    for i in range(shinepos-500-32, shinepos-49-32, 1):
        if matchespromoter(seq, i, limit):
            return i
    return -1

def findgene(seq, start, minlength, limit):
    for i in range(start, len(seq)-minlength, 1):
        trip = seq[i:i+3]
        if trip == 'ATG':
            # Show the ATG and the preamble, should be 6 + 7 long, but let's show 15
            preamble = seq[i-15:i]
            print(f'ATG found at position: {i} {preamble} {seq[i:i+3]} ')
            # Have ATG
            atgpos = i
            stoppos = findstop(seq, atgpos, n, 3, minlength)
            if stoppos == -1 :
                print('----------------------stop no good')
            continue
            # Have ATG, STOP
            stop = seq[stoppos:stoppos+3]
            orflength = stoppos + 3 - atgpos
            print(f'STOP found at position: {stoppos} {stop} {orflength}')
            shinepos = findshine(seq, atgpos, limit)
            if shinepos == -1 :
                print('----------------------Shine no good')
            continue
            # Have Shine, ATG, STOP
            print(f'Shine found at position: {shinepos} {seq[shinepos:shinepos+6]}')
            promoterpos = findpromoter(seq, shinepos, limit + 1)
            # allowing 2 mismatches
            if promoterpos == -1 :
                print('----------------------Promoter no good')
            continue
            # Have Promoter, Shine, ATG, STOP, i.e., gene
            return(promoterpos, shinepos, atgpos, stoppos)
                
        