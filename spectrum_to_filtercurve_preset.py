'''Utility for Audacity: trasforms the exported spectrum of a wavefile in a FilterCurve effect preset
v2: translated to english; can define inversion and dB gain; if infile has dot or comma as a decimal separator, values in outfile will follow the same scheme'''

tail = "_eq"
infile = input("Spectrum export file: ")
inv = input("Apply inversion [y/N]? ")
if str(inv).lower() == "y":
    tail = tail+"_inv"
    inv_factor = -1
    print("Inverted")
else:
    inv_factor = 1
    print("Not inverted")
db = input("Gain (dB) [0]: ")
try:
    db_factor = float(db)
    print("Gain applied "+str(db_factor)+" dB")
except:
    db_factor = float(0)
    print("Gain applied 0.0 dB")
tail=tail+"_"+str(db_factor)+"dB"
outfile = str(infile[:infile.rfind('.')])+tail+".txt"

f=[]
v=[]

try:
    with open(infile) as file:
        for line in file.readlines()[1:]: # Skip header line
            fields = line.split()
            comma = 1 if ',' in fields[1] else 0
            f.append(fields[0])
            v.append(float(fields[1].replace(",",".")))
    outstring = "FilterCurve:"
    for (n,freq) in enumerate(f):
        outstring = outstring+'f'+str(n)+'="'+str(freq)+'" '
    outstring = outstring+'FilterLength="8191" InterpolateLin="0" InterpolationMethod="B-spline" '
    for (n,val) in enumerate(v):
        val_out = str((inv_factor * val) + db_factor)
        if comma == 1:
            val_out.replace(".",",")
        outstring = outstring+'v'+str(n)+'="'+val_out+'" '        
except:
    print("File not found")
    exit()

with open(outfile, 'w') as fout:
    fout.write(outstring)

