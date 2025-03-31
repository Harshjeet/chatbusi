<template>
  <div class="query-form">
    <h2>Business Query</h2>
    <textarea 
      v-model="query" 
      placeholder="Enter your query..." 
      rows="4" 
      :disabled="loading">
    </textarea>
    
    <button 
      @click="handleQuery" 
      :disabled="loading"
    >
      {{ loading ? 'Processing...' : 'Submit' }}
    </button>

    <!-- Loader -->
    <div v-if="loading" class="loader"></div>
  </div>
</template>

<script>
import { sendQuery } from '../services/api';

export default {
  data() {
    return {
      query: '',
      loading: false
    };
  },
  methods: {
    async handleQuery() {
      if (!this.query.trim()) {
        alert('Please enter a query.');
        return;
      }

      this.loading = true;  // Show loader

      try {
        const response = await sendQuery(this.query);
        this.$emit('query-response', response);
      } catch (error) {
        alert('Failed to fetch insights. Please try again.');
      } finally {
        this.loading = false;  // Hide loader
      }
    }
  }
};
</script>

<style scoped>
.query-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  max-width: 700px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background: #f9f9f9;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
  resize: none;
}

button {
  padding: 12px 20px;
  background: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.3s;
}

button:hover {
  background: #45a049;
}

button:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.loader {
  border: 5px solid #f3f3f3;
  border-top: 5px solid #3498db;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 10px auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
