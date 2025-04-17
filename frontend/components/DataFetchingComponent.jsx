import { useState, useEffect } from 'react';
import Loader from './Loader';

const DataFetchingComponent = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    fetch('/api/predict', { method: 'POST' })
      .then(res => res.json())
      .then(data => {
        setData(data);
        setLoading(false);
      });
  }, []);

  if (loading) return <Loader />;
  return <div>{/* Render your data here */}</div>;
};

export default DataFetchingComponent;
