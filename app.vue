<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-6">Slider Demo</h1>
    
    <div class="mb-6">
      <label for="slider" class="block mb-2">Value: {{ sliderValue }}</label>
      <input 
        id="slider" 
        type="range" 
        min="0" 
        max="100" 
        v-model="sliderValue"
        class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
      />
    </div>
    
    <div class="p-4 border rounded-md bg-gray-50">
      <p>The current slider value is: <strong>{{ sliderValue }}</strong></p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const sliderValue = ref(50);
</script>

<style>
.container {
  max-width: 600px;
}

input[type="range"] {
  accent-color: #4f46e5;
}
</style>
