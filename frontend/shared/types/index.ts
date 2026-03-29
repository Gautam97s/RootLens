export type LogLevel = "DEBUG" | "INFO" | "WARNING" | "ERROR" | "CRITICAL";

export interface LogItem {
	id: number;
	timestamp: string;
	service: string;
	level: LogLevel;
	message: string;
	trace_id: string | null;
}

export interface LogsListResponse {
	total: number;
	limit: number;
	offset: number;
	items: LogItem[];
}

export interface LogsQueryParams {
	start_time?: string;
	end_time?: string;
	service?: string;
	level?: LogLevel;
	limit?: number;
	offset?: number;
}
