<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-6">Interactive Computation Demo</h1>
    
    <div class="mb-6">
      <label for="slider" class="block mb-2">Value: {{ sliderValue }}</label>
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
      class="mb-6 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      :disabled="isLoading"
    >
      {{ isLoading ? 'Computing...' : 'Compute' }}
    </button>
    
    <div class="p-4 border rounded-md bg-gray-50 mb-4">
      <p>The current slider value is: <strong>{{ sliderValue }}</strong></p>
    </div>
    
    <div v-if="computedResult !== null" class="p-4 border rounded-md bg-green-50">
      <p>Computed result: <strong>{{ computedResult }}</strong></p>
      <p class="text-sm text-gray-600 mt-2">This is the discrepancy stopping time.</p>
    </div>
    
    <div v-if="error" class="p-4 border rounded-md bg-red-50 mt-4">
      <p class="text-red-600">{{ error }}</p>
    </div>

    <!-- Residuals Chart Component -->
    <ResidualsChart :residuals="residuals" v-if="residuals.length > 0" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import ResidualsChart from './components/ResidualsChart.vue';

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
  } catch (err) {
    error.value = `Failed to compute: ${err.message}`;
    console.error(err);
  } finally {
    isLoading.value = false;
  }
}
</script>

<style>
.container {
  max-width: 800px;
}

input[type="range"] {
  accent-color: #4f46e5;
}
</style>
