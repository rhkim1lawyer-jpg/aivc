import React from 'react';

function History({ items, onBack, onSelect }) {
  return (
    <div className="result-section">
      <button className="back-btn" onClick={onBack}>← 돌아가기</button>
      <h3 style={{ fontSize: 14, color: '#888', marginBottom: 12 }}>명령 히스토리</h3>

      {items.length === 0 && (
        <p style={{ color: '#555', textAlign: 'center', padding: 40 }}>
          아직 내린 명령이 없습니다
        </p>
      )}

      {items.map((item) => (
        <div key={item.id} className="history-item" onClick={() => onSelect(item)}>
          <div className="msg">{item.message}</div>
          <div className="meta">
            {new Date(item.created_at).toLocaleString('ko-KR')} · {item.status}
          </div>
        </div>
      ))}
    </div>
  );
}

export default History;
