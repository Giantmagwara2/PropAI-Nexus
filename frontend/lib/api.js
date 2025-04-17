// /frontend/lib/api.js

export const fetchWithApiKey = async (url) => {
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${process.env.REACT_APP_API_KEY}`,
      },
    });
  
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    return response;
  };
  