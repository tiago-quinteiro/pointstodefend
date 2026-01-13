import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import TourPage from "./pages/TourPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/tour/:tour" element={<TourPage />} />
    </Routes>
  );
}

export default App;

