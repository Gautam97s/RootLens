import { PropsWithChildren } from "react";

interface CardProps extends PropsWithChildren {
	title?: string;
}

export default function Card({ title, children }: CardProps) {
	return (
		<section
			style={{
				border: "1px solid #e5e7eb",
				borderRadius: 10,
				padding: 16,
				background: "#ffffff",
			}}
		>
			{title ? <h3 style={{ marginTop: 0 }}>{title}</h3> : null}
			{children}
		</section>
	);
}
