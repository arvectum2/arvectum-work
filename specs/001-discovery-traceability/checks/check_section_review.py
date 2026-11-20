"""Pinned source review; structural only, not product acceptance or task admission."""
import hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
DIR="specs/001-discovery-traceability"
PIN="00d478dac8e66b2ed08aaa7d74dbaf5b818f1cd0"
PRIOR="365c2e293bd0ad741dee42b58297b4257b3a5c13"
MODE="discovery_only"
SOURCES=json.loads("[{\"path\":\"docs/roadmap/ROADMAP.md\",\"sha256\":\"b0d7855b98ce72874db97a90d1509a76492868a0a089def39399f1bc306afce2\"},{\"path\":\"docs/discovery/AW-020-C2-FOCUSED-BUYER-VALIDATION-PLAN.md\",\"sha256\":\"5144b60b238690cc0b7dd62502e39efb53eb353fd885ae8e0f752499eb28a85c\"}]")
GATES=json.loads("[{\"id\":\"REVIEW-01\",\"source\":\"docs/roadmap/ROADMAP.md\",\"first_line\":195,\"last_line\":217,\"label\":\"AW-020 evidence and GO\",\"rule\":\"Original buyer evidence and economics; no GO by synthetic demo.\"},{\"id\":\"REVIEW-02\",\"source\":\"docs/roadmap/ROADMAP.md\",\"first_line\":284,\"last_line\":319,\"label\":\"AW-060/100/200\",\"rule\":\"GO/Pivot/Stop and separate MVP admission remain distinct.\"},{\"id\":\"REVIEW-03\",\"source\":\"docs/discovery/AW-020-C2-FOCUSED-BUYER-VALIDATION-PLAN.md\",\"first_line\":200,\"last_line\":214,\"label\":\"AW-020-C2 next internal actions\",\"rule\":\"Detailed plan admits internal preparation; roadmap line 189 has older deferred status, reconcile explicitly. Stop before outbound send.\"}]")
def scan(raw):
    out=[];heading=0;fence=False
    for i,l in enumerate(raw.decode("utf-8").splitlines(),1):
        if not l.strip():continue
        if l.lstrip().startswith(("\x60\x60\x60","~~~")):
            fence=not fence;kind="format"
        elif fence:kind="code"
        elif re.match(r"^#{1,6}\s",l):heading=i;kind="heading"
        elif re.fullmatch(r"\s*\|?\s*[:\-]+(?:\s*\|\s*[:\-]+)+\s*\|?\s*",l) or re.fullmatch(r"\s*[-*_]{3,}\s*",l):kind="format"
        elif re.match(r"^\s*\|",l):kind="table"
        elif re.match(r"^\s*(?:[-*+]|\d+[.)])\s+",l):kind="list"
        else:kind="prose"
        out.append([i,heading,kind])
    return out
def validate(data,original,prior,current):
    errors=[]
    if data.get("schema")!="arvectum.source-section-review/1" or data.get("source_commit")!=PIN or data.get("review_baseline")!=PRIOR or data.get("mode")!=MODE or data.get("actual_acceptance_verified") is not False or data.get("execution_authorized") is not False:errors.append("scope/authority")
    if data.get("gates") is None: return errors+["missing gates"]
    src=data.get("sources",[]);paths=[s["path"] for s in src]
    if paths!=[s["path"] for s in SOURCES]:return errors+["source coverage"]
    for a,s in zip(src,SOURCES):
        p=s["path"];b=original[p]
        if hashlib.sha256(b).hexdigest()!=s["sha256"] or a.get("sha256")!=s["sha256"]:errors.append("source hash "+p)
        if not prior[p].startswith(b) or prior[p]!=current[p]:errors.append("unreviewed source change "+p)
        if a.get("rows")!=scan(b):errors.append("line/heading coverage "+p)
    rows=data["gates"]
    if len(rows)!=len(GATES):errors.append("gate coverage")
    for row,g in zip(rows,GATES):
        if any(row.get(k)!=v for k,v in g.items()):errors.append("gate identity/scope")
        if row.get("review_state") not in {"unverified","verified"}:errors.append("state")
        if row.get("review_state")=="verified":
            ev=row.get("evidence",[])
            if not ev or any(e.get("criterion")!=row["id"] or e.get("outcome")!="pass" or not re.fullmatch(r"[a-f0-9]{64}",e.get("artifact_sha256","")) or not e.get("receipt_ref") or not e.get("review_ref") for e in ev):errors.append("missing criterion-specific evidence "+row["id"])
    return errors
def inputs():
    def read(ref,p):return subprocess.check_output(["git","-C",str(ROOT),"show",ref+":"+p])
    original={s["path"]:read(PIN,s["path"]) for s in SOURCES}
    prior={p:read(PRIOR,p) for p in original}
    current={p:(ROOT/p).read_bytes() for p in original}
    return json.loads((ROOT/DIR/"section-review.json").read_text()),original,prior,current
if __name__=="__main__":
    errors=validate(*inputs())
    if errors:raise SystemExit("\n".join(errors))
    print("Structural source/section coverage PASS; no actual acceptance or authority.")
