import { LineChart, Line, XAxis, YAxis, Tooltip } from "recharts";

export default function EquityChart({ data }) {
  return (
    <LineChart width={600} height={300} data={data}>
      <XAxis dataKey="Date" />
      <YAxis />
      <Tooltip />
      <Line type="monotone" dataKey="Equity" stroke="#000" />
    </LineChart>
  );
}
