import zipfile, hashlib, io, subprocess, sys
T={"22ca9931e0799e3285ac802f65677bc0859790acb9081b65addc340477f60a90":"C4 v2","a845053fd43af7a5642ae5287b2a1c762a83446867de8652f6dceae071358fe9":"C4 v1"}
def walk(name, data, depth=0, out=None):
    try: z=zipfile.ZipFile(io.BytesIO(data))
    except Exception as e: print("  "*depth+f"[not a readable zip] {name}: {e}"); return
    for i in z.infolist():
        if i.is_dir(): continue
        b=z.read(i); h=hashlib.sha256(b).hexdigest()
        flag = f"  <<< HIT {T[h]}" if h in T else ""
        nm=i.filename
        if any(k in nm.lower() for k in ("wave3","context-model","context-v2")) or flag: print("  "*depth+f"{name} :: {nm} {h[:16]} {len(b)}{flag}")
        if nm.lower().endswith(".zip"): walk(name+"::"+nm,b,depth+1)
    print("  "*depth+f"scanned {name}: {len(z.infolist())} members")
zips=subprocess.run(["git","-C","aios","ls-tree","-r","--name-only","origin/main"],capture_output=True,text=True).stdout.splitlines()
for p in [z for z in zips if z.lower().endswith(".zip")]:
    d=subprocess.run(["git","-C","aios","show","origin/main:"+p],capture_output=True).stdout
    walk(p,d)
