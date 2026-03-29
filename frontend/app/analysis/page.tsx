import Card from "../../shared/components/Card";

export default function AnalysisPage() {
	return (
		<main style={{ maxWidth: 1000, margin: "0 auto", padding: 24 }}>
			<h1>Analysis</h1>
			<Card title="Upcoming APIs">
				<p style={{ margin: 0, color: "#4b5563" }}>
					Correlation, timeline reconstruction, and root-cause visualization will be rendered here in the next phases.
				</p>
			</Card>
		</main>
	);
}
