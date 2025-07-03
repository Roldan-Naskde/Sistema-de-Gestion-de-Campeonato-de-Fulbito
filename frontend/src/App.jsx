import React from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
import Navbar from './components/Navbar';
import AppRoutes from './routes';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      {/* El Navbar debe estar DENTRO de AppRoutes, o AppRoutes debe envolver el Navbar */}
      <AppRoutes />
    </QueryClientProvider>
  );
}

export default App;