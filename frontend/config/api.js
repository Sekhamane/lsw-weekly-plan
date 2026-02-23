// API Configuration
// This file configures the backend API URL for different environments

const API_BASE_URL = process.env.REACT_APP_API_URL || 
  (process.env.NODE_ENV === 'production' 
    ? 'https://lsw-api.up.railway.app'  // Production Railway URL
    : 'http://localhost:8000');           // Local development

export default API_BASE_URL;

console.log(`[API Config] Using API_URL: ${API_BASE_URL}`);
