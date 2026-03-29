"use client";

import { ButtonHTMLAttributes } from "react";

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement>;

export default function Button({ children, style, ...props }: ButtonProps) {
	return (
		<button
			{...props}
			style={{
				border: "1px solid #d1d5db",
				background: "#111827",
				color: "#ffffff",
				borderRadius: 8,
				padding: "8px 12px",
				fontWeight: 600,
				cursor: "pointer",
				...style,
			}}
		>
			{children}
		</button>
	);
}
