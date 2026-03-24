import React, { useState } from 'react';

function CommandInput({ onSubmit, loading, onHistory }) {
  const [message, setMessage] = useState('');

  const handleSubmit = () => {
    if (!message.trim() || loading) return;
    onSubmit(message.trim());
    setMessage('');
  };

  if (loading) {
    return (
      <div className="command-section">
        <div className="loading">
          <p>팀이 작업 중입니다<span className="dots"></span></p>
          <p style={{ fontSize: 13, color: '#666', marginTop: 12 }}>
            팀장이 명령을 분석하고 팀원들에게 배분 중...
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="command-section">
      <textarea
        className="command-input"
        placeholder="명령을 입력하세요&#10;&#10;예: 다음 주 마케팅 전략 보고서 작성해줘"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button className="btn btn-primary" onClick={handleSubmit} disabled={!message.trim()}>
        명령 내리기
      </button>
      <button className="btn btn-secondary" onClick={onHistory}>
        이전 명령 보기
      </button>
    </div>
  );
}

export default CommandInput;
