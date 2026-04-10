import React, { useState } from 'react';
import './App.css';

interface Skill {
  id: string;
  name: string;
  category: string;
  status: 'active' | 'pending' | 'error';
  hash: string;
}

const App: React.FC = () => {
  const [skills] = useState<Skill[]>([
    { id: '1', name: 'External Skill Retrieval', category: 'Orchestration', status: 'active', hash: 'sha256-bd43e3...' },
    { id: '2', name: 'Parallel Agent Dispatcher', category: 'Orchestration', status: 'active', hash: 'sha256-a9f21d...' },
    { id: '3', name: 'CodeRabbit Reviewer', category: 'Quality', status: 'active', hash: 'sha256-7f8e9a...' },
    { id: '4', name: 'Security Auditor', category: 'Security', status: 'active', hash: 'sha256-2c3d4e...' },
    { id: '5', name: 'Memory Cycle', category: 'Core', status: 'pending', hash: 'sha256-5f6g7h...' },
  ]);

  return (
    <div className="dashboard-container">
      <aside className="sidebar">
        <div>
          <h2>Smart Library</h2>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>v2.2.7 | Hardened</p>
        </div>
        <nav style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <button className="nav-btn active">Skill Health</button>
          <button className="nav-btn">Security Audit</button>
          <button className="nav-btn">Activity Log</button>
        </nav>
      </aside>

      <main className="main-content">
        <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
          <h1>Skill Health Dashboard</h1>
          <div className="status-badge status-active">System: Optimal</div>
        </header>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '1.5rem' }}>
          {skills.map(skill => (
            <div key={skill.id} className="card">
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1rem' }}>
                <h3 style={{ margin: 0 }}>{skill.name}</h3>
                <span className={`status-badge status-${skill.status}`}>{skill.status}</span>
              </div>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem', marginBottom: '1rem' }}>
                Category: <strong>{skill.category}</strong>
              </p>
              <div style={{ background: 'rgba(0,0,0,0.2)', padding: '0.5rem', borderRadius: '8px', fontSize: '0.75rem', fontFamily: 'monospace' }}>
                Hash: {skill.hash}
              </div>
            </div>
          ))}
        </div>

        <section style={{ marginTop: '3rem' }}>
          <h2>🛡️ Security Overview</h2>
          <div className="card" style={{ borderLeft: '4px solid var(--accent-blue)' }}>
            <p><strong>SHA-256 Enforcement:</strong> Active</p>
            <p><strong>Mandatory Audits:</strong> Required for all external fetch events.</p>
            <p style={{ color: 'var(--success)', marginTop: '0.5rem' }}>✓ All local skills pass integrity check.</p>
          </div>
        </section>
      </main>
    </div>
  );
};

export default App;
