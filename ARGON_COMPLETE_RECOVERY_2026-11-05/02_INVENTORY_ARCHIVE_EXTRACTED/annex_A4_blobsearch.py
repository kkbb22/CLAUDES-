import subprocess, hashlib, sys, json
targets = {
 "22ca9931e0799e3285ac802f65677bc0859790acb9081b65addc340477f60a90":"C4 Wave3.5 v2 (manifest-declared)",
 "a845053fd43af7a5642ae5287b2a1c762a83446867de8652f6dceae071358fe9":"C4 Wave3.5 v1 superseded (manifest-declared)",
}
for repo in sys.argv[1:]:
    p = subprocess.run(["git","-C",repo,"cat-file","--batch-all-objects","--batch-check=%(objectname) %(objecttype) %(objectsize)"],capture_output=True,text=True)
    blobs=[l.split() for l in p.stdout.splitlines() if l.split()[1]=="blob"]
    allobjs=len(p.stdout.splitlines())
    hits=[]
    proc = subprocess.Popen(["git","-C",repo,"cat-file","--batch"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    for oid,t,sz in blobs:
        proc.stdin.write((oid+"\n").encode()); proc.stdin.flush()
        hdr=proc.stdout.readline().split()
        n=int(hdr[2]); data=proc.stdout.read(n); proc.stdout.read(1)
        h=hashlib.sha256(data).hexdigest()
        if h in targets: hits.append((oid,h,targets[h]))
    proc.stdin.close()
    print(repo, "objects:",allobjs,"blobs hashed:",len(blobs),"hits:",hits)
