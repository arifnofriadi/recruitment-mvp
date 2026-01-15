<template>
  <div id="app">
    <header class="app-header">
      <div class="header-inner">
        <h1>Recruitment Dashboard</h1>
        <nav>
          <a href="#">Home</a>
          <a href="#">Candidates</a>
          <a href="#">Clients</a>
        </nav>
      </div>
    </header>

    <main class="dashboard">
      <aside class="list-panel">
        <CandidateList 
          :candidates="candidates" 
          :selected-candidate="selectedCandidate"
          @select="selectCandidate" 
          @edit="openEditForm"
          @delete="handleDelete"
          @create="openCreateForm"
        />
        <ClientList 
          :clients="clients"
          :selected-client="selectedClient"
          @select="selectClient"
        />
      </aside>

      <DetailPanel 
        :selected-candidate="selectedCandidate"
        :selected-client="selectedClient"
      />
    </main>

    <footer class="app-footer">
      <div>© 2026 Recruitment MVP — Minimal dashboard for hiring teams</div>
    </footer>

    <div v-if="showForm" class="modal-overlay" @click.self="closeForm">
      <div class="modal">
        <h3>{{ isEditing ? 'Edit Candidate' : 'New Candidate' }}</h3>
        <form @submit.prevent="submitForm">
          <label>Name<br /><input v-model="formCandidate.name" required /></label>
          <label>Email<br /><input v-model="formCandidate.email" type="email" required /></label>
          <label>Role<br /><input v-model="formCandidate.role" required /></label>
          <label>Internal Score<br /><input v-model.number="formCandidate.internal_score" type="number" min="0" max="100" required /></label>
          <label>Client Feedback<br /><textarea v-model="formCandidate.client_feedback"></textarea></label>
          <div class="modal-actions">
            <button type="submit" class="btn-save">Save</button>
            <button type="button" @click="closeForm">Cancel</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
// Import API service and child components
import api from './services/api';
import CandidateList from './components/CandidateList.vue';
import ClientList from './components/ClientList.vue';
import DetailPanel from './components/DetailPanel.vue';

// State is still managed here (single source of truth)
const candidates = ref([]);
const clients = ref([]);
const selectedCandidate = ref(null);
const selectedClient = ref(null);
const showForm = ref(false);
const isEditing = ref(false);
const formCandidate = ref({ name: '', email: '', role: '', internal_score: 0, client_feedback: '' });

// Function to fetch data using the API service
const fetchData = async () => {
  try {
    const [candidateResponse, clientResponse] = await Promise.all([
      api.getCandidates(),
      api.getClients()
    ]);
    candidates.value = candidateResponse.data;
    clients.value = clientResponse.data;
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

// Function to handle selection
const selectCandidate = (candidate) => {
  selectedCandidate.value = candidate;
  selectedClient.value = null; // Optional: close client detail
};
const selectClient = (client) => {
  selectedClient.value = client;
  selectedCandidate.value = null; // Optional: close candidate detail
};

// Run fetchData when component mounts
onMounted(fetchData);

const openCreateForm = () => {
  isEditing.value = false;
  formCandidate.value = { name: '', email: '', role: '', internal_score: 0, client_feedback: '' };
  showForm.value = true;
};

const openEditForm = (candidate) => {
  isEditing.value = true;
  formCandidate.value = { ...candidate };
  showForm.value = true;
};

const closeForm = () => {
  showForm.value = false;
};

const submitForm = async () => {
  try {
    let resp;
    if (isEditing.value) {
      resp = await api.updateCandidate(formCandidate.value.id, formCandidate.value);
    } else {
      resp = await api.createCandidate(formCandidate.value);
    }
    // Refresh the list and update the selected candidate to reflect saved data
    await fetchData();
    if (resp && resp.data) selectedCandidate.value = resp.data;
    closeForm();
  } catch (err) {
    console.error('Save error', err);
    alert(err?.response?.data?.error || 'Failed to save candidate');
  }
};

const handleDelete = async (candidate) => {
  if (!confirm(`Delete ${candidate.name}? This cannot be undone.`)) return;
  try {
    await api.deleteCandidate(candidate.id);
    // refresh list
    await fetchData();
    if (selectedCandidate.value && selectedCandidate.value.id === candidate.id) selectedCandidate.value = null;
  } catch (err) {
    console.error('Delete error', err);
    alert(err?.response?.data?.error || 'Failed to delete candidate');
  }
};
</script>

<style>
/* Gaya global tetap di sini */
#app { font-family: Avenir, Helvetica, Arial, sans-serif; }
header.app-header { background-color: #42b983; color: white; padding: 0.75rem 1rem; }
.header-inner { display:flex; justify-content:space-between; align-items:center; max-width:1100px; margin:0 auto; }
.header-inner h1 { margin:0; font-size:1.2rem }
.header-inner nav a { color:rgba(255,255,255,0.9); margin-left:12px; text-decoration:none }
.dashboard { display: flex; height: calc(100vh - 100px); max-width:1100px; margin:1rem auto; box-shadow:0 2px 8px rgba(0,0,0,0.05); }
.list-panel { width: 360px; border-right: 1px solid #ddd; padding: 1rem; overflow-y: auto; background:#fff }
.list-section { margin-bottom: 2rem; }
.list-section h2 { margin-bottom: 0.5rem; }
.list-section ul { list-style-type: none; padding: 0; }
.list-section li { padding: 0.75rem; border: 1px solid #eee; margin-bottom: 0.5rem; border-radius: 4px; cursor: pointer; display:flex; justify-content:space-between; align-items:center }
.list-section li:hover { background-color: #f9f9f9; }
.list-section li.active { background-color: #eaf7f0; border-color: #42b983; }
.app-footer { text-align:center; padding:12px; color:#666; font-size:0.9rem }

/* Modal */
.modal-overlay { position:fixed; inset:0; background:rgba(0,0,0,0.4); display:flex; align-items:center; justify-content:center }
.modal { background:#fff; padding:1rem 1.25rem; border-radius:8px; width:420px; max-width:92% }
.modal label { display:block; margin-bottom:8px; font-size:0.95rem }
.modal input, .modal textarea { width:100%; padding:8px; margin-top:6px; box-sizing:border-box }
.modal-actions { display:flex; gap:8px; justify-content:flex-end; margin-top:12px }
.btn-save { background:#42b983; color:#fff; border:none; padding:8px 12px; border-radius:6px; cursor:pointer }
</style>