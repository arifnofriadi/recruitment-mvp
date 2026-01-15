<template>
  <div class="list-section">
    <h2>Clients</h2>
    <ul>
      <li 
        v-for="client in clients" 
        :key="client.id" 
        @click="$emit('select', client)"
        :class="{ active: selectedClient && selectedClient.id === client.id }"
      >
        {{ client.name }}
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  clients: Array,
  selectedClient: Object
});

defineEmits(['select']);
</script>