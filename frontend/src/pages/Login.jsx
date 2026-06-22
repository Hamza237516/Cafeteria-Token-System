import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

export default function Login() {
  const [rollNumber, setRollNumber] = useState('');
  const [password, setPassword] = useState(''); // We collect it but won't strictly verify it for this simplified demo
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');

    try {
      // In a real app, we'd hit a dedicated /login endpoint. 
      // For this demo, we will try to register the user. If they exist, 
      // the backend throws a 400 error which we catch below.
      const response = await axios.post('http://127.0.0.1:8000/api/users/', {
        name: "Student", // Default name if creating a new user
        roll_number: rollNumber,
        password: password,
        role: "student"
      });

      // If successful (new user created), save ID and redirect
      localStorage.setItem('userId', response.data.id);
      localStorage.setItem('userRole', response.data.role);
      navigate('/student');

    } catch (err) {
        // If the user already exists (Roll number taken), our backend returns a 400 error.
        // We will simulate a "login" by just accepting that they exist for this portfolio project.
        if (err.response && err.response.status === 400) {
            // Note: In a production app, you would verify the password here.
            // For now, we are bypassing strict auth to focus on the core token logic.
            localStorage.setItem('userRollNumber', rollNumber);
            localStorage.setItem('userRole', 'student'); // Defaulting to student for testing
            navigate('/student');
        } else {
            setError("Something went wrong connecting to the server.");
        }
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '50px auto', textAlign: 'center' }}>
      <h2>Sign In</h2>
      <p style={{ color: 'gray', marginBottom: '20px' }}>Enter your Roll Number to access the portal.</p>
      
      <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        <input 
          type="text" 
          placeholder="Roll Number (e.g., CS101)" 
          value={rollNumber}
          onChange={(e) => setRollNumber(e.target.value)}
          required
          style={{ padding: '10px', fontSize: '16px', borderRadius: '5px', border: '1px solid #ccc' }}
        />
        <input 
          type="password" 
          placeholder="Password" 
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          style={{ padding: '10px', fontSize: '16px', borderRadius: '5px', border: '1px solid #ccc' }}
        />
        
        {error && <p style={{ color: 'red', margin: '0' }}>{error}</p>}

        <button 
          type="submit" 
          style={{ 
            padding: '12px', 
            fontSize: '16px', 
            backgroundColor: '#007BFF', 
            color: 'white', 
            border: 'none', 
            borderRadius: '5px',
            cursor: 'pointer'
          }}
        >
          Login
        </button>
      </form>
    </div>
  );
}