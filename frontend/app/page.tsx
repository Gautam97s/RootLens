import Link from "next/link";

import Card from "../shared/components/Card";

const navItems = [
	{ href: "/logs", label: "Logs Explorer", desc: "Filter and inspect ingested logs" },
	{ href: "/incidents", label: "Incidents", desc: "Incident summary placeholders" },
	{ href: "/analysis", label: "Analysis", desc: "Correlation and timeline placeholders" },
];

export default function HomePage() {
	return (
		<main style={{ maxWidth: 1000, margin: "0 auto", padding: 24 }}>
			<h1 style={{ marginBottom: 6 }}>RootLens Dashboard</h1>
			<p style={{ marginTop: 0, color: "#4b5563" }}>
				Basic UI for ingestion and logs query features.
			</p>

			<div style={{ display: "grid", gap: 12, gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))" }}>
				{navItems.map((item) => (
					<Card key={item.href} title={item.label}>
						<p style={{ color: "#4b5563", marginTop: 0 }}>{item.desc}</p>
						<Link href={item.href}>Open</Link>
					</Card>
				))}
			</div>
		</main>
	);
}
