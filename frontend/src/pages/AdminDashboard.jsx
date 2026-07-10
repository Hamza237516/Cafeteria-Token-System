import React, { useState } from 'react';
import { Scanner } from '@yudiel/react-qr-scanner';
import { scanToken } from '../api/api';

export default function AdminDashboard() {
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleScan = async (text) => {
    // This stops the scanner from firing a hundred times a second
    if (text) {
      try {
        // Send the scanned text (the UUID) to our Python backend
        const response = await scanToken(text);
        setMessage(`Success! Meal token verified and marked as used.`);
        setError('');
      } catch (err) {
        // If the backend says the token is invalid or already used
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