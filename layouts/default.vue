<template>
  <div class="app-container">
    <!-- Sidebar -->
    <div class="sidebar">
      <div class="sidebar-header">
        <h1 class="sidebar-title">Early Stopping</h1>
      </div>
      <nav class="sidebar-nav">
        <NuxtLink to="/" class="nav-item" active-class="active">
          <span class="icon">📊</span>
          <span>Dashboard</span>
        </NuxtLink>
        <NuxtLink to="/residuals" class="nav-item" active-class="active">
          <span class="icon">📈</span>
          <span>Residuals</span>
        </NuxtLink>
        <NuxtLink to="/about" class="nav-item" active-class="active">
          <span class="icon">ℹ️</span>
          <span>About</span>
        </NuxtLink>
      </nav>
      <div class="sidebar-footer">
        <p class="text-xs text-gray-500">Early Stopping Demo v1.0</p>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
  min-height: 100vh;
}

.sidebar {
  width: 250px;
  background-color: #1e293b;
  color: white;
  display: flex;
  flex-direction: column;
  border-right: 1px solid #334155;
}

.sidebar-header {
  padding: 1.5rem 1rem;
  border-bottom: 1px solid #334155;
}

.sidebar-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.sidebar-nav {
  flex: 1;
  padding: 1rem 0.5rem;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  margin: 0.25rem 0;
  border-radius: 0.5rem;
  color: #cbd5e1;
  text-decoration: none;
  transition: all 0.2s;
}

.nav-item:hover {
  background-color: #334155;
  color: white;
}

.nav-item.active {
  background-color: #3b82f6;
  color: white;
}

.icon {
  margin-right: 0.75rem;
  font-size: 1.25rem;
}

.sidebar-footer {
  padding: 1rem;
  border-top: 1px solid #334155;
  text-align: center;
}

.main-content {
  flex: 1;
  padding: 2rem;
  background-color: #f8fafc;
  overflow-y: auto;
}
</style> 