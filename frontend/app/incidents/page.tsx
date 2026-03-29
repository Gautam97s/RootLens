import Card from "../../shared/components/Card";

export default function IncidentsPage() {
	return (
		<main style={{ maxWidth: 1000, margin: "0 auto", padding: 24 }}>
			<h1>Incidents</h1>
			<Card title="Coming Next">
				<p style={{ margin: 0, color: "#4b5563" }}>
					Incident summary UI will be connected after correlation, timeline, and root-cause APIs are ready.
				</p>
			</Card>
		</main>
	);
}
