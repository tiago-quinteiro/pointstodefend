import { useNavigate } from "react-router-dom";
import "./Home.css";

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="home">
      <h1>Points to Defend</h1>

      <div className="tour-buttons">
        <button onClick={() => navigate("/tour/ATP")}>
          <img src="/atp_logo.png" alt="ATP" />
        </button>

        <button onClick={() => navigate("/tour/WTA")}>
          <img src="/wta_logo.png" alt="WTA" />
        </button>
      </div>
    </div>
  );
}
