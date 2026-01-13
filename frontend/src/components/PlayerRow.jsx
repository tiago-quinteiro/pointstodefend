import { useState } from "react";
import PointsBreakdown from "./PointsBreakdown";
import "./PlayerRow.css";

export default function PlayerRow({ player }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="player-row">
      <button className="player-summary" onClick={() => setOpen(!open)}>
        <span>{player.rank}</span>
        <span>{player.name}</span>
        <span>{player.country}</span>
        <span>{player.points} pts</span>
        <span>{player.pointsToDefend} defend</span>
      </button>

      {open && <PointsBreakdown playerId={player.id} />}
    </div>
  );
}
