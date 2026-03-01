
import React, { useEffect, useState } from "react";

function Dashboard() {
  const [usageData, setUsageData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/get_usage")
      .then(res => res.json())
      .then(data => setUsageData(data));
  }, []);

  return (
    <div>
      <h2>Water Usage Records</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Apartment</th>
            <th>Usage (Liters)</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {usageData.map((item, index) => (
            <tr key={index}>
              <td>{item.apartment_no}</td>
              <td>{item.usage_liters}</td>
              <td>{item.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;
