export default function PointsBreakdown() {
  // mocked data for now
  const weeks = [
    { week: "Week 1", points: 250 },
    { week: "Week 5", points: 500 },
    { week: "Week 10", points: 1000 }
  ];

  return (
    <div className="points-breakdown">
      {weeks.map((w) => (
        <div key={w.week}>
          {w.week}: {w.points} pts
        </div>
      ))}
    </div>
  );
}
