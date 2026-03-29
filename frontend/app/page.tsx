"use client";
import { useState } from "react";

export default function Home() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const uploadAPK = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);

    const res = await fetch("http://localhost:8000/upload-apk", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult({ ...data.risk, filename: file.name });

    setLoading(false);
  };

  return (
    <div style={{background:"#0d1117",color:"white",minHeight:"100vh",padding:"40px"}}>
      <h1 style={{textAlign:"center"}}>ThreatLens AI Scanner</h1>

      <div style={{textAlign:"center",margin:"40px"}}>
        <input type="file" onChange={uploadAPK}/>
      </div>

      {loading && <p style={{textAlign:"center"}}>Scanning...</p>}

      {result && (
        <div style={{maxWidth:"600px",margin:"auto"}}>
          
          <div style={{background:"#161b22",padding:"20px",marginBottom:"10px"}}>
            <h3>{result.filename}</h3>
            <p>Score: {result.score}/100</p>
          </div>

          <div style={{background:"#161b22",padding:"20px",marginBottom:"10px"}}>
            <p>Risk: {result.risk}</p>
            <div style={{background:"#333",height:"10px"}}>
              <div style={{
                width: result.score + "%",
                height:"10px",
                background: result.risk==="HIGH"?"red":result.risk==="MEDIUM"?"orange":"green"
              }} />
            </div>
          </div>

          <div style={{background:"#161b22",padding:"20px"}}>
            <h3>Findings</h3>
            <ul>
              {result.findings.map((f,i)=><li key={i}>{f}</li>)}
            </ul>
          </div>

        </div>
      )}
    </div>
  );
}
