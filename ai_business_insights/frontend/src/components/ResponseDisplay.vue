<template>
  <div v-if="response" class="response-display">
    <h3>AI Insights</h3>

    <!-- Render markdown content -->
    <div v-html="markdownContent" class="markdown-content"></div>

    <DownloadButton :response="response.response" />
  </div>
</template>

<script>
import { marked } from 'marked';
import DownloadButton from './DownloadButton.vue';

export default {
  props: {
    response: Object
  },
  components: {
    DownloadButton
  },
  computed: {
    markdownContent() {
      return marked(this.response.response || '');
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

.markdown-content h1, h2, h3, h4, h5, h6 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.markdown-content p {
  margin-bottom: 15px;
}

.markdown-content ul {
  list-style-type: disc;
  margin-left: 20px;
}

.markdown-content code {
  background: #f1f1f1;
  padding: 2px 5px;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
}

.markdown-content pre {
  background: #f1f1f1;
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
}
</style>
