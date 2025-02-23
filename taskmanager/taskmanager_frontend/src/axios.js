import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

const token = localStorage.getItem('token');
const res = await axios.get('tasks/', {
  headers: { Authorization: `Bearer ${token}` },
});


export default instance;
