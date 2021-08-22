'''Utility x Audacity: trasforma lo spettro di un wavefile in un preset per l'effetto FilterCurve'''

infile = input("File spettro: ")
outfile = str(infile[:infile.rfind('.')])+"_eq.txt"

f=[]
v=[]

try:
    with open(infile) as file:
        for line in file.readlines()[1:]: # Salta linea di intestazione
            fields = line.split()
            f.append(fields[0])
            v.append(fields[1])
    outstring = "FilterCurve:"
    for (n,freq) in enumerate(f):
        outstring=outstring+'f'+str(n)+'="'+str(freq)+'" '
    outstring=outstring+'FilterLength="8191" InterpolateLin="0" InterpolationMethod="B-spline" '
    for (n,val) in enumerate(v):
        outstring=outstring+'v'+str(n)+'="'+str(val)+'" '        
except:
    print("File non trovato")
    exit()

with open(outfile, 'w') as fout:
    fout.write(outstring)

