import { useParams } from "react-router-dom";
import PlayerRow from "../components/PlayerRow";

export default function TourPage() {
  const { tour } = useParams(); // "ATP" or "WTA"

  return (
    <div>
      <h1>{tour} Points to Defend</h1>

      {/* Temporary mocked data */}
      <PlayerRow
        player={{
          name: "Novak Djokovic",
          age: 37,
          country: "Serbia",
          points: 9855,
          pointsToDefend: 2000,
          rank: 1
        }}
      />
    </div>
  );
}
