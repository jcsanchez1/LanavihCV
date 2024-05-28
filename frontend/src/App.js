import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import './App.css';

function App() {
    const isAuthenticated = () => {
        // Aquí puedes añadir tu lógica para verificar si el usuario está autenticado
        // Por ejemplo, puedes verificar si hay un token en el localStorage o una sesión activa
        return !!sessionStorage.getItem('user');
    };

    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/login" element={<Login />} />
                    <Route 
                        path="/dashboard" 
                        element={
                            isAuthenticated() ? <Dashboard /> : <Navigate to="/login" />
                        }
                    />
                    <Route 
                        path="/" 
                        element={<Navigate to="/login" />} 
                    />
                </Routes>
            </div>
        </Router>
    );
}

export default App;

