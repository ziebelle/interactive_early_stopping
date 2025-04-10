<template>
  <div class="about-page">
    <h1 class="text-3xl font-bold mb-6">About This Project</h1>
    
    <div class="content bg-white rounded-lg shadow-sm p-6">
      <h2 class="text-xl font-semibold mb-4">Early Stopping Visualization</h2>
      
      <p class="mb-4">
        This application demonstrates the concept of early stopping in iterative algorithms.
        It visualizes how residuals change during iterations and helps understand when to stop
        the algorithm to avoid overfitting.
      </p>
      
      <h3 class="text-lg font-medium mt-6 mb-2">Landweber Algorithm</h3>
      <p class="mb-4">
        The demo uses the Landweber iterative algorithm, which is commonly used to solve linear inverse problems.
        The algorithm iteratively updates the solution and computes residuals at each step.
      </p>
      
      <h3 class="text-lg font-medium mt-6 mb-2">Discrepancy Principle</h3>
      <p class="mb-4">
        We use the discrepancy principle as a stopping criterion. This principle stops the iteration
        when the residual norm reaches a specified value related to the noise level.
      </p>
      
      <h3 class="text-lg font-medium mt-6 mb-2">Technologies Used</h3>
      <ul class="list-disc pl-6 mb-4 space-y-1">
        <li>Frontend: Vue.js/Nuxt</li>
        <li>Backend: FastAPI (Python)</li>
        <li>Data Visualization: Chart.js</li>
        <li>Numerical Computations: NumPy, SciPy</li>
      </ul>
      
      <div class="mt-8 pt-4 border-t border-gray-200">
        <p class="text-sm text-gray-600">
          This is an educational project designed to help understand the concept of regularization
          by early stopping in inverse problems.
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.about-page {
  max-width: 800px;
  margin: 0 auto;
}
</style> 