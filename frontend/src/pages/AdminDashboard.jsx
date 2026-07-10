import React, { useState } from 'react';
import { Scanner } from '@yudiel/react-qr-scanner';
import { scanToken } from '../api/api';

export default function AdminDashboard() {
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleScan = async (text) => {
    if (text) {
      // 1. THIS LINE PROVES THE SCANNER WORKS
      console.log("✅ I successfully scanned a code! The ID is:", text); 
      
      try {
        const response = await scanToken(text);
        setMessage(`Success! Meal token verified and marked as used.`);
        setError('');
      } catch (err) {
        // 2. THIS LINE SHOWS US IF THE BACKEND REJECTED IT
        console.error("❌ Backend Error:", err); 
        setError(err.response?.data?.detail || "Invalid or already used token.");
        setMessage('');
      }
    }
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      <h2>Admin Scanner</h2>
      <p style={{ color: 'gray' }}>Point the camera at a student's QR code.</p>

      {/* The Webcam Scanner Box */}
      <div style={{ 
        maxWidth: '350px', 
        margin: '20px auto', 
        border: '4px solid #333', 
        borderRadius: '10px', 
        overflow: 'hidden' 
      }}>
        <Scanner onResult={(text) => handleScan(text)} />
      </div>

      {/* Status Messages */}
      {message && <p style={{ color: 'green', fontSize: '18px', fontWeight: 'bold' }}>{message}</p>}
      {error && <p style={{ color: 'red', fontSize: '18px', fontWeight: 'bold' }}>{error}</p>}
    </div>
  );
}