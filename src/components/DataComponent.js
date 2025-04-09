// src/components/DataComponent.js
import React, { useEffect, useState } from 'react';
import { fetchData } from '../apiService';

const DataComponent = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const getData = async () => {
      try {
        const result = await fetchData();
        setData(result);
      } catch (error) {
        console.error('Error loading data:', error);
      }
    };

    getData();
  }, []);

  return (
    <div>
      <h1>Data from Backend</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default DataComponent;
