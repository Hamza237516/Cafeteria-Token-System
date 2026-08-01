import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { QRCodeCanvas } from 'qrcode.react'; // This draws the QR code
import { generateToken } from '../api/api';

export default function StudentDashboard() {
  const [tokenId, setTokenId] = useState(null);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  // Retrieve the user info we saved during login
  const userId = localStorage.getItem('userId');
  const rollNumber = localStorage.getItem('userRollNumber') || 'Student';

  const handleBookMeal = async () => {
    setError('');
    try {
      // For this demo, we will hardcode meal_id as 1 (e.g., "Today's Lunch")
      // In a full app, the user would select a meal from a dropdown.
      const response = await generateToken({ 
        user_id: parseInt(userId) || 1, 
        meal_id: 1 
      });
      
      // The backend returns a UUID string, which we save to state
      setTokenId(response.id); 
    } catch (err) {
      // If they try to book twice, our backend's double-booking protection will trigger this!
      setError(err.response?.data?.detail || "Failed to generate token.");
    }
  };

  const handleLogout = () => {
    localStorage.clear();
    navigate('/login');
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      <h2>Welcome, {rollNumber}!</h2>
      <p style={{ color: 'gray' }}>Book your meal token for today's lunch.</p>

      {/* If we have a token, show the QR Code. If not, show the Book button */}
      {tokenId ? (
        <div style={{ 
          marginTop: '30px', 
          padding: '20px', 
          border: '2px solid #4CAF50', 
          borderRadius: '10px',
          display: 'inline-block'
        }}>
          <h3 style={{ color: '#4CAF50', marginTop: 0 }}>Token Active</h3>
         <QRCodeCanvas value={tokenId} size={256} marginSize={4} />
          <p style={{ fontSize: '12px', color: 'gray', marginTop: '10px' }}>ID: {tokenId}</p>
        </div>
      ) : (
        <div style={{ marginTop: '30px' }}>
          <button 
            onClick={handleBookMeal}
            style={{ padding: '15px 30px', fontSize: '18px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}
          >
            Generate Meal Token
          </button>
        </div>
      )}

      {error && <p style={{ color: 'red', marginTop: '20px' }}>{error}</p>}

      <div style={{ marginTop: '50px' }}>
        <button 
          onClick={handleLogout}
          style={{ padding: '10px 20px', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}
        >
          Logout
        </button>
      </div>
    </div>
  );
}