import React, { useState } from 'react';

function CommandResult({ result, onBack }) {
  const [expandedTask, setExpandedTask] = useState(null);

  if (!result) return null;

  return (
    <div className="result-section">
      <button className="back-btn" onClick={onBack}>← 새 명령</button>

      <div className="plan-box">
        <h3>실행 계획</h3>
        <p>{result.plan}</p>
      </div>

      <h3 style={{ fontSize: 14, color: '#888', marginBottom: 10 }}>
        팀원 작업 ({result.subtasks?.length || 0}건)
      </h3>

      {result.subtasks?.map((task, i) => (
        <div
          key={task.id || i}
          className="subtask"
          onClick={() => setExpandedTask(expandedTask === i ? null : i)}
          style={{ cursor: 'pointer' }}
        >
          <div className="subtask-header">
            <span className="subtask-title">{task.title}</span>
            <span className="subtask-badge">{task.assignee}</span>
          </div>
          {expandedTask === i && task.result && (
            <div className="subtask-result">{task.result}</div>
          )}
        </div>
      ))}

      {result.final_report && (
        <div className="report-box">
          <h3>최종 보고서</h3>
          <div className="report-content">{result.final_report}</div>
        </div>
      )}
    </div>
  );
}

export default CommandResult;
