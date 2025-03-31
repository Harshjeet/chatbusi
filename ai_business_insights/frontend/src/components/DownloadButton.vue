<template>
  <div class="download-buttons">
    <button @click="download('pdf')">Download PDF</button>
    <button @click="download('csv')">Download CSV</button>
  </div>
</template>

<script>
import { downloadPdf, downloadCsv } from '../services/api';

export default {
  props: {
    response: String
  },
  methods: {
    async download(format) {
      try {
        if (format === 'pdf') {
          const file = await downloadPdf(this.response);
          this.triggerDownload(file, 'report.pdf');
        } else if (format === 'csv') {
          const file = await downloadCsv(this.response);
          this.triggerDownload(file, 'report.csv');
        }
      } catch (error) {
        alert('Binary file responses are only supported in the paid version.');
      }
    },
    triggerDownload(file, filename) {
      const url = window.URL.createObjectURL(new Blob([file]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  }
};
</script>

<style scoped>
.download-buttons {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  margin-top: 10px;
}

button {
  padding: 8px 16px;
  background: #27ae60;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background: #2ecc71;
}
</style>
