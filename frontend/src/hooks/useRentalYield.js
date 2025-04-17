// /frontend/src/hooks/useRentalYield.js
import { useState } from 'react';
import axios from 'axios';

const useRentalYield = (endpoint) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchRentalYield = async (formData) => {
    setLoading(true);
    try {
      const response = await axios.post(endpoint, formData, {
        headers: {
          'x-api-key': process.env.REACT_APP_API_KEY,
          'Content-Type': 'application/json',
        },
      });
      setData(response.data);
      setError(null);
    } catch (err) {
      console.error('Rental Yield API Error:', err);
      setError(err.response?.data?.detail || 'Server Error');
      setData(null);
    } finally {
      setLoading(false);
    }
  };

  return { data, loading, error, fetchRentalYield };
};

export default useRentalYield;
