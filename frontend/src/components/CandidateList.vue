<template>
  <div class="list-section">
    <div class="list-header">
      <h2>Candidates</h2>
      <button class="btn-new" @click.stop="emit('create')">+ New</button>
    </div>

    <ul>
      <li 
        v-for="candidate in candidates" 
        :key="candidate.id" 
        @click="emit('select', candidate)"
        :class="{ active: selectedCandidate && selectedCandidate.id === candidate.id }"
      >
        <div class="item-main">{{ candidate.name }} <small>— {{ candidate.role }}</small></div>
        <div class="item-actions">
          <button class="btn-edit" @click.stop="emit('edit', candidate)">Edit</button>
          <button class="btn-delete" @click.stop="emit('delete', candidate)">Delete</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  candidates: Array,
  selectedCandidate: Object
});

const emit = defineEmits(['select', 'edit', 'delete', 'create']);
</script>

<style scoped>
.list-header { display: flex; justify-content: space-between; align-items: center; }
.btn-new { background:#42b983; color:#fff; border:none; padding:6px 10px; border-radius:4px; cursor:pointer; }
.btn-new:hover { opacity:0.9 }
ul { list-style: none; padding: 0; }
li { display:flex; justify-content:space-between; align-items:center; padding:0.6rem; border:1px solid #eee; margin-bottom:0.5rem; border-radius:4px; cursor:pointer; }
.item-main small { color: #666; }
.item-actions { display:flex; gap:8px; }
.btn-edit { background:#ffd54f; border:none; padding:4px 8px; border-radius:4px; cursor:pointer; }
.btn-delete { background:#ef5350; color:#fff; border:none; padding:4px 8px; border-radius:4px; cursor:pointer; }
.btn-edit:hover, .btn-delete:hover { opacity:0.9 }
</style>