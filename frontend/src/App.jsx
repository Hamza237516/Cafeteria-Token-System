import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import StudentDashboard from './pages/StudentDashboard'; // Add this import!

function App() {
  return (
    <Router>
      <div style={{ padding: '20px', fontFamily: 'sans-serif', maxWidth: '600px', margin: '0 auto' }}>
        <header style={{ borderBottom: '1px solid #ccc', paddingBottom: '10px', marginBottom: '20px' }}>
          <h1>Cafeteria Token System</h1>
        </header>
        
        <Routes>
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/login" element={<Login />} />
          {/* Add the new student route below! */}
          <Route path="/student" element={<StudentDashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;