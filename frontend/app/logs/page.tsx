"use client";

import { FormEvent, useState } from "react";

import LogTable from "../../modules/logs/components/LogTable";
import { useLogs } from "../../modules/logs/hooks/useLogs";
import Button from "../../shared/components/Button";
import Card from "../../shared/components/Card";
import Loader from "../../shared/components/Loader";

export default function LogsPage() {
	const { data, params, setParams, isLoading, error } = useLogs({ limit: 10, offset: 0 });
	const [service, setService] = useState<string>("");
	const [level, setLevel] = useState<string>("");
	const [startTime, setStartTime] = useState<string>("");
	const [endTime, setEndTime] = useState<string>("");

	const onApplyFilters = (event: FormEvent) => {
		event.preventDefault();
		setParams({
			service: service || undefined,
			level: (level || undefined) as "DEBUG" | "INFO" | "WARNING" | "ERROR" | "CRITICAL" | undefined,
			start_time: startTime || undefined,
			end_time: endTime || undefined,
			offset: 0,
		});
	};

	const canGoPrev = (params.offset ?? 0) > 0;
	const canGoNext = (params.offset ?? 0) + (params.limit ?? 10) < data.total;

	return (
		<main style={{ maxWidth: 1100, margin: "0 auto", padding: 24, display: "grid", gap: 12 }}>
			<h1 style={{ marginBottom: 0 }}>Logs</h1>
			<p style={{ marginTop: 0, color: "#4b5563" }}>
				Query logs by time, service, level, and paginate the results.
			</p>

			<Card title="Filters">
				<form
					onSubmit={onApplyFilters}
					style={{ display: "grid", gap: 10, gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))" }}
				>
					<input placeholder="Service" value={service} onChange={(e) => setService(e.target.value)} />
					<select value={level} onChange={(e) => setLevel(e.target.value)}>
						<option value="">All Levels</option>
						<option value="DEBUG">DEBUG</option>
						<option value="INFO">INFO</option>
						<option value="WARNING">WARNING</option>
						<option value="ERROR">ERROR</option>
						<option value="CRITICAL">CRITICAL</option>
					</select>
					<input
						type="datetime-local"
						value={startTime}
						onChange={(e) => setStartTime(e.target.value)}
						title="Start time"
					/>
					<input
						type="datetime-local"
						value={endTime}
						onChange={(e) => setEndTime(e.target.value)}
						title="End time"
					/>
					<Button type="submit">Apply</Button>
				</form>
			</Card>

			<Card title={`Results (${data.total})`}>
				{isLoading ? <Loader /> : <LogTable logs={data.items} />}
				{error ? <p style={{ color: "#b91c1c" }}>{error}</p> : null}
			</Card>

			<div style={{ display: "flex", gap: 8 }}>
				<Button
					type="button"
					onClick={() => setParams({ offset: Math.max((params.offset ?? 0) - (params.limit ?? 10), 0) })}
					disabled={!canGoPrev}
				>
					Previous
				</Button>
				<Button
					type="button"
					onClick={() => setParams({ offset: (params.offset ?? 0) + (params.limit ?? 10) })}
					disabled={!canGoNext}
				>
					Next
				</Button>
			</div>
		</main>
	);
}
