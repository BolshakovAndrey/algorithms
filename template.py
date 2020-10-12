infilename = 'input.txt'
outfilename = 'output.txt'
infile = open(infilename)
outfile = open(outfilename, 'w')

linenum = 0
edges = 0
N = - 1
graph = {}
for line in infile:
    inputs = line.split()

    if linenum == 0:
        N = int(inputs[0])
    else:
        string = inputs[0]
        k = len(string) - 2
        for i in range(k):
            if i == 0:
                prev_word = string[0:3]
            else:
                cur_word = string[i:i + 3]
                if prev_word in graph:
                    if cur_word in graph[prev_word]:
                        graph[prev_word][cur_word] += 1
                    else:
                        graph[prev_word][cur_word] = 1
                        edges += 1
                else:
                    graph[prev_word] = {cur_word: 1}
                    edges += 1
                prev_word = cur_word
                if i == k - 1 and cur_word not in graph:
                    graph[cur_word] = {}

    linenum += 1
    if linenum > N:
        break

vert = len(graph)

outfile.write(str(vert) + '\n')
outfile.write(str(edges) + '\n')
for prev_word in graph:
    for cur_word in graph[prev_word]:
        outfile.write(prev_word + ' ' + cur_word + ' ' + str(graph[prev_word][cur_word]) + '\n')

outfile.close()
infile.close()