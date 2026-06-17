import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api';

const apiClient = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const registerUser = async (userData) => {
    const response = await apiClient.post('/users/', userData);
    return response.data;
};

export const getMenu = async () => {
    const response = await apiClient.get('/meals/');
    return response.data;
};

export const generateToken = async (tokenData) => {
    const response = await apiClient.post('/tokens/', tokenData);
    return response.data;
};

export const scanToken = async (tokenId) => {
    const response = await apiClient.put(`/tokens/${tokenId}/scan`);
    return response.data;
};

export default apiClient;