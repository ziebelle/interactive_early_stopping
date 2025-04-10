<template>
  <div class="residuals-page">
    <div class="page-header">
      <h1 class="text-2xl font-bold mb-4">Residuals Analysis</h1>
      <p class="text-gray-600 mb-6">
        Adjust the noise level and compute residuals to analyze the early stopping algorithm.
      </p>
    </div>

    <div class="control-panel p-6 bg-white rounded-lg shadow-sm mb-6">
      <div class="mb-6">
        <label for="slider" class="block mb-2 font-medium">Noise Level: {{ sliderValue }}</label>
        <input 
          id="slider" 
          type="range" 
          min="0.01" 
          max="0.1" 
          step="0.01"
          v-model="sliderValue"
          class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
        />
      </div>
      
      <button 
        @click="computeResult" 
        class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 flex items-center"
        :disabled="isLoading"
      >
        <span v-if="isLoading" class="mr-2">⏳</span>
        <span>{{ isLoading ? 'Computing...' : 'Compute Residuals' }}</span>
      </button>
    </div>
    
    <div v-if="computedResult !== null" class="result-panel p-6 bg-white rounded-lg shadow-sm mb-6">
      <div class="flex items-center mb-2">
        <div class="w-3 h-3 bg-green-500 rounded-full mr-2"></div>
        <h2 class="text-lg font-semibold">Computation Results</h2>
      </div>
      <p class="mb-2">Discrepancy stopping time: <strong>{{ computedResult }}</strong></p>
      <p class="text-sm text-gray-600">This represents the optimal iteration to stop the algorithm.</p>
    </div>
    
    <div v-if="error" class="error-panel p-6 bg-red-50 border border-red-200 rounded-lg mb-6">
      <div class="flex items-center">
        <div class="w-5 h-5 text-red-600 mr-2">⚠️</div>
        <p class="text-red-600">{{ error }}</p>
      </div>
    </div>

    <!-- Residuals Chart -->
    <div class="chart-wrapper bg-white rounded-lg shadow-sm p-4">
      <ResidualsChart :residuals="residuals" v-if="residuals.length > 0" />
      <div v-else class="flex flex-col items-center justify-center py-10 text-gray-500">
        <div class="text-6xl mb-4">📈</div>
        <p>No residuals data available. Run computation first.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import ResidualsChart from '../components/ResidualsChart.vue';

const sliderValue = ref(0.05);
const computedResult = ref(null);
const error = ref(null);
const residuals = ref([]);
const isLoading = ref(false);

async function computeResult() {
  try {
    isLoading.value = true;
    error.value = null;
    const response = await fetch('http://localhost:8000/compute', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ value: sliderValue.value }),
    });
    
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    
    const data = await response.json();
    computedResult.value = data.computed;
    residuals.value = data.residuals || [];
    
    if (residuals.value.length === 0) {
      error.value = "No residuals data returned from the server";
    }
  } catch (err) {
    error.value = `Failed to compute: ${err.message}`;
    console.error(err);
  } finally {
    isLoading.value = false;
  }
}
</script>

<style scoped>
.residuals-page {
  max-width: 900px;
  margin: 0 auto;
}

.chart-wrapper {
  min-height: 450px;
}

input[type="range"] {
  accent-color: #3b82f6;
}
</style> 