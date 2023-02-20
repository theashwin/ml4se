import csv
import json
import sys
import os

class JavaRSExtractor:

    def __init__(self, filename):
        self.rs = []
        try:
            with open(filename, mode='r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')

                # This statement is used to skip the header row
                # next(csv_reader, None)

                for line in csv_reader:
                    self.rs.append(line)

        except IOError:
            print(f'IOError')
            sys.exit(0)

    def generateControlFlowGraph(self):
      # Class Name, function name, line number, if block, parent
        hmap = {}
        for idx, row in enumerate(self.rs):
            s_idx = str(idx)
            key = row[0]+row[1]
            edges = hmap.get(key, [])

            if len(edges) == 0:
                edges.append('s -> if'+s_idx)
                edges.append('if'+s_idx+' -> m' + s_idx)
                edges.append('if'+s_idx+' -> block'+s_idx)
                edges.append('block'+s_idx+' -> m'+s_idx)
            else:
                if 'if' in row[4] or 'for' in row[4]:
                    n = len(edges)
                    prev_idx = 0
                    for i in range(len(edges)):
                        if "block" in edges[i]:
                            x = edges[i].split(" -> ")

                            if "block" in x[0]:
                                prev_idx = x[0].replace("block", "")
                            else:
                                prev_idx = x[1].replace("block", "")
                    del_idx = []
                    for i in range(len(edges)):
                        if "block"+prev_idx in edges[i]:
                            del_idx.append(i)

                    # Remove the prev block edges that need to be updated
                    edges = [i for j, i in enumerate(edges) if j not in del_idx]

                    edges.append('if'+prev_idx+' -> if'+s_idx)
                    edges.append('if'+s_idx+' -> m'+s_idx)
                    edges.append('if'+s_idx+' -> block'+s_idx)
                    edges.append('block'+s_idx+' -> m'+s_idx)
                    edges.append('m'+s_idx+' -> m'+prev_idx)
                else:
                    prev_idx = edges[-1].split(' -> ')[0].replace('if', '').replace('m', '').replace('block', '')
                    edges.append('m'+prev_idx+' -> if'+s_idx)
                    edges.append('if'+s_idx+' -> m'+s_idx)
                    edges.append('if'+s_idx+' -> block'+s_idx)
                    edges.append('block'+s_idx+' -> m'+s_idx)

            hmap[key] = edges

        print(hmap['HazelcastManifestTransformeroverridePackageDefinitionResolution'])

        # OUTPUT_PATH = ''
        for k, v in hmap.items():

            last_node = v[-1].split(" -> ")[1]
            # v.append(last_node + " -> e" )
            os.system("echo 'digraph { " + "; ".join(v) + " }' | dot -Tsvg > "+k+".svg")


if __name__ == '__main__':
    jrx = JavaRSExtractor('<PATH_TO_CSV_DATA>/control-flow.csv')
    jrx.generateControlFlowGraph()
