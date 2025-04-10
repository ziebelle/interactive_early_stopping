<template>
  <div class="home-page">
    <h1 class="text-3xl font-bold mb-6">Interactive Early Stopping</h1>
    
    <div class="welcome-card bg-white p-6 rounded-lg shadow-sm mb-8">
      <h2 class="text-xl font-semibold mb-3">Welcome to the Early Stopping Demo</h2>
      <p class="text-gray-700 mb-4">
        This interactive application demonstrates early stopping techniques in iterative algorithms.
        Explore how different noise levels affect convergence and optimal stopping times.
      </p>
      
      <div class="flex gap-4 mt-6">
        <NuxtLink 
          to="/residuals" 
          class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 inline-flex items-center"
        >
          <span class="mr-2">📈</span>
          <span>Explore Residuals</span>
        </NuxtLink>
      </div>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div class="info-card bg-white p-5 rounded-lg shadow-sm">
        <div class="text-3xl mb-3">🔍</div>
        <h3 class="text-lg font-medium mb-2">About Early Stopping</h3>
        <p class="text-gray-600">
          Early stopping prevents overfitting by halting training when performance on validation data begins to degrade.
        </p>
      </div>
      
      <div class="info-card bg-white p-5 rounded-lg shadow-sm">
        <div class="text-3xl mb-3">⚙️</div>
        <h3 class="text-lg font-medium mb-2">How It Works</h3>
        <p class="text-gray-600">
          The demo uses the Landweber algorithm and the discrepancy principle to determine optimal stopping time.
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-page {
  max-width: 900px;
  margin: 0 auto;
}

.info-card {
  transition: transform 0.2s;
}

.info-card:hover {
  transform: translateY(-4px);
}
</style> 