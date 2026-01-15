<template>
  <section class="detail-panel">
    <div class="detail-card" v-if="selectedCandidate">
      <h2>Candidate Detail</h2>
      <p><strong>Name:</strong> {{ selectedCandidate.name }}</p>
      <p><strong>Email:</strong> {{ selectedCandidate.email }}</p>
      <p><strong>Role:</strong> {{ selectedCandidate.role }}</p>
      <p><strong>Internal Score:</strong> {{ selectedCandidate.internal_score }}</p>
      <p><strong>Client Feedback:</strong> {{ selectedCandidate.client_feedback || 'No feedback yet.' }}</p>
    </div>
    <div class="detail-card" v-if="selectedClient">
      <h2>Client Detail</h2>
      <p><strong>Name:</strong> {{ selectedClient.name }}</p>
      <p><strong>Industry:</strong> {{ selectedClient.industry }}</p>
      <p><strong>Requirements:</strong> {{ selectedClient.requirements_summary }}</p>
    </div>
    <div v-if="!selectedCandidate && !selectedClient">
      <p>Please select a candidate or a client to view details.</p>
    </div>
  </section>
</template>

<script setup>
defineProps({
  selectedCandidate: Object,
  selectedClient: Object
});
</script>

<style scoped>
.detail-panel {
  flex-grow: 1;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.detail-card {
  border: 1px solid #ddd;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.detail-card h2 {
  margin-top: 0;
  color: #42b983;
}
</style>