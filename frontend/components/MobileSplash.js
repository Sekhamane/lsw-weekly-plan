import React from "react";

export default function MobileSplash() {
  return (
    <div style={{
      minHeight: "100vh",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      background: "#F8F5F0"
    }}>
      <img src="https://leathersoleworks.co.ls/kemeli_logo.png" alt="Leather Sole Works Logo" width={120} height={120} />
      <h1 style={{ color: "#4B2E19", margin: 16 }}>Leather Sole Works</h1>
      <p style={{ color: "#D4B06A" }}>Production Management System</p>
    </div>
  );
}
