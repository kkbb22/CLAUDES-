import subprocess, hashlib, sys, csv
repo, ref, out = sys.argv[1:4]
paths = subprocess.run(["git","-C",repo,"ls-tree","-r","-z","--long",ref],capture_output=True).stdout.split(b"\0")
rows=[]
for e in paths:
    if not e: continue
    meta,path=e.split(b"\t",1)
    mode,typ,blob,size=meta.split()
    data=subprocess.run(["git","-C",repo,"cat-file","blob",blob.decode()],capture_output=True).stdout
    rows.append([path.decode('utf-8','replace'),mode.decode(),blob.decode(),hashlib.sha256(data).hexdigest(),len(data)])
with open(out,"w",newline="") as f:
    w=csv.writer(f); w.writerow(["path","mode","git_blob_sha1","sha256","bytes"]); w.writerows(rows)
print(out,len(rows),"files")
