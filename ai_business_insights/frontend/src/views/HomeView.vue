<template>
  <div class="home-view">
    <QueryForm @query-response="handleResponse" />
    
    <ResponseDisplay 
      v-if="response" 
      :response="response" 
    />
  </div>
</template>

<script>
import QueryForm from '../components/QueryForm.vue';
import ResponseDisplay from '../components/ResponseDisplay.vue';

export default {
  components: {
    QueryForm,
    ResponseDisplay
  },
  data() {
    return {
      response: null
    };
  },
  methods: {
    handleResponse(data) {
      this.response = data;
    }
  }
};
</script>

<style>
.home-view {
  max-width: 1200px;
  margin: 0 auto;
  padding: 30px;
  font-family: Arial, sans-serif;
  background: #f5f5f5;
  min-height: 100vh;
}
</style>
