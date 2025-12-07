import React, { useEffect, useState } from 'react';

const Activities = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : 'http://localhost:8000/api/activities/';
  const [data, setData] = useState([]);

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Fetched activities:', results);
      });
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2>Activities</h2>
      <ul className="list-group">
        {data.map((a, i) => (
          <li key={i} className="list-group-item">
            {a.type} - {a.duration} min - {a.points} pts
          </li>
        ))}
      </ul>
    </div>
  );
};
export default Activities;
