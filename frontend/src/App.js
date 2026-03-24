import React, { useState, useEffect } from 'react';
import CommandInput from './components/CommandInput';
import CommandResult from './components/CommandResult';
import History from './components/History';
import './App.css';

const API = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

function App() {
  const [view, setView] = useState('home'); // home | result | history
  const [loading, setLoading] = useState(false);
  const [currentResult, setCurrentResult] = useState(null);
  const [history, setHistory] = useState([]);

  const sendCommand = async (message) => {
    setLoading(true);
    try {
      const res = await fetch(`${API}/commands`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message }),
      });
      const data = await res.json();
      setCurrentResult(data);
      setView('result');
    } catch (err) {
      alert('서버 연결 실패: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  const loadHistory = async () => {
    try {
      const res = await fetch(`${API}/commands`);
      const data = await res.json();
      setHistory(data);
      setView('history');
    } catch (err) {
      alert('히스토리 로딩 실패');
    }
  };

  return (
    <div className="app">
      <header className="header">
        <h1 onClick={() => setView('home')}>AIVC</h1>
        <span className="subtitle">AI Virtual Company</span>
      </header>

      {view === 'home' && (
        <CommandInput onSubmit={sendCommand} loading={loading} onHistory={loadHistory} />
      )}
      {view === 'result' && (
        <CommandResult result={currentResult} onBack={() => setView('home')} />
      )}
      {view === 'history' && (
        <History items={history} onBack={() => setView('home')} onSelect={(item) => { setCurrentResult(item); setView('result'); }} />
      )}
    </div>
  );
}

export default App;
