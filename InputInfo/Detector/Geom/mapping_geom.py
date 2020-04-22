import re

def get_geometry(input_file, output_file):
    fin = open(input_file,"r")
    fout = open(output_file,"w")
    lines = fin.readlines()
    # map_name_pos = {}
    fout.write("######\n")
    fout.write("name_pos_map = {\n")
    for l in lines:
        s1 = re.findall('FPix_B[m,p][I,O]_D.*_BLD.*_PNL.*_RNG.* r/phi/z = .*/.*/.* cmssw',l)
        if len(s1) != 0:
            s1 = s1[0]
            s1 = s1.split(' ')
            name_m = s1[0]
            pos_m = map(float,s1[3].split('/'))
            fout.write("'%s': %s,\n"%(name_m,str(pos_m)))
            # map_name_pos[name_m] = pos_m
    fout.write("}")


input_file = "SiPixelDetsUpdatedAfterFlippedChange.txt"
output_file = "SiPixelDetsUpdatedAfterFlippedChange.py"

get_geometry(input_file,output_file)