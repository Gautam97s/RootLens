"use client";

import { LogItem } from "@/shared/types";

interface LogTableProps {
	logs: LogItem[];
}

function levelColor(level: string): string {
	if (level === "ERROR" || level === "CRITICAL") return "#b91c1c";
	if (level === "WARNING") return "#b45309";
	if (level === "INFO") return "#1d4ed8";
	return "#374151";
}

export default function LogTable({ logs }: LogTableProps) {
	if (logs.length === 0) {
		return <p style={{ margin: 0 }}>No logs found for selected filters.</p>;
	}

	return (
		<div style={{ overflowX: "auto" }}>
			<table style={{ width: "100%", borderCollapse: "collapse" }}>
				<thead>
					<tr style={{ textAlign: "left", borderBottom: "1px solid #e5e7eb" }}>
						<th style={{ padding: "10px 8px" }}>Time</th>
						<th style={{ padding: "10px 8px" }}>Service</th>
						<th style={{ padding: "10px 8px" }}>Level</th>
						<th style={{ padding: "10px 8px" }}>Message</th>
						<th style={{ padding: "10px 8px" }}>Trace ID</th>
					</tr>
				</thead>
				<tbody>
					{logs.map((log) => (
						<tr key={log.id} style={{ borderBottom: "1px solid #f3f4f6" }}>
							<td style={{ padding: "10px 8px", whiteSpace: "nowrap" }}>
								{new Date(log.timestamp).toLocaleString()}
							</td>
							<td style={{ padding: "10px 8px" }}>{log.service}</td>
							<td style={{ padding: "10px 8px", color: levelColor(log.level), fontWeight: 700 }}>
								{log.level}
							</td>
							<td style={{ padding: "10px 8px" }}>{log.message}</td>
							<td style={{ padding: "10px 8px", color: "#6b7280" }}>{log.trace_id ?? "-"}</td>
						</tr>
					))}
				</tbody>
			</table>
		</div>
	);
}
