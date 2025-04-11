import { useState } from 'react';
import axios from 'axios';

const usePrediction = (endpoint) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchPrediction = async (formData) => {
    setLoading(true);
    try {
      const response = await axios.post(endpoint, formData, {
        headers: { 'x-api-key': process.env.REACT_APP_API_KEY },
      });
      setData(response.data);
      setError(null);
    } catch (err) {
      setError(err.response?.data || 'Server Error');
      setData(null);
    } finally {
      setLoading(false);
    }
  };

  return { data, loading, error, fetchPrediction };
};

export default usePrediction;
