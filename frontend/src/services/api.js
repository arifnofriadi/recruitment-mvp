import axios from 'axios';

// Create axios instance with baseURL
const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000/api', // URL backend Flask
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
  // Function to get candidates
  getCandidates() {
    return apiClient.get('/candidates');
  },
  // Function to get clients
  getClients() {
    return apiClient.get('/clients');
  },
  // Create a new candidate
  createCandidate(payload) {
    return apiClient.post('/candidates', payload);
  },
  // Update candidate
  updateCandidate(id, payload) {
    return apiClient.put(`/candidates/${id}`, payload);
  },
  // Delete candidate
  deleteCandidate(id) {
    return apiClient.delete(`/candidates/${id}`);
  },
  // You can add other functions here, for example:
  // updateCandidateFeedback(id, feedback) { ... }
};