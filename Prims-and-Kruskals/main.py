import sys
import kruskals
import prims
import glb
import time

start = time.time()
def usage():
    print("USAGE: main.py [\"inputfile.txt\"] [selectedAlgo] where p = prims , k = kruskals")
    sys.exit()

def main():
    # if len(sys.argv) < 3:
    #     usage()
    inputfile = sys.argv[1]
    prefDelimiter = '\t'
    selectedAlgo = sys.argv[2]
    if(selectedAlgo == 'p'):
        #prims
        prims.read_graph(inputfile, prefDelimiter)
        graph,tdist = prims.prims()
        glb.print_pretty()
        print(f"Total Distance of the graph : {tdist}")
    elif(selectedAlgo == 'k'):
        #kruskals
        kruskals.read_graph(inputfile, prefDelimiter)
        graph,tdist = kruskals.kruskals()
        glb.print_pretty()
        print(f"Total Distance of the graph : {tdist}")
    else:
        usage()

if __name__ == "__main__":
    main()
    
    end = time.time()
print(end - start)





