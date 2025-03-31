<template>
  <div v-if="response" class="response-display">
    <h3>AI Insights</h3>

    <!-- Render markdown content -->
    <div v-html="markdownContent" class="markdown-content"></div>

    <div class="download-buttons">
      <button @click="downloadPdf">Download PDF</button>

      <!-- Only show CSV download if a table is detected -->
      <button v-if="containsTable" @click="downloadCsv">
        Download CSV
      </button>
    </div>
  </div>
</template>

<script>
import { marked } from 'marked';
import { downloadPdf, downloadCsv } from '../services/api';

export default {
  props: {
    response: Object
  },
  computed: {
    markdownContent() {
      return marked(this.response.response || '');
    },
    containsTable() {
      // Check if the response contains a markdown table
      const tableRegex = /\|(.+?)\|\n(\|[-:]+\|)+\n((?:\|.*?\|\n?)+)/;
      return tableRegex.test(this.response.response);
    }
  },
  methods: {
    async downloadPdf() {
      try {
        await downloadPdf(this.response.response);
      } catch (error) {
        alert('Failed to download PDF');
      }
    },
    async downloadCsv() {
      try {
        await downloadCsv(this.response.response);
      } catch (error) {
        alert('No table found or CSV download failed.');
      }
    }
  }
};
</script>

<style scoped>
.response-display {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: #f5f5f5;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

h3 {
  color: #2c3e50;
  font-size: 22px;
  margin-bottom: 15px;
}

.markdown-content {
  white-space: pre-wrap;
  line-height: 1.6;
  color: #34495e;
}

.download-buttons {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

button {
  padding: 12px 20px;
  background: #3498db;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.3s;
}

button:hover {
  background: #2980b9;
}
</style>
