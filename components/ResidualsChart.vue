<template>
  <div class="chart-container">
    <h3 class="text-xl font-semibold mb-3">Residuals by Iteration</h3>
    <Line v-if="chartData.datasets[0].data.length" :data="chartData" :options="chartOptions" />
    <p v-else class="text-gray-500">No residuals data available. Run computation first.</p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const props = defineProps({
  residuals: {
    type: Array,
    default: () => []
  }
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      title: {
        display: true,
        text: 'Residual Value'
      }
    },
    x: {
      title: {
        display: true,
        text: 'Iteration'
      }
    }
  }
};

const chartData = computed(() => {
  const labels = props.residuals.map((_, index) => index + 1);
  
  return {
    labels,
    datasets: [
      {
        label: 'Residuals',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 2,
        data: props.residuals
      }
    ]
  };
});
</script>

<style scoped>
.chart-container {
  height: 400px;
  margin-top: 20px;
  padding: 10px;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  background-color: white;
}
</style> 