import React, { useEffect, useState } from 'react';

const Users = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/users/`
    : 'http://localhost:8000/api/users/';
  const [data, setData] = useState([]);

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Fetched users:', results);
      });
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <ul className="list-group">
        {data.map((u, i) => (
          <li key={i} className="list-group-item">
            {u.name} ({u.email}) - Team: {u.team}
          </li>
        ))}
      </ul>
    </div>
  );
};
export default Users;
